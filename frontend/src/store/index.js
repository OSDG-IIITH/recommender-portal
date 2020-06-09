import Vue from 'vue'
import Vuex from 'vuex'
import category from './modules/category'
import search from './modules/search'
import user from './modules/user'
import createLogger from '../plugins/logger'

Vue.use(Vuex)

const debug = process.env.NODE_ENV !== 'production'

export default new Vuex.Store({
    modules: {
        category,
        search,
        user
    },
    strict: debug,
    plugins: debug ? [createLogger()] : []
})
