// root level mutations

export default {
    INIT_CATEGORIES: async (state, { categories }) => {
        state.categories = categories;
    }
};
