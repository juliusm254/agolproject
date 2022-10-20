import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import axios from "axios";
import "./index.css";

// axios.defaults.baseURL = "https://agol-bvtwuypbsq-km.a.run.app/operations/";
axios.defaults.baseURL = "http://127.0.0.1:8000/operations";

createApp(App).use(store).use(router, axios).mount("#app");
