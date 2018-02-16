import 'whatwg-fetch'

const API_VERSION = 'v2'

function parseResponse(response) {
  return response.json().then(json => {
    return response.ok ? json : Promise.reject(json);
  });
}

export default {
  setSession (sessionId) {
    this.sessionId = sessionId
    return this
  },
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
      credentials: 'include',
      headers: {
        'Accept': 'application/json',
        'Oxapsessionid': this.sessionId ? this.sessionId : ''
      }
    }).then(parseResponse)
  },
  post (endpoint, data) {
    // perform fetch and return response (if any)
    return window.fetch('/' + API_VERSION + '/' + endpoint, {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Oxapsessionid': this.sessionId ? this.sessionId : ''
      },
      body: JSON.stringify(data),
      credentials: 'include'
    }).then(parseResponse)
  },
  put (endpoint, data) {
    // perform fetch and return response (if any)
    return window.fetch('/' + API_VERSION + '/' + endpoint, {
      method: 'PUT',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Oxapsessionid': this.sessionId ? this.sessionId : ''
      },
      body: JSON.stringify(data),
      credentials: 'include'
    }).then(parseResponse)
  },
  delete (endpoint, data) {
    // perform fetch and return response (if any)
    return window.fetch('/' + API_VERSION + '/' + endpoint, {
      method: 'DELETE',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Oxapsessionid': this.sessionId ? this.sessionId : ''
      },
      body: JSON.stringify(data),
      credentials: 'include'
    }).then(parseResponse)
  }
}
