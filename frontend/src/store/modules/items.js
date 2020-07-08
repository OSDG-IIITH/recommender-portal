import itemsApi from "../../api/items";

const state = () => ({
    data: {
        "5ef34628ab0e5c2b04ddf1c5": {
            _id: "5ef34628ab0e5c2b04ddf1c5",
            flags: [],
            hidden: false,
            title: "test2",
            url: "http://test.com",
            year_release: 2010,
            genres: [],
            seasons: 2,
            episode_length: 3,
            season_length: 3,
            streaming: null,
            category: "anime"
        }
    }
});

const getters = {
    getKeysByCategory: state => category => {
        if (!category) return Object.keys(state.data);

        return Object.keys(state.data).filter(
            key => state.data[key].category === category
        );
    },
    getItemById: state => id => state.data[id]
};

const actions = {
    async addItem({ commit }, item) {
        const category = item.category;
        delete item.category;
        await itemsApi
            .addItem(category, item)
            .then(item_res => {
                commit("ADD_ITEM", {
                    item: { data: { ...item_res.data, category } }
                });
            })
            .catch(err => console.error(err));
    },
    async updateItem({ commit, rootState }, item) {
        const category = item.category;
        delete item.category;
        // Call the api first
        await itemsApi.updateItem(category, item._id, item).then(item_res => {
            // Delete first
            commit("DEL_ITEM", { itemId: item._id });
            // then add
            commit("ADD_ITEM", {
                item: { data: { ...item_res.data, category } }
            });
        });
        commit("SET_LIKES", { likes: rootState.likes });
        commit("SET_RATINGS", { ratings: rootState.ratings });
    },
    async fetchItems({ commit, rootState }, categoryId) {
        await itemsApi
            .getItems(categoryId)
            .then(items => {
                items.data.forEach(item => {
                    commit("ADD_ITEM", {
                        item: { data: { ...item, category: categoryId } }
                    });
                });
            })
            .catch(err => console.error(err));

        commit("SET_LIKES", { likes: rootState.likes });
        commit("SET_RATINGS", { ratings: rootState.ratings });
    }
};

const mutations = {
    ADD_ITEM: (state, { item: { data } }) => {
        state.data = {
            ...state.data,
            [data._id]: {
                ...data,
                rating: 0,
                like: 0
            }
        };
    },
    DEL_ITEM: (state, { itemId }) => {
        delete state.data[itemId];
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
