<template>
  <v-list>
    <v-list-item>Title: {{ post.title }}</v-list-item>
    <v-list-item>URL: {{ post.url }}</v-list-item>
    <v-list-item>Year of Release: {{ post.year_release }}</v-list-item>
    <v-list-item>
      Genres:
      <div v-for="item in post.genres" :key="item">{{ item }},</div>
    </v-list-item>
    <div v-if="post.category === 'anime'">
      <v-list-item>Seasons: {{ post.seasons }}</v-list-item>
      <v-list-item>Episode Length: {{ post.episode_length }}</v-list-item>
      <v-list-item>Season Length: {{ post.season_length }}</v-list-item>
    </div>

    <div v-if="post.category === 'books'">
      <v-list-item>Author: {{ post.author }}</v-list-item>
    </div>

    <div v-if="post.category === 'movies'">
      <v-list-item>Language: {{ post.language }}</v-list-item>
      <v-list-item>Director: {{ post.director }}</v-list-item>
    </div>

    <div v-if="post.category === 'music'">
      <v-list-item>Artist: {{ post.artist }}</v-list-item>
      <v-list-item>Album: {{ post.album }}</v-list-item>
    </div>

    <div v-if="post.category === 'shows'">
      <v-list-item>Seasons: {{ post.seasons }}</v-list-item>
      <v-list-item>Episode Length: {{ post.episode_length }}</v-list-item>
      <v-list-item>Season Length: {{ post.season_length }}</v-list-item>
    </div>

    <v-list-item v-if="post.category !== 'books'">
      Streaming on:
      <div v-for="item in post.streaming" :key="item">{{ item }},</div>
    </v-list-item>
  </v-list>
</template>

<script>
export default {
  name: "PostDetails",
  props: ["post"]
};
</script>