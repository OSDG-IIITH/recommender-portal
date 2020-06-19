<template>
  <v-app>
    <Navbar :current="$route.name"/>
    <v-content>
      <router-view/>
      <!-- <FloatingButton :openSheet="openSheet" :currPage="$route.name" />
      <v-bottom-sheet v-model="sheet" inset>
        <StepperSheet :closeSheet="closeSheet" :sheetType="sheetType" :stepNum="stepNum"/>
      </v-bottom-sheet> -->
      <AddPost :currPage="$route.name"/>
    </v-content>
  </v-app>
</template>

<script>
import Navbar from './components/Navbar'
import AddPost from './components/AddPost'
// import FloatingButton from './components/FloatingButton'
// import StepperSheet from './components/StepperSheet'



export default {
  name: 'App',
  props: {
      source: String,
  },
  components: {
    Navbar,
    AddPost
    // FloatingButton,
    // StepperSheet
  },
  data: () => ({
    drawer: null,
    sheet: false,
    stepNum: 1,
    currPage: 'Home',
    current: 'Home'
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
