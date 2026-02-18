export default function HomePage() {
  return (
    <main style={{ maxWidth: 980, margin: "0 auto", padding: "2rem 1rem 3rem" }}>
      <section style={{ border: "1px solid var(--line)", background: "var(--card)", borderRadius: 18, padding: "1.5rem" }}>
        <p style={{ marginTop: 0, textTransform: "uppercase", letterSpacing: ".08em", fontSize: ".75rem", color: "var(--brand)", fontWeight: 700 }}>
          Framework Scaffold
        </p>
        <h1 style={{ marginTop: 0 }}>Truth J Blue Next.js Workspace</h1>
        <p>
          Next.js and Tailwind are now installed for future framework development. Your live production site still deploys
          from the static <code>site/</code> directory.
        </p>
        <ul>
          <li>Run <code>npm run dev</code> to start local Next development.</li>
          <li>Run <code>npm run build</code> to verify production framework builds.</li>
          <li>Static launch site remains at <code>site/</code> and is unaffected.</li>
        </ul>
        <p>
          Continue building in this app while keeping the existing GitHub Pages deployment stable.
        </p>
      </section>
    </main>
  );
}
