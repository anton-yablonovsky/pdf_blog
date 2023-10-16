import { defineStore } from "pinia";
import axios from "axios";

export const useStore = defineStore("store", {
  state: () => {
    return {
      csrf: null,
      is_authenticated: null,
    };
  },
  // could also be defined as
  // state: () => ({ count: 0 })
  actions: {
    async getCsrf() {
      await axios
        .get("api/get_csrf/")
        .then((response) => {
          this.csrf = response.data.token;
          console.log(this.csrf);
        })
        .catch((error) => {
          console.log(error);
        });
    },

    async isAuthenticated() {
      await axios
        .get("api/session/")
        .then((response) => {
          if (response.data.is_authenticated) {
            this.is_authenticated = true;
          } else {
            this.is_authenticated = false;
          }
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
});
