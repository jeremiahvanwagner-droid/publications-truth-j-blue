#!/usr/bin/env python3
"""Phase 6 launch gate checks for the Truth J Blue publications site."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import ssl
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen


INDEXABLE_PATHS = [
    "/",
    "/publications.html",
    "/books.html",
    "/programs.html",
    "/about-jeremiah.html",
    "/manifesto.html",
    "/philosophy.html",
    "/sitemap.html",
    "/contact.html",
    "/privacy.html",
    "/terms.html",
]

BANNED_PROGRAM_PATTERNS = [
    r"site\.truthjblue\.com/payment-link",
    r"buy\.stripe\.com",
    r"gumroad\.com",
    r"paypal\.com",
]

META_PATTERNS = {
    "title": re.compile(r"<title>[^<]+</title>", re.IGNORECASE | re.DOTALL),
    "description": re.compile(r'<meta\s+name=["\']description["\']', re.IGNORECASE),
    "canonical": re.compile(r'<link\s+rel=["\']canonical["\']', re.IGNORECASE),
    "og:title": re.compile(r'<meta\s+property=["\']og:title["\']', re.IGNORECASE),
    "og:description": re.compile(r'<meta\s+property=["\']og:description["\']', re.IGNORECASE),
    "og:image": re.compile(r'<meta\s+property=["\']og:image["\']', re.IGNORECASE),
    "twitter:card": re.compile(r'<meta\s+name=["\']twitter:card["\']', re.IGNORECASE),
    "twitter:title": re.compile(r'<meta\s+name=["\']twitter:title["\']', re.IGNORECASE),
    "twitter:description": re.compile(r'<meta\s+name=["\']twitter:description["\']', re.IGNORECASE),
    "twitter:image": re.compile(r'<meta\s+name=["\']twitter:image["\']', re.IGNORECASE),
}


@dataclass
class CheckResult:
    name: str
    passed: bool
    detail: str


class LaunchGate:
    def __init__(
        self,
        fetch_base_url: str,
        canonical_base_url: str,
        timeout: int,
        insecure: bool,
    ) -> None:
        self.fetch_base_url = fetch_base_url.rstrip("/")
        self.canonical_base_url = canonical_base_url.rstrip("/")
        self.timeout = timeout
        self.insecure = insecure
        self.ssl_context = ssl._create_unverified_context() if insecure else None
        self.results: List[CheckResult] = []

    def _record(self, name: str, passed: bool, detail: str) -> None:
        self.results.append(CheckResult(name=name, passed=passed, detail=detail))

    def _fetch_url(self, path: str) -> str:
        if path == "/":
            return f"{self.fetch_base_url}/"
        if path.startswith("/"):
            return f"{self.fetch_base_url}{path}"
        return f"{self.fetch_base_url}/{path}"

    def _canonical_url(self, path: str) -> str:
        if path == "/":
            return f"{self.canonical_base_url}/"
        if path.startswith("/"):
            return f"{self.canonical_base_url}{path}"
        return f"{self.canonical_base_url}/{path}"

    def _fetch(self, path: str) -> Tuple[Optional[int], str, Dict[str, str], Optional[str]]:
        url = self._fetch_url(path)
        request = Request(
            url,
            headers={"User-Agent": "TruthJBlueLaunchGate/1.1 (+https://pub.jeremiahvanwagner.com)"},
        )

        try:
            if self.ssl_context is not None:
                response = urlopen(request, timeout=self.timeout, context=self.ssl_context)
            else:
                response = urlopen(request, timeout=self.timeout)

            with response:
                status = response.getcode()
                body = response.read().decode("utf-8", errors="replace")
                headers = {k.lower(): v for k, v in response.getheaders()}
                return status, body, headers, None
        except HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")
            headers = {k.lower(): v for k, v in exc.headers.items()}
            return exc.code, body, headers, None
        except URLError as exc:
            reason = str(exc.reason) if getattr(exc, "reason", None) else str(exc)
            return None, "", {}, reason
        except ssl.SSLError as exc:
            return None, "", {}, str(exc)
        except Exception as exc:  # pragma: no cover
            return None, "", {}, str(exc)

    def _check_core_urls(self) -> Dict[str, str]:
        pages: Dict[str, str] = {}
        for path in INDEXABLE_PATHS:
            status, body, _, error = self._fetch(path)
            name = f"Core URL {path} returns 200"
            if error:
                self._record(name, False, error)
                continue
            if status != 200:
                self._record(name, False, f"HTTP {status}")
                continue
            self._record(name, True, "HTTP 200")
            pages[path] = body
        return pages

    def _check_about_alias(self) -> None:
        status, body, _, error = self._fetch("/about.html")
        if error:
            self._record("about.html alias behavior", False, error)
            return
        if status not in {200, 301, 302}:
            self._record("about.html alias behavior", False, f"Unexpected HTTP {status}")
            return

        has_noindex = "noindex,follow" in body
        has_target = "url=about-jeremiah.html" in body
        passed = has_noindex and has_target
        detail = "contains noindex and redirect target" if passed else "missing noindex and/or redirect target"
        self._record("about.html alias behavior", passed, detail)

    def _check_robots(self) -> None:
        status, body, _, error = self._fetch("/robots.txt")
        if error:
            self._record("robots.txt reachable", False, error)
            return
        if status != 200:
            self._record("robots.txt reachable", False, f"HTTP {status}")
            return

        self._record("robots.txt reachable", True, "HTTP 200")
        expected = f"Sitemap: {self.canonical_base_url}/sitemap.xml"
        self._record(
            "robots.txt sitemap pointer",
            expected in body,
            f"expected line: {expected}",
        )

    def _check_sitemap(self) -> None:
        status, body, _, error = self._fetch("/sitemap.xml")
        if error:
            self._record("sitemap.xml reachable", False, error)
            return
        if status != 200:
            self._record("sitemap.xml reachable", False, f"HTTP {status}")
            return

        self._record("sitemap.xml reachable", True, "HTTP 200")

        try:
            root = ET.fromstring(body)
        except ET.ParseError as exc:
            self._record("sitemap.xml is valid XML", False, str(exc))
            return

        self._record("sitemap.xml is valid XML", True, "parse ok")
        ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        locs = [node.text for node in root.findall("sm:url/sm:loc", ns) if node.text]
        required = {self._canonical_url(path) for path in INDEXABLE_PATHS}
        missing = sorted(required.difference(set(locs)))

        if missing:
            detail = "missing URLs: " + ", ".join(missing)
            self._record("sitemap.xml includes required URLs", False, detail)
        else:
            self._record("sitemap.xml includes required URLs", True, "all required URLs present")

        status_failures: List[str] = []
        for url in sorted(set(locs)):
            parsed = urlparse(url)
            fetch_path = parsed.path or "/"
            if parsed.query:
                fetch_path = f"{fetch_path}?{parsed.query}"

            page_status, _, _, page_error = self._fetch(fetch_path)
            if page_error:
                status_failures.append(f"{url} ({page_error})")
                continue
            if page_status != 200:
                status_failures.append(f"{url} (HTTP {page_status})")

        if status_failures:
            self._record("Sitemap URLs return 200", False, "; ".join(status_failures))
        else:
            self._record("Sitemap URLs return 200", True, "all sitemap URLs returned HTTP 200")

    def _check_404(self) -> None:
        status, body, _, error = self._fetch("/404-test")
        if error:
            self._record("Custom 404 behavior", False, error)
            return

        body_lower = body.lower()
        looks_like_404 = "404" in body_lower or "not found" in body_lower
        passed = status == 404 or (status == 200 and looks_like_404)
        detail = f"HTTP {status}" if passed else f"Expected 404 behavior, got HTTP {status}"
        self._record("Custom 404 behavior", passed, detail)

    def _check_page_metadata(self, pages: Dict[str, str]) -> None:
        expected_image = f"{self.canonical_base_url}/assets/og-default.svg"
        title_index: Dict[str, List[str]] = {}
        desc_index: Dict[str, List[str]] = {}
        failures: List[str] = []

        for path, body in pages.items():
            for key, pattern in META_PATTERNS.items():
                if not pattern.search(body):
                    failures.append(f"{path} missing {key}")

            h1_count = len(re.findall(r"<h1\b", body, flags=re.IGNORECASE))
            if h1_count != 1:
                failures.append(f"{path} expected 1 h1, found {h1_count}")

            canonical_match = re.search(
                r'<link\s+rel=["\']canonical["\']\s+href=["\']([^"\']+)["\']',
                body,
                flags=re.IGNORECASE,
            )
            expected_canonical = self._canonical_url(path)
            if not canonical_match:
                failures.append(f"{path} missing canonical href")
            elif canonical_match.group(1).strip() != expected_canonical:
                failures.append(
                    f"{path} canonical mismatch ({canonical_match.group(1).strip()} != {expected_canonical})"
                )

            title_match = re.search(r"<title>(.*?)</title>", body, flags=re.IGNORECASE | re.DOTALL)
            if title_match:
                title = " ".join(title_match.group(1).split())
                if title:
                    title_index.setdefault(title, []).append(path)

            desc_match = re.search(
                r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']*)["\']',
                body,
                flags=re.IGNORECASE,
            )
            if desc_match:
                description = " ".join(desc_match.group(1).split())
                if description:
                    desc_index.setdefault(description, []).append(path)

            og_image_match = re.search(
                r'<meta\s+property=["\']og:image["\']\s+content=["\']([^"\']+)["\']',
                body,
                flags=re.IGNORECASE,
            )
            if og_image_match and og_image_match.group(1).strip() != expected_image:
                failures.append(f"{path} og:image mismatch")

            tw_image_match = re.search(
                r'<meta\s+name=["\']twitter:image["\']\s+content=["\']([^"\']+)["\']',
                body,
                flags=re.IGNORECASE,
            )
            if tw_image_match and tw_image_match.group(1).strip() != expected_image:
                failures.append(f"{path} twitter:image mismatch")

        for title, locations in title_index.items():
            if len(locations) > 1:
                failures.append(f"Duplicate <title> on {locations}: {title}")

        for description, locations in desc_index.items():
            if len(locations) > 1:
                failures.append(f"Duplicate description on {locations}: {description}")

        if failures:
            self._record("Live metadata parity", False, "; ".join(failures))
        else:
            self._record("Live metadata parity", True, "all indexable pages meet metadata contract")

    def _check_jsonld(self, pages: Dict[str, str]) -> None:
        failures: List[str] = []
        pattern = re.compile(
            r'<script\s+type=["\']application/ld\+json["\']\s*>(.*?)</script>',
            flags=re.IGNORECASE | re.DOTALL,
        )

        for path, body in pages.items():
            blocks = pattern.findall(body)
            for i, block in enumerate(blocks, start=1):
                snippet = block.strip()
                if not snippet:
                    failures.append(f"{path} empty JSON-LD block #{i}")
                    continue
                try:
                    json.loads(snippet)
                except json.JSONDecodeError as exc:
                    failures.append(f"{path} invalid JSON-LD block #{i} ({exc})")

        if failures:
            self._record("Live JSON-LD validity", False, "; ".join(failures))
        else:
            self._record("Live JSON-LD validity", True, "all JSON-LD blocks parsed")

    def _check_program_policy(self, pages: Dict[str, str]) -> None:
        body = pages.get("/programs.html", "")
        if not body:
            self._record("Program link policy", False, "/programs.html was not available for policy checks")
            return

        for pattern in BANNED_PROGRAM_PATTERNS:
            if re.search(pattern, body, flags=re.IGNORECASE):
                self._record("Program link policy", False, f"Prohibited checkout link pattern found: {pattern}")
                return

        if "truthjblue.com/" not in body:
            self._record("Program link policy", False, "Missing truthjblue.com program-page links")
            return

        self._record("Program link policy", True, "no checkout links present; program-page links present")

    def run(self) -> List[CheckResult]:
        pages = self._check_core_urls()
        self._check_about_alias()
        self._check_robots()
        self._check_sitemap()
        self._check_404()

        if pages:
            self._check_page_metadata(pages)
            self._check_jsonld(pages)
            self._check_program_policy(pages)

        return self.results


def render_markdown(canonical_base_url: str, fetch_base_url: str, results: List[CheckResult]) -> str:
    total = len(results)
    passed = sum(1 for result in results if result.passed)
    failed = total - passed
    run_time = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")
    gate = "PASS" if failed == 0 else "FAIL"

    lines = [
        "# Phase 6 Launch Gate Report",
        "",
        f"- Run (UTC): {run_time}",
        f"- Canonical Base URL: {canonical_base_url}",
        f"- Fetch Base URL: {fetch_base_url}",
        f"- Gate Status: {gate}",
        f"- Checks Passed: {passed}/{total}",
        "",
        "| Status | Check | Detail |",
        "| --- | --- | --- |",
    ]

    for result in results:
        status = "PASS" if result.passed else "FAIL"
        detail = result.detail.replace("|", "\\|").replace("\n", " ").strip()
        lines.append(f"| {status} | {result.name} | {detail} |")

    return "\n".join(lines) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run live launch-gate checks.")
    parser.add_argument(
        "--base-url",
        default="https://pub.jeremiahvanwagner.com",
        help="Canonical base URL contract (default: %(default)s)",
    )
    parser.add_argument(
        "--fetch-base-url",
        default=None,
        help="Optional fetch base URL when validating via alternate host (for example GitHub Pages URL).",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=20,
        help="HTTP timeout in seconds (default: %(default)s)",
    )
    parser.add_argument(
        "--insecure",
        action="store_true",
        help="Skip TLS certificate verification for diagnostics.",
    )
    parser.add_argument(
        "--output",
        default="docs/launch/reports/latest-launch-gate.md",
        help="Path for markdown report output (default: %(default)s)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    canonical_base = args.base_url.rstrip("/")
    fetch_base = args.fetch_base_url.rstrip("/") if args.fetch_base_url else canonical_base

    gate = LaunchGate(
        fetch_base_url=fetch_base,
        canonical_base_url=canonical_base,
        timeout=args.timeout,
        insecure=args.insecure,
    )
    results = gate.run()
    report = render_markdown(canonical_base, fetch_base, results)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report, encoding="utf-8")

    print(report)
    print(f"Report written to {output_path}")

    any_failed = any(not result.passed for result in results)
    return 1 if any_failed else 0


if __name__ == "__main__":
    sys.exit(main())
