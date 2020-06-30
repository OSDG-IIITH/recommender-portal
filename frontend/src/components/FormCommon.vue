<template>
    <v-form v-model="valid">
        <v-checkbox v-model="form.hidden" label="Hidden"></v-checkbox>

        <v-text-field
            v-model="form.title"
            type="text"
            label="Title"
            :rules="nameRules"
        ></v-text-field>

        <v-text-field
            v-model="form.url"
            type="text"
            label="Url"
            :rules="nameRules"
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
            v-model="form.year_release"
            type="text"
            label="Year"
            :rules="nameRules"
        ></v-text-field>

        <v-btn
            color="secondary"
            @click="$emit('continue', JSON.stringify(form))"
            :disabled="!valid"
            >Continue</v-btn
        >
        <v-btn text @click="$emit('cancel')">Cancel</v-btn>
    </v-form>
</template>

<script>
export default {
    name: "FormCommon",
    data: () => ({
        valid: true,
        nameRules: [v => !!v || "Required"],
        form: {}
    })
};
</script>
