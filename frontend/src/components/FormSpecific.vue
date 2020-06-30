<template>
<div>
    <div v-if="sheetType === 'movies'">
        <v-form
            ref="form"
            v-model="valid"
            lazy-validation
        >
            <v-text-field
                v-model="name"
                label="Language"
                required
            ></v-text-field>

            <v-text-field
                v-model="name"
                label="Director"
                required
            ></v-text-field>

            <v-text-field
                v-model="name"
                label="Streaming on"
                required
            ></v-text-field>

        </v-form>
    </div>
    <div v-else-if="sheetType === 'anime'">
        <v-form
            ref="form"
            v-model="valid"
            lazy-validation
        >
            <v-text-field
                v-model="numberValue"
                label="Seasons"
                required
            ></v-text-field>

            <v-text-field
                v-model="name"
                label="Episode Length"
                required
            ></v-text-field>

            <v-text-field
                v-model="name"
                label="Season Length"
                required
            ></v-text-field>

            <v-text-field
                v-model="name"
                label="Streaming on"
                required
            ></v-text-field>

        </v-form>
    </div>
    <div v-else-if="sheetType === 'shows'">
        <v-form
            ref="form"
            v-model="valid"
            lazy-validation
        >
            <v-text-field
                v-model="numberValue"
                label="Seasons"
                required
            ></v-text-field>

            <v-text-field
                v-model="name"
                label="Episode Length"
                required
            ></v-text-field>

            <v-text-field
                v-model="name"
                label="Season Length"
                required
            ></v-text-field>

            <v-text-field
                v-model="name"
                label="Streaming on"
                required
            ></v-text-field>

        </v-form>
    </div>
    <div v-else-if="sheetType === 'music'">
        <v-form
            ref="form"
            v-model="valid"
            lazy-validation
        >

            <v-text-field
                v-model="name"
                label="Artist"
                required
            ></v-text-field>

            <v-text-field
                v-model="name"
                label="Album"
                required
            ></v-text-field>

            <v-text-field
                v-model="name"
                label="Streaming on"
                required
            ></v-text-field>

        </v-form>
    </div>
    <div v-else-if="sheetType === 'books'">
        <v-form
            ref="form"
            v-model="valid"
            lazy-validation
        >

            <v-text-field
                v-model="name"
                label="Author"
                required
            ></v-text-field>

        </v-form>
    </div>
</div>
</template>

<script>
export default {
    name: "FormSpecific",
    props: {
        sheetType: String
    }
};
</script>