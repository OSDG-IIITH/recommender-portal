import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

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
    component: () => import('@/views/Books.vue')
  },
  {
    path: '/movies',
    name: 'Movies',
    component: () => import('@/views/Movies.vue')
  },
  {
    path: '/anime',
    name: 'Anime',
    component: () => import('@/views/Anime.vue')
  },
  {
    path: '/shows',
    name: 'Shows',
    component: () => import('@/views/Shows.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
