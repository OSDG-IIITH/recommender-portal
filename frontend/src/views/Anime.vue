<template>
  <div class="home">
    <v-content>
      <HelloWorld :helloworld="helloworld"/>
    </v-content>
  </div>
</template>

<script>
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  components: {
    HelloWorld,
  },
}
</script>

<style scoped>
  .home {
    background-color: bisque;
  }
</style>
