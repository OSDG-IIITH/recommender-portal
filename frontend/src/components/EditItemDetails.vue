<template>
  <v-list rounded dense flat>
    <v-subheader>Edit More Information</v-subheader>
    <v-list-item>
      <v-list-item-icon>
        <v-icon>mdi-calendar</v-icon>
      </v-list-item-icon>
      <v-list-item-content>
        <v-text-field 
          label="Year released" 
          :placeholder="post.year_release" 
          outlined>
        </v-text-field>
      </v-list-item-content>
    </v-list-item>

    <template v-if="post.category === 'anime' || post.category === 'shows'">
      <v-list-item>
        <v-list-item-icon>
          <v-icon>mdi-file-multiple</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-text-field 
            label="Number of Seasons" 
            :placeholder="post.seasons" 
            outlined>
          </v-text-field>
        </v-list-item-content>
      </v-list-item>
      <v-list-item>
        <v-list-item-icon>
          <v-icon>mdi-view-comfy</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-text-field 
            label="Season Length" 
            :placeholder="post.season_length" 
            outlined>
          </v-text-field>
        </v-list-item-content>
      </v-list-item>
      <v-list-item>
        <v-list-item-icon>
          <v-icon>mdi-clock-end</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-text-field 
            label="Episode Length" 
            :placeholder="post.episode_length" 
            outlined>
          </v-text-field>
        </v-list-item-content>
      </v-list-item>
    </template>

    <template v-else-if="post.category === 'books'">
      <v-list-item>
        <v-list-item-icon>
          <v-icon>mdi-book-account</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-text-field 
            label="Author" 
            :placeholder="post.author" 
            outlined>
          </v-text-field>
        </v-list-item-content>
      </v-list-item>
    </template>

    <template v-else-if="post.category === 'movies'">
      <v-list-item>
        <v-list-item-icon>
          <v-icon>mdi-calendar</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-text-field 
            label="Language" 
            :placeholder="post.language" 
            outlined>
          </v-text-field>
        </v-list-item-content>
      </v-list-item>
      <v-list-item>
        <v-list-item-icon>
          <v-icon>mdi-calendar</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-text-field 
            label="Director" 
            :placeholder="post.director" 
            outlined>
          </v-text-field>
        </v-list-item-content>
      </v-list-item>
    </template>

    <template v-else-if="post.category === 'music'">
      <v-list-item>
        <v-list-item-icon>
          <v-icon>mdi-account-music</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-text-field 
            label="Artist" 
            :placeholder="post.artist" 
            outlined>
          </v-text-field>
        </v-list-item-content>
      </v-list-item>
      <v-list-item>
        <v-list-item-icon>
          <v-icon>mdi-music-box-multiple</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-text-field 
            label="Album" 
            :placeholder="post.album" 
            outlined>
          </v-text-field>
        </v-list-item-content>
      </v-list-item>
    </template>

    <v-list-item v-if="post.category !== 'books'">
      <v-list-item-icon>
        <v-icon>mdi-lan</v-icon>
      </v-list-item-icon>
      <v-list-item-content>
        <v-text-field 
            label="Streaming Platforms" 
            :placeholder="post.streaming" 
            outlined>
        </v-text-field>
      </v-list-item-content>
    </v-list-item>
  </v-list>
</template>

<script>
export default {
  name: "EditItemDetails",
  props: {
    post: Object,
    editmode: Boolean
  }
};
</script>
