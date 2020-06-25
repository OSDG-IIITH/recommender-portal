<template>
  <v-app color="#EDEBD7">
    <Navbar :current="$route.name" />
    <v-main>
      <v-content>
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
    }
  }
};
</script>
