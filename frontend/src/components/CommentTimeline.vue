<template>
  <div class="comment-timeline">
  <v-timeline dense>
    <v-timeline-item v-for="n in 3" :key="n">
      <template v-slot:icon>
        <v-avatar>
          <img src="http://i.pravatar.cc/64">
        </v-avatar>
      </template>
      <v-card class="elevation-2">
        <v-card-title class="headline">Great!</v-card-title>
        <v-card-subtitle>Commenter Name -  June 14, 10:30 am</v-card-subtitle>
        <v-card-text>
          Lorem ipsum dolor sit amet, no nam oblique veritus. Commune scaevola imperdiet nec ut, sed euismod convenire principes at.
        </v-card-text>
      </v-card>
    </v-timeline-item>
  </v-timeline>
  </div>
</template>

<script>
  export default {
    name: 'CommentTimeline',
  }
</script>

<style>
  .comment-timeline {
    width: 90%;
  }
</style>