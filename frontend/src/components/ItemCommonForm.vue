<template>
    <v-form>
        <v-text-field
            v-model.trim="$v.form.title.$model"
            type="text"
            label="Title"
            :error-messages="titleErrors"
        ></v-text-field>

        <v-text-field
            v-model.trim="$v.form.url.$model"
            type="text"
            label="Url"
            :error-messages="urlErrors"
        ></v-text-field>

        <v-text-field v-model="form.flags" label="Flags"></v-text-field>
        <small>Add values seperated by commas</small>
        <v-text-field
            v-model="form.genres"
            label="Genres"
            type="text"
        ></v-text-field>
        <small>Add values seperated by commas</small>

        <v-text-field
            v-model="$v.form.year_release.$model"
            type="text"
            label="Year"
            :error-messages="year_releaseErrors"
        ></v-text-field>

        <v-btn
            color="secondary"
            @click="$emit('continue', JSON.stringify(form))"
            :disabled="$v.form.$invalid"
            >Continue</v-btn
        >
        <v-btn text @click="$emit('cancel')">Cancel</v-btn>
    </v-form>
</template>

<script>
import { validationMixin } from "vuelidate";
import { required, numeric } from "vuelidate/lib/validators";

export default {
    mixins: [validationMixin],
    name: "ItemCommonForm",
    data: () => ({
        valid: false,
        nameRules: [v => !!v || "Required"],
        form: {
            title: "",
            url: "",
            genres: "",
            year_release: "",
            flags: ""
        }
    }),
    validations: {
        form: {
            title: { required },
            url: {
                required,
                isURL(val) {
                    const expression = /(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})/gi;
                    const regex = new RegExp(expression);
                    if (val.match(regex)) return true;
                    return false;
                }
            },
            year_release: { required, numeric }
        }
    },
    computed: {
        titleErrors: function() {
            const errors = [];
            if (!this.$v.form.title.$dirty) return errors;
            !this.$v.form.title.required && errors.push("Title is required");
            return errors;
        },
        urlErrors: function() {
            const errors = [];
            if (!this.$v.form.url.$dirty) return errors;
            !this.$v.form.url.required && errors.push("URL is required");
            !this.$v.form.url.isURL && errors.push("Not a correct URL");
            return errors;
        },
        year_releaseErrors: function() {
            const errors = [];
            if (!this.$v.form.year_release.$dirty) return errors;
            !this.$v.form.year_release.required &&
                errors.push("Year is required");
            !this.$v.form.year_release.numeric &&
                errors.push("Year should be a number");
            return errors;
        }
    }
};
</script>
