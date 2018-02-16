import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index'
// import Login from '@/components/Login'
import MasterAdmin from '@/components/MasterAdmin/MasterAdmin'
import MasterAdminLogin from '@/components/MasterAdmin/Login'
// import ContextAdmin from '@/components/ContextAdmin'
import * as APP_TYPES from '@/store/app-types'
import store from '@/store'

Vue.use(Router)

const routes = [
  // { path: '/login/:app', name: 'login', component: Login },
  { path: '/' + APP_TYPES.INDEX, name: APP_TYPES.INDEX, component: Index },
  { path: '/' + APP_TYPES.MASTER_ADMIN, name: APP_TYPES.MASTER_ADMIN, component: MasterAdmin },
  { path: '/master-login', name: 'master-login', component: MasterAdminLogin },
  // { path: '/' + APP_TYPES.CONTEXT_ADMIN, name: APP_TYPES.CONTEXT_ADMIN, component: ContextAdmin },
  { path: '/', redirect: '/' + APP_TYPES.INDEX }
]

const router = new Router({ routes, mode: 'history' })

// handle autologin requests if possible
router.beforeEach((to, from, next) => {
  switch (to.name) {
    case APP_TYPES.MASTER_ADMIN:
      if (store.state.MasterAdmin.session) next()
      else next({ name: 'master-login' })
      break
    // case APP_TYPES.CONTEXT_ADMIN:
    //   if (store.getters.sessions[to.name]) next()
    //   else next({ name: 'login', params: { app: to.name }})

    //   break
    default:
      next()
  }
})

export default router
