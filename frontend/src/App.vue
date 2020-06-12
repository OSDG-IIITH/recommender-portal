<template>
  <v-app>
    <Navbar :drawer="drawer"/>
    <v-app-bar
      app
      color="indigo"
      dark
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>Recommender@IIIT-H</v-toolbar-title>
    </v-app-bar>
    <v-content>
      <router-view/>
      <FloatingButton :openSheet="openSheet" />
      <v-bottom-sheet v-model="sheet" inset>
        <StepperSheet :closeSheet="closeSheet" :sheetType="sheetType" :stepNum="stepNum"/>
      </v-bottom-sheet>
    </v-content>
  </v-app>
</template>

<script>
import Navbar from './components/Navbar'
import FloatingButton from './components/FloatingButton'
import StepperSheet from './components/StepperSheet'

export default {
  name: 'App',
  props: {
      source: String,
  },
  components: {
    Navbar,
    FloatingButton,
    StepperSheet
  },
  data: () => ({
    drawer: null,
    sheet: false,
    stepNum: 1,
  }),
  methods: {
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
