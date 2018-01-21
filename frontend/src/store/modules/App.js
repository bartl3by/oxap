import { App as types } from '../mutation-types'
import * as APP_TYPES from '../app-types'
import api from '../api'
import Exception from '../util/Exception'

const state = {
  currentApp: APP_TYPES.INDEX,
  endpoints: [],
  endpointsLoading: false,
  endpointsError: false,
  sessionCreating: false,
  sessionDeleting: false,
  sessionError: false,
  sessions: {},
  sessionsCount: 0
}

const mutations = {
  [types.SET_CURRENT] (state, val) {
    if (Object.values(APP_TYPES).includes(val)) {
      state.currentApp = val
    } else {
      throw Exception(val + ' is not a valid application')
    }
  },
  [types.ENDPOINTS_LIST_REQUEST] (state) {
    state.endpointsLoading = true
    state.endpointsError = false
  },
  [types.ENDPOINTS_LIST_ERROR] (state) {
    state.endpointsLoading = false
    state.endpointsError = true
  },
  [types.ENDPOINTS_LIST_SUCCESS] (state, data) {
    state.endpointsLoading = false
    state.endpointsError = false
    state.endpoints = data
  },
  [types.SESSION_CREATE_REQUEST] (state) {
    state.sessionCreating = true
    state.sessionError = false
  },
  [types.SESSION_CREATE_SUCCESS] (state, payload) {
    state.sessionCreating = false
    state.sessionError = false
    state.sessions[payload.app] = payload.data
    state.sessionsCount = Object.keys(state.sessions).length
  },
  [types.SESSION_CREATE_ERROR] (state, data) {
    state.sessionCreating = false
    state.sessionError = data
  },
  [types.SESSION_DELETE_REQUEST] (state) {
    state.sessionDeleting = true
  },
  [types.SESSION_DELETE_SUCCESS] (state, key) {
    state.sessionDeleting = false
    delete state.sessions[key]
    // hack to force reactivity
    state.sessions = Object.assign({}, state.sessions)
    state.sessionsCount = Object.keys(state.sessions).length
  },
  [types.SESSION_DELETE_ERROR] (state) {
    state.sessionDeleting = false
  }
}

const getters = {
  currentApp: state => state.currentApp,
  currentEndpoint: state => state.currentEndpoint,
  endpoints: state => state.endpoints,
  sessions: state => state.sessions,
  sessionError: state => state.sessionError
}

const actions = {
  setCurrentApp: ({ commit }, app) => {
    commit(types.SET_CURRENT, app)
  },
  login: ({ commit, state }, payload) => {
    const creds = payload.creds
    const app = payload.app

    const endpoint = state.endpoints.find(function (endpoint) {
      return endpoint.endpoint_id === payload.creds.endpoint_id
    })

    commit(types.SESSION_CREATE_REQUEST, creds)
    return api.createSession(creds).then(function (data) {
      data.endpoint = endpoint
      commit(types.SESSION_CREATE_SUCCESS, { app, data })
      return data
    }).catch(function (e) {
      commit(types.SESSION_CREATE_ERROR, e)
    })
  },
  logout: ({ commit, state }, id) => {
    api.deleteSession(id).then(function () {
      // find the session key which contains the session id passed in, commit the delete
      for (const key in state.sessions) {
        if (state.sessions[key].id === id) commit(types.SESSION_DELETE_SUCCESS, key)
      }
    })
  },
  loadEndpoints: ({ commit }) => {
    commit(types.ENDPOINTS_LIST_REQUEST)
    return api.getEndpoints().then(function (data) {
      commit(types.ENDPOINTS_LIST_SUCCESS, data)
      return data
    })
  },
  autologin: () => {
    // for now, check if the user has an endpoint selected. If they do, go on. If not, reject.
    // TODO: incorporate actual autologin as well
    // return state.currentEndpoint ? Promise.resolve() : Promise.reject()
  }
}

export default {
  state,
  mutations,
  getters,
  actions
}
