<template>
  <div>
  <div v-for="page in menu" :key="page.title">
  <div v-if="page.title === current">
  <v-app-bar 
  app
  :color="page.color"
  >
    <span class="hidden-md-and-up">
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
    </span>

    <v-toolbar-title>
      <router-link to="/" tag="span" 
      style="cursor: pointer; font-size:20px">
        <b>{{ appTitle }}</b>
      </router-link>
    </v-toolbar-title>

    <v-spacer></v-spacer>
    <SearchBox/>
    <v-spacer></v-spacer>

     <template v-slot:extension
      >
        <v-tabs 
          class="hidden-sm-and-down"
          v-model="tabs"
          fixed-tabs
        >
        <v-tabs-slider></v-tabs-slider>
          
          <v-tab 
          class="primary--text"
          v-for="item in menu"
          :key="item.title"
          :to="item.path"
          >
            <v-icon> {{ item.icon }} </v-icon>
          </v-tab>
        </v-tabs>
      </template>

    <v-toolbar-items
    class="hidden-sm-and-down">
      <v-menu offset-y open-on-hover transition="slide-x-reverse-transition">
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="black"
          dark
          icon
          v-bind="attrs"
          v-on="on"
          class="mr-2"
        >
          <v-icon size="4vw"> mdi-account-circle </v-icon>
        </v-btn>
      </template>

      <v-list nav>
        <v-list-item
          v-for="(item, index) in profileitems"
          :key="index"
          :to="item.path"
        >
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item>
        <v-list-item to="/search">
          <v-list-item-icon>
              <v-icon>mdi-magnify</v-icon>
          </v-list-item-icon>
          <v-list-item-title>Search</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
    </v-toolbar-items>
  </v-app-bar>
  <v-navigation-drawer
    v-model="drawer"
    absolute
    temporary
    :color="page.color"
  >
    <v-list
      nav
      dense
    >
      <v-list-item-group
        v-model="group"
        active-class="white--text text--accent-4"
      >
        <v-list-item v-for="item in menu" :key="item.title" :to="item.path">
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item>
      </v-list-item-group>
    </v-list>
    <v-menu offset-y open-on-hover>
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          class="ml-12"
          color="grey darken-2"
          dark
          v-bind="attrs"
          v-on="on"
        >
          My Profile
        </v-btn>
      </template>
      
      <v-list nav>
        <v-list-item
          v-for="(item, index) in profileitems"
          :key="index"
          :to="item.path"
        >
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item>
        <v-list-item to="/search">
          <v-list-item-icon>
              <v-icon>mdi-magnify</v-icon>
          </v-list-item-icon>
          <v-list-item-title>Search</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
  </v-navigation-drawer>
  </div>
  </div>
  </div>
</template>


<script>
import SearchBox from '@/components/SearchBox'
export default {
  name: 'Navbar',
  components: {
    SearchBox
  },
  props: {
    current: String
  },
  data(){
    return {
      appTitle: 'Recommender@IIIT-H',
      drawer: false,
      menu: [
          { title: 'Home', path: '/', icon: 'mdi-home', color: '#c2c2d6'},
          { title: 'Books', path: '/books', icon: 'mdi-book', color: '#00aaaa'},
          { title: 'Movies', path: '/movies', icon: 'mdi-movie', color: '#ff99a0'},
          { title: 'Music', path: '/music', icon: 'mdi-music-note', color: '#8cb3d9'},
          { title: 'Anime', path: '/anime', icon: 'mdi-fire', color: '#ffaa66'},
          { title: 'Shows', path: '/shows', icon: 'mdi-television-classic', color: '#b3b3b3'},
     ],
     profileitems: [
          { index: 1, title: 'Profile', path: '#' },
          { index: 2, title: 'Settings', path: '#'},
          { index: 3, title: 'Logout', path: '#'}
     ]
    }
  },
}
</script>