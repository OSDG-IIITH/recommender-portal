<template>
  <v-toolbar app>
    <span class="hidden-sm-and-up">
      <v-toolbar-side-icon @click="sidebar = !sidebar">
      </v-toolbar-side-icon>
      </span>
      <v-toolbar-title>
        <router-link to="/" tag="span" style="cursor: pointer">
          {{ appTitle }}
        </router-link>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items class="hidden-xs-only">
      <v-btn
        flat
        v-for="item in menu"
        :key="item.title"
        :to="item.path">
        {{ item.title }}
      </v-btn>
      <v-menu offset-y>
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="primary"
          dark
          v-bind="attrs"
          v-on="on"
        >
          My Profile
        </v-btn>
      </template>
      <v-list>
        <v-list-item
          v-for="(item, index) in profileitems"
          :key="index"
        >
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
    </v-toolbar-items>
  </v-toolbar>
</template>


<script>
export default {
  name: 'Navbar',
  props: {
    drawer: Boolean
  },
  data(){
    return {
      appTitle: 'Recommender@IIIT-H',
      sidebar: false,
      menu: [
          { title: 'Home', path: '/' },
          { title: 'Books', path: '/books'},
          { title: 'Movies', path: '/movies'},
          { title: 'Music', path: '/music'},
          { title: 'Anime', path: '/anime'},
          { title: 'Shows', path: '/shows'},
     ],
     profileitems: [
          { index: 1, title: 'Profile' },
          { index: 2, title: 'Settings'},
          { index: 3, title: 'Logout'}
     ]
    }
  },
}
</script>