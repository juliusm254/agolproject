<script setup>
import { onMounted } from 'vue'
import { useApi } from "../resources/composables/useApi";

const { driverList,getDriverList } = useApi();

onMounted(() => {
  //script
  getDriverList()
})

</script>




<template>  
  <div class="">
    <h1 class="">Driver List</h1>
  </div>

  <!-- Table -->
  <div class="flex items-center justify-center">
    <table class="border-collapse border-2 border-gray-500">
      <thead>
        <tr>
          <th class="border border-gray-400 px-4 py-2 text-gray-800">Order No.</th>
          <th class="border border-gray-400 px-4 py-2 text-gray-800">Truck</th>
          <th class="border border-gray-400 px-4 py-2 text-gray-800">Transporter</th>
          <th class="border border-gray-400 px-4 py-2 text-gray-800">Trailer</th>
          <!-- <th class="border border-gray-400 px-4 py-2 text-gray-800">Order No.</th>
          <th class="border border-gray-400 px-4 py-2 text-gray-800">Truck</th> -->
        </tr>
      </thead>
      <tbody>
        <tr v-for="driver in driverList" v-bind:key="driver.id">
          <td class="border border-gray-400 px-4 py-2">{{ driver.id }}</td>
          <!-- <td class="border border-gray-400 px-4 py-2">{{ order.truck_details["registration"] }}</td>
          <td class="border border-gray-400 px-4 py-2">{{ order.truck_details["transporter"]  }}</td>
          <td class="border border-gray-400 px-4 py-2">{{ order.trailer_details["registration"] }}</td> -->
          <td class="border border-gray-400 px-4 py-2">
            <router-link
                :to="`/`"
                class="button is-light"
                >Edit</router-link>
            </td>
          <!-- <td class="border border-gray-400 px-4 py-2">{{ order.id }}</td> -->
        </tr>            
      </tbody>
    </table>
  </div>
  <!-- Table -->
</template>


<!-- 
<script>
import axios from "axios";

// import { toast } from 'bulma-toast'

export default {
  name: "Home",
  data() {
    return {
      trucks: [],
      trailers: [],
      drivers: [],
    };
  },
  mounted() {
    this.getTrucks();
    this.getDrivers();
    this.getTrailers();
  },

  methods: {
    async getTrucks() {
      let config = {
        headers: {
          Authorization: "Bearer " + localStorage.getItem("access_token"),
          "Content-Type": "application/json",
        },
      };
      // this.$store.commit('setIsLoading', true)
      this.showNextButton = false;
      this.showPreviousButton = false;

      await axios
        .get(`/customer-truck/`, config)
        .then((response) => {
          console.log(response.data);
          this.trucks = response.data;
          // this.num_orders = response.data.count
        })

        // await axios
        //     .get(`/api/v1/leads/?page=${this.currentPage}&search=${this.query}`)
        //     .then(response => {
        //         this.leads = response.data.results
        //         console.log(response.data)

        //     // for (let i = 0; i < response.data.length; i++) {
        //     //     this.leads.push(response.data[i])

        //         if (response.data.next) {
        //             this.showNextButton = true
        //         }
        //         if (response.data.previous) {
        //             this.showPreviousButton = true
        //         }
        // })

        .catch((error) => {
          console.log(error);
        });
      // this.$store.commit('setIsLoading', false)
    },
    async getTrailers() {
      let config = {
        headers: {
          Authorization: "Bearer " + localStorage.getItem("access_token"),
          "Content-Type": "application/json",
        },
      };
      // this.$store.commit('setIsLoading', true)
      this.showNextButton = false;
      this.showPreviousButton = false;

      await axios
        .get(`/customer-trailer/`, config)
        .then((response) => {
          console.log(response.data);
          this.trailers = response.data;
          // this.num_orders = response.data.count
        })

        // await axios
        //     .get(`/api/v1/leads/?page=${this.currentPage}&search=${this.query}`)
        //     .then(response => {
        //         this.leads = response.data.results
        //         console.log(response.data)

        //     // for (let i = 0; i < response.data.length; i++) {
        //     //     this.leads.push(response.data[i])

        //         if (response.data.next) {
        //             this.showNextButton = true
        //         }
        //         if (response.data.previous) {
        //             this.showPreviousButton = true
        //         }
        // })

        .catch((error) => {
          console.log(error);
        });
      // this.$store.commit('setIsLoading', false)
    },

    async getDrivers() {
      // this.$store.commit('setIsLoading', true)
      this.showNextButton = false;
      this.showPreviousButton = false;
      let config = {
        headers: {
          Authorization: "Bearer " + localStorage.getItem("access_token"),
          "Content-Type": "application/json",
        },
      };

      await axios.get(`/customer-driver/`, config).then((response) => {
        console.log(response.data);
        this.drivers = response.data;
        // this.num_orders = response.data.count
      });

      // this.$store.commit('setIsLoading', false)
    },
  },
};
</script> -->
