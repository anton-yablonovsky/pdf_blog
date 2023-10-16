<script>
import axios from "axios";
import router from "../router";
import { useStore } from "../stores/store.js";

export default {
  data() {
    return {
      store: useStore(),
      username: "",
      password: "",
    };
  },
  methods: {
    async submitForm(e) {
      const formData = {
        username: this.username,
        password: this.password,
      };

      await axios
        .post("api/login/", formData, {
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": this.store.csrf,
          },
          credentials: "same-origin",
        })
        .then((response) => {
          console.log(response);
          router.push("/");
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<template>
  <div class="log-in-page">
    <h1>Log in</h1>
    <form @submit.prevent="submitForm">
      <label class="form-label">Username</label>
      <input type="username" class="form-control" v-model="username" />
      <label class="form-label">Password</label>
      <input type="password" class="form-control" v-model="password" />
      <br /><br />
      <button class="btn btn-primary">Submit</button>
    </form>
  </div>
</template>
