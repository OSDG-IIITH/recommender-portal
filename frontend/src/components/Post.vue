<template>
   <v-card
    class="xs-12 sm-6 md-4 lg-3 xl-2 elevation-20"
    color="#4d2600"
    shaped
    dark
  >
    <v-img
        class="shrink ma-2"
        contain
        src="https://cdn.vuetifyjs.com/images/cards/halcyon.png"
    ></v-img>
    <v-card-title class="display-1">{{name}} &nbsp; <v-chip small light>{{ $route.name }}</v-chip></v-card-title>
    <v-card-text>
      {{ description }}
      <p>
      <span class="text--lighten-2 display-0">
        ({{ rating }})
      </span>
      <v-rating
        v-model="rating"
        color="yellow accent-4"
        dense
        half-increments
        hover
      ></v-rating>
      </p>
    </v-card-text>
    <v-card-actions class="pa-0">
      <v-btn text>
        <v-icon color = "red">mdi-heart</v-icon>
        {{ likes }}
      </v-btn>

      <v-btn
        color="purple" icon>
        <v-icon>mdi-bookmark</v-icon>
      </v-btn>
      <v-btn
        color="white" icon>
        <v-icon>mdi-link</v-icon>
      </v-btn>
      <v-spacer></v-spacer>
      <v-btn
        color="blue darken-2"
        @click="show = !show"
        icon
      >
        <v-icon>mdi-comment</v-icon>
      </v-btn>

    </v-card-actions>
     <v-expand-transition>
      <div v-show="show">
        <v-divider></v-divider>
        <v-container
          id="scroll-target"
          class="overflow-y-auto"
        >
          <v-row
            v-scroll:#scroll-target="onScroll"
            align="center"
            justify="center"
          >
            <!-- <CommentTimeline/> -->
          </v-row>
        </v-container>
      </div>
    </v-expand-transition>
  </v-card>
</template>

<script>
import CommentTimeline from '@/components/CommentTimeline'
export default {
  name: 'Post',

  components: {
    CommentTimeline
  },

  props: {
    post: Object
  },

  data: () => ({
    description: 'lorem ipsum',
    name: 'Example title',
    rating: 4.3,
    show: false,
    menu: false
  })
}
</script>

<style scoped>
  .v-card--shaped {
  border-radius: 2em 0em;
  }
</style>
