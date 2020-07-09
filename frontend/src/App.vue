<template>
    <v-app color="#EDEBD7">
        <Navbar :current="$route.name" />
        <v-main>
            <v-content>
                <router-view />
                <AddItem :currPage="$route.name" />
            </v-content>
        </v-main>
    </v-app>
</template>

<script>
import Navbar from '@/components/Navbar'
import AddItem from '@/components/AddItem'
export default {
  name: 'App',
  props: {
    source: String
  },
  components: {
    Navbar,
    AddItem
  },
  data: () => ({
    drawer: null,
    sheet: false,
    stepNum: 1,
    currPage: 'Home',
    current: 'Home'
  }),
  created () {
    this.$store.dispatch('user/getCurrentUserData')
  },
  methods: {
    closeSheet: function () {
      this.sheet = false
    },
    openSheet: function (sheetType) {
      this.stepNum = 1
      this.sheetType = sheetType
      this.sheet = true
    },
    changeCurrPage: function (newCurrPage) {
      this.currPage = newCurrPage
    }
  }
}
</script>
