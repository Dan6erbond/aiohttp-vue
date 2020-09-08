import axios from "axios";
import { BootstrapVue, IconsPlugin } from "bootstrap-vue";
import "bootstrap-vue/dist/bootstrap-vue.css";
import "bootstrap/dist/css/bootstrap.css";
import Vue from "vue";
import App from "./App.vue";

Vue.config.productionTip = false;

Vue.use(BootstrapVue);
Vue.use(IconsPlugin);

console.log(window.location.host);

Vue.prototype.$http = axios.create({
  baseURL: window.location.host,
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
  },
});

new Vue({
  render: (h) => h(App),
}).$mount("#app");
