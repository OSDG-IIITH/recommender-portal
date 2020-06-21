import Vue from "vue";
import Vuex from "vuex";
import items from "./modules/items";
import likes from "./modules/likes";
import ratings from "./modules/ratings";
import user from "./modules/user";
import createLogger from "../plugins/logger";
import updateItem from "../plugins/updateItem";

Vue.use(Vuex);

const debug = process.env.NODE_ENV !== "production";

export default new Vuex.Store({
    modules: {
        items,
        likes,
        ratings,
        user
    },
    strict: debug,
    plugins: debug ? [createLogger(), updateItem] : []
});
