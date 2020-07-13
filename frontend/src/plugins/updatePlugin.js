export default function(store) {
    store.subscribe((mutation, state) => {
        switch (mutation.type) {
            case "likes/INIT_LIKES":
            case "likes/ADD_LIKE":
                store.commit("items/SET_LIKES", { likes: state.likes });
                break;
            case "ratings/INIT_RATINGS":
            case "ratings/ADD_RATING":
                store.commit("items/SET_RATINGS", { ratings: state.ratings });
                break;
            case "ADD_TOKEN":
                store.dispatch("user/getCurrentUserData");
                break;
            case "REMOVE_TOKEN":
                store.commit("user/REMOVE_USERDATA");
        }
    });
}
