import "./globals.css";

export const metadata = {
  title: "Truth J Blue Framework Workspace",
  description: "Next.js framework workspace for Truth J Blue publication system.",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
