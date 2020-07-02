<template>
    <v-app color="#EDEBD7">
        <Navbar :current="$route.name" />
        <v-main>
            <v-content>
                <v-btn @click="check">Dummy </v-btn>
                <router-view />
                <AddPost :currPage="$route.name" />
            </v-content>
        </v-main>
    </v-app>
</template>

<script>
import Navbar from "@/components/Navbar";
import AddPost from "@/components/AddPost";
export default {
    name: "App",
    props: {
        source: String
    },
    components: {
        Navbar,
        AddPost
    },
    data: () => ({
        drawer: null,
        sheet: false,
        stepNum: 1,
        currPage: "Home",
        current: "Home"
    }),
    created() {
        this.$store.dispatch("user/getCurrentUserData");
    },
    methods: {
        closeSheet: function() {
            this.sheet = false;
        },
        openSheet: function(sheetType) {
            this.stepNum = 1;
            this.sheetType = sheetType;
            this.sheet = true;
        },
        changeCurrPage: function(newCurrPage) {
            this.currPage = newCurrPage;
        },
        check: function() {
            // Do your debuging of actions / mutations here
        }
    }
};
</script>
