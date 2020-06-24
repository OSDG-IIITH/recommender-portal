<template>
  <v-card class="xs-12 sm-6 md-4 lg-3 xl-2 elevation-3" outline>
    <v-img class="shrink ma-2" contain src="https://cdn.vuetifyjs.com/images/cards/halcyon.png"></v-img>
    <v-card-title class="display-1">
      {{name}} &nbsp;
      <v-chip small light>{{ $route.name }}</v-chip>
    </v-card-title>
    <v-card-text>
      {{ description }}
      <p>
        <span class="text--lighten-2 display-0">({{ rating }})</span>
        <v-rating v-model="rating" color="yellow accent-4" dense half-increments hover></v-rating>
      </p>
    </v-card-text>
    <v-card-actions class="pa-0">
      <v-tooltip top>
        <template v-slot:activator="{ on, attrs }">
          <v-btn color="red" icon v-bind="attrs" v-on="on">
            <v-icon>mdi-thumb-up</v-icon>
          </v-btn>
        </template>
        <span>Like</span>
      </v-tooltip>

      <v-tooltip top>
        <template v-slot:activator="{ on, attrs }">
          <v-btn color="red" icon v-bind="attrs" v-on="on">
            <v-icon>mdi-thumb-down</v-icon>
          </v-btn>
        </template>
        <span>Dislike</span>
      </v-tooltip>

      <v-tooltip top>
        <template v-slot:activator="{ on, attrs }">
          <v-btn color="green" icon v-bind="attrs" v-on="on">
            <v-icon>mdi-bookmark</v-icon>
          </v-btn>
        </template>
        <span>Favorite</span>
      </v-tooltip>

      <v-tooltip top>
        <template v-slot:activator="{ on, attrs }">
          <v-btn color="white" icon v-bind="attrs" v-on="on">
            <v-icon>mdi-link</v-icon>
          </v-btn>
        </template>
        <span>Link</span>
      </v-tooltip>

      <v-spacer></v-spacer>

      <v-tooltip top>
        <template v-slot:activator="{ on, attrs }">
          <v-btn color="blue darken-2" @click="show = !show" icon v-bind="attrs" v-on="on">
            <v-icon>mdi-comment</v-icon>
          </v-btn>
        </template>
        <span>Comment</span>
      </v-tooltip>
    </v-card-actions>
    <v-expand-transition>
      <div v-show="show">
        <v-divider></v-divider>
        <v-container id="scroll-target" class="overflow-y-auto">
          <v-row v-scroll:#scroll-target="onScroll" align="center" justify="center">
            <!-- <CommentTimeline/> -->
          </v-row>
        </v-container>
      </div>
    </v-expand-transition>
  </v-card>
</template>

<script>
import CommentTimeline from "@/components/CommentTimeline";
export default {
  name: "Post",

  components: {
    CommentTimeline
  },

  props: {
    post: Object
  },

  data: () => ({
    description: "lorem ipsum",
    name: "Example title",
    rating: 4.3,
    show: false,
    menu: false
  })
};
</script>
