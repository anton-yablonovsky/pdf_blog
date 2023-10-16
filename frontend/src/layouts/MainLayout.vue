<script>
import { RouterView } from "vue-router";
import axios from "axios";
import { useStore } from "../stores/store.js";

export default {
  data() {
    return {
      store: useStore(),
      username: null,
    };
  },

  async mounted() {
    console.log("MainLayout has mounted!");
    await this.store.getCsrf();
    console.log(this.store.is_authenticated);
    await this.store.isAuthenticated();
    console.log(this.store.is_authenticated);

    await axios
      .get("api/get_username/")
      .then((response) => {
        console.log(response);
        this.username = response.data.username;
      })
      .catch((error) => {
        console.log(error);
      });
  },
};
</script>
<template>
  <div v-if="this.store.is_authenticated">
    <nav id="toolbar" class="navbar navbar-inverse fixed-top">
      <ul class="nav nav-pills">
        <li class="nav-item">
          <a><router-link class="nav-link active" to="/">Main</router-link></a>
        </li>
        <li class="nav-item">
          <a
            ><router-link class="nav-link active" to="/admin"
              >Admin</router-link
            ></a
          >
        </li>
        <li class="nav-item">
          <a
            ><router-link class="nav-link active" to="/about"
              >About</router-link
            ></a
          >
        </li>
        <li class="nav-item">
          <a
            ><router-link class="nav-link active" to="/login"
              >Logout</router-link
            ></a
          >
        </li>
        <li class="nav-item">
          <h1>{{ this.username }}</h1>
        </li>
      </ul>
    </nav>
    <RouterView />
  </div>
  <div v-else>
    <h1>You are not allowed to visit this page, try to login!</h1>
    <a class="btn btn-primary" href="/login" role="button">Login</a>
  </div>
</template>
