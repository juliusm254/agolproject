import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import axios from "axios";
import "./style.css";

axios.defaults.baseURL = "https://agol-bvtwuypbsq-km.a.run.app/operations/";

createApp(App).use(store).use(router, axios).mount("#app");
