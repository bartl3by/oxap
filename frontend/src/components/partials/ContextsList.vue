<template>
  <b-table striped :items="contexts" :fields="displayFields">

  </b-table>
</template>

<script>
  import { mapGetters } from 'vuex'

  export default {
    name: 'ContextsList',
    methods: {
      loadContexts () {
        this.$store.dispatch('getContexts')
      }
    },
    mounted: function () {
      this.loadContexts()
    },
    computed: {
      displayFields: {
        get: function () {
          return {
            id: {
              label: 'ID',
              sortable: true
            },
            name: {
              sortable: true
            },
            enabled: {
              sortable: true
            },
            'average_size': {
              sortable: true
            },
            usedQuota: {
              sortable: true
            },
            loginMappings: {
              sortable: true
            },
            'filestore_name': {
              label: 'Filestore'
            },
            filestoreId: {
              label: 'Filestore ID'
            }
          }
        }
      },
      ...mapGetters([
        'contexts'
      ])
    }
  }
</script>
