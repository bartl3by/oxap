import Vue from 'vue'
import Vuex from 'vuex'
import App from './modules/App'
import MasterAdmin from './modules/MasterAdmin'
import ContextAdmin from './modules/ContextAdmin'

Vue.use(Vuex)

const debug = process.env.NODE_ENV !== 'production'

export default new Vuex.Store({
  modules: {
    App,
    MasterAdmin,
    ContextAdmin
  },
  strict: debug,
  plugins: []
})
