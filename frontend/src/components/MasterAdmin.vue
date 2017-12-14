<template>
  
    <b-card no-body>
      <b-tabs card>
        <b-tab title="Endpoint Configuration" disabled>
          
        </b-tab>
        <b-tab title="Contexts">
            <ox-contexts-list />
        </b-tab>
        
      </b-tabs>
    </b-card>
  
</template>

<script>
  import Vue from 'vue'
  import ContextsList from './ContextsList'

  Vue.component('ox-contexts-list', ContextsList)

  export default {
    name: 'MasterAdmin',
    methods: {},
    computed: {}
  }
</script>


