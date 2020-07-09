<template>
    <v-hover v-slot:default="{ hover }">
      <v-card
        class="xs-12 sm-6 md-4 lg-3 xl-2"
        :elevation="hover ? 6 : 3"
        :class="{ 'on-hover': hover }"
        outline
        shaped
      >
        <v-img
          class="white--text align-end"
          :aspect-ratio="4/3"
          :src="
              `https://via.placeholder.com/200x150.png?text=${(
                  post.title || 'N A'
              )
                  .split(' ')
                  .map(val => val.substring(0, 1))
                  .join('')}`
          ">
          <v-card-title class="display-1">
            {{ post.title }} &nbsp;
            <v-chip x-small light>{{ $route.name }}</v-chip>
          </v-card-title>
        </v-img>
        <v-card-text>
          <p>
            <div v-for="item in post.genres" :key="item">
              <v-chip small color="secondary" class="ma-1" label>{{ item }}</v-chip>
            </div>
          </p>
          <p>
            <v-rating v-model="rating" color="yellow accent-4" dense half-increments hover @click="rating({  })"></v-rating>
            <span class="text--lighten-2 display-0">({{ rating }})</span>
          </p>
        </v-card-text>
        <v-card-actions class="pa-0">
          <v-tooltip top>
            <template v-slot:activator="{ on, attrs }">
              <v-btn color="red darken-2" icon v-bind="attrs" v-on="on" @click="like({ _id: post._id, value: 1, category_id: post.category })">
                <v-icon>mdi-thumb-up</v-icon>
              </v-btn>
            </template>
            <span>Like</span>
          </v-tooltip>

          <v-tooltip top>
            <template v-slot:activator="{ on, attrs }">
              <v-btn color="red darken-2" icon v-bind="attrs" v-on="on" @click="like({ _id: post._id, value: -1, category_id: post.category })">
                <v-icon>mdi-thumb-down</v-icon>
              </v-btn>
            </template>
            <span>Dislike</span>
          </v-tooltip>

          <v-tooltip right>
            <template v-slot:activator="{ on, attrs }">
              <v-btn color="green" icon v-bind="attrs" v-on="on">
                <v-icon>mdi-bookmark</v-icon>
              </v-btn>
            </template>
            <span>Favorite</span>
          </v-tooltip>

          <v-spacer></v-spacer>

          <v-tooltip left>
            <template v-slot:activator="{ on, attrs }">
              <v-btn color="grey darken-2" dark icon v-bind="attrs" v-on="on">
                <v-icon>mdi-open-in-new</v-icon>
              </v-btn>
            </template>
            <span>Stream/Download</span>
          </v-tooltip>
          <v-tooltip top>
            <template v-slot:activator="{ on, attrs }">
              <v-btn color="blue darken-2" icon v-bind="attrs" v-on="on">
                <v-icon>mdi-comment</v-icon>
              </v-btn>
            </template>
            <span>Comment</span>
          </v-tooltip>
          <v-tooltip top>
            <template #activator="{ on: onTooltip }">
              <v-btn @click="show = !show" icon v-on="onTooltip">
                <v-icon color="yellow darken-2">{{ show? 'mdi-chevron-up' : 'mdi-information' }}</v-icon>
              </v-btn>
            </template>
            <span>{{ show? 'Show Less' : 'Read More' }}</span>
          </v-tooltip>
        </v-card-actions>
        <v-expand-transition>
          <div v-show="show">
            <ItemDetails :post="post" />
          </div>
        </v-expand-transition>
      </v-card>
    </v-hover>
</template>

<script>
// import CommentTimeline from "@/components/CommentTimeline";
import ItemDetails from '@/components/ItemDetails'
import { mapState, mapActions } from 'vuex'

export default {
  name: 'Item',

  components: {
    ItemDetails
  },

  data: function () {
    return {
      show: false
    }
  },

  props: {
    post_id: String
  },
  computed: {
    ...mapState({
      post (state) {
        return state.items.data[`${this.post_id}`]
      }
    }),
    rating: {
        get() {
            return this.post.rating
        },
        set(newValue) {
            this.setRating(
                {
                    _id: this.post._id, 
                    rating: newValue,
                    category_id: this.post.category
                }
            )
        }
    }
  },
  methods: {
    ...mapActions({
      like: 'likes/upsertLike',
      setRating: 'ratings/upsertRating'
    })
  }
}
</script>
