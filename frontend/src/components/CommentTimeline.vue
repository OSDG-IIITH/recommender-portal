<template>
  <div class="comment-timeline">
  <v-timeline dense>

    <v-timeline-item>
      <template v-slot:icon>
        <v-avatar>
          <img src="http://i.pravatar.cc/64">
        </v-avatar>
      </template>
      <v-text-field v-model="input" flat label="Leave a comment..." solo @keydown.enter="addComment()">
        <template v-slot:append>
          <v-btn depressed class="mx-0" @click="addComment()" light>Post</v-btn>
        </template>
      </v-text-field>
    </v-timeline-item>

    <v-timeline-item v-for="comment in timeline" :key="comment.time">
      <template v-slot:icon>
        <v-avatar>
          <img src="http://i.pravatar.cc/64">
        </v-avatar>
      </template>
      <v-card class="elevation-2">
        <!--v-card-title class="headline">Great!</v-card-title-->
        <v-card-subtitle>{{ comment.by }} -  {{ comment.time }}</v-card-subtitle>
        <v-card-text>
          {{ comment.text }}
        </v-card-text>
      </v-card>
    </v-timeline-item>
  </v-timeline>
  </div>
</template>

<script>
  export default {
    name: 'CommentTimeline',
    data: () => ({
      comments: [
        {
          by: 'Commenter Name',
          text: "Lorem ipsum dolor sit amet, no nam oblique veritus.",
          time: (new Date()).toTimeString()
        },
        {
          by: 'Commenter Name',
          text: "Lorem ipsum dolor sit amet, no nam oblique veritus.",
          time: (new Date()).toTimeString()
        },
      ],
      input: ""
    }),
    computed: {
      timeline () {
        return this.comments.slice().reverse();
      }
    },
    methods: {
      addComment: function() {
        if(this.input.trim().length > 0){
          const time = (new Date()).toTimeString();
          this.comments.push({
            by: 'Current User',
            text: this.input,
            time: time
          });
          this.input = "";
        }
      }
    }
  }
</script>

<style>
  .comment-timeline {
    width: 18vw;
  }
</style>