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
      .then(function () {
        return [{
          'average_size': 464345,
          'enabled': true,
          'filestoreId': 1,
          'filestore_name': 'billybob',
          'id': 1,
          'loginMappings': '?',
          'name': 'Context 1',
          'readDatabase': {},
          'usedQuota': 0,
          'userAttributes': {},
          'writeDatabase': {}
        },
        {
          'average_size': 444224,
          'enabled': true,
          'filestoreId': 2,
          'filestore_name': 'steve',
          'id': 2,
          'loginMappings': '?',
          'name': 'Context 2',
          'readDatabase': {},
          'usedQuota': 23432353242,
          'userAttributes': {},
          'writeDatabase': {}
        }]
      })
  }
}
