<template>
    <div class="home">
        <v-content>
            <v-container fluid>
                <p>
                    <v-btn @click="check">Dummy </v-btn>
                    <v-btn
                        @click="
                            () => {
                                isAuthenticated ? logout() : login();
                            }
                        "
                        >{{ isAuthenticated ? "Logout" : "Login" }}
                    </v-btn>
                </p>
                <span>
                    Lorem ipsum, dolor sit amet consectetur adipisicing elit.
                    Quam harum quidem asperiores dolore fugiat inventore vitae
                    corporis libero eos, facere dolorem nam, deserunt error
                    velit cum temporibus accusantium exercitationem enim!
                </span>
            </v-container>
        </v-content>
    </div>
</template>

<script>
import { mapActions, mapState } from "vuex";

export default {
    name: "Home",
    computed: mapState({
        isAuthenticated: state => state.isAuthenticated
    }),
    methods: {
        ...mapActions({
            logout: "logOut"
        }),
        check: function() {
            console.log("DEBUG Function!");
            // NOTE: Do your debuging of actions / mutations here
        },
        login: function() {
            window.location.href =
                "https://login.iiit.ac.in/cas/login?service=http://0.0.0.0:8000/login";
        }
    }
};
</script>
