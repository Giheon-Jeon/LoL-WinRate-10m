/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'bg-deep': '#05070a',
        'bg-card': 'rgba(15, 18, 26, 0.85)',
        'gold-bright': '#f0e6d2',
        'gold-main': '#c8aa6e',
        'gold-dark': '#785a28',
        'blue-team': '#1f8ece',
        'red-team': '#e84057',
        'text-primary': '#f0f0f0',
        'text-secondary': '#a0a0a0',
        'border-glass': 'rgba(200, 170, 110, 0.2)',
      },
      boxShadow: {
        'glow': '0 0 25px rgba(200, 170, 110, 0.15)',
        'glow-blue': '0 0 15px rgba(31, 142, 206, 0.3)',
        'glow-red': '0 0 15px rgba(232, 64, 87, 0.3)',
        'glow-gold': '0 0 15px rgba(200, 170, 110, 0.3)',
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        outfit: ['Outfit', 'sans-serif'],
      }
    },
  },
  plugins: [],
}
