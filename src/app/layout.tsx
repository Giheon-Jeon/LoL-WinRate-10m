import type { Metadata } from "next";
import { Inter, Cinzel } from "next/font/google";
import "./globals.css";

const inter = Inter({
  subsets: ["latin"],
  variable: "--font-inter",
  display: "swap",
});

const cinzel = Cinzel({
  subsets: ["latin"],
  variable: "--font-cinzel",
  display: "swap",
});

export const metadata: Metadata = {
  title: "LoL early 10m Win-Rate Predictor | Hextech ML Lab",
  description: "Predict match outcomes based on early 10 minutes game data using various Machine Learning models including XGBoost, Random Forest, and Logistic Regression.",
  keywords: ["League of Legends", "Win Rate Predictor", "Machine Learning", "FastAPI", "Next.js", "XGBoost", "Hextech", "LoL analytics"],
  authors: [{ name: "Giheon Jeon" }],
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="ko" className={`${inter.variable} ${cinzel.variable}`}>
      <head>
        <link rel="icon" href="/favicon.ico" sizes="any" />
      </head>
      <body>
        {children}
      </body>
    </html>
  );
}
