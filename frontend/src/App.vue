<template>
    <v-app>
        <Navbar />
        <v-content>
            <v-btn @click="onClick"> 1</v-btn>
            <v-btn @click="onClick2">2</v-btn>
            <v-btn @click="onClick3">3</v-btn>
            <v-btn @click="onClick4">4</v-btn>
            <router-view />
            <FloatingButton :openSheet="openSheet" />
            <v-bottom-sheet v-model="sheet" inset>
                <StepperSheet
                    :closeSheet="closeSheet"
                    :sheetType="sheetType"
                    :stepNum="stepNum"
                />
            </v-bottom-sheet>
        </v-content>
    </v-app>
</template>

<script>
import { mapActions, mapMutations } from "vuex";

import Navbar from "./components/Navbar";
import FloatingButton from "./components/FloatingButton";
import StepperSheet from "./components/StepperSheet";

export default {
    name: "App",
    props: {
        source: String
    },
    components: {
        Navbar,
        FloatingButton,
        StepperSheet
    },
    data: () => ({
        drawer: null,
        sheet: false,
        stepNum: 1
    }),
    methods: {
        ...mapActions({
            addItem: "items/addItem"
        }),
        ...mapMutations(["INIT_LIKES"]),
        onClick: async function() {
            const obj = {
                flags: [],
                hidden: false,
                title: "test2",
                url: "http://test.com",
                year_release: 2010,
                genres: [],
                language: "hindi",
                director: "me",
                streaming: "hotstar"
            };
            console.log("hi");
            console.log("before");
            console.log(obj);
            await this.addItem({ category: "movies", ...obj });
            console.log("after");
        },
        onClick2: function() {
            this.$store.commit("likes/INIT_LIKES", {
                likes: {
                    movies: {
                        "5eeb4f1de814bee6f814d628": 1,
                        "5eee5b4989429fe5ccefc549": -1,
                        "5eee5d1c89429fe5ccefc550": 1
                    }
                }
            });
        },
        onClick3: async function() {
            await this.$store.dispatch("user/getCurrentUserData");
        },
        closeSheet: function() {
            this.sheet = false;
        },
        openSheet: function(sheetType) {
            this.stepNum = 1;
            this.sheetType = sheetType;
            this.sheet = true;
        }
    }
};
</script>
