<template>
    <div class="add-post">
        <v-content>
            <FloatingButton :openSheet="openSheet" :currPage="currPage" />
            <v-bottom-sheet v-model="sheet" inset>
                <StepperSheet
                    :closeSheet="closeSheet"
                    :sheetType="sheetType"
                    :stepNum="stepNum"
                />
            </v-bottom-sheet>
        </v-content>
    </div>
</template>

<script>
import FloatingButton from './FloatingButton'
import StepperSheet from './StepperSheet'

export default {
  name: 'AddPost',
  props: {
    currPage: String
  },
  components: {
    FloatingButton,
    StepperSheet
  },
  data: () => ({
    drawer: null,
    sheetType: null,
    sheet: false,
    stepNum: 1,
    current: 'Home'
  }),
  methods: {
    closeSheet: function () {
      this.sheet = false
    },
    openSheet: function (sheetType) {
      this.stepNum = 1
      this.sheetType = sheetType
      this.sheet = true
    }
  }
}
</script>
