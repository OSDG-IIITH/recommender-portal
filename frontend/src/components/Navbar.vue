<template>
  <div>
  <v-app-bar 
  app
  >
    <span class="hidden-md-and-up">
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
    </span>

    <v-toolbar-title>
      <router-link to="/" tag="span" 
      style="cursor: pointer; font-size:20px">
        {{ appTitle }}
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
          <div v-if="item.title === current">
            <v-icon :color = item.color> {{ item.icon }} </v-icon>
          </div>
          <div v-else>
            <v-icon :color="black"> {{ item.icon }} </v-icon>
          </div>
          </v-tab>
        </v-tabs>
      </template>

    <v-toolbar-items
    class="hidden-sm-and-down">
      <v-menu offset-y>
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="primary"
          dark
          v-bind="attrs"
          v-on="on"
          style="width:95%; margin-left:2.5%;"
        >
          <v-icon size="3vw"> mdi-account-circle </v-icon>
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
      </v-list>
    </v-menu>
    </v-toolbar-items>
  </v-app-bar>
  <v-navigation-drawer
    v-model="drawer"
    absolute
    temporary
  >
    <v-list
      nav
      dense
    >
      <v-list-item-group
        v-model="group"
        active-class="deep-purple--text text--accent-4"
      >
        <v-list-item v-for="item in menu" :key="item.title" :to="item.path">
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item>
      <v-list-item>
        <v-list-item-icon>
            <v-icon>mdi-magnify</v-icon>
        </v-list-item-icon>
        <v-list-item-title>Search</v-list-item-title>
      </v-list-item>
      </v-list-item-group>
    </v-list>
    <v-menu offset-y>
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="primary"
          dark
          v-bind="attrs"
          v-on="on"
          style="width:95%; margin-left:2.5%;"
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
      </v-list>
    </v-menu>
  </v-navigation-drawer>
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
          { title: 'Home', path: '/', icon: 'mdi-home', color: 'black'},
          { title: 'Books', path: '/books', icon: 'mdi-book', color: 'green'},
          { title: 'Movies', path: '/movies', icon: 'mdi-movie', color: 'pink darken-2'},
          { title: 'Music', path: '/music', icon: 'mdi-music-note', color: '#006699'},
          { title: 'Anime', path: '/anime', icon: 'mdi-fire', color: '#ffd24d'},
          { title: 'Shows', path: '/shows', icon: 'mdi-television-classic', color: 'grey'},
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