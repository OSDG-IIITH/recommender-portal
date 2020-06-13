<template>
  <v-card
    class="mx-auto"
    
  >
    <v-img
      src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"
    ></v-img>

    <v-card-title>
      title
    </v-card-title>

    <v-card-text>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit,
        sed do eiusmod tempor incididunt ut labore et dolore
        magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
    </v-card-text>

    <v-card-actions>
        <v-btn 
        text
        >
            <v-icon color = "red">mdi-heart</v-icon>
            {{ likes }}
        </v-btn>
      <v-spacer></v-spacer>

      <v-btn
        color="purple"
        text
        text-align = "center"
      >
            <v-icon>mdi-share</v-icon>
            share
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
