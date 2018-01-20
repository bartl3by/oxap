<template>
  <b-container>
    <b-form @submit.prevent="login">
      <b-alert :show="loginError" variant="danger">{{ loginError }}</b-alert>
      <b-form-row>
        <b-col sm="12" md="6" offset-md="3" lg="4" offset-lg="4">
          <b-form-group id="username-input" label="User Name" label-for="username">
            <b-form-input id="username" type="text" v-model="username" required></b-form-input>
          </b-form-group>
        </b-col>
      </b-form-row>
      <b-form-row>
        <b-col sm="12" md="6" offset-md="3" lg="4" offset-lg="4">
          <b-form-group id="password-input" label="Password" label-for="password">
            <b-form-input id="password" type="password" v-model="password" required></b-form-input>
          </b-form-group>
        </b-col>
      </b-form-row>
      <b-form-row>
        <b-col sm="12" md="6" offset-md="3" lg="4" offset-lg="4">
          <b-form-group id="endpoint-select" label="Endpoint" label-for="endpoint">
            <b-form-select id="endpoint" :options="endpoints" @input="selectEndpoint" value-field="endpoint_id" text-field="endpoint_name" required></b-form-select>
          </b-form-group>
        </b-col>
      </b-form-row>
      <b-form-row class="text-right">
        <b-col sm="12" md="6" offset-md="3" lg="4" offset-lg="4">
          <b-button variant="primary" type="submit">Login</b-button>
        </b-col>
      </b-form-row>
    </b-form>
  </b-container>
</template>

<script>
  import { mapState } from 'vuex'

  export default {
    name: 'Login',
    methods: {
      login: function () {
        // get the application being logged into from the route param
        const returnApp = this.$route.params.app

        // construct the credentials payload required by the session service
        const creds = {
          'account_id': this.endpoint.oxap_account_id,
          'endpoint_id': this.endpoint.endpoint_id,
          'username': this.username,
          'password': this.password,
          'role': 'oxap'
        }

        const router = this.$router

        // attempt login
        this.$store.dispatch('login', { app: returnApp, creds }).then(function (data) {
          router.replace({ name: returnApp })
        })

        return false
      },
      selectEndpoint: function (id) {
        this.endpoint = this.endpoints.find(function (item) {
          return item.endpoint_id === id
        })
      }
    },
    data () {
      return {
        username: null,
        password: null,
        endpoint: null
      }
    },
    computed: mapState({
      endpoints: state => state.App.endpoints,
      loginError: state => state.App.sessionError
    }),
    mounted: function () {
      this.$store.dispatch('loadEndpoints')
    }
  }
</script>