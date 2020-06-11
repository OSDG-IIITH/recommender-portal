<template>
  <v-navigation-drawer
      v-model="drawer"
      app
    >
      <v-list dense>
        <v-list-item link to='/'>
          <v-list-item-action>
            <v-icon>mdi-home</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Home</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link to='/books'>
          <v-list-item-action>
            <v-icon>mdi-book</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Books</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link to='/movies'>
          <v-list-item-action>
            <v-icon>mdi-movie</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Movies</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link to='anime'>
          <v-list-item-action>
            <v-icon>mdi-fire</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Anime</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link to='shows'>
          <v-list-item-action>
            <v-icon>mdi-film</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Shows</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
</template>

<script>
export default {
  name: 'Navbar',
  props: {
    drawer: Boolean
  }
}
</script>