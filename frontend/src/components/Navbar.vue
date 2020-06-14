<template>
  <div>
  <v-app-bar app>
    <span class="hidden-md-and-up">
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
    </span>

    <v-toolbar-title>
      <router-link to="/" tag="span" style="cursor: pointer">
        {{ appTitle }}
      </router-link>
    </v-toolbar-title>

    <v-spacer></v-spacer>
    <SearchBox/>
    <v-spacer></v-spacer>
    <template v-slot:extension class="hidden-md-and-down">
        <v-tabs
          v-model="tabs"
          fixed-tabs
        >
          <v-tabs-slider></v-tabs-slider>
          <v-tab class="primary--text">
            <v-icon>mdi-home</v-icon>
          </v-tab>
<v-tab class="primary--text">
            <v-icon>mdi-book</v-icon>
          </v-tab>
<v-tab class="primary--text">
            <v-icon>mdi-movie</v-icon>
          </v-tab>
<v-tab class="primary--text">
            <v-icon>mdi-music-note</v-icon>
          </v-tab>
<v-tab class="primary--text">
            <v-icon>mdi-fire</v-icon>
          </v-tab>
<v-tab class="primary--text">
            <v-icon>mdi-television-classic</v-icon>
          </v-tab>
        </v-tabs>
      </template>

    <v-toolbar-items>
      <v-menu offset-y>
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            class="hidden-sm-and-down"
            color="primary"
            dark
            v-bind="attrs"
            v-on="on"
          >
            <span class="hidden-sm-and-down">My Profile</span>
            <v-icon class="hidden-md-and-up">mdi-account</v-icon>
          </v-btn>
        </template>
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
  data () {
    return {
      appTitle: 'Recommender @ IIIT-H',
      drawer: false,
      menu: [
        // { title: 'Home', path: '/', icon: 'mdi-home'},
        { title: 'Books', path: '/books', icon: 'mdi-book'},
        { title: 'Movies', path: '/movies', icon: 'mdi-movie'},
        { title: 'Music', path: '/music', icon: 'mdi-music-note'},
        { title: 'Anime', path: '/anime', icon: 'mdi-fire'},
        { title: 'Shows', path: '/shows', icon: 'mdi-television-classic'}
      ],
      profileitems: [
        { index: 1, title: 'Profile', path: '#' },
        { index: 2, title: 'Settings', path: '#'},
        { index: 3, title: 'Logout', path: '#'}
      ]
    }
  }
}
</script>
