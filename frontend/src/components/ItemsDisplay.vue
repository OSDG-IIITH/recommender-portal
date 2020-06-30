<template>
  <v-container fluid>
    <v-virtual-scroll :items="posts">
      <v-row align="start" justify="space-between" dark class="masonry">
        <v-col
          cols="12"
          xs="12"
          sm="6"
          md="4"
          lg="3"
          xl="2"
          class="child"
          v-for="post in posts"
          :key="post.title"
        >
          <Post />
        </v-col>
      </v-row>
    </v-virtual-scroll>
  </v-container>
</template>

<script>
import Post from "@/components/Post";
var msnry = new Masonry(".masonry", {
  // options
  itemSelector: "[class*='col-']"
});
export default {
  name: "ItemsDisplay",
  components: {
    Post
  },
  mounted: async function() {
    await this.$store.dispatch('items/fetchItems', this.$route.name);
  },
  computed: {
    posts: function() {
      return this.$store.getters["items/getItemsByCategory"](this.$route.name);
    }
  }
};
</script>
