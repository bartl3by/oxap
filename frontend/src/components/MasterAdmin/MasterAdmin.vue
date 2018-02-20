<template>
  
    <b-card no-body>
      <b-tabs card>
        <b-tab title="Endpoint Configuration" disabled>
          
        </b-tab>
        <b-tab title="Contexts">
          <b-dropdown variant="primary" :text="endpointName">
            <template slot="button-content">
              <i class="fa fa-sitemap"></i> {{ endpointName }}
            </template>
            <b-dropdown-item v-for="endpoint in endpoints" :key="endpoint.endpoint_id" @click="selectEndpoint(endpoint)">{{ endpoint.endpoint_name }}</b-dropdown-item>
          </b-dropdown>
          <div class="float-right">
            <b-button variant="secondary" @click="createContext" :disabled="!currentEndpoint"><i class="fa fa-cubes"></i> Create Context</b-button>
          </div>
          <ox-contexts-list @clickContext="editContext" />
        </b-tab>
      </b-tabs>
      <ox-edit-context ref="editContextDialog" @visibility:set="val => showContextEditDialog = val" :show="showContextEditDialog" :context="currentContext"></ox-edit-context>
    </b-card>
    
</template>

<script>
  import Vue from 'vue'
  import { mapState } from 'vuex'
  import ContextsList from './partials/ContextsList'
  import EditContext from './partials/EditContext'

  Vue.component('ox-contexts-list', ContextsList)
  Vue.component('ox-edit-context', EditContext)

  export default {
    name: 'MasterAdmin',
    methods: {
      selectEndpoint (endpoint) {
        const store = this.$store
        store.dispatch('MasterAdmin/setEndpoint', endpoint).then(function () {
          store.dispatch('MasterAdmin/getContexts')
        })
      },
      createContext () {
        this.currentContext = false;
        this.showContextEditDialog = true;
      },
      editContext (context) {
        this.currentContext = context;
        this.showContextEditDialog = true;
      }
    },
    data () {
      return {
        currentContext: {},
        showContextEditDialog: false
      }
    },
    computed: mapState({
      contexts: state => state.MasterAdmin.contexts,
      endpoints: state => state.MasterAdmin.session && state.MasterAdmin.session.account_id && state.App.accounts ? state.App.accounts[state.MasterAdmin.session.account_id].endpoints : false,
      endpointName: state => state.MasterAdmin.currentEndpoint ? state.MasterAdmin.currentEndpoint.endpoint_name : 'Choose an Endpoint',
      currentEndpoint: state => state.MasterAdmin.currentEndpoint
    })
  }
</script>


