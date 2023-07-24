<template>
    <div class="page-sign-up">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title text-center">Reset Password</h1>
                <!-- prevent form submit from sending to server -->
                <form @submit.prevent="submitForm">
                    
                    
                    <div class="field">
                        <label>Email</label>
                        <div class="control">
                            <!-- v-model for two-way data binding between template value
                                 and data property value-->
                            <input type="email" class="input" v-model="email">
                        </div>
                    </div>
                    
                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-dark">Send Email</button>
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
import jQuery from 'jquery'
export default {
    name: 'ResetPassword',
    data(){
        return {
            email:'',
            errors: []
        }
    },
    mounted(){
        document.title = 'Reset Password | d-commerce'
    },
    methods: {
        // using jQuery
        getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        },
       
        
        async submitForm() {
            this.errors = []

            if (this.email === '') {
                this.errors.push('The email is missing')
            }


            if (!this.errors.length) {
                const config = {
                    headers:{
                        'Content-Type': 'application/json'
                    }
                }
                const email = this.email;
                const body = JSON.stringify({ email })
                
                axios.defaults.withCredentials = true;
                axios.defaults.headers.common = {
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken' : this.getCookie('csrftoken')
                };


                await axios.post('/api/v1/users/reset_password/', body, config)
                .then(response => {
                    
                    console.log(response)
                    this.$router.push('/reset-password-done')
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
        }
        
      
        
  
    },
   
}
</script>