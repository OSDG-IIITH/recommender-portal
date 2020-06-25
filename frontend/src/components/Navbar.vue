<template>
  <div>
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
                    <v-btn flat icon v-bind="attrs" v-on="on">
                      <v-icon>{{ item.icon }}</v-icon>
                    </v-btn>
                  </template>
                  <span>{{ item.title }}</span>
                </v-tooltip>
              </v-tab>
            </v-tabs>
          </template>

          <v-toolbar-items>
            <v-menu offset-y open-on-hover transition="slide-x-reverse-transition">
              <template v-slot:activator="{ on, attrs }">
                <v-btn dark icon v-bind="attrs" v-on="on" class="mr-2">
                  <v-icon>mdi-account-circle</v-icon>
                </v-btn>
              </template>

              <v-list nav>
                <v-list-item v-for="(item, index) in profileitems" :key="index" :to="item.path">
                  <v-list-item-title>{{ item.title }}</v-list-item-title>
                </v-list-item>
              </v-list>
            </v-menu>
            <v-btn>
              <v-switch v-model="$vuetify.theme.dark" hide-details inset></v-switch>
              <v-icon>mdi-brightness-4</v-icon>
            </v-btn>
          </v-toolbar-items>
        </v-app-bar>
        <v-navigation-drawer
          v-model="drawer"
          absolute
          temporary
          :color="page.color"
          :mini-variant.sync="mini"
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
                <v-list-item-title>{{ item.title }}</v-list-item-title>
              </v-list-item>
            </v-list-item-group>
          </v-list>
        </v-navigation-drawer>
      </div>
    </div>
  </div>
</template>


<script>
import SearchBox from "@/components/SearchBox";
export default {
  name: "Navbar",
  components: {
    SearchBox
  },
  props: {
    current: String
  },
  data() {
    return {
      appTitle: "Recommender@IIIT-H",
      drawer: false,
      mini: true,
      menu: [
        { title: "Home", path: "/", icon: "mdi-home", color: "#4e4d5c" },
        { title: "Books", path: "/books", icon: "mdi-book", color: "#2D4654" },
        {
          title: "Movies",
          path: "/movies",
          icon: "mdi-movie",
          color: "#05668d"
        },
        {
          title: "Music",
          path: "/music",
          icon: "mdi-music-note",
          color: "#D00000"
        },
        { title: "Anime", path: "/anime", icon: "mdi-fire", color: "#F48C06" },
        {
          title: "Shows",
          path: "/shows",
          icon: "mdi-television-classic",
          color: "#FFBA08"
        }
      ],
      profileitems: [
        { index: 1, title: "Profile", path: "#" },
        { index: 2, title: "Settings", path: "#" },
        { index: 3, title: "Logout", path: "#" }
      ]
    };
  }
};
</script>
