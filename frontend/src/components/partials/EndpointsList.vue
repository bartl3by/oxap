<template>
    <b-form-select value-field="endpoint_id" text-field="endpoint_name" :value="value" :options="options" @input="changeValue">
</template>

<script>
  import { mapState } from 'vuex'

  export default {
    name: 'EndpointsList',
    props: [
      'value'
    ],
    methods: {
      changeValue (val) {
        this.$emit('change', val)
        this.$store.dispatch('setCurrentEndpoint', val)
      }
    },
    computed: mapState({
      options: state => state.App.endpoints
    })
  }
</script>