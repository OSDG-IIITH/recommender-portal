<template>
    <div>
        <div v-if="sheetType === 'movies'">
            <v-form ref="form" v-model="valid">
                <v-text-field
                    v-model="form.language"
                    label="Language"
                    :rules="required"
                ></v-text-field>

                <v-text-field
                    v-model="form.director"
                    label="Director"
                    :rules="required"
                ></v-text-field>

                <v-text-field
                    v-model="form.streaming"
                    label="Streaming on"
                    :rules="required"
                ></v-text-field>
                <v-btn
                    color="secondary"
                    @click="$emit('continue', JSON.stringify(form))"
                    :disabled="!valid"
                    >Submit</v-btn
                >
                <v-btn text @click="$emit('cancel')">Cancel</v-btn>
            </v-form>
        </div>
        <div v-else-if="sheetType === 'anime'">
            <v-form ref="form" v-model="valid">
                <v-text-field
                    v-model="form.seasons"
                    label="Seasons"
                    :rules="required"
                ></v-text-field>

                <v-text-field
                    v-model="form.episode_length"
                    label="Episode Length"
                    :rules="required"
                ></v-text-field>

                <v-text-field
                    v-model="form.season_length"
                    label="Season Length"
                    :rules="required"
                ></v-text-field>

                <v-text-field
                    v-model="form.streaming"
                    label="Streaming on"
                    :rules="required"
                ></v-text-field>
                <v-btn
                    color="secondary"
                    @click="$emit('continue', JSON.stringify(form))"
                    :disabled="!valid"
                    >Submit</v-btn
                >
                <v-btn text @click="$emit('cancel')">Cancel</v-btn>
            </v-form>
        </div>
        <div v-else-if="sheetType === 'shows'">
            <v-form ref="form" v-model="valid">
                <v-text-field
                    v-model="form.seasons"
                    label="Seasons"
                    :rules="required"
                ></v-text-field>

                <v-text-field
                    v-model="form.episode_length"
                    label="Episode Length"
                    :rules="required"
                ></v-text-field>

                <v-text-field
                    v-model="form.season_length"
                    label="Season Length"
                    :rules="required"
                ></v-text-field>

                <v-text-field
                    v-model="form.streaming"
                    label="Streaming on"
                    :rules="required"
                ></v-text-field>
                <v-btn
                    color="secondary"
                    @click="$emit('continue', JSON.stringify(form))"
                    :disabled="!valid"
                    >Submit</v-btn
                >
                <v-btn text @click="$emit('cancel')">Cancel</v-btn>
            </v-form>
        </div>
        <div v-else-if="sheetType === 'music'">
            <v-form ref="form" v-model="valid">
                <v-text-field
                    v-model="form.artist"
                    label="Artist"
                    :rules="required"
                ></v-text-field>

                <v-text-field
                    v-model="form.album"
                    label="Album"
                    :rules="required"
                ></v-text-field>

                <v-text-field
                    v-model="form.streaming"
                    label="Streaming on"
                    :rules="required"
                ></v-text-field>
                <v-btn
                    color="secondary"
                    @click="$emit('continue', JSON.stringify(form))"
                    :disabled="!valid"
                    >Submit</v-btn
                >
                <v-btn text @click="$emit('cancel')">Cancel</v-btn>
            </v-form>
        </div>
        <div v-else-if="sheetType === 'books'">
            <v-form ref="form" v-model="valid">
                <v-text-field
                    v-model="form.author"
                    label="Author"
                    :rules="required"
                ></v-text-field>
                <v-btn
                    color="secondary"
                    @click="$emit('continue', JSON.stringify(form))"
                    :disabled="!valid"
                    >Submit</v-btn
                >
                <v-btn text @click="$emit('cancel')">Cancel</v-btn>
            </v-form>
        </div>
    </div>
</template>

<script>
export default {
    name: "FormSpecific",
    props: {
        sheetType: String
    },
    data: () => ({
        valid: true,
        form: {},
        required: [v => !!v || "Required"]
    })
};
</script>
