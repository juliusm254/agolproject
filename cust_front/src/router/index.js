import { createRouter, createWebHistory } from "vue-router";
import HomePage from "../views/HomePage.vue";
import LogIn from "../views/LogIn.vue";
import OrderEdit from "../views/OrderEdit.vue";
import TruckAdd from "../views/TruckAdd.vue";
import DriverAdd from "../views/DriverAdd.vue";
import TraillerAdd from "../views/TraillerAdd.vue";
import DriverList from "../views/DriverList.vue";
import OrderBulk from "../views/OrderBulk.vue";
import store from "../store";

const routes = [
  {
    path: "/",
    name: "HomePage",
    component: HomePage,
  },
  {
    path: "/login",
    name: "LogIn",
    component: LogIn,
  },
  {
    path: "/add-driver",
    name: "DriverAdd",
    component: DriverAdd,
  },

  {
    path: "/edit-order",
    name: "OrderEdit",
    component: OrderEdit,
  },
  {
    path: "/add-truck",
    name: "TruckAdd",
    component: TruckAdd,
  },
  {
    path: "/add-trailer",
    name: "TraillerAdd",
    component: TraillerAdd,
  },
  {
    path: "/drivers",
    name: "DriverList",
    component: DriverList,
  },
  {
    path: "/bulk-balance",
    name: "OrderBulk",
    component: OrderBulk,
  },
  {
    path: "/orders",
    name: "OrderList",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import( "../views/OrderList.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

router.beforeEach(() => {
  console.log(store.state.auth);
});

export default router;
