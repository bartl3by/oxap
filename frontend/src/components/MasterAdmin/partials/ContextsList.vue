<template>
  <b-table striped hover small tbody-tr-class="click_editable" :items="contexts" :fields="displayFields" @row-clicked="clickContext">

  </b-table>
</template>

<script>
  import { mapState } from 'vuex'

  export default {
    name: 'ContextsList',
    methods: {
      loadContexts () {
        this.$store.dispatch('MasterAdmin/getContexts')
      },
      clickContext(context) {
        this.$emit('clickContext', context)
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
            maxQuota: {
              sortable: true
            },
            loginMappings: {
              sortable: false
            },
            
          }
        }
      },
      ...mapState({
        contexts: state => state.MasterAdmin.contexts
      })
    }
  }
</script>
