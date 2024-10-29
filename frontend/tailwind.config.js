/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/**/*.{html,jsx,tsx,vue,js,ts}"],
  theme: {
    extend: {
      backgroundColor: {
				'primary': 'var(--color-bg-primary)',
				'secondary': 'var(--color-bg-secondary)',
				'tatary': 'var(--color-bg-tatary)',
				'btn-primary': 'var(--color-bg-btn-primary)',
				'btn-secondary': 'var(--color-bg-btn-secondary)',
			},
      textColor:{
        'primary': 'var(--color-text-primary)',
        'secondary': 'var(--color-text-secondary)',
      }
    },
  },
  plugins: [],
}

