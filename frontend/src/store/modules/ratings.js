const state = () => [];

const getters = {};

const actions = {
    async upsertRating({ commit }, payload) {
        // TODO upsetRating to DB using itemsApi.rateItem function and commit ADD_RATING and DEL_RATING
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
    ADD_RATING: (state, rating) => {
        // TODO: add rating to state
    },
    DEL_RATING: (state, rating) => {
        // TODO: delete rating to state
    }
};

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
};
