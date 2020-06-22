<template>
  <v-container fluid>
    <v-row :align="start" :justify="space-between" class="grey lighten-5 masonry">
      <v-col
        cols="12"
        xs="12"
        sm="6"
        md="4"
        lg="3"
        xl="2"
        v-for="card in cards"
        :key="card.title"
        class="child"
      >
        <Post />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";
import Post from "@/components/Post";
export default {
  name: "ItemsDisplay",
  data() {
    return {
      cards: []
    };
  },
  components: {
    Post
  },
  mounted: function() {
    let data = null;
    axios
      .get(
        "https://www.googleapis.com/books/v1/volumes?q=+subject:thriller&maxResults=20"
      )
      .then(response =>
        response.data.items.forEach(item =>
          this.cards.push({
            title: item.volumeInfo.title,
            image: item.volumeInfo.imageLinks.thumbnail,
            description: item.volumeInfo.description
          })
        )
      );
  }
};
</script>
