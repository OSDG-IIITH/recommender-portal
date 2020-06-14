<template>
  <v-app>
    <Navbar/>
    <v-content>
      <SearchBox/>
      <router-view/>
      <FloatingButton :openSheet="openSheet" :currPage="currPage" />
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
import SearchBox from './components/SearchBox'

export default {
  name: 'App',
  props: {
      source: String,
  },
  components: {
    Navbar,
    FloatingButton,
    StepperSheet,
    SearchBox
  },
  data: () => ({
    drawer: null,
    sheet: false,
    stepNum: 1,
    currPage: 'Movies'
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
