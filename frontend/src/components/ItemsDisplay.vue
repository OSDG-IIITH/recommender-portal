<template>
    <v-container fluid>
        <v-row class="masonry" align="start" justify="space-between" dark>
        <template v-if="loading">
            <v-col
                class="child"
                cols="12"
                xs="12"
                sm="6"
                md="4"
                lg="3"
                xl="2"
                v-for="_ in stubArray"
                :key="_"
            >
                <v-boilerplate type="card-avatar, article, actions"></v-boilerplate>
            </v-col>
        </template>
        <template v-else>
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
        </template>
        </v-row>
    </v-container>
</template>

<script>
import Item from '@/components/Item'

var msnry = new Masonry('.masonry', {
  // options
  itemSelector: '.child'
})

export default {
  name: 'ItemsDisplay',
  components: {
    Item,
    VBoilerplate: {
      functional: true,
      render (h, { data, props, children }) {
        return h('v-skeleton-loader', {
          ...data,
          props: {
            boilerplate: true,
            elevation: 2,
            ...props
          }
        }, children)
      }
    }
  },
  data () {
    return {
      loading: false,
      stubArray: Array.from({ length: Math.floor(Math.random() * (10 - 6 + 1) + 6) })
    }
  },
  created: async function () {
    this.loading = true
    await this.$store.dispatch('items/fetchItems', this.$route.name)
    this.loading = false
  },
  computed: {
    post_keys: function () {
      return this.$store.getters['items/getKeysByCategory'](
        this.$route.name
      )
    }
  },
  watch: {
    $route: async function (to, from) {
      this.loading = true
      await this.$store.dispatch('items/fetchItems', to.name)
      this.loading = false
    }
  }
}
</script>
