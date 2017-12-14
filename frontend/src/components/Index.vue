<template>
  <b-container>
    <b-row>
      <b-col>
        <b-jumbotron header="OX Admin Panel" lead="Because life is too short for command line.">
          <p>Right now, only Master Admin is supported. More features will be added soon.</p>
          <b-btn variant="primary" @click="selectMasterAdmin">Master Admin Panel</b-btn>
        </b-jumbotron>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
  export default {
    name: 'Index',
    methods: {
      selectMasterAdmin () {
        this.$parent.selectMasterAdmin()
      }
    },
    computed: {}
  }
</script>
