<template>
  <v-form ref="form" v-model="valid" :lazy-validation="true">
    <v-container fluid>
      <v-row align="start" justify="space-around">
        <v-col md="12" cols="12">
          <v-text-field
            v-model.trim="$v.form.title.$model"
            type="text"
            label="Title"
            min="3"
            max="100"
            outlined
            filled
            clearable
            dense
            :placeholder="post.title"
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
            :placeholder="post.url"
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
                    No results matching "
                    <strong>{{ search }}</strong>". Press
                    <kbd>enter</kbd> to create a new one
                  </v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </template>
          </v-combobox>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>

<script>
import { validationMixin } from "vuelidate";
import { required, numeric, url } from "vuelidate/lib/validators";

export default {
  mixins: [validationMixin],
  name: "EditItemCommonForm",
  props: ["post"],
  data: function() {
    return {
      valid: true,
      genre_options: ["Gaming", "Programming", "Vue", "Vuetify"],
      search: null,
      nameRules: [v => !!v || "Required"],
      form: {
        title: this.post.title,
        link: this.post.url,
        genres: this.post.genres,
        year_release: this.post.year_release,
        flags: this.post.flags
      }
    };
  },
  validations: {
    form: {
      title: {},
      link: {
        url
      },
      genres: {},
      year_release: { numeric }
    }
  },
  computed: {
    titleErrors: function() {
      const errors = [];
      if (!this.$v.form.title.$dirty) return errors;
      return errors;
    },
    urlErrors: function() {
      const errors = [];
      if (!this.$v.form.link.$dirty) return errors;
      !this.$v.form.link.url && errors.push("Not a correct URL");
      return errors;
    },
    genreErrors: function() {
      const errors = [];
      if (!this.$v.form.genres.$dirty) return errors;
      return errors;
    },
    year_releaseErrors: function() {
      const errors = [];
      if (!this.$v.form.year_release.$dirty) return errors;
      !this.$v.form.year_release.numeric &&
        errors.push("Year should be a number");
      return errors;
    }
  },
  methods: {
    submit: function() {
      const editCommonFormData = JSON.stringify(this.form);
      this.$v.$reset();
      this.$emit("editCommonSubmit", editCommonFormData);
    },
    reset: function() {
      this.form = {
        title: this.post.title,
        link: this.post.url,
        genres: this.post.genres,
        year_release: this.post.year_release,
        flags: this.post.flags
      };
      this.$v.$reset();
    }
  },
  mounted() {
    this.$root.$on("EditItemCommonFormReset", () => {
      this.reset();
    });
    this.$root.$on("EditItemCommonFormSubmit", () => {
      this.submit();
    });
  }
};
</script>
