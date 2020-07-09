<template>
  <v-list rounded dense flat>
    <v-subheader>More Information</v-subheader>
    <v-list-item>
      <v-list-item-icon>
        <v-icon>mdi-calendar</v-icon>
      </v-list-item-icon>
      <v-list-item-content>
        <v-tooltip left>
            <template v-slot:activator="{ on, attrs }">
              <v-list-item-title v-bind="attrs" v-on="on">{{ post.year_release }}</v-list-item-title>
            </template>
            <span>Year Released</span>
        </v-tooltip>
      </v-list-item-content>
    </v-list-item>

    <template v-if="post.category === 'anime' || post.category === 'shows'">
      <v-list-item>
        <v-list-item-icon>
          <v-icon>mdi-file-multiple</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>{{ post.seasons }} seasons</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-list-item>
        <v-list-item-icon>
          <v-icon>mdi-view-comfy</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>{{ post.season_length }} episodes per season</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-list-item>
        <v-list-item-icon>
          <v-icon>mdi-clock-end</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>{{ post.episode_length }} minute(s)</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </template>

    <template v-else-if="post.category === 'books'">
      <v-list-item>
        <v-list-item-icon>
          <v-icon>mdi-book-account</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-tooltip left>
            <template v-slot:activator="{ on, attrs }">
              <v-list-item-title v-bind="attrs" v-on="on">{{ post.author }}</v-list-item-title>
            </template>
            <span>Author</span>
          </v-tooltip>
        </v-list-item-content>
      </v-list-item>
    </template>

    <template v-else-if="post.category === 'movies'">
      <v-list-item>
        <v-list-item-icon>
          <v-icon>mdi-calendar</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-tooltip left>
            <template v-slot:activator="{ on, attrs }">
              <v-list-item-title v-bind="attrs" v-on="on">{{ post.language }}</v-list-item-title>
            </template>
            <span>Language</span>
          </v-tooltip>
        </v-list-item-content>
      </v-list-item>
      <v-list-item>
        <v-list-item-icon>
          <v-icon>mdi-calendar</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-tooltip left>
            <template v-slot:activator="{ on, attrs }">
              <v-list-item-title v-bind="attrs" v-on="on">{{ post.director }}</v-list-item-title>
            </template>
            <span>Director</span>
          </v-tooltip>
        </v-list-item-content>
      </v-list-item>
    </template>

    <template v-else-if="post.category === 'music'">
      <v-list-item>
        <v-list-item-icon>
          <v-icon>mdi-account-music</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-tooltip left>
            <template v-slot:activator="{ on, attrs }">
              <v-list-item-title v-bind="attrs" v-on="on">{{ post.artist }}</v-list-item-title>
            </template>
            <span>Artist</span>
          </v-tooltip>
        </v-list-item-content>
      </v-list-item>
      <v-list-item>
        <v-list-item-icon>
            <v-icon >mdi-music-box-multiple</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-tooltip left>
              <template v-slot:activator="{ on, attrs }">
              <v-list-item-title v-bind="attrs" v-on="on">{{ post.album }}</v-list-item-title>
            </template>
            <span>Album</span>
          </v-tooltip>
        </v-list-item-content>
      </v-list-item>
    </template>

    <v-list-item v-if="post.category !== 'books'">
      <v-list-item-icon>
          <v-icon>mdi-lan</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-tooltip left>
            <template v-slot:activator="{ on, attrs }">
              <v-list-item-title v-bind="attrs" v-on="on">{{ post.streaming }}</v-list-item-title>
            </template>
            <span>Streaming On</span>
          </v-tooltip>
        </v-list-item-content>
    </v-list-item>
  </v-list>

</template>

<script>
export default {
  name: 'PostDetails',
  props: ['post']
}
</script>
