export default function(store) {
    store.subscribe((mutation, state) => {
        switch (mutation.type) {
            case "likes/INIT_LIKES":
            case "likes/UPSERT_LIKE":
                store.commit("items/SET_LIKES", { likes: state.likes });
                break;
            case "ratings/INIT_RATINGS":
            case "ratings/UPSERT_RATING":
                store.commit("items/SET_RATINGS", { ratings: state.ratings });
                break;
        }
    });
}
