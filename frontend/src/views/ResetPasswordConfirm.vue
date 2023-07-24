<template>
    <div class="page-sign-up">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title text-center">New Password</h1>
                <!-- prevent form submit from sending to server -->
                <form @submit.prevent="submitForm">
                    
                    <div class="field">
                        <label>Password</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password">
                        </div>
                    </div>

                    <div class="field">
                        <label>Repeat password</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password2">
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-dark">Change Password</button>
                        </div>
                    </div>
                </form>
            </div>
            
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'ResetPasswordConfirm',
    props: ['uid', 'token'],
    data(){
        return {
            password:'',
            password2: '',
            errors: []
        }
    },
    mounted(){
        document.title = 'Reset Password Confirm | d-commerce'
    },
    methods: {
        submitForm() {
            this.errors = []

            if (this.password === '') {
                this.errors.push('The password is too short')
            }

            if (this.password !== this.password2) {
                this.errors.push('The passwords don\'t match')
            }

            if (!this.errors.length) {
                
                const uid = this.uid
                const token = this.token
                const new_password = this.password
                const re_new_password = this.password2
               
                const config = {
                    headers:{
                        'Content-Type': 'application/json'
                    }
                }
               
                const body = JSON.stringify({ uid, token, new_password, re_new_password })
                console.log(body)
                axios
                    .post("/api/v1/users/reset_password_confirm/", body, config)
                    .then(response => {
                        toast({
                            message: 'Reset password successful, please login!',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 5000,
                            position: 'bottom-right',
                        })

                        this.$router.push('/login')
                    })
                    .catch(error => {
                        if (error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }

                            console.log(JSON.stringify(error.response.data))
                        } else if (error.message) {
                            this.errors.push('Something went wrong. Please try again')
                            
                            console.log(JSON.stringify(error))
                        }
                    })

                    
            }
        },
        
      
        
  
    }
}
</script>