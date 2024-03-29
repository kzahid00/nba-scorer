/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.{html,htm}"],
  theme: {
    extend: {
      colors: {
        'darkmode': '#292929',
        'white': '#fff',
        'darkcompliment' : '#191a1c'
      },
    },    
  },
  plugins: [],
}

