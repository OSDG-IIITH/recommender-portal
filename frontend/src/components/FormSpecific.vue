<template>
<div>
    <div v-if="sheetType === 'Movies'">
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
    <div v-else-if="sheetType === 'Anime'">
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
    <div v-else-if="sheetType === 'Shows'">
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
    <div v-else-if="sheetType === 'Music'">
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
    <div v-else-if="sheetType === 'Books'">
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