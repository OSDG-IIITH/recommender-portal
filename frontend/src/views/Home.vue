<template>
  <div class="home">
    <v-content>
      <v-container fluid>
        <p>
          <v-btn @click="check">Dummy </v-btn>
        </p>
        <span>
          Lorem ipsum, dolor sit amet consectetur adipisicing elit. Quam harum quidem asperiores
          dolore fugiat inventore vitae corporis libero eos, facere dolorem nam, deserunt error
          velit cum temporibus accusantium exercitationem enim!
        </span>
      </v-container>
    </v-content>
  </div>
</template>

<script>
export default {
  name: 'Home',
  methods: {
    check: function () {
      console.log('DEBUG Function!')
      // NOTE: Do your debuging of actions / mutations here
    }
  }
}
</script>
