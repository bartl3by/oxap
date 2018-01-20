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
  sessionError: false,
  sessions: {}
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
  [types.SESSION_CREATE_SUCCESS] (state, appName, data) {
    state.sessionCreating = false
    state.sessionError = false
    state.sessions[appName] = data
  },
  [types.SESSION_CREATE_ERROR] (state, data) {
    state.sessionCreating = false
    state.sessionError = data
  },
  [types.SESSION_SET_FOR_APP] (state, payload) {
    state.sessions[payload.app] = payload.data
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
  login: ({ commit }, payload) => {
    const creds = payload.creds
    const app = payload.app

    commit(types.SESSION_CREATE_REQUEST, creds)
    return api.createSession(creds).then(function (data) {
      commit(types.SESSION_SET_FOR_APP, { app, data })
      return data
    }).catch(function (e) {
      commit(types.SESSION_CREATE_ERROR, e)
    })
  },
  loadEndpoints: ({ commit }) => {
    commit(types.ENDPOINTS_LIST_REQUEST)
    return api.getEndpoints().then(function (data) {
      commit(types.ENDPOINTS_LIST_SUCCESS, data)
      return data
    })
  },
  // setCurrentEndpoint: ({ commit }, id) => {
  //   commit(types.SET_ENDPOINT, id)
  // },

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
