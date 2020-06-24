import Vue from 'vue'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import colors from 'vuetify/lib/util/colors'

Vue.use(Vuetify)

const opts = {
  theme: {
    themes: {
      light: {
        primary: colors.shades.black,
        secondary: "#847271",
      },
      dark: {
        primary: colors.shades.white,
        secondary: "#616161",
      },
    },
  },
}

export default new Vuetify(opts)
