<template>
  <b-container>
    <b-row>
      <b-col sm="12" md="8" offset-md="2">
        <h2>Master Admin Login</h2>
        <b-alert show variant="primary">Log in to the Master Admin panel using your Master Admin credentials. </b-alert>
      </b-col>
    </b-row>
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
          <b-form-group id="account-select" label="Account" label-for="account">
            <b-form-select id="account" :options="accounts" @input="selectAccount" value-field="account_id" text-field="account_name" required></b-form-select>
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
  import * as appTypes from '@/store/app-types'

  export default {
    name: 'Login',
    methods: {
      login () {
        // construct the credentials payload required by the session service
        const creds = {
          'account_id': this.account ? this.account.account_id : false,
          'username': this.username,
          'password': this.password
        }

        const router = this.$router
        const store = this.$store

        // attempt login
        this.$store.dispatch('MasterAdmin/login', creds).then(function (data) {
          store.dispatch('setCurrentApp', appTypes.MASTER_ADMIN).then(function () {
            router.replace({ name: appTypes.MASTER_ADMIN })
          })
        })

        return false
      },
      selectAccount (id) {
        this.account = this.accounts[id]
      }
    },
    data () {
      return {
        username: null,
        password: null,
        account: null
      }
    },
    computed: mapState({
      accounts: state => state.App.accounts,
      endpoints: state => state.endpoints,
      loginError: state => state.MasterAdmin.sessionError
    }),
    mounted: function () {
      const selectAccount = this.selectAccount
      if (!this.endpoints || !this.endpoints.length) {
        this.$store.dispatch('loadEndpoints').then(function (data) {
          // automatically select the first value
          selectAccount(Object.keys(data)[0])
        })
      }
    }
  }
</script>