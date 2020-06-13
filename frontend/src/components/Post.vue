<template>
  <v-card
    class="mx-auto"
    
  >
    <v-img
      src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"
    ></v-img>

    <v-card-title>
      Title
    </v-card-title>

    <v-card-text>
      Post description
    </v-card-text>

    <v-card-actions>
      <v-spacer></v-spacer>
      
      <v-btn 
        text
      >
        <v-icon color = "red">mdi-heart</v-icon>
        {{ likes }}
      </v-btn>

      <v-btn 
        color="purple"
        icon
        >
        <v-icon>mdi-bookmark</v-icon>
      </v-btn>
      <v-btn
        color="purple"
        icon
      >
        <v-icon>mdi-link</v-icon>
      </v-btn>

      <v-btn
        color="blue"
        @click="show = !show"
      >
        <v-icon>mdi-comment</v-icon>
        comment
      </v-btn>
    </v-card-actions>

    <v-expand-transition>
      <div v-show="show">
        <v-divider></v-divider>
        <v-container fluid>
        <v-textarea
            filled
            auto-grow
            value="comment box should be here"
        ></v-textarea>
  </v-container>
      </div>
    </v-expand-transition>
  </v-card>
</template>

<script>
  export default {
    name: 'Post',
    props: {
        post: Object
    },

    data: () => ({
      show: false,
    }),
  }
</script>
