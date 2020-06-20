import Vue from 'vue'
import VueRouter from 'vue-router'
import CategoryPage from '@/views/CategoryPage.vue'
import SearchPage from '@/views/SearchPage.vue'
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
    component: CategoryPage
  },
  {
    path: '/movies',
    name: 'Movies',
    component: CategoryPage
  },
  {
    path: '/music',
    name: 'Music',
    component: CategoryPage
  },
  {
    path: '/anime',
    name: 'Anime',
    component: CategoryPage
  },
  {
    path: '/shows',
    name: 'Shows',
    component: CategoryPage
  },
  {
    path: '/search',
    name: 'Search',
    component: SearchPage
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
