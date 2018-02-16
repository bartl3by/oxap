import http from '@/store/util/http'
import Exception from '@/store/util/Exception'

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

  deleteSession: (id) => {
    return http.delete('oxap/session', { 'Oxapsessionid': id })
  },

  createContext: (data, endpointId) => {
    return http.post('context?endpoint_id=' + endpointId, data)
  },

  updateContext: (contextId, data, endpointId) => {
    return http.put('context/' + contextId + '?endpoint_id=' + endpointId, data)
  },

  deleteContext: (contextId, endpointId) => {
    return http.delete('context/' + contextId + '?endpoint_id=' + endpointId);
  },

  /**
   * Get available contexts for an accountId/endpointId
   */
  getContexts: (endpointId, sessionId) => {
    return http.setSession(sessionId).get('context', { 'endpoint_id': endpointId })
      .then(json => {
        if (json.error) {
          throw new ApiException('Error fetching contexts.')
        }
        return json
      })
  }
}
