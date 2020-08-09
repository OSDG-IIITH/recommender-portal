<template>
  <ais-instant-search index-name="demo_ecommerce" :search-client="searchClient">
    <div class="left-panel">
      <ais-clear-refinements />
      <v-list disabled>
        <v-header><h4>Common Details</h4></v-header>
        <v-list-item-group v-model="item" color="primary">
            <v-list-item
            v-for="(item, i) in commonDetails"
            :key="i"
            >
            <v-list-item-content>
                <v-list-item-title v-text="item.text"></v-list-item-title>
                <ais-refinement-list attribute="" searchable />
            </v-list-item-content>
            </v-list-item>
        </v-list-item-group>
      </v-list>
      <v-list disabled>
        <v-header><h4>Specific Details</h4></v-header>
        <v-list-item-group v-model="item" color="primary">
            <v-list-item
            v-for="(item, i) in specificDetails"
            :key="i"
            >
            <v-list-item-content>
                <v-list-item-title v-text="item.text"></v-list-item-title>
                <ais-refinement-list attribute="" searchable />
            </v-list-item-content>
            </v-list-item>
        </v-list-item-group>
      </v-list>
      <ais-configure :hitsPerPage="20" />
    </div>
    <div class="right-panel">
      <v-row>
        <v-col cols="8"><ais-search-box /></v-col>
        <v-col cols="4">
          <v-select
          v-model="e7"
          :items="categories"
          label="Select Categories"
          multiple
          chips
        ></v-select>
        </v-col>
      </v-row>
      <ais-hits>
        <div slot="item" slot-scope="{ item }">
          {{ item.name }}
        </div>
      </ais-hits>
      <ais-pagination />
    </div>
  </ais-instant-search>
</template>

<script>
import algoliasearch from 'algoliasearch/lite';
import 'instantsearch.css/themes/algolia-min.css';

export default {
    name: 'SearchPage',
    data() {
        return {
        e7: [],
        commonDetails: [
            { text: 'Title:' , attri: 'title' },
            { text: 'Genres:', attri: 'genres' },
            { text: 'Year of Release:', attri: 'year_release' },
        ],
        specificDetails: [
            { text: 'Language:' , attri: 'language' },
            { text: 'Director:', attri: 'director' },
            { text: 'Season:', attri: 'seasons' },
            { text: 'Season Length:' , attri: 'season_length' },
            { text: 'Episode Length:', attri: 'episode_length' },
            { text: 'Artist:', attri: 'artist' },
            { text: 'ALbum:' , attri: 'album' },
            { text: 'Author:', attri: 'author' },
            { text: 'Streaming on:', attri: 'streaming' },
        ],
        categories: ['Books', 'Movies', 'Music', 'Anime', 'Shows'],

        // APPROPRIATE DATA NEEDED
        searchClient: algoliasearch(
            'B1G2GM9NG0',
            'aadef574be1f9252bb48d4ea09b5cfe5'
            ),
        };
    },
};
</script>

<style>
body {
  font-family: sans-serif;
  padding: 1em;
}

.ais-Hits-list {
  margin-top: 0;
  margin-bottom: 1em;
}

.ais-InstantSearch {
  display: grid;
  grid-template-columns: 1fr 4fr;
  grid-gap: 1em;
}

</style>