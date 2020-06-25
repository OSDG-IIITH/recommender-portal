<template>
  <v-layout row>
    <v-text-field
      class="mx-4 mx-xs-6"
      flat
      hide-details
      label="Search"
      prepend-inner-icon="mdi-magnify"
      solo-inverted
    ></v-text-field>
  </v-layout>
</template>
<script>
export default {
  name: "SearchBox"
};
</script>
