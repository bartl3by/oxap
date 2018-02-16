<template>
  <b-modal size="lg" :title="title" v-model="showModal" @ok="onSubmit">

    <b-alert :show="!!contextError" variant="danger">{{ contextError }}</b-alert>

    <b-form @submit="onSubmit">
      <b-container>

        <b-form-input placeholder="Context Name" v-model="form.context.name"></b-form-input>
        <b-form-input type="number" placeholder="Max Quota (bytes)" v-model="form.context.maxQuota"></b-form-input>
        
        <fieldset>
          <legend>Context Admin</legend>
          <b-row>
            <b-col>
              <b-form-input placeholder="First Name" required v-model="form.user.given_name" @change="updateDisplayName"></b-form-input>
            </b-col>
            <b-col>
              <b-form-input placeholder="Last Name" required v-model="form.user.sur_name" @change="updateDisplayName"></b-form-input>
            </b-col>
          </b-row>
          <b-row>
            <b-col>
              <b-form-input placeholder="Display Name" v-model="form.user.display_name"></b-form-input>
            </b-col>
          </b-row>
          <b-row>
            <b-col>
              <b-form-input placeholder="User Name" required v-model="form.user.name"></b-form-input>
            </b-col>
            <b-col>
              <b-form-input placeholder="Password" required v-model="form.user.password" type="password"></b-form-input>
            </b-col>
          </b-row>
          <b-row>
            <b-col>
              <b-form-input placeholder="Primary Email" required v-model="form.user.primaryEmail" type="email"></b-form-input>
            </b-col>
            <b-col>
              <b-form-input placeholder="Email 1" v-model="form.user.email" type="email"></b-form-input>
            </b-col>
            <b-col>
              <b-form-input placeholder="Email 2" v-model="form.user.email1" type="email"></b-form-input>
            </b-col>
          </b-row>
        </fieldset>
      </b-container>
    </b-form>
    <div slot="modal-ok">
      Save
    </div>
  </b-modal>
</template>

<script>
  import { mapState } from 'vuex'

  export default {
    name: 'EditContext',
    props: [
      'show',
      'context'
    ],
    methods: {
      updateDisplayName () {
        this.form.user.display_name = this.form.user.given_name + ' ' + this.form.user.sur_name
      },
      onSubmit (evt) {
        // prevent the modal from hiding before save is done
        evt.preventDefault()
        
        if (this.contextId) {
          this.$store.dispatch('MasterAdmin/updateContext', this.contextId, this.form).then(this.close)
        } else {
          this.$store.dispatch('MasterAdmin/createContext', this.form).then(this.close).catch(() => {})
        }
      },
      close () {
        this.showModal = false;
      }
    },
    data () {
      return {
        contextId: false,
        form: {
          context: {
            name: '',
            maxQuota: 0
          },
          user: {
            given_name: '',
            sur_name: '',
            display_name: '',
            email: '',
            email1: '',
            name: null,
            password: null,
            primaryEmail: null
          }
        }
      }
    },
    computed: {
      showModal: {
        get () {
          return this.show || false
        },
        set (val) {
          this.$emit('visibility:set', val)
        }
      },
      title () { return this.id ? 'Edit Context' : 'Create Context' },
      ...mapState({
        currentEndpoint: state => state.MasterAdmin.currentEndpoint,
        contextSaving: state => state.MasterAdmin.contextSaving,
        contextError: state => state.MasterAdmin.contextError
      })
    },
    watch: {
      show () {
        this.showModal = this.show
      }
    },
    mounted: function () {
      if (this.context) {
        // this.form = this.context 
      }
    }
  }
</script>