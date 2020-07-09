<template>
    <v-stepper v-model="stepNum" vertical dark>
        <v-overlay :absolute="true" :value="overlay">
            <v-progress-circular indeterminate size="64"></v-progress-circular>
        </v-overlay>
        <h3 class="pa-2 ma-1 text-center text-sm-left text-overline white--text">
            Add {{ sheetType }}
        </h3>
        <v-stepper-step :complete="stepNum > 1" step="1">
            Step 1
            <small>Common details</small>
        </v-stepper-step>
        <v-stepper-content step="1">
            <!-- Common fields form -->
            <FormCommon v-on:continue="submit1" v-on:cancel="closeSheet" />
        </v-stepper-content>

        <v-stepper-step step="2">
            Step 2
            <small>Extra details</small>
        </v-stepper-step>
        <v-stepper-content step="2">
            <!-- Actual schema depending on $route.name -->

            <FormSpecific
                :sheetType="sheetType"
                v-on:continue="submit2"
                v-on:cancel="closeSheet"
            />
        </v-stepper-content>
    </v-stepper>
</template>

<script>
import FormCommon from '@/components/FormCommon'
import FormSpecific from '@/components/FormSpecific'

export default {
  name: 'StepperSheetTemp',
  components: {
    FormCommon,
    FormSpecific
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
    submit1: function (data) {
      // get back data
      this.formData = JSON.parse(data)

      // convert flags to array
      if (this.formData.flags) {
        this.formData.flags = this.formData.flags
          .split(',')
          .map(a => a.trim())
      }

      // convert genres to array
      if (this.formData.genres) {
        this.formData.genres = this.formData.genres
          .split(',')
          .map(a => a.trim())
      }

      this.stepNum = 2
    },

    submit2: async function (data) {
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
    }
  }
}
</script>
