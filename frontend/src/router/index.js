import Vue from 'vue'
import VueRouter from 'vue-router'
import ItemsDisplay from '@/views/ItemsDisplay.vue'
import Home from '@/views/Home.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/books',
    name: 'Books',
    component: ItemsDisplay
  },
  {
    path: '/movies',
    name: 'Movies',
    component: ItemsDisplay
  },
  {
    path: '/music',
    name: 'Music',
    component: ItemsDisplay
  },
  {
    path: '/anime',
    name: 'Anime',
    component: ItemsDisplay
  },
  {
    path: '/shows',
    name: 'Shows',
    component: ItemsDisplay
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
