<template>
    <v-stepper v-model="stepNum" vertical>
        <v-overlay :absolute="true" :value="overlay">
            <v-progress-circular indeterminate size="64"></v-progress-circular>
        </v-overlay>
        <h3 class="pa-2 ma-1 text-center text-sm-left text-overline white--text">
            Add {{ sheetType }}
        </h3>
        <v-stepper-step editable :complete="stepNum > 1" step="1"> Step 1 <small>Common details</small></v-stepper-step>
        <v-stepper-content step="1">
            <ItemCommonForm
              v-on:continue="commonSubmit"
              v-on:next="goToSpecific"
              v-on:cancel="cancel"
            />
        </v-stepper-content>

        <v-stepper-step editable step="2">Step 2 <small>Extra details</small></v-stepper-step>
        <v-stepper-content step="2">
            <ItemSpecificForm
                :sheetType="sheetType"
                v-on:continue="specificSubmit"
                v-on:previous="goToCommon"
                v-on:cancel="cancel"
            />
        </v-stepper-content>
    </v-stepper>
</template>

<script>
import ItemCommonForm from '@/components/ItemCommonForm'
import ItemSpecificForm from '@/components/ItemSpecificForm'

export default {
  name: 'AddItemSheet',
  components: {
    ItemCommonForm,
    ItemSpecificForm
  },
  props: {
    stepNum: Number,
    closeSheet: Function,
    sheetType: String
  },
  data () {
    return {
      overlay: false,
      formData: {}
    }
  },
  methods: {
    goToCommon: function (currentValid, changeSection = true) {
      this.specificValid = currentValid
      if (changeSection) this.stepNum = 1
    },
    goToSpecific: function (currentValid, changeSection = true) {
      this.commonValid = currentValid
      if (changeSection) this.stepNum = 2
    },
    commonSubmit: function (data) {
      // get back data
      this.formData = JSON.parse(data)
    },

    specificSubmit: async function (data) {
      this.formData = {
        ...this.formData,
        ...JSON.parse(data)
      }
      console.log(this.formData)

      // start loading
      this.overlay = true

      // call the action
      await this.$store.dispatch('items/addItem', {
        // so as to remove __ob__
        ...JSON.parse(JSON.stringify(this.formData)),
        category: this.sheetType
      })

      // stop loading
      this.overlay = false

      // close the sheet
      this.formData = {}
      this.closeSheet()
    },
    cancel: function () {
      this.formData = {}
      this.closeSheet()
    }
  }
}
</script>
