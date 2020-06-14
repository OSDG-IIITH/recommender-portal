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
  name: 'Music',
  components: {
    HelloWorld,
  }
}
</script>
