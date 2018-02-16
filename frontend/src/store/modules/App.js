import { App as types } from '@/store/mutation-types'
import * as APP_TYPES from '@/store/app-types'
import api from '@/store/api'
import Exception from '@/store/util/Exception'

const state = {
  currentApp: APP_TYPES.INDEX,
  accounts: {},
  endpointsLoading: false,
  endpointsError: false
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
    state.accounts = data
  }
}

const getters = {
  currentApp: state => state.currentApp
}

const actions = {
  setCurrentApp: ({ commit }, app) => {
    commit(types.SET_CURRENT, app)
  },
  loadEndpoints: ({ commit }) => {
    commit(types.ENDPOINTS_LIST_REQUEST)
    return api.getEndpoints().then(function (data) {
      // make sure returned data is acceptable
      if (!data && !data instanceof Array) {
        commit(types.ENDPOINTS_LIST_ERROR)
        return false
      }

      // api returns endpoints and accounts in a flat structure.
      // change to strucutre of one account:many endpoints
      const accounts = {}
      data.forEach(function (item) {
        // create item in accounts object if it doesn't yet exist
        if (!accounts[item.oxap_account_id]) {
          accounts[item.oxap_account_id] = {
            'account_id': item['oxap_account_id'],
            'account_name': item['oxap_account_name'],
            'account_description': item['oxap_account_description'],
            endpoints: []
          }
        }

        // add endpoint to the account
        accounts[item.oxap_account_id].endpoints.push({
          'endpoint_id': item['endpoint_id'],
          'endpoint_name': item['endpoint_name'],
          'endpoint_description': item['endpoint_description']
        })
      })

      // set the values in the store
      commit(types.ENDPOINTS_LIST_SUCCESS, accounts)
      return accounts
    })
  }
}

export default {
  state,
  mutations,
  getters,
  actions
}
