<template>
    <v-app>
        <Navbar />
        <v-content>
            <v-btn @click="dummyMethod">DUMMY COMPONENT</v-btn>
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
        async dummyMethod() {
            // dummy method to test the integration you can call any action here using this.$store.dispatch()
            console.log("DEBUG");
            // do your work here
            console.log("/DEBUG");
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
