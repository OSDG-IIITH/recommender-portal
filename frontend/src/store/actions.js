// root level actions
import category from "../api/category";
import userStore from "../api/users";
import { setAuthToken, removeAuthToken } from "../api/authToken";

export default {
    async getCategories({ commit }) {
        await category
            .getCategories()
            .then(categories => {
                console.log(categories);
                commit("INIT_CATEGORIES", { categories: categories.data });
            })
            .catch(err => console.error(err));
    },
    async getToken({ commit }, { ticket }) {
        commit("START_LOGIN");
        await userStore
            .login(ticket)
            .then(token_res => {
                const token = token_res.data.token;
                setAuthToken(token);
                commit("ADD_TOKEN", { token });
            })
            .catch(err => console.error(err));
    },
    logOut({ commit }) {
        removeAuthToken();
        commit("REMOVE_TOKEN");
    }
};
