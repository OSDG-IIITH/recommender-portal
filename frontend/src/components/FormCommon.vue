<template>
    <v-form
        ref="form"
        v-model="valid"
        lazy-validation
    >

        <v-text-field
          label="Flags"
        ></v-text-field>

        <v-checkbox
          v-model="checkbox"
          label="Hidden"
        ></v-checkbox>

        <v-text-field
          v-model="name"
          label="Title"
          required
        ></v-text-field>

        <v-text-field
          v-model="url"
          label="Url"
          required
        ></v-text-field>

        <v-text-field
          v-model="numberValue"
          label="Year"
          required
        ></v-text-field>

        <v-text-field
          v-model="name"
          label="Genre"
        ></v-text-field>
    </v-form>
</template>

<script>
export default {
    name: "FormCommon"
};
</script>