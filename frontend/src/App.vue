<template>
  <v-app>
    <Navbar />
    <v-content>
      <v-btn @click="getitems()"> Hii</v-btn>
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
import users from "./api/users";

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
    getitems: async () => {
      try {
        const obj = {
          title: "test2",
          url: "http://test.com",
          year_release: 2010,
          language: "hindi",
          director: "me",
          streaming: "hotstar"
        };

        console.log("before");
        const a = await users.getCurrentUser();
        console.log(a);
        console.log("after");
      } catch (err) {
        console.error(err.response.data);
      }
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
