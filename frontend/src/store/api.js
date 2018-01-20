import http from './util/http'
import Exception from './util/Exception'

class ApiException extends Exception {
  constructor (msg) {
    super(msg, Exception.ERROR_TYPE_API)
  }
}

export default {

  /**
   * List all endpoints available by the server
   */
  getEndpoints: () => {
    return http.get('oxap/endpoints')
  },

  createSession: (creds) => {
    return http.post('oxap/session', creds)
  },

  /**
   * Get available contexts for an accountId/endpointId
   */
  getContexts: (accountId, endpointId) => {
    return http.get('context', { accountId, endpointId })
      .then(json => {
        if (json.error) {
          throw new ApiException('Error fetching contexts.')
        }
        return json
      })
  }
}
