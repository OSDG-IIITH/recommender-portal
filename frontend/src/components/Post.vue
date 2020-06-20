<template>
   <v-card
    class="mx-auto elevation-20"
    color="green darken-2"
    dark
    style="max-width: 20vw; max-height: 70vw;"
  >
    <v-img
        class="shrink ma-2"
        contain
        height="15vw"
        src="https://cdn.vuetifyjs.com/images/cards/halcyon.png"
    ></v-img>
    <v-divider light></v-divider>
    <v-row>
      <v-col>
        <v-card-title primary-title style="font-size:2vw">
          
            <div>Halycon Days</div>
            
        </v-card-title>
      </v-col>
    </v-row>
    <v-divider light></v-divider>
    <v-card-actions class="pa-0">
      
      <span class="text--lighten-2 mr-1" style="font-size:1.5vw">
        ({{ rating }})
      </span>
      <v-rating
        v-model="rating"
        color="yellow accent-4"
        dense
        half-increments
        hover
        size="1.5vw"
      ></v-rating>
    </v-card-actions>
    
    <v-card-actions class="pa-0">
      <v-btn 
        text x-small
      >
        <v-icon 
        size="2.5vw" color = "red">mdi-heart</v-icon>
        {{ likes }}
      </v-btn>

      <v-btn 
        color="purple"
        icon x-small
        >
        <v-icon size="2.5vw">mdi-bookmark</v-icon>
      </v-btn>
      <v-btn
        color="white"
        icon x-small
      >
        <v-icon size="2vw">mdi-link</v-icon>
      </v-btn>
      <v-spacer></v-spacer>
      <v-btn
        color="blue darken-2"
        @click="show = !show"
        icon
      >
        <v-icon size="2.5vw">mdi-comment</v-icon>
      </v-btn>
      
    </v-card-actions>
     <v-expand-transition>
      <div v-show="show">
        <v-divider></v-divider>
        <CommentTimeline/>
      </div>
    </v-expand-transition>
  </v-card>
</template>

<script>
import CommentTimeline from '@/components/CommentTimeline'
  export default {
    name: 'Post',

    components:{
      CommentTimeline
    },

    props: {
        post: Object
    },

    data: () => ({
      rating: 4.3,
      show: false
    }),
  }
</script>
