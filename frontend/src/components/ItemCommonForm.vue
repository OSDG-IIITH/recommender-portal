<template>
    <v-form ref="form" v-model="valid">
        <v-container fluid>
            <v-row align="start" justify="space-around">
                <v-col md="12" cols="12">
                    <v-text-field
                        v-model.trim="$v.form.title.$model"
                        type="text"
                        label="Title"
                        min=3
                        max=100
                        outlined
                        filled
                        clearable
                        dense
                        placeholder="Angrezi Medium"
                        prepend-inner-icon="mdi-format-title"
                        :error-messages="titleErrors"
                        required
                    ></v-text-field>
                </v-col>
                <v-col md="12" cols="12">
                    <v-text-field
                        v-model.trim="$v.form.link.$model"
                        type="url"
                        label="Link"
                        outlined
                        filled
                        clearable
                        dense
                        placeholder="https://www.hotstar.com/in/movies/angrezi-medium/"
                        prepend-inner-icon="mdi-link-variant-plus"
                        :error-messages="urlErrors"
                        required
                        ></v-text-field>
                </v-col>
                <v-col md="12" cols="12">
                        <v-slider
                        v-model="$v.form.year_release.$model"
                        class="align-center"
                        thumb-label="always"
                        label="Year released"
                        min="1950"
                        :max="(new Date()).getFullYear()"
                        :value="(new Date()).getFullYear()"
                        :error-messages="year_releaseErrors"
                        required
                        ></v-slider>
                </v-col>
                <v-col md="12" cols="12">
                     <v-combobox
                        v-model.trim="$v.form.genres.$model"
                        :items="genre_options"
                        :search-input.sync="search"
                        hint="Add a genre if it does not already exist"
                        label="Genre(s)"
                        hide-selected
                        multiple
                        outlined
                        filled
                        clearable
                        prepend-inner-icon="mdi-view-grid-plus-outline"
                        small-chips
                        :error-messages="genreErrors"
                        required
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
            </v-row>
            <v-row align="start" justify="space-between">
                <v-col cols="12" xs="12" class="align-center">
                  <v-btn-toggle rounded>
                    <v-btn outlined large @click="$emit('next', !$v.form.$invalid)" :color="isValid? 'success': 'error'">
                        <v-icon>mdi-chevron-double-down</v-icon>
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
import { required, numeric, url } from 'vuelidate/lib/validators'

export default {
  mixins: [validationMixin],
  name: 'ItemCommonForm',
  data: () => ({
    valid: false,
    genre_options: ['Gaming', 'Programming', 'Vue', 'Vuetify'],
    search: null,
    nameRules: [v => !!v || 'Required'],
    form: {
      title: '',
      link: '',
      genres: [],
      year_release: '',
      flags: []
    }
  }),
  validations: {
    form: {
      title: { required },
      link: {
        required,
        url
      },
      genres: {required},
      year_release: { required, numeric }
    }
  },
  watch: {
    isValid (val, oldVal) {
      this.$emit('next', val, false)
    }
  },
  computed: {
    titleErrors: function () {
      const errors = []
      if (!this.$v.form.title.$dirty) return errors
      !this.$v.form.title.required && errors.push('Title is required')
      return errors
    },
    urlErrors: function () {
      const errors = []
      if (!this.$v.form.link.$dirty) return errors
      !this.$v.form.link.required && errors.push('URL is required')
      !this.$v.form.link.url && errors.push('Not a correct URL')
      return errors
    },
    genreErrors: function () {
      const errors = []
      if (!this.$v.form.genres.$dirty) return errors
      !this.$v.genres.required && errors.push('At least ONE genre is required!')
      return errors
    },
    year_releaseErrors: function () {
      const errors = []
      if (!this.$v.form.year_release.$dirty) return errors
      !this.$v.form.year_release.required &&
                  errors.push('Year is required')
      !this.$v.form.year_release.numeric &&
                  errors.push('Year should be a number')
      return errors
    }
  },
  methods: {
    submit: function () {
      const formData = JSON.stringify(this.form)
      this.$v.$reset()
      this.$emit('continue', formData)
    },
    reset: function () {
      this.$refs.form.reset()
      this.form = {
        title: '',
        link: '',
        genres: [],
        year_release: '',
        flags: []
      }
      this.$v.$reset()
    },
    cancel: function () {
      this.form = {
        title: '',
        link: '',
        genres: [],
        year_release: '',
        flags: []
      }
      this.$v.$reset()
      this.$refs.form.reset()
      this.$emit('cancel')
    }
  },
  mounted () {
    this.$root.$on('ItemCommonForm', () => {
      this.cancel()
    })
  }
}
</script>
