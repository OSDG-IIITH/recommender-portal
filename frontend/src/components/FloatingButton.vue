<template>
  <v-card id="create">
    <v-speed-dial
      v-model="fab"
      :top="top"
      :bottom="bottom"
      :right="right"
      :left="left"
      :direction="direction"
      :open-on-hover="hover"
      :transition="transition"
    >
      <template v-slot:activator>
        <v-btn
          v-model="fab"
          color="blue darken-3"
          dark
          fab
        >
          <v-icon v-if="fab">mdi-close</v-icon>
          <v-icon v-else>mdi-plus</v-icon>
        </v-btn>
      </template>

      <v-bottom-sheet v-model="sheet" inset>
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            fab
            dark
            small
            color="grey darken-2"
            v-bind="attrs"
            v-on="on"
          >
            <v-icon>mdi-film</v-icon>
          </v-btn>
        </template>
        <v-sheet class="text-center" height="70vw">
          <v-btn
            class="mt-6"
            text
            color="red"
            @click="sheet = !sheet"
          >
            close
          </v-btn>
          <div class="py-3">
            <StepperSheet :steppersheet="steppersheet"/>
          </div>
        </v-sheet>
      </v-bottom-sheet>

      <v-bottom-sheet v-model="sheet" inset>
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            fab
            dark
            small
            color="yellow darken-3"
            v-bind="attrs"
            v-on="on"
          >
            <v-icon>mdi-fire</v-icon>
          </v-btn>
        </template>
        <v-sheet class="text-center" height="70vw">
          <v-btn
            class="mt-6"
            text
            color="red"
            @click="sheet = !sheet"
          >
            close
          </v-btn>
          <div class="py-3">
            <StepperSheet :steppersheet="steppersheet"/>
          </div>
        </v-sheet>
      </v-bottom-sheet>

      <v-bottom-sheet v-model="sheet" inset>

        <template v-slot:activator="{ on, attrs }">
          <v-btn
            fab
            dark
            small
            color="pink"
            v-bind="attrs"
            v-on="on"
          >
            <v-icon>mdi-movie</v-icon>
          </v-btn>
        </template>

        <v-sheet class="text-center" height="70vw">
          <v-btn
            class="mt-6"
            text
            color="red"
            @click="sheet = !sheet"
          >
            close
          </v-btn>
          <div class="py-3">
            <StepperSheet :steppersheet="steppersheet"/>
          </div>
        </v-sheet>
      </v-bottom-sheet>

      <v-bottom-sheet v-model="sheet" inset>
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            fab
            dark
            small
            color="indigo"
            v-bind="attrs"
            v-on="on"
          >
            <v-icon>mdi-music-note</v-icon>
          </v-btn>
        </template>
        <v-sheet class="text-center" height="70vw">
          <v-btn
            class="mt-6"
            text
            color="red"
            @click="sheet = !sheet"
          >
            close
          </v-btn>
          <div class="py-3">
            <StepperSheet :steppersheet="steppersheet"/>
          </div>
        </v-sheet>
      </v-bottom-sheet>

      <v-bottom-sheet v-model="sheet" inset>
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            fab
            dark
            small
            color="green darken-2"
            v-bind="attrs"
            v-on="on"
          >
            <v-icon>mdi-book-variant</v-icon>
          </v-btn>
        </template>
        <v-sheet class="text-center" height="70vw">
          <v-btn
            class="mt-6"
            text
            color="red"
            @click="sheet = !sheet"
          >
            close
          </v-btn>
          <div class="py-3">
            <StepperSheet :steppersheet="steppersheet"/>
          </div>
        </v-sheet>
      </v-bottom-sheet>
      
      
    </v-speed-dial>
  </v-card>
</template>

<script>
  import StepperSheet from '@/components/StepperSheet'
  export default {
    name: 'FloatingButton',
    props: {
        floatingbutton: Object
    },
    components: {
        StepperSheet
    },
    data: () => ({
      sheet:false,
      direction: 'top',
      fab: false,
      fling: false,
      hover: false,
      tabs: null,
      top: false,
      right: true,
      bottom: true,
      left: false,
      transition: 'slide-y-reverse-transition',
    }),

    // computed: {
    //   activeFab () {
    //     switch (this.tabs) {
    //       case 'one': return { class: 'pink', icon: 'movie' }
    //       case 'two': return { class: 'pink', icon: 'movie' }
    //       case 'three': return { class: 'pink', icon: 'movie' }
    //       case 'four': return { class: 'pink', icon: 'movie' }
    //       case 'five': return { class: 'pink', icon: 'movie' }
    //       default: return {}
    //     }
    //   },
    // },

    watch: {
      top (val) {
        this.bottom = !val
      },
      right (val) {
        this.left = !val
      },
      bottom (val) {
        this.top = !val
      },
      left (val) {
        this.right = !val
      },
    },
  }
</script>

<style>
  #create .v-speed-dial {
    position: fixed;
  }

  #create .v-btn--floating {
    position: relative;
  }
</style>

