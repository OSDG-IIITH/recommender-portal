// root level actions
import category from "../api/category";

export default {
    async getCategories({ commit }) {
        await category
            .getCategories()
            .then(categories => {
                console.log(categories);
                commit("INIT_CATEGORIES", { categories: categories.data });
            })
            .catch(err => console.error(err));
    }
};
