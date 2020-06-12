<template>
  <div id="float-button">
    <v-speed-dial
      v-model="fab"
      bottom
      right
      direction="top"
      transition='slide-y-reverse-transition'
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

      <v-btn
          fab
          dark
          small
          color="grey darken-2"
          @click="openSheet('Shows')"
      >
        <v-icon>mdi-film</v-icon>
      </v-btn>

      <v-btn
          fab
          dark
          small
          color="yellow darken-3"
          @click="openSheet('Anime')"
      >
        <v-icon>mdi-fire</v-icon>
      </v-btn>

      <v-btn
          fab
          dark
          small
          color="indigo"
          @click="openSheet('Music')"
      >
        <v-icon>mdi-music-note</v-icon>
      </v-btn>

      <v-btn
          fab
          dark
          small
          color="pink"
          @click="openSheet('Movies')"
      >
        <v-icon>mdi-movie</v-icon>
      </v-btn>

      <v-btn
          fab
          dark
          small
          color="green darken-2"
          @click="openSheet('Books')"
      >
        <v-icon>mdi-book</v-icon>
      </v-btn>

    </v-speed-dial>
  </div>
</template>

<script>
  export default {
    name: 'FloatingButtonTemp',
    props: {
      openSheet: Function,
    },
    data: () => ({
      fab: false,
    })
  };
</script>

<style>
  #float-button {
    position: fixed;
    bottom: 0;
    right: 0;
  }
</style>