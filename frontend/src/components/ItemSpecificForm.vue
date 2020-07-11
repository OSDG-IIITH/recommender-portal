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
                                No results matching "<strong>{{ search }}</strong>". Press <kbd>enter</kbd> to create a new one
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
                                placeholder="English"
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
                                placeholder="James Cameron"
                                prepend-inner-icon="mdi-account-tie"
                                :error-messages="directorErrors"
                            ></v-text-field>
                        </v-col>
                </template>
                <template v-else-if="sheetType === 'anime' || sheetType === 'shows'">
                    <v-col md="12" cols="12">
                         <v-slider
                            v-model="$v.form.seasons.$model"
                            append-icon="mdi-file-multiple"
                            min="1"
                            max="20"
                            label="Seasons"
                            thumb-label="always"
                            :error-messages="seasonsErrors"
                        >
                           <template v-slot:thumb-label="{ value }">
                                {{ value }}
                            </template>
                        </v-slider>
                    </v-col>
                    <v-col md="12" cols="12">
                        <v-slider
                            v-model="$v.form.season_length.$model"
                            append-icon="mdi-view-comfy"
                            min="1"
                            max="100"
                            label="Episodes per season"
                            thumb-label="always"
                            :error-messages="season_lengthErrors"
                        >
                           <template v-slot:thumb-label="{ value }">
                                {{ value }}
                            </template>
                        </v-slider>
                    </v-col>
                    <v-col md="12" cols="12">
                        <v-slider
                            v-model="$v.form.episode_length.$model"
                            append-icon="mdi-clock-end"
                            min="5"
                            max="180"
                            label="Episode Length"
                            thumb-label="always"
                            :error-messages="episode_lengthErrors"
                        >
                           <template v-slot:thumb-label="{ value }">
                                {{ value }}m
                            </template>
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
                            placeholder="Akon"
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
                            placeholder="Konvicted"
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
                        placeholder=""
                        prepend-inner-icon="mdi-book-account"
                        :error-messages="authorErrors"
                        ></v-text-field>
                    </v-col>
                </template>
            </v-row>
            <v-row align="start" justify="space-between">
                <v-col cols="12" xs="12" class="align-center">
                  <v-btn-toggle rounded>
                     <v-btn outlined large @click="$emit('previous', !$v.form.$invalid)" :color="$v.form.$invalid? 'error' : 'success'">
                        <v-icon>mdi-chevron-double-up</v-icon>
                    </v-btn>
                    <v-btn outlined large color="accent" @click="submit" :disabled="isCommonValid">
                        <v-icon left>mdi-cloud-upload-outline</v-icon> Add Post
                    </v-btn>
                    <v-btn outlined large :color="$v.form.$invalid? 'warning' : 'error'" @click="$v.form.$invalid? 'reset' : 'cancel'">
                        <v-icon left>{{$v.form.$invalid? 'mdi-refresh' : 'mdi-close'}}</v-icon>
                        {{$v.form.$invalid? 'Reset' : 'Cancel'}}
                    </v-btn>
                  </v-btn-toggle>
                </v-col>
            </v-row>
        </v-container>
    </v-form>

</template>

<script>
import { validationMixin } from 'vuelidate'
import { required, numeric } from 'vuelidate/lib/validators'

const templates = {
  movies: {
    language: '',
    director: '',
    streaming: []
  },
  shows: {
    seasons: '',
    episode_length: '',
    season_length: '',
    streaming: []
  },
  anime: {
    seasons: '',
    episode_length: '',
    season_length: '',
    streaming: []
  },
  music: {
    artist: '',
    streaming: '',
    album: ''
  },
  books: {
    author: ''
  }
}

const getRequiredErrors = (check, field) => {
  if (check) return [`${field} is required`]
  return []
}

const getNumErrors = (check, field) => {
  if (check) return [`${field} should be number`]
  return []
}

export default {
  name: 'ItemSpecificForm',
  mixins: [validationMixin],
  props: ['sheetType', 'isCommonValid'],
  data () {
    const data = {
      valid: true,
      search: null,
      streamingChoices: [
        'netflix',
        'hotstar',
        'torrent',
        'prime',
        'youtube'
      ],
      listeningChoices: [
        'youtube',
        'spotify',
        'gaana',
        'prime',
        'apple',
        'saavn'
      ],
      form: templates[this.sheetType]
    }
    return data
  },
  validations () {
    switch (this.sheetType) {
      case 'movies':
        return {
          form: {
            language: { required },
            director: { required },
            streaming: { required }
          }
        }
      case 'anime':
      case 'shows':
        return {
          form: {
            seasons: { required, numeric },
            episode_length: { required, numeric },
            season_length: { required, numeric },
            streaming: { required }
          }
        }
      case 'music':
        return {
          form: {
            artist: { required },
            streaming: { required }
          }
        }
      case 'books':
        return {
          form: {
            author: { required }
          }
        }
    }
  },
  methods: {
    submit: function () {
      const formData = JSON.stringify(this.form)
      this.form = templates[this.sheetType]
      this.$v.$reset()
      this.$emit('continue', formData)
      this.$root.$emit('ItemCommonForm')
    },
    reset: function () {
      this.form = templates[this.sheetType]
      this.$v.$reset()
      this.$refs.form.reset()
    },
    cancel: function () {
      this.form = templates[this.sheetType]
      this.$v.$reset()
      this.$refs.form.reset()
      this.$emit('cancel')
      this.$root.$emit('ItemCommonForm')
    }
  },
  watch: {
    sheetType (val, oldVal) {
      this.form = templates[val]
    },
    isValid (val, oldVal) {
      this.$emit('previous', val, false)
    }
  },
  computed: {
    isValid () {
      return !this.$v.form.$invalid
    },
    languageErrors () {
      let errors = []
      if (!this.$v.form.language.$dirty) return errors
      errors = [
        ...getRequiredErrors(
          !this.$v.form.language.required,
          'language'
        )
      ]
      return errors
    },
    directorErrors () {
      let errors = []
      if (!this.$v.form.director.$dirty) return errors
      errors = [
        ...getRequiredErrors(
          !this.$v.form.director.required,
          'director'
        )
      ]
      return errors
    },
    streamingErrors () {
      let errors = []
      if (!this.$v.form.streaming.$dirty) return errors
      errors = [
        ...getRequiredErrors(
          !this.$v.form.streaming.required,
          'streaming'
        )
      ]
      return errors
    },
    episode_lengthErrors () {
      let errors = []
      if (!this.$v.form.episode_length.$dirty) return errors
      errors = [
        ...getRequiredErrors(
          !this.$v.form.episode_length.required,
          'Episode Length'
        ),
        ...getNumErrors(
          !this.$v.form.episode_length.numeric,
          'Episode Length'
        )
      ]
      return errors
    },
    season_lengthErrors () {
      let errors = []
      if (!this.$v.form.season_length.$dirty) return errors
      errors = [
        ...getRequiredErrors(
          !this.$v.form.season_length.required,
          'Season Length'
        ),
        ...getNumErrors(
          !this.$v.form.season_length.numeric,
          'Season Length'
        )
      ]
      return errors
    },
    seasonsErrors () {
      let errors = []
      if (!this.$v.form.seasons.$dirty) return errors
      errors = [
        ...getRequiredErrors(!this.$v.form.seasons.required, 'Seasons'),
        ...getNumErrors(!this.$v.form.seasons.numeric, 'Seasons')
      ]
      return errors
    },
    artistErrors () {
      let errors = []
      if (!this.$v.form.artist.$dirty) return errors
      errors = [
        ...getRequiredErrors(!this.$v.form.artist.required, 'Artist')
      ]
      return errors
    },
    authorErrors () {
      let errors = []
      if (!this.$v.form.author.$dirty) return errors
      errors = [
        ...getRequiredErrors(!this.$v.form.author.required, 'Author')
      ]
      return errors
    }
  }
}
</script>
