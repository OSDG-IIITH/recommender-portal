<template>
  <v-stepper v-model="stepNum" vertical dark>
    <h3 class="pa-2 ma-1 text-center text-sm-left text-overline">Add {{ sheetType }}</h3>
    <v-stepper-step :complete="stepNum > 1" step="1">
      Step 1
      <small>Common details</small>
    </v-stepper-step>
    <v-stepper-content step="1">
      <!-- Common fields form -->

      <FormCommon/>
      
      <v-btn color="secondary" @click="stepNum = 2">Continue</v-btn>
      <v-btn text @click="closeSheet">Cancel</v-btn>
    </v-stepper-content>

    <v-stepper-step step="2">
      Step 2
      <small>Extra details</small>
    </v-stepper-step>
    <v-stepper-content step="2">
      <!-- Actual schema depending on $route.name -->
      
      <FormSpecific :sheetType="sheetType"/>

      <v-btn color="secondary" @click="closeSheet">Submit</v-btn>
      <v-btn text @click="closeSheet">Cancel</v-btn>
    </v-stepper-content>
  </v-stepper>
</template>

<script>
import FormCommon from "@/components/FormCommon";
import FormSpecific from "@/components/FormSpecific";

export default {
  name: "StepperSheetTemp",
  components:{
    FormCommon,
    FormSpecific
  },
  props: {
    stepNum: Number,
    closeSheet: Function,
    sheetType: String
  }
};
</script>
