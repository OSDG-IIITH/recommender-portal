// root level mutations

export default {
    INIT_CATEGORIES: (state, { categories }) => {
        state.categories = categories;
    },
    ADD_TOKEN: (state, { token }) => {
        state.token = token;
        state.isAuthenticated = true;
        state.loading = false;
    },
    REMOVE_TOKEN: state => {
        state.token = null;
        state.isAuthenticated = false;
    },
    START_LOGIN: state => {
        state.token = null;
        state.isAuthenticated = false;
        state.loading = true;
    }
};
