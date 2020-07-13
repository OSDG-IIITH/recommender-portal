<template>
  <div class="navbar">
    <div v-for="page in menu" :key="page.title">
      <div v-if="page.title === current">
        <v-app-bar app :color="page.color">
          <span class="hidden-md-and-up">
            <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
          </span>
          <span class="hidden-sm-and-down">
            <v-toolbar-title>
              <router-link to="/" tag="span" color="primary">
                <b>{{ appTitle }}</b>
              </router-link>
            </v-toolbar-title>
          </span>

          <v-spacer></v-spacer>
          <SearchBox />
          <v-spacer></v-spacer>

          <template v-slot:extension>
            <v-tabs class="hidden-sm-and-down" v-model="tabs" fixed-tabs>
              <v-tabs-slider></v-tabs-slider>
              <v-tab class="primary--text" v-for="item in menu" :key="item.title" :to="item.path">
                <v-tooltip bottom>
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn text icon v-bind="attrs" v-on="on">
                      <v-icon>{{ item.icon }}</v-icon>
                    </v-btn>
                  </template>
                  <span>{{ item.name }}</span>
                </v-tooltip>
              </v-tab>
            </v-tabs>
          </template>
          <v-speed-dial
              v-model="fab"
              open-on-hover
              flat
              top
              right
              direction="left"
              transition="slide-x-reverse-transition"
            >
              <template v-slot:activator>
                <v-btn v-model="fab" flat depressed icon text>
                  <v-icon v-if="fab">mdi-close</v-icon>
                  <v-icon v-else>mdi-dots-vertical</v-icon>
                </v-btn>
              </template>
              <v-btn-toggle rounded>
                <v-btn text flat depressed>
                  <v-switch v-model="$vuetify.theme.dark" hide-details flat inset></v-switch>
                  <v-icon>mdi-brightness-4</v-icon>
                </v-btn>
                <v-btn text flat depressed icon to="/profile">
                  <v-tooltip bottom>
                    <template #activator="{ on }">
                      <v-icon v-on="on">mdi-account-circle</v-icon>
                    </template>
                    <span>Profile</span>
                  </v-tooltip>
                </v-btn>
                <v-btn text flat depressed icon to="/settings">
                  <v-tooltip bottom>
                    <template #activator="{ on }">
                      <v-icon v-on="on">mdi-cog</v-icon>
                    </template>
                    <span>Settings</span>
                  </v-tooltip>
                </v-btn>
                <v-btn text flat depressed icon @click="() => {isAuthenticated ? logout() : login()}">
                  <v-tooltip bottom>
                    <template #activator="{ on }">
                      <v-icon v-on="on">{{ isAuthenticated? "mdi-logout" : "mdi-login"}}</v-icon>
                    </template>
                    <span>{{ isAuthenticated? "Logout" : "Login"}}</span>
                  </v-tooltip>
                </v-btn>
              </v-btn-toggle>
            </v-speed-dial>
        </v-app-bar>
        <v-navigation-drawer
          v-model="drawer"
          absolute
          temporary
          :color="page.color"
          :mini-variant.sync="mini"
          app
        >
          <v-list-item>
            <v-btn icon @click.stop="mini = !mini">
              <v-icon>{mini? mdi-chevron-right : mdi-chevron-left }</v-icon>
            </v-btn>
            <v-list-item-title>Reco@IIIT-H</v-list-item-title>
          </v-list-item>
          <v-list nav dense>
            <v-list-item-group>
              <v-list-item v-for="item in menu" :key="item.title" :to="item.path">
                <v-list-item-icon>
                  <v-icon>{{ item.icon }}</v-icon>
                </v-list-item-icon>
                <v-list-item-title>{{ item.name }}</v-list-item-title>
              </v-list-item>
            </v-list-item-group>
          </v-list>
        </v-navigation-drawer>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import SearchBox from '@/components/SearchBox'

export default {
  name: 'Navbar',
  components: {
    SearchBox
  },
  props: {
    current: String
  },
  computed: mapState({
    isAuthenticated: state => state.isAuthenticated
  }),
  methods: {
    ...mapActions({
      logout: 'logOut'
    }),
    login: function () {
      window.location.replace('https://login.iiit.ac.in/cas/login?service=http://0.0.0.0:8000/login')
    }
  },
  data () {
    return {
      tabs: null,
      fab: null,
      appTitle: 'Recommender@IIIT-H',
      drawer: false,
      mini: true,
      menu: [
        { title: 'home', name: 'Home', path: '/', icon: 'mdi-home', color: '#4e4d5c' },
        { title: 'books', name: 'Books', path: '/books', icon: 'mdi-book', color: '#2D4654' },
        {
          title: 'movies',
          name: 'Movies',
          path: '/movies',
          icon: 'mdi-movie',
          color: '#05668d'
        },
        {
          title: 'music',
          name: 'Music',
          path: '/music',
          icon: 'mdi-music-note',
          color: '#D00000'
        },
        { title: 'anime', name: 'Anime', path: '/anime', icon: 'mdi-fire', color: '#F48C06' },
        {
          title: 'shows',
          name: 'Shows',
          path: '/shows',
          icon: 'mdi-television-classic',
          color: '#FFBA08'
        }
      ]
    }
  }
}
</script>
