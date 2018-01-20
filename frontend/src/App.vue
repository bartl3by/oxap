<template>
  <div id="app">

    <b-navbar toggleable="md" type="dark" variant="primary" sticky>
      <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>
      <b-navbar-brand><img src="./assets/logo.png"></b-navbar-brand>
      <b-collapse is-nav id="nav_collapse">
        <b-navbar-nav>
          <b-nav-item @click="selectMasterAdmin" :class="{ active: isActiveMasterAdmin }">Master Admin</b-nav-item>
          <b-nav-item @click="selectContextAdmin" :class="{ active: isActiveContextAdmin }">Context Admin</b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
      
    <router-view/>
  </div>
</template>

<script>

// import Vue from 'vue'
import { mapState } from 'vuex'
import * as APP_TYPES from '@/store/app-types'

export default {
  name: 'app',
  methods: {
    selectApp (app) {
      this.$store.dispatch('setCurrentApp', app)
      this.$emit('selectApp', app)
      this.$router.push('/' + app)
    },
    selectMasterAdmin () {
      this.selectApp(APP_TYPES.MASTER_ADMIN)
    },
    selectContextAdmin () {
      this.selectApp(APP_TYPES.CONTEXT_ADMIN)
    }
  },
  computed: mapState({
    isActiveMasterAdmin: state => (state.App.currentApp === APP_TYPES.MASTER_ADMIN),
    isActiveContextAdmin: state => (state.App.currentApp === APP_TYPES.CONTEXT_ADMIN),
    currentApp: state => state.App.currentApp,
    endpoints: state => state.App.endpoints
  })
}
</script>

<style lang="scss">
  nav.navbar {
    
    // background-color: #3c73aa;

    .navbar-brand img {
      height: 20px;
    }
  }
</style>
