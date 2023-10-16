<script>
import { RouterView } from "vue-router";
import axios from "axios";
import { useStore } from "../stores/store.js";

export default {
  data() {
    return {
      store: useStore(),
    };
  },

  async mounted() {
    console.log("AdditionalLayout is mounted!");
    await this.store.getCsrf();
  },
};
</script>
<template>
  <RouterView />
</template>
