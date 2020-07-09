<template>
    <v-container fluid>
        <v-row class="masonry" align="start" justify="space-between" dark>
            <v-col
                class="child"
                cols="12"
                xs="12"
                sm="6"
                md="4"
                lg="3"
                xl="2"
                v-for="post_key in post_keys"
                :key="post_key"
            >
                <Item :post_id="post_key" />
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import Item from "@/components/Item";

var msnry = new Masonry(".masonry", {
    // options
    itemSelector: ".child"
});

export default {
    name: "ItemsDisplay",
    components: {
        Item
    },
    created: async function() {
        await this.$store.dispatch("items/fetchItems", this.$route.name);
    },
    computed: {
        post_keys: function() {
            return this.$store.getters["items/getKeysByCategory"](
                this.$route.name
            );
        }
    }
};
</script>
