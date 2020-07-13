import Vue from "vue";
import Vuex from "vuex";
import rootActions from "./actions";
import rootMutaions from "./mutations";
import items from "./modules/items";
import likes from "./modules/likes";
import ratings from "./modules/ratings";
import user from "./modules/user";
import createLogger from "../plugins/logger";
import updatePlugin from "../plugins/updatePlugin";

Vue.use(Vuex);

const debug = process.env.NODE_ENV !== "production";

export default new Vuex.Store({
    // root level state
    state: {
        categories: [],
        token: null,
        isAuthenticated: false,
        loading: false
    },
    actions: rootActions,
    mutations: rootMutaions,
    modules: {
        items,
        likes,
        ratings,
        user
    },
    strict: debug,
    plugins: debug ? [createLogger(), updatePlugin] : []
});
