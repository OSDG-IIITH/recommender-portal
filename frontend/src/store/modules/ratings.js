import itemsApi from "../../api/items";

const state = () => [];

const getters = {};

const actions = {
    async upsertRating({ commit }, payload) {
        const { _id: item_id, rating, category_id } = payload;

        // Call the API first
        await itemsApi
            .rateItem(category_id, item_id, rating)
            .then(rating_res => {
                // Del the prev rating
                commit("DEL_RATING", { item_id });

                // add new rating
                commit("ADD_RATING", { item_id, rating });
            })
            .catch(err => console.error(err));
    }
};

const mutations = {
    INIT_RATINGS: (state, { ratings }) => {
        const rating_list = [];
        for (let category in ratings) {
            for (let _id in ratings[category]) {
                rating_list.push({
                    _id,
                    rating: ratings[category][_id].rating
                });
            }
        }
        state.push(...rating_list);
    },
    ADD_RATING: (state, payload) => {
        state.push({
            _id: payload.item_id,
            rating: payload.rating
        });
    },
    DEL_RATING: (state, payload) => {
        const index = state.findIndex(
            rating_list => rating_list["_id"] === payload.item_id
        );
        if (index !== -1) state.splice(index, 1);
    }
};

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
};
