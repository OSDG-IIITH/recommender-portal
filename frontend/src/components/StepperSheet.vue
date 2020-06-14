<template>

    <v-stepper v-model="stepNum" vertical>

        <v-stepper-step :complete="stepNum > 1" step="1">
            Step 1
            <small>Basic Details</small>
        </v-stepper-step>
        <v-stepper-content step="1">
            <v-textarea height="200px"></v-textarea>
            <v-btn color="primary" @click="stepNum = 2">Continue</v-btn>
            <v-btn text @click="closeSheet">Cancel</v-btn>
        </v-stepper-content>

        <v-stepper-step step="2">
            Step 2
            <small>Specifics</small>
        </v-stepper-step>
        <v-stepper-content step="2">
            <v-textarea height="200px"></v-textarea>
            <v-btn color="primary" @click="closeSheet">Submit</v-btn>
            <v-btn text @click="closeSheet">Cancel</v-btn>
        </v-stepper-content>

        </v-stepper>

</template>

<script>
export default {
  name: 'StepperSheetTemp',
  props: {
    stepNum: Number,
    closeSheet: Function,
    sheetType: String
  }
}
</script>
