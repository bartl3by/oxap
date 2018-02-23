<template>
  <b-modal size="lg" :title="title" v-model="showModal" @ok="onSubmit" @show="onLoad" no-close-on-backdrop lazy>

    <b-alert :show="!!contextError" variant="danger">{{ contextError }}</b-alert>

    <b-form @submit="onSubmit">
      <b-container>
        <b-form-group label="Context Name" label-for="form-context-name" description="">
          <b-form-input placeholder="Context Name" id="form-context-name" v-model="form.context.name"></b-form-input>
        </b-form-group>
        <b-form-group label="Max Quota (bytes)" label-for="form-max-quota" description="">
          <b-form-input type="number" placeholder="Max Quota (bytes)" id="form-max-quota" v-model="form.context.maxQuota"></b-form-input>
        </b-form-group>

        <fieldset v-if="!form.context.id">
          <legend>Context Admin</legend>
          <b-form-group label="Admin Name">
            <b-row>
              <b-col>
                <b-form-input placeholder="First Name" id="form-context-first-name" required v-model="form.user.given_name" @change="updateDisplayName"></b-form-input>
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
          </b-form-group>
          <b-form-group label="Login Credentials">
            <b-row>
              <b-col>
                <b-form-input placeholder="User Name" required v-model="form.user.name"></b-form-input>
              </b-col>
              <b-col>
                <b-form-input placeholder="Password" required v-model="form.user.password" type="password"></b-form-input>
              </b-col>
            </b-row>
          </b-form-group>
          <b-form-group label="Email Addresses">
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
          </b-form-group>
        </fieldset>

        <b-button variant="danger" size="sm" v-if="form.context.id" @click="onDelete">Delete Context</b-button>
      </b-container>
    </b-form>
    <div slot="modal-ok">
      Save
    </div>
  </b-modal>
</template>

<script>
  import { mapState } from 'vuex'

  const defaultForm = {
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
      onLoad () {
        if (this.context && this.context.id) {
          this.contextId = this.context.id
          
          // deep copy the merged values of the default form and the context passed in
          this.form.context = JSON.parse(JSON.stringify(Object.assign({}, defaultForm.context, this.context)))
        } else {
          this.contextId = false

          // deep copy the default form values
          this.form = JSON.parse(JSON.stringify(defaultForm))
        }
        this.$store.dispatch('MasterAdmin/clearContextError')
      },
      onSubmit (evt) {
        // prevent the modal from hiding before save is done
        evt.preventDefault()
        
        if (this.contextId) {
          this.$store.dispatch('MasterAdmin/updateContext', {contextId: this.contextId, data: this.form.context}).then(this.close).catch(() => {})
        } else {
          this.$store.dispatch('MasterAdmin/createContext', this.form).then(this.close).catch(() => {})
        }
      },
      onDelete () {
        if (window.confirm('Are you sure you want to delete this context?')) {
          this.$store.dispatch('MasterAdmin/deleteContext', this.contextId).then(this.close).catch(() => {})
        }
      },
      close () {
        this.showModal = false;
      }
    },
    data () {
      return {
        contextId: false,
        form: JSON.parse(JSON.stringify(defaultForm)) // deep copy of the form default values
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
      title () { return this.contextId ? 'Edit Context' : 'Create Context' },
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
    }
  }
</script>