import 'whatwg-fetch'

const API_VERSION = 'v2'

export default {
  get (endpoint, data) {
    let params = ''

    // construct parameters to pass based on data passed in. Could be string or object
    if (data !== null && typeof data !== 'undefined' && typeof data === 'object') {
      for (const key in data) {
        if (data[key] !== null && typeof data[key] === 'object') {
          data[key] = JSON.stringify(data[key])
        } else {
          params += (params === '' ? '' : '&') + encodeURIComponent(key) + '=' + encodeURIComponent(data[key])
        }
      }
    } else {
      params = data
    }

    // perform fetch and get the response json to pass along
    return window.fetch('/' + API_VERSION + '/' + endpoint + (params && params.length ? '?' + params : ''), {
      credentials: 'include'
    }).then(response => response.json())
  },
  post (endpoint, data) {
    // perform fetch and return response (if any)
    return window.fetch('/' + API_VERSION + '/' + endpoint, {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data),
      credentials: 'include'
    }).then(response => response.json())
  },
  put (endpoint, data) {
    // perform fetch and return response (if any)
    return window.fetch('/' + API_VERSION + '/' + endpoint, {
      method: 'PUT',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data),
      credentials: 'include'
    }).then(response => response.json())
  },
  delete (endpoint, data) {
    // perform fetch and return response (if any)
    return window.fetch('/' + API_VERSION + '/' + endpoint, {
      method: 'DELETE',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data),
      credentials: 'include'
    }).then(response => response.json())
  }
}
