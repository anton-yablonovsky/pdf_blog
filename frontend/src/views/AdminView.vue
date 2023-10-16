<script>
import axios from "axios";
import { useStore } from "../stores/store.js";

export default {
  data() {
    return {
      store: useStore(),
      username: null,
      password: null,
      pdf: null,
    };
  },

  async mounted() {
    await this.store.isAuthenticated();
  },

  methods: {
    async addUser(e) {
      const formData = {
        username: this.username,
        password: this.password,
      };

      await axios
        .post("api/create_user/", formData, {
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": this.store.csrf,
          },
          credentials: "same-origin",
        })
        .then((response) => {
          alert("Success!");
        })
        .catch((error) => {
          console.log(error);
          alert("Error!");
        });
    },

    async addArticle(e) {
      const formData = {
        pdf: document.getElementById("pdf").files[0],
      };

      await axios
        .post("api/create_article/", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
            "X-CSRFToken": this.store.csrf,
          },
          credentials: "same-origin",
        })
        .then((response) => {
          alert("Success!");
        })
        .catch((error) => {
          console.log(error);
          alert("Error!");
        });
    },
  },
};
</script>

<template>
  <div class="log-in-page" v-if="this.store.is_authenticated">
    <form @submit.prevent="addUser">
      <h1>Form for creating non-admin user</h1>
      <label class="form-label">Username:</label><br />
      <input type="username" class="form-control" v-model="username" /><br />
      <label class="form-label">Password:</label><br />
      <input type="password" class="form-control" v-model="password" /><br />
      <button class="btn btn-primary">Add user</button>
    </form>

    <form @submit.prevent="addArticle">
      <h1>Form for creating article</h1>
      <label class="form-label">PDF file:</label><br />
      <input type="file" id="pdf" class="form-control" /><br />
      <button class="btn btn-primary">Add article</button>
    </form>
  </div>
  <div v-else>
    <h1>You are not allowed to visit this page, try to login!</h1>
    <a class="btn btn-primary" href="/login" role="button">Login</a>
  </div>
</template>
