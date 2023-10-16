import { createApp } from "vue";
import App from "./App.vue";
import router from "./router/index.js";
import axios from "axios";
import { getIpPort } from "./helpers/helper.js";

import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";

import { createPinia } from "pinia";

// I need to change ip and port as in network configuration. In case LAN - ip:80, in case WAN - config_ip:ip.
var network = getIpPort();
const pinia = createPinia();

axios.defaults.baseURL = `http://${network["ip"]}:80/backend/`;
const app = createApp(App).use(router, axios);
app.use(pinia);

app.mount("#app");
