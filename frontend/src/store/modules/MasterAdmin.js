import { MasterAdmin as types } from '../mutation-types'
import api from '../api'
import Exception from '../util/Exception'

const state = {
  contexts: [],
  contextsLoading: false,
  contextsError: false
}

const mutations = {
  [types.CONTEXTS_LIST_REQUEST] (state) {
    state.contextsLoading = true
    state.contextsError = false
  },
  [types.CONTEXTS_LIST_ERROR] (state) {
    state.contextsLoading = false
    state.contextsError = true
  },
  [types.CONTEXTS_LIST_SUCCESS] (state, data) {
    state.contextsLoading = false
    state.contextsError = false
    state.contexts = data
  }
}

const getters = {
  contexts: (state) => {
    return state.contexts
  }
}

const actions = {
  getContexts: ({ commit, rootState }) => {
    commit(types.CONTEXTS_LIST_REQUEST)
    return api.getContexts().then((data) => {
      commit(types.CONTEXTS_LIST_SUCCESS, data)
    }).catch(function (e) {
      const error = e instanceof Exception ? e.msg : e
      commit(types.CONTEXTS_LIST_ERROR, error)
    })
  }
}

export default {
  state,
  mutations,
  getters,
  actions
}
