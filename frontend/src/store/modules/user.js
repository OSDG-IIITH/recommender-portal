import usersApi from "../../api/users";

const state = () => ({
    userData: {}
});

const getters = {};

const actions = {
    async getCurrentUserData({ commit }) {
        await usersApi
            .getCurrentUser()
            .then(currentUser => {
                commit("ADD_USERDATA", { userData: currentUser.data });
                commit(
                    "likes/INIT_LIKES",
                    { likes: currentUser.data.likes },
                    { root: true }
                );
                commit(
                    "ratings/INIT_RATINGS",
                    { ratings: currentUser.data.ratings },
                    { root: true }
                );
            })
            .catch(err => {
                console.error(err);
            });
    }
};

const mutations = {
    ADD_USERDATA: (state, { userData }) => {
        state.userData = userData;
    },
    REMOVE_USERDATA: state => {
        state.userData = {};
    }
};

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
};
