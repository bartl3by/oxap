const ERROR_TYPE_API = 'api'
const ERROR_TYPE_DATA = 'data'

class Exception {

  static get ERROR_TYPE_API () {
    return ERROR_TYPE_API
  }

  static get ERROR_TYPE_DATA () {
    return ERROR_TYPE_DATA
  }

  static get ERROR_TYPES () {
    return {
      'ERROR_TYPE_API': ERROR_TYPE_API,
      'ERROR_TYPE_DATA': ERROR_TYPE_DATA
    }
  }

  constructor (msg, err) {
    this.msg = msg
    this.err = err
  }
}

export default Exception
