<template>
  <v-hover v-slot:default="{ hover }" close-delay="200">
    <v-card
      class="xs-12 sm-6 md-4 lg-3 xl-2 elevation-3"
      outline
      shaped
      :elevation="hover ? 40 : 3"
    >
      <v-img class="white--text align-end" src="https://cdn.vuetifyjs.com/images/cards/halcyon.png">
        <v-card-title class="display-1">
          {{ name }} &nbsp;
          <v-chip small light>{{ $route.name }}</v-chip>

          <v-spacer></v-spacer>

          <v-menu
            v-model="menu"
            bottom
            right
            rounded
            offset-x
            transition="slide-x-transition"
            origin="top left"
          >
            <template #activator="{ on: onMenu }">
              <v-tooltip bottom>
                <template #activator="{ on: onTooltip }">
                  <v-btn icon v-on="{ ...onMenu, ...onTooltip }">
                    <v-icon color="white">mdi-more</v-icon>
                  </v-btn>
                </template>
                <span>Read More</span>
              </v-tooltip>
            </template>
            <v-card dark width="300">
              <v-list>
                <v-list-item>
                  <v-list-item-content>
                    <PostDetails :post="post" />
                  </v-list-item-content>
                  <v-list-item-action>
                    <v-btn icon @click="menu = false">
                      <v-icon>mdi-close-circle</v-icon>
                    </v-btn>
                  </v-list-item-action>
                </v-list-item>
              </v-list>
            </v-card>
          </v-menu>
        </v-card-title>
      </v-img>
      <v-card-text>
        {{ description }}
        <p>
          <v-rating v-model="post.rating" color="yellow accent-4" dense half-increments hover @click="rating({ _id: post._id, rating: post.rating, category_id: post.category })"></v-rating>
          <span class="text--lighten-2 display-0">({{ post.rating }})</span>
        </p>
      </v-card-text>
      <v-card-actions class="pa-0">
        <v-tooltip top>
          <template v-slot:activator="{ on, attrs }">
            <v-btn color="red" icon v-bind="attrs" v-on="on" @click="like({ _id: post._id, value: 1, category_id: post.category })">
              <v-icon>mdi-thumb-up</v-icon>
            </v-btn>
          </template>
          <span>Like</span>
        </v-tooltip>

        <v-tooltip top>
          <template v-slot:activator="{ on, attrs }">
            <v-btn color="red" icon v-bind="attrs" v-on="on" @click="like({ _id: post._id, value: -1, category_id: post.category })">
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
      <!-- <v-expand-transition>
        <div v-show="show">
          <v-divider></v-divider>
          <v-container id="scroll-target" class="overflow-y-auto">
            <v-row v-scroll:#scroll-target="onScroll" align="center" justify="center">
              <CommentTimeline/>
            </v-row>
          </v-container>
        </div>
      </v-expand-transition>-->
    </v-card>
  </v-hover>
</template>

<script>
// import CommentTimeline from "@/components/CommentTimeline";
import PostDetails from "@/components/PostDetails";
import { mapState } from "vuex";
import { mapActions } from "vuex";

export default {
  name: "Post",

  components: {
    // CommentTimeline,
    PostDetails
  },

  props: {
    post_id: Number
  },
  computed: {
    ...mapState({
      post(state) {
        return state.items.data[`${this.post_id}`];
      }
    })
  },
  methods: {
    ...mapActions({
      like: 'likes/upsertLike',
      rating: 'ratings/upsertRating'
    })
  }
};
</script>
