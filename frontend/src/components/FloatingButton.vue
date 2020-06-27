<template>
  <div id="float-button">
    <v-speed-dial
      open-on-hover="true"
      v-model="fab"
      bottom
      right
      direction="top"
      transition="slide-y-reverse-transition"
    >
      <template v-slot:activator>
        <div v-if="currPage === 'Home' || currPage==='Search'">
          <v-btn v-model="fab" color="!$vuetify.theme.primary" dark="$vuetify.theme.dark" fab>
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
                v-bind="attrs"
                v-on="on"
                :color="item.color"
                @click="openSheet(item.title)"
              >
                <v-tooltip left>
                  <template #activator="{ on }">
                    <v-icon v-on="on">{{ item.icon }}</v-icon>
                  </template>
                  <span>Add {{ item.title }}</span>
                </v-tooltip>
              </v-btn>
          </div>
        </div>
      </template>

      <div v-for="item in categories" :key="item.title">
        <v-tooltip left>
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              v-if="item.title !== currPage"
              fab
              dark
              v-bind="attrs"
              v-on="on"
              small
              :color="item.color"
              @click="openSheet(item.title)"
            >
              <v-icon>{{ item.icon }}</v-icon>
            </v-btn>
          </template>
          <span>Add {{ item.title }}</span>
        </v-tooltip>
      </div>
    </v-speed-dial>
  </div>
</template>

<script>
export default {
  name: "FloatingButton",
  props: {
    openSheet: Function,
    currPage: String
  },
  data: () => ({
    fab: false,
    categories: [
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

.v-speed-dial {
  position: absolute;
}
</style>
