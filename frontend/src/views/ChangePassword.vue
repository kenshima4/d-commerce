<template>
    <div class="page-sign-up">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title text-center">Change Password</h1>
                
                <!-- prevent form submit from sending to server -->
                <form @submit.prevent="submitForm">
                    <p>Hello {{ username }}, please change your password below. </p>
                    
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
    name: 'ChangePassword',
    data(){
        return {
            username: '',
            email:'',
            password:'',
            password2: '',
            errors: []
        }
    },
    mounted(){
        document.title = 'Change Password | d-commerce'
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
                const formData = {
                    username: localStorage.getItem('username'),
                    password: this.password
                }

                axios
                    .post("/api/v1/accounts/change_password/", formData)
                    .then(response => {
                        toast({
                            message: 'Password successfully changed! Please login',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 3000,
                            position: 'bottom-right',
                        })

                        this.$router.push('/login')
                    })
                    .catch((error) => {
                   
                        this.errors.push(error);
                        console.log(JSON.stringify(error))
                   
                    })

                  
            }
        },
        
      
        
  
    },
    computed: {
        username: state => {
            return localStorage.getItem('username'); // Retrieve the username from local storage
        }
    }
}
</script>