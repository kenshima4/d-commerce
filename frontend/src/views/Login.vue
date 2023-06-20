<template>
    <div class="page-sign-up">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title has-text-centered">Login</h1>
                <!-- prevent form submit from sending to server -->
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Username</label>
                        <div class="control">
                            <!-- v-model for two-way data binding between template value
                                 and data property value-->
                            <input type="text" class="input" v-model="username">
                        </div>
                    </div>

                    <div class="field">
                        <label>Password</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password">
                        </div>
                    </div>

                    

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-dark">Login</button>
                        </div>
                    </div>

                    <div class="content has-text-centered">
                        <p>Forgot your password? <router-link to="/reset-password">
                            <strong>Reset Password</strong></router-link>
                        </p>

                        <p>Don't have an account? <router-link to="/sign-up">
                            <strong>Sign Up</strong></router-link>
                        </p>


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
    name: 'Login',
    data(){
        return {
            username: '',
            password:'',
            errors: []
        }
    },
    mounted(){
        document.title = 'Login | d-commerce'
    },
    methods: {
        async submitForm() {
            axios.defaults.headers.common["Authorization"] = ""

            localStorage.removeItem("token")

            const formData = {
                username: this.username,
                password: this.password
            }

            await axios
                .post("/api/v1/token/login/", formData)
                .then(response => {
                    const token = response.data.auth_token

                    this.$store.commit('setToken', token)
                    
                    axios.defaults.headers.common["Authorization"] = "Token " + token

                    localStorage.setItem("token", token)

                    const toPath = this.$route.query.to || '/cart'

                    this.$router.push(toPath)
                })
                .catch(error => {
                    if (error.response) {
                        for (const property in error.response.data) {
                            this.errors.push(`${error.response.data[property]}`)
                        }
                    } else {
                        this.errors.push('Something went wrong. Please try again')
                        
                        console.log(JSON.stringify(error))
                    }
                })

                this.updateUserName()
        },
        updateUserName() {
            this.$store.commit('username', this.username);
            localStorage.setItem('username', this.username);
        },
        
        
        
    }
}
</script>

<style scoped>
.button{
  width:100%;
}

</style>