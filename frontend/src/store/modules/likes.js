import itemsApi from "../../api/items";

const state = () => [];

const getters = {};

const actions = {
    async upsertLike({ commit }, payload) {
        const {_id: item_id, value, category_id} = payload;

        await itemsApi
            .likeItem(category_id, item_id, value)
            .then(res_item => {
                commit("DEL_LIKE", {item_id});
                commit("ADD_LIKE", {item_id, value});
            })
            .catch(err => console.log(err));
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
            value: payload.value});
    },
    DEL_LIKE: (state, payload) => {
        const index = state.findIndex(
            likes => likes["_id"] === payload.item_id
        );
        if(index !== -1) state.splice(index, 1);
    }
};

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
};
