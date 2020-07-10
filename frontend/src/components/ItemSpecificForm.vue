<template>
    <div>
        <div v-if="sheetType === 'movies'">
            <v-form ref="form" v-model="valid">
                <v-text-field
                    v-model="$v.form.language.$model"
                    label="Language"
                    :error-messages="languageErrors"
                ></v-text-field>

                <v-text-field
                    v-model="$v.form.director.$model"
                    label="Director"
                    :error-messages="directorErrors"
                ></v-text-field>

                <v-select
                    v-model="$v.form.streaming.$model"
                    :items="streamingChoices"
                    label="Streaming on"
                    :error-messages="streamingErrors"
                ></v-select>
                <v-btn
                    color="secondary"
                    @click="submit"
                    :disabled="$v.form.$invalid"
                    >Submit</v-btn
                >
                <v-btn text @click="cancel">Cancel</v-btn>
            </v-form>
        </div>
        <div v-else-if="sheetType === 'anime' || sheetType === 'shows'">
            <v-form ref="form">
                <v-text-field
                    v-model="$v.form.seasons.$model"
                    label="Seasons"
                    :error-messages="seasonsErrors"
                ></v-text-field>

                <v-text-field
                    v-model="$v.form.episode_length.$model"
                    label="Episode Length"
                    :error-messages="episode_lengthErrors"
                ></v-text-field>

                <v-text-field
                    v-model="$v.form.season_length.$model"
                    label="Season Length"
                    :error-messages="season_lengthErrors"
                ></v-text-field>

                <v-select
                    v-model="$v.form.streaming.$model"
                    :items="streamingChoices"
                    label="Streaming on"
                    :error-messages="streamingErrors"
                ></v-select>
                <v-btn
                    color="secondary"
                    @click="submit"
                    :disabled="$v.form.$invalid"
                    >Submit</v-btn
                >
                <v-btn text @click="cancel">Cancel</v-btn>
            </v-form>
        </div>
        <div v-else-if="sheetType === 'music'">
            <v-form ref="form">
                <v-text-field
                    v-model="$v.form.artist.$model"
                    label="Artist"
                    :error-messages="artistErrors"
                ></v-text-field>

                <v-text-field v-model="form.album" label="Album"></v-text-field>

                <v-select
                    v-model="$v.form.streaming.$model"
                    :items="listeningChoices"
                    label="Streaming on"
                    :error-messages="streamingErrors"
                ></v-select>
                <v-btn
                    color="secondary"
                    @click="submit"
                    :disabled="$v.form.$invalid"
                    >Submit</v-btn
                >
                <v-btn text @click="cancel">Cancel</v-btn>
            </v-form>
        </div>
        <div v-else-if="sheetType === 'books'">
            <v-form ref="form">
                <v-text-field
                    v-model="$v.form.author.$model"
                    label="Author"
                    :error-messages="authorErrors"
                ></v-text-field>
                <v-btn
                    color="secondary"
                    @click="submit"
                    :disabled="$v.form.$invalid"
                    >Submit</v-btn
                >
                <v-btn text @click="cancel">Cancel</v-btn>
            </v-form>
        </div>
    </div>
</template>

<script>
import { validationMixin } from "vuelidate";
import { required, numeric } from "vuelidate/lib/validators";

const templates = {
    movies: {
        language: "",
        director: "",
        streaming: ""
    },
    shows: {
        seasons: "",
        episode_length: "",
        season_length: "",
        streaming: ""
    },
    anime: {
        seasons: "",
        episode_length: "",
        season_length: "",
        streaming: ""
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

const getRequiredErrors = (check, field) => {
    if (check) return [`${field} is required`];
    return [];
};

const getNumErrors = (check, field) => {
    if (check) return [`${field} should be number`];
    return [];
};

export default {
    name: "ItemSpecificForm",
    mixins: [validationMixin],
    props: ["sheetType"],
    data() {
        const data = {
            valid: true,
            streamingChoices: [
                "netflix",
                "hotstar",
                "torrent",
                "prime",
                "youtube",
                "other  "
            ],
            listeningChoices: [
                "youtube",
                "spotify",
                "gaana",
                "prime",
                "apple",
                "saavn"
            ],
            form: templates[this.sheetType]
        };
        return data;
    },
    validations() {
        switch (this.sheetType) {
            case "movies":
                return {
                    form: {
                        language: { required },
                        director: { required },
                        streaming: { required }
                    }
                };
            case "anime":
            case "shows":
                return {
                    form: {
                        seasons: { required, numeric },
                        episode_length: { required, numeric },
                        season_length: { required, numeric },
                        streaming: { required }
                    }
                };
            case "music":
                return {
                    form: {
                        artist: { required },
                        streaming: { required }
                    }
                };
            case "books":
                return {
                    form: {
                        author: { required }
                    }
                };
        }
    },
    methods: {
        submit: function() {
            const formData = JSON.stringify(this.form);
            this.form = templates[this.sheetType];
            this.$v.$reset();
            this.$emit("continue", formData);
        },
        cancel: function() {
            this.form = templates[this.sheetType];
            this.$v.$reset();
            this.$emit("cancel");
        }
    },
    watch: {
        sheetType(val, oldVal) {
            this.form = templates[val];
        }
    },
    computed: {
        languageErrors() {
            let errors = [];
            if (!this.$v.form.language.$dirty) return errors;
            errors = [
                ...getRequiredErrors(
                    !this.$v.form.language.required,
                    "language"
                )
            ];
            return errors;
        },
        directorErrors() {
            let errors = [];
            if (!this.$v.form.director.$dirty) return errors;
            errors = [
                ...getRequiredErrors(
                    !this.$v.form.director.required,
                    "director"
                )
            ];
            return errors;
        },
        streamingErrors() {
            let errors = [];
            if (!this.$v.form.streaming.$dirty) return errors;
            errors = [
                ...getRequiredErrors(
                    !this.$v.form.streaming.required,
                    "streaming"
                )
            ];
            return errors;
        },
        episode_lengthErrors() {
            let errors = [];
            if (!this.$v.form.episode_length.$dirty) return errors;
            errors = [
                ...getRequiredErrors(
                    !this.$v.form.episode_length.required,
                    "Episode Length"
                ),
                ...getNumErrors(
                    !this.$v.form.episode_length.numeric,
                    "Episode Length"
                )
            ];
            return errors;
        },
        season_lengthErrors() {
            let errors = [];
            if (!this.$v.form.season_length.$dirty) return errors;
            errors = [
                ...getRequiredErrors(
                    !this.$v.form.season_length.required,
                    "Season Length"
                ),
                ...getNumErrors(
                    !this.$v.form.season_length.numeric,
                    "Season Length"
                )
            ];
            return errors;
        },
        seasonsErrors() {
            let errors = [];
            if (!this.$v.form.seasons.$dirty) return errors;
            errors = [
                ...getRequiredErrors(!this.$v.form.seasons.required, "Seasons"),
                ...getNumErrors(!this.$v.form.seasons.numeric, "Seasons")
            ];
            return errors;
        },
        artistErrors() {
            let errors = [];
            if (!this.$v.form.artist.$dirty) return errors;
            errors = [
                ...getRequiredErrors(!this.$v.form.artist.required, "Artist")
            ];
            return errors;
        },
        authorErrors() {
            let errors = [];
            if (!this.$v.form.author.$dirty) return errors;
            errors = [
                ...getRequiredErrors(!this.$v.form.author.required, "Author")
            ];
            return errors;
        }
    }
};
</script>
