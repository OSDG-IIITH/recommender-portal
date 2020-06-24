import Vue from 'vue'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'

Vue.use(Vuetify)

const opts = {
    theme: {
        themes: {
          light: {
            primary: '#3f51b5',
            secondary: '#ffe6ff',
            anchor: '#8c9eff',
          },
        },
    },
}

export default new Vuetify(opts)
