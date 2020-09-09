import axios from "axios";
import { BootstrapVue, IconsPlugin } from "bootstrap-vue";
import "bootstrap-vue/dist/bootstrap-vue.css";
import "bootstrap/dist/css/bootstrap.css";
import Vue from "vue";
import VueRouter from "vue-router";
import App from "./App.vue";
import Main from "./Main.vue";
import Process from "./Process.vue";

Vue.config.productionTip = false;

Vue.use(VueRouter);

Vue.use(BootstrapVue);
Vue.use(IconsPlugin);

Vue.prototype.$http = axios.create({
  baseURL: window.location.host.split(":")[0],
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
  },
});

const routes = [
  { path: "/", component: Main },
  { path: "/processes/:pid", component: Process },
];

const router = new VueRouter({
  mode: "history",
  routes,
});

new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");
