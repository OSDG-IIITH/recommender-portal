import itemsApi from "../../api/items";

const state = () => ({
    data: {}
});

const getters = {
    getItemsByCategory: state => category => {
        // TODO: filter state items for category
    },
    getItemsById: state => id => state.data[id]
};

const actions = {
    async addItem({ commit }, item) {
        await itemsApi
            .addItem(item.category, item)
            .then(item_res => {
                commit("ADD_ITEM", { item: item_res });
            })
            .catch(err => console.error(err));
    },
    async updateItem({ commit }, item) {
        // TODO: implement update item
    },
    async fetchItems({ commit }, categoryId) {
        // TODO: implement fetch items and commit ADD_ITEM for all

        // Set likes and rating for them this should be in then
        commit("SET_LIKES");
        commit("SET_RATINGS");
    }
};

const mutations = {
    ADD_ITEM: (state, { item: { data } }) => {
        state.data = {
            ...state.data,
            [data._id]: data
        };
    },
    DEL_ITEM: (state, { itemId }) => {
        // TODO: DEL item mutation
    },
    SET_LIKES: (state, { likes }) => {
        likes
            .filter(like => like._id in state.data)
            .forEach(like => {
                state.data[like._id]["like"] = like.value;
            });
    },
    SET_RATINGS: (state, { ratings }) => {
        ratings
            .filter(rating => rating._id in state.data)
            .forEach(rating => {
                state.data[rating._id]["rating"] = rating.rating;
            });
    }
};

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
};
