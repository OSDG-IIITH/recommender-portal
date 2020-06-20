const state = () => [];

const getters = {};

const actions = {
    async upsertLike({ commit }, payload) {
        // TODO upsetLike to DB using itemsApi.likeItem function and commit ADD_LIKE and DEL_LIKE
    }
};

const mutations = {
    INIT_LIKES: (state, { likes }) => {
        const likes_list = [];

        for (let category in likes) {
            for (let _id in likes[category]) {
                likes_list.push({
                    _id,
                    value: likes[category][_id]
                });
            }
        }
        state.push(...likes_list);
    },
    ADD_LIKE: (state, like) => {
        // TODO: Add like to state
    },
    DEL_LIKE: (state, like) => {
        // TODO: Del like from state
    }
};

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
};
