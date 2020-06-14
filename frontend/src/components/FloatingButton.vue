<template>
  <div id="float-button">
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
        <v-btn v-model="fab" color="blue darken-3" dark fab>
          <v-icon v-if="fab">mdi-close</v-icon>
          <v-icon v-else>mdi-plus</v-icon>
        </v-btn>
      </template>

      <v-tooltip left>
        <template v-slot:activator="{on,attrs}">
          <v-btn fab dark small color="grey darken-2" @click="openSheet('Shows')">
            <v-icon>mdi-film</v-icon>
          </v-btn>
        </template>
        <span>Add Show</span>
      </v-tooltip>

      <v-btn fab dark small color="yellow darken-3" @click="openSheet('Anime')">
        <v-icon>mdi-fire</v-icon>
      </v-btn>

      <v-btn fab dark small color="indigo" @click="openSheet('Music')">
        <v-icon>mdi-music-note</v-icon>
      </v-btn>

      <v-btn fab dark small color="pink" @click="openSheet('Movies')">
        <v-icon>mdi-movie</v-icon>
      </v-btn>

      <v-btn fab dark small color="green darken-2" @click="openSheet('Books')">
        <v-icon>mdi-book</v-icon>
      </v-btn>
    </v-speed-dial>
  </div>
</template>

<script>
export default {
  name: "FloatingButtonTemp",
  props: {
    openSheet: Function
  },
  data: () => ({
    direction: "top",
    fab: false,
    fling: false,
    hover: true,
    tabs: null,
    top: false,
    right: true,
    bottom: true,
    left: false,
    transition: "slide-y-reverse-transition"
  }),

  computed: {
    activeFab() {
      switch (this.tabs) {
        case "one":
          return { class: "purple", icon: "account_circle" };
        case "two":
          return { class: "red", icon: "edit" };
        case "three":
          return { class: "green", icon: "keyboard_arrow_up" };
        default:
          return {};
      }
    }
  }
};
</script>

<style>
#float-button .v-btn--floating {
  position: absolute;
  bottom: 0.5rem;
  right: 0.5rem;
}
#float-button .v-speed-dial {
  position: absolute;
}
</style>
