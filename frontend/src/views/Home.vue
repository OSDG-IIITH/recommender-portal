<template>
  <div class="home">
    <v-content>
      <HelloWorld :helloworld="helloworld"/>
      <FloatingButton :floatingbutton="floatingbutton"/>
    </v-content>
  </div>
</template>

<script>
import HelloWorld from '@/components/HelloWorld.vue'
import FloatingButton from '@/components/FloatingButton'

export default {
  name: 'Home',
  components: {
    HelloWorld,
    FloatingButton
  }
}
</script>

<style scoped>
  .home {
    background-color: bisque;
  }
</style>
