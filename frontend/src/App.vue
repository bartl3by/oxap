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
        <b-navbar-nav class="ml-auto">
          <b-nav-item-dropdown right v-if="sessionsCount">
            <!-- Using button-content slot -->
            <template slot="button-content">
              <i class="fa fa-users"></i> Sessions
            </template>
            <b-dropdown-item v-for="(session, key) in sessions" :key="key" @click="selectApp(key)">
              <b-media right-align vertical-align="center">
                <b-button slot="aside" title="Logout this session" @click="logout(session.id)"><i class="fa fa-sign-out"></i></b-button>
                <h6>{{ key }}</h6>
                <small>{{ session.endpoint.endpoint_name }}</small>
              </b-media>  
            </b-dropdown-item>
            
          </b-nav-item-dropdown>
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
    },
    logout (id) {
      this.$store.dispatch('logout', id)
    }
  },
  computed: mapState({
    isActiveMasterAdmin: state => (state.App.currentApp === APP_TYPES.MASTER_ADMIN),
    isActiveContextAdmin: state => (state.App.currentApp === APP_TYPES.CONTEXT_ADMIN),
    currentApp: state => state.App.currentApp,
    endpoints: state => state.App.endpoints,
    sessions: state => state.App.sessions,
    sessionsCount: state => state.App.sessionsCount
  }),
  watch: {
    sessions: function () {
      if (!this.sessions.hasOwnProperty(this.currentApp)) this.$router.push('/login/' + this.currentApp)
    }
  }
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
