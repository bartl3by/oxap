import { MasterAdmin as types } from '@/store/mutation-types'
import api from '@/store/api'
import Exception from '@/store/util/Exception'
import * as roleTypes from '@/store/role-types'

const state = {
  contexts: [],
  contextsLoading: false,
  contextsError: false,
  contextSaving: false,
  contextError: false,
  currentContext: {},
  currentEndpoint: false,
  session: false,
  sessionCreating: false,
  sessionError: false
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
  },
  [types.SET_ENDPOINT] (state, data) {
    state.currentEndpoint = data
  },
  [types.CONTEXT_CREATE_REQUEST] (state) {
    state.contextSaving = true
    state.contextError = false
  },
  [types.CONTEXT_CREATE_SUCCESS] (state) {
    state.contextSaving = false
    state.contextError = false
  },
  [types.CONTEXT_CREATE_ERROR] (state, err) {
    state.contextSaving = false
    state.contextError = err
  },
  [types.CONTEXT_UPDATE_REQUEST] (state) {
    state.contextSaving = true
    state.contextError = false
  },
  [types.CONTEXT_UPDATE_SUCCESS] (state) {
    state.contextSaving = false
    state.contextError = false
  },
  [types.CONTEXT_UPDATE_ERROR] (state, err) {
    state.contextSaving = false
    state.contextError = err
  },
  [types.CONTEXT_DELETE_REQUEST] (state) {
    state.contextSaving = true
    state.contextError = false
  },
  [types.CONTEXT_DELETE_SUCCESS] (state) {
    state.contextSaving = false
    state.contextError = false
  },
  [types.CONTEXT_DELETE_ERROR] (state, err) {
    state.contextSaving = false
    state.contextError = err
  },
  [types.SESSION_CREATE_REQUEST] (state) {
    state.sessionCreating = true
    state.sessionError = false
  },
  [types.SESSION_CREATE_SUCCESS] (state, data) {
    state.sessionCreating = false
    state.sessionError = false
    state.session = data
  },
  [types.SESSION_CREATE_ERROR] (state, data) {
    state.sessionCreating = false
    state.sessionError = data
  },
  [types.SESSION_DELETE_REQUEST] (state) {
    state.sessionDeleting = true
  },
  [types.SESSION_DELETE_SUCCESS] (state) {
    state.sessionDeleting = false
    state.session = false
  },
  [types.SESSION_DELETE_ERROR] (state) {
    state.sessionDeleting = false
  }
}

const getters = {
  session: (state) => state.session,
  contexts: (state) => state.contexts,
  currentContext: (state) => state.currentContext,
  contextSaving: (state) => state.contextSaving,
  contextError: (state) => state.contextError
}

const actions = {
  getContexts: ({ commit, state }) => {
    if (state.currentEndpoint) {
      commit(types.CONTEXTS_LIST_REQUEST)
      return api.getContexts(state.currentEndpoint.endpoint_id, state.session.id).then((data) => {
        commit(types.CONTEXTS_LIST_SUCCESS, data)
      }).catch(function (e) {
        const error = e instanceof Exception ? e.msg : e
        commit(types.CONTEXTS_LIST_ERROR, error)
      })
    }
  },
  createContext: ({ commit, state, dispatch }, data) => {
    commit(types.CONTEXT_CREATE_REQUEST)
    return api.createContext(data, state.currentEndpoint.endpoint_id).then((data) => {
      commit(types.CONTEXT_CREATE_SUCCESS)
      dispatch('getContexts')
      return data
    }).catch((e) => {
      commit(types.CONTEXT_CREATE_ERROR, e)
      throw new Exception(e)
    })
  },
  updateContext: ({ commit, state, dispatch }, contextId, data) => {
    commit(types.CONTEXT_UPDATE_REQUEST)
    return api.updateContext(contextId, data, state.currentEndpoint.endpoint_id).then((data) => {
      commit(types.CONTEXT_UPDATE_SUCCESS)
      dispatch('getContexts')
      return data
    }).catch((e) => {
      commit(types.CONTEXT_UPDATE_ERROR, e)
    })
  },
  deleteContext: ({ commit, state, dispatch }, contextId) => {
    commit(types.CONTEXT_DELETE_REQUEST)
    return api.deleteContext(contextId, state.currentEndpoint.endpoint_id).then(() => {
      commit(types.CONTEXT_DELETE_SUCCESS)
      dispatch('getContexts')
    }).catch((e) => {
      commit(types.CONTEXT_DELETE_ERROR, e)
    })
  },
  setEndpoint: ({ commit }, endpoint) => {
    commit(types.SET_ENDPOINT, endpoint)
  },
  login: ({ commit, state }, payload) => {
    // make sure all necessary info provided
    if (!payload.username || !payload.password || !payload.account_id) {
      throw new Exception('Required paramaters (username, password, account_id) not provided.')
    }

    // set role in the payload
    payload.role = roleTypes.ROLE_OXAP

    // mark that the session is being created
    commit(types.SESSION_CREATE_REQUEST, payload)

    // try to create the session on the server
    return api.createSession(payload).then(function (data) {
      // set session info and mark as success
      commit(types.SESSION_CREATE_SUCCESS, data)
      return data
    }).catch(function (e) {
      // note session create error
      commit(types.SESSION_CREATE_ERROR, e)
    })
  },
  logout: ({ commit, state }, id) => {
    api.deleteSession(id).then(function () {
      commit(types.SESSION_DELETE_SUCCESS)
    })
  }
}

export default {
  namespaced: true,
  state,
  mutations,
  getters,
  actions
}
