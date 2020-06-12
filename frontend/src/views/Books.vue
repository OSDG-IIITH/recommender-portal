<template>
    <v-content class="base">
        <v-card class="mx-auto px-1">
            <v-row dense v-for="row in cards" :key="row[0].title">
                <v-col v-for="card in row" :key="card.title" :cols="3">
                    <v-card class="pa-2 card">
                        <Card :card="card"/>
                    </v-card>
                </v-col>
            </v-row>
        </v-card>
    </v-content>  
</template>

<script>
import axios from 'axios'
import Card from '../components/Card'
export default {
    data() {
        return {
            cards : []
        }
    },
    components: {
        Card,
    },
    mounted: function(){
        let data = null
        axios
            .get('https://www.googleapis.com/books/v1/volumes?q=+subject:thriller&maxResults=20')
            .then(response => {
                data = response.data.items
                for (let i = 0; i<data.length / 4; i++) {
                    const temp = []
                    for (let j = 0; j < 4 ; j++) {
                        if ( i * 4 + j > data.length - 1){
                            break
                        }
                        const tempObj = {
                        title: data[i * 4 + j].volumeInfo.title,
                        image: data[i * 4 + j].volumeInfo.imageLinks.thumbnail,
                        description: data[i * 4 + j].volumeInfo.description
                    }
                    temp.push(tempObj)
                }
                this.cards.push(temp)
            }
            console.log(this.cards)
        })
    }
}

</script>

<style scoped>
  .base,.mx-auto,.card {
    background-color: bisque;
  }
  
</style>