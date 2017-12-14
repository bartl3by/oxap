import { App as types } from '../mutation-types'
import * as APP_TYPES from '../app-types'
import Exception from '../util/Exception'

const state = {
  currentApp: APP_TYPES.INDEX
}

const mutations = {
  [types.SET_CURRENT] (state, val) {
    if (Object.values(APP_TYPES).includes(val)) {
      state.currentApp = val
    } else {
      throw Exception(val + ' is not a valid application')
    }
  }
}

const getters = {
  currentApp: state => state.currentApp
}

const actions = {
  setCurrentApp: ({ commit }, app) => {
    commit(types.SET_CURRENT, app)
  }
}

export default {
  state,
  mutations,
  getters,
  actions
}
