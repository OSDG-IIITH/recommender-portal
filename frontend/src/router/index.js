import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/views/Home.vue')
  },
  {
    path: '/books',
    name: 'Books',
    component: () => import('@/views/CategoryPage.vue')
  },
  {
    path: '/movies',
    name: 'Movies',
    component: () => import('@/views/CategoryPage.vue')
  },
  {
    path: '/music',
    name: 'Music',
    component: () => import('@/views/CategoryPage.vue')
  },
  {
    path: '/anime',
    name: 'Anime',
    component: () => import('@/views/CategoryPage.vue')
  },
  {
    path: '/shows',
    name: 'Shows',
    component: () => import('@/views/CategoryPage.vue')
  },
  {
    path: '/search',
    name: 'Search',
    component: () => import('@/views/SearchPage.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
