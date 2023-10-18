<script>
import axios from "axios";
import { useStore } from "../stores/store.js";

export default {
  data() {
    return {
      store: useStore(),
      username: null,
      password: null,
      title: null,
      content: null,
      titles_list: [],
    };
  },

  async mounted() {
    await this.store.isAuthenticated();
    axios
      .get("api/get_articles_list/")
      .then((response) => {
        this.titles_list = response.data.articles_list;
      })
      .catch((error) => {
        console.log(error);
        alert("Error!");
      });
  },
  methods: {
    async showPdf(title) {
      const formData = {
        title: title,
      };

      await axios
        .post("api/send_pdf/", formData, {
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": this.store.csrf,
            Accept: "application/pdf",
          },
          credentials: "same-origin",
          responseType: "blob",
        })
        .then((response) => {
          console.log(response);
          var blob = new Blob([response.data], {
            type: "application/pdf",
          });
          var pdfUrl = URL.createObjectURL(blob);
          window.open(pdfUrl);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<template>
  <div>
    <h1>Main page</h1>
    <li v-for="title in this.titles_list">
      <a @click="showPdf(title)" href="#">{{ title }}</a>
    </li>
  </div>
</template>
