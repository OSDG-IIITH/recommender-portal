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
    ADD_LIKE: (state, payload) => {
        state.push({
            _id: payload.item_id, 
            value: payload.value})
    },
    DEL_LIKE: (state, payload) => {
        index = state.findIndex(likes => likes["_id"] == payload.item_id)
        state.splice(index, 1)
    }
};

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
};
