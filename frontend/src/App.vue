<template>
  <v-app>
    <Navbar :drawer="drawer"/>
    <v-app-bar
      app
      color="indigo"
      dark
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>Application</v-toolbar-title>
    </v-app-bar>
    <v-content>
      <router-view/>
    </v-content>
  </v-app>
</template>

<script>
import HelloWorld from './components/HelloWorld';
import Navbar from './components/Navbar'

export default {
  name: 'App',
  props: {
      source: String,
  },
  components: {
    HelloWorld,
    Navbar
  },
  data: () => ({
    drawer: null,
  }),
};
</script>
