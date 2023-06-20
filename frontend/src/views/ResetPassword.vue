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
        getCookie(name) {
            let cookieValue = null;

            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();

                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));

                        break;
                    }
                }
            }

            return cookieValue;
        },
        
        
        submitForm() {
            this.errors = []

            

            if (this.email === '') {
                this.errors.push('The email is missing')
            }
            

            if (!this.errors.length) {
                const formData = {
                    email: this.email,
                }
                const csrftoken = this.getCookie('csrftoken');
                console.log(" got cookie !!!" + csrftoken)
                const headers = {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken
                }

              
                axios
                    .post("/api/v1/reset_password/", formData, {headers: headers
                    })
                    .then(response => {
                        toast({
                            message: 'If you have an account with us, please check your email for the link!',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            position: 'bottom-right',
                        })

                        
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