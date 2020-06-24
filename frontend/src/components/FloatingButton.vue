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
        <div v-if="currPage === 'Home' || currPage==='Search'">
          <v-btn
            v-model="fab"
            color="#8080bb"
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
              v-model="fab"
              fab
              dark
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

    </v-speed-dial>
  </div>
</template>

<script>
  export default {
    name: 'FloatingButton',
    props: {
      openSheet: Function,
      currPage: String
    },
    data: () => ({
      fab: false,
      categories: [
        { title: 'Shows', path: '/shows', icon: 'mdi-television-classic', color: 'grey darken-2'},
        { title: 'Anime', path: '/anime', icon: 'mdi-fire', color: 'yellow darken-3'},
        { title: 'Music', path: '/music', icon: 'mdi-music-note', color: 'blue lighten-1'},
        { title: 'Movies', path: '/movies', icon: 'mdi-movie', color: 'pink lighten-2'},
        { title: 'Books', path: '/books', icon: 'mdi-book', color: '#009999'}  
      ]
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