import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index'
import MasterAdmin from '@/components/MasterAdmin'
import * as APP_TYPES from '@/store/app-types'

Vue.use(Router)

const routes = [
  // { path: '/login', name: 'login', component: Login },
  { path: '/' + APP_TYPES.INDEX, name: 'Index', component: Index },
  { path: '/' + APP_TYPES.MASTER_ADMIN, name: 'MasterAdmin', component: MasterAdmin },
  { path: '/', redirect: '/' + APP_TYPES.INDEX }
]

const router = new Router({ routes, mode: 'history' })

export default router
