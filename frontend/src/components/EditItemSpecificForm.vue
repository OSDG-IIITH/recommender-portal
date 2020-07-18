<template>
  <v-form ref="form" v-model="valid" :lazy-validation="true">
    <v-container fluid>
      <v-row align="start" justify="space-around">
        <template v-if="sheetType !== 'books'">
          <v-col md="12" cols="12">
            <v-combobox
              v-model="$v.form.streaming.$model"
              :items="sheetType == 'music'? listeningChoices: streamingChoices"
              :search-input.sync="search"
              hint="Add a platform if it does not already exist"
              label="Streaming On"
              hide-selected
              multiple
              outlined
              filled
              clearable
              prepend-inner-icon="mdi-lan"
              small-chips
              :error-messages="streamingErrors"
            >
              <template v-slot:no-data>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title>
                      No results matching "
                      <strong>{{ search }}</strong>". Press
                      <kbd>enter</kbd> to create a new one
                    </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </template>
            </v-combobox>
          </v-col>
        </template>
        <template v-if="sheetType === 'movies'">
          <v-col md="12" cols="12">
            <v-text-field
              v-model="$v.form.language.$model"
              label="Language"
              outlined
              filled
              clearable
              dense
              :placeholder="post.language"
              prepend-inner-icon="mdi-google-translate"
              :error-messages="languageErrors"
            ></v-text-field>
          </v-col>
          <v-col md="12" cols="12">
            <v-text-field
              v-model="$v.form.director.$model"
              label="Director"
              outlined
              filled
              clearable
              dense
              :placeholder="post.director"
              prepend-inner-icon="mdi-account-tie"
              :error-messages="directorErrors"
            ></v-text-field>
          </v-col>
        </template>
        <template v-else-if="sheetType === 'anime' || sheetType === 'shows'">
          <v-col md="12" cols="12">
            <v-slider
              v-model="$v.form.seasons.$model"
              min="1"
              max="20"
              label="Seasons"
              thumb-label="always"
              :error-messages="seasonsErrors"
            >
              <template v-slot:thumb-label="{ value }">{{ value }}</template>
            </v-slider>
          </v-col>
          <v-col md="12" cols="12">
            <v-slider
              v-model="$v.form.season_length.$model"
              min="1"
              max="100"
              label="Episodes per season"
              thumb-label="always"
              :error-messages="season_lengthErrors"
            >
              <template v-slot:thumb-label="{ value }">{{ value }}</template>
            </v-slider>
          </v-col>
          <v-col md="12" cols="12">
            <v-slider
              v-model="$v.form.episode_length.$model"
              min="5"
              max="180"
              label="Episode Length"
              thumb-label="always"
              :error-messages="episode_lengthErrors"
            >
              <template v-slot:thumb-label="{ value }">{{ value }}m</template>
            </v-slider>
          </v-col>
        </template>
        <template v-else-if="sheetType === 'music'">
          <v-col md="12" cols="12">
            <v-text-field
              v-model="$v.form.artist.$model"
              label="Artist"
              outlined
              filled
              clearable
              dense
              :placeholder="post.artist"
              prepend-inner-icon="mdi-account-music"
              :error-messages="artistErrors"
            ></v-text-field>
          </v-col>

          <v-col md="12" cols="12">
            <v-text-field
              v-model="form.album"
              label="Album"
              outlined
              filled
              clearable
              dense
              :placeholder="post.album"
              prepend-inner-icon="mdi-music-box-multiple"
            ></v-text-field>
          </v-col>
        </template>
        <template v-else-if="sheetType === 'books'">
          <v-col md="12" cols="12">
            <v-text-field
              v-model="$v.form.author.$model"
              label="Author"
              outlined
              filled
              clearable
              dense
              :placeholder="post.author"
              prepend-inner-icon="mdi-book-account"
              :error-messages="authorErrors"
            ></v-text-field>
          </v-col>
        </template>
      </v-row>
      <v-row align="start" justify="space-between">
        <v-col cols="12" xs="12" class="align-center">
          <v-btn @click="reset" small rounded>
            <v-icon>mdi-refresh</v-icon>Reset
          </v-btn>&nbsp;&nbsp;
          <v-btn @click="submit" small rounded>
            <v-icon>mdi-check</v-icon>Save
          </v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>

<script>
import { validationMixin } from "vuelidate";
import { required, numeric } from "vuelidate/lib/validators";

function initialiseform(post) {
  if (post.category == "movies") {
    return {
      language: post.language,
      director: post.director,
      streaming: post.streaming
    };
  } else if (post.category == "shows") {
    return {
      seasons: post.seasons,
      episode_length: post.episode_length,
      season_length: post.season_length,
      streaming: post.streaming
    };
  } else if (post.category == "anime") {
    return {
      seasons: post.seasons,
      episode_length: post.episode_length,
      season_length: post.season_length,
      streaming: post.streaming
    };
  } else if (post.category == "music") {
    return {
      artist: post.artist,
      streaming: post.streaming,
      album: post.album
    };
  }
  if (post.category == "books") {
    return {
      author: post.author
    };
  }
}

const templates = {
  movies: {
    language: "",
    director: "",
    streaming: []
  },
  shows: {
    seasons: "",
    episode_length: "",
    season_length: "",
    streaming: []
  },
  anime: {
    seasons: "",
    episode_length: "",
    season_length: "",
    streaming: []
  },
  music: {
    artist: "",
    streaming: "",
    album: ""
  },
  books: {
    author: ""
  }
};

const getNumErrors = (check, field) => {
  if (check) return [`${field} should be number`];
  return [];
};

export default {
  name: "EditItemSpecificForm",
  mixins: [validationMixin],
  props: ["post"],
  data: function() {
    return {
      valid: true,
      search: null,
      streamingChoices: ["netflix", "hotstar", "torrent", "prime", "youtube"],
      listeningChoices: [
        "youtube",
        "spotify",
        "gaana",
        "prime",
        "apple",
        "saavn"
      ],
      form: initialiseform(this.post),
      sheetType: this.post.category,
    };
  },
  validations() {
    switch (this.sheetType) {
      case "movies":
        return {
          form: {
            language: {},
            director: {},
            streaming: {}
          }
        };
      case "anime":
      case "shows":
        return {
          form: {
            seasons: { numeric },
            episode_length: { numeric },
            season_length: { numeric },
            streaming: {}
          }
        };
      case "music":
        return {
          form: {
            artist: {},
            streaming: {}
          }
        };
      case "books":
        return {
          form: {
            author: {}
          }
        };
    }
  },
  methods: {
    submit: function() {
      const editSpecificFormData = JSON.stringify(this.form);
      this.$root.$emit("EditItemCommonFormSubmit");
      this.$v.$reset();
      this.$emit("editSpecificSubmit", editSpecificFormData);
    },
    reset: function() {
      this.form = initialiseform(this.post);
      this.$v.$reset();
      this.$root.$emit("EditItemCommonFormReset");
    }
  },
  computed: {
    languageErrors() {
      let errors = [];
      if (!this.$v.form.language.$dirty) return errors;
      return errors;
    },
    directorErrors() {
      let errors = [];
      if (!this.$v.form.director.$dirty) return errors;
      return errors;
    },
    streamingErrors() {
      let errors = [];
      if (!this.$v.form.streaming.$dirty) return errors;
      return errors;
    },
    episode_lengthErrors() {
      let errors = [];
      if (!this.$v.form.episode_length.$dirty) return errors;
      errors = [
        ...getNumErrors(!this.$v.form.episode_length.numeric, "Episode Length")
      ];
      return errors;
    },
    season_lengthErrors() {
      let errors = [];
      if (!this.$v.form.season_length.$dirty) return errors;
      errors = [
        ...getNumErrors(!this.$v.form.season_length.numeric, "Season Length")
      ];
      return errors;
    },
    seasonsErrors() {
      let errors = [];
      if (!this.$v.form.seasons.$dirty) return errors;
      errors = [...getNumErrors(!this.$v.form.seasons.numeric, "Seasons")];
      return errors;
    },
    artistErrors() {
      let errors = [];
      if (!this.$v.form.artist.$dirty) return errors;
      return errors;
    },
    authorErrors() {
      let errors = [];
      if (!this.$v.form.author.$dirty) return errors;
      return errors;
    }
  }
};
</script>
