<template>
    <div class="add-post">
        <v-content>
            <AddItemButton :openSheet="openSheet" :currPage="currPage" />
            <v-bottom-sheet v-model="sheet" inset>
                <AddItemSheet
                    :closeSheet="closeSheet"
                    :sheetType="sheetType"
                    :stepNum="stepNum"
                />
            </v-bottom-sheet>
        </v-content>
    </div>
</template>
<script>
import AddItemButton from './AddItemButton'
import AddItemSheet from './AddItemSheet'

export default {
  name: 'AddItem',
  props: {
    currPage: String
  },
  components: {
    AddItemButton,
    AddItemSheet
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
