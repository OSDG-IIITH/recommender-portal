<template>
  <div id="float-button">
    <v-speed-dial
      open-on-hover = true
      v-model="fab"
      bottom
      right
      direction="top"
      transition='slide-y-reverse-transition'
    >
      <template v-slot:activator>
        <div v-if="currPage === 'Home'">
        <v-btn
          v-model="fab"
          color="blue darken-3"
          dark
          fab
        >
          <v-icon v-if="fab">mdi-close</v-icon>
          <v-icon v-else>mdi-plus</v-icon>
        </v-btn>
        </div>
        <div v-else>
          <div v-for="item in categories" :key="item.title">
            <v-btn
            v-if="item.title === currPage"
            fab
            dark
            small
            :color="item.color"
            @click="openSheet(item.title)"
            >
              <v-icon>{{ item.icon }}</v-icon>
            </v-btn>
          </div>
        </div>
      </template>
      
      <div v-for="item in categories" :key="item.title">
      <v-btn
          v-if="item.title !== currPage"
          fab
          dark
          small
          :color="item.color"
          @click="openSheet(item.title)"
      >
        <v-icon>{{ item.icon }}</v-icon>
      </v-btn>
      </div>

      <!-- <v-btn
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
      </v-btn> -->

    </v-speed-dial>
  </div>
</template>

<script>
  export default {
    name: 'FloatingButtonTemp',
    props: {
      openSheet: Function,
      currPage: String
    },
    data: () => ({
      fab: false,
      categories: [
          { title: 'Shows', path: '/shows', icon: 'mdi-television-classic', color: 'grey darken-2'},
          { title: 'Anime', path: '/anime', icon: 'mdi-fire', color: 'yellow darken-3'},
          { title: 'Music', path: '/music', icon: 'mdi-music-note', color: 'indigo'},
          { title: 'Movies', path: '/movies', icon: 'mdi-movie', color: 'pink'},
          { title: 'Books', path: '/books', icon: 'mdi-book', color: 'green darken-2'},
     ],
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