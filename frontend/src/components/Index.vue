<template>
  <b-container>
    <b-row>
      <b-col>
        <b-jumbotron header="OX Admin Panel" lead="Because life is too short for command line.">
          <p>Right now, only Master Admin and Context Admin are supported. More features will be added soon.</p>
          <b-btn variant="primary" @click="selectMasterAdmin">Master Admin Panel</b-btn> <b-btn variant="primary" @click="selectContextAdmin">Context Admin Panel</b-btn> 
        </b-jumbotron>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
  import * as APP_TYPES from '@/store/app-types'

  export default {
    name: 'Index',
    methods: {
      selectMasterAdmin () {
        this.$parent.selectApp(APP_TYPES.MASTER_ADMIN)
      },
      selectContextAdmin () {
        this.$parent.selectApp(APP_TYPES.CONTEXT_ADMIN)
      }
    }
  }
</script>
