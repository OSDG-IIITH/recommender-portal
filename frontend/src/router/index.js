import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import('@/views/Home.vue')
  },
  {
    path: '/books',
    name: 'books',
    component: () => import('@/views/CategoryPage.vue')
  },
  {
    path: '/movies',
    name: 'movies',
    component: () => import('@/views/CategoryPage.vue')
  },
  {
    path: '/music',
    name: 'music',
    component: () => import('@/views/CategoryPage.vue')
  },
  {
    path: '/anime',
    name: 'anime',
    component: () => import('@/views/CategoryPage.vue')
  },
  {
    path: '/shows',
    name: 'shows',
    component: () => import('@/views/CategoryPage.vue')
  },
  {
    path: '/search',
    name: 'search',
    component: () => import('@/views/SearchPage.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
