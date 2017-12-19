import http from './util/http'
import Exception from './util/Exception'

class ApiException extends Exception {
  constructor (msg) {
    super(msg, Exception.ERROR_TYPE_API)
  }
}

export default {

  getContexts: () => {
    return http.get('context')
      .then(json => {
        if (json.error) {
          throw new ApiException('Error fetching contexts.')
        }
        return json
      })
  }
}
