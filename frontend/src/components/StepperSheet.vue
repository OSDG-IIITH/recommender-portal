<template>
  <v-stepper v-model="stepNum" vertical dark>
    <h3 class="pa-2 ma-1 text-center text-sm-left text-overline">Add {{ sheetType }}</h3>
    <v-stepper-step :complete="stepNum > 1" step="1">
      Step 1
      <small>Common details</small>
    </v-stepper-step>
    <v-stepper-content step="1">
      <!-- TODO add common fields form     -->
      <v-textarea>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Distinctio
        omnis dolorum, enim eum vitae rem iusto adipisci cumque perspiciatis
        illo unde facere aperiam aliquam est voluptates doloribus nobis tempora totam.
      </v-textarea>
      <v-btn color="secondary" @click="stepNum = 2">Continue</v-btn>
      <v-btn text @click="closeSheet">Cancel</v-btn>
    </v-stepper-content>

    <v-stepper-step step="2">
      Step 2
      <small>Extra details</small>
    </v-stepper-step>
    <v-stepper-content step="2">
      <!-- TODO add actual schema depending on $route.name -->
      <v-textarea>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Distinctio
        omnis dolorum, enim eum vitae rem iusto adipisci cumque perspiciatis
        illo unde facere aperiam aliquam est voluptates doloribus nobis tempora totam.
      </v-textarea>
      <v-btn color="secondary" @click="closeSheet">Submit</v-btn>
      <v-btn text @click="closeSheet">Cancel</v-btn>
    </v-stepper-content>
  </v-stepper>
</template>

<script>
export default {
  name: "StepperSheetTemp",
  props: {
    stepNum: Number,
    closeSheet: Function,
    sheetType: String
  }
};
</script>