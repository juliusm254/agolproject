<script setup>
import { onMounted, ref } from 'vue'
import { useApi } from "../resources/composables/useApi";
// import  useSafetyForm from "../resources/composables/trucks";

const { trailer, truck, labResultsDetail, getTruck, getLabResultsDetail } = useApi();
// const { truckid } = useSafetyForm();

// const trailler = ref("");

//  trailler.value = truckid.trailer_details.registration


onMounted(() => {
  //script
  getLabResultsDetail();
  getTruck()
})


</script>

<!-- 

<script>
import axios from "axios";
import useSafetyForm from "../resources/composables/trucks";
import { onMounted } from "vue";

export default {
  setup() {
    const {
      truck,
      trailer,
      truckid,
      trailerid,
      labResults,
      orderid,
      getTruck,
      getLabResults,
    } = useSafetyForm();

    onMounted(getTruck(), getLabResults());

    // const labResultsSelect = ref('')

    const submitForm = async (value) => {
      const payload = {
        status: value.target.value,
        order: orderid.value,
        // truck: this.truckid,
        // trailer: this.trailerid,
        // truck_pressure: this.truck_pressure,
        // oxygen_content: this.oxygen_content,
        // methane_content: this.methane_content
      };
      console.log(payload);
      await axios.post(`/lab-results-create/`, payload).then((response) => {
        console.log(response.data);
      });
    };

    return {
      submitForm,
      getLabResults,
      // labResultsSelect,
      truckid,
      trailerid,
      orderid,
      truck,
      trailer,
      labResults,
    };
  },
  data() {
    return {
      // questions:[{question: '', value:''}]
    };
  },
  // methods: {
  //       async submitForm() {

  //         console.log('Methods')

  //           let config = {
  //             headers: {
  //               "Content-Type": "application/json",
  //               "Access-Control-Allow-Origin": "http://localhost:8000/",
  //             },
  //           };

  //           const payload = {
  //             order: this.orderid,
  //             truck: this.truckid,
  //             trailer: this.trailerid,
  //             truck_pressure: this.truck_pressure,
  //             oxygen_content: this.oxygen_content,
  //             methane_content: this.methane_content

  //           };
  //           console.log(payload)
  //           await axios
  //           .post(`/lab-results/`, payload)
  //           .then((response) => {
  //             console.log(response.data)
  //           })
  //     },

  //   }
};
</script> -->

<template>
  <div>
    <h4>Truck Reg: {{truck}}</h4>
    <h4>Trailer Reg: {{trailer}}</h4>
  </div>
  <h3>Lab Results</h3>
 
  <p>{{labResultsDetail}}</p>
  <p>{{}}</p>
  <!-- <p>{{truckid.trailer_details.registration}}</p> -->

  <h4>Oxygen: {{ labResultsDetail.oxygen }}</h4>
  <h4>Pressure: {{ labResultsDetail.pressure }}</h4>
  <h4>Nitrogen: {{ labResultsDetail.nitrogen }}</h4>
  <h4>Methane: {{ labResultsDetail.methane }}</h4>
  <!-- </div> -->
  <div>
    <button @click="submitForm" type="submit" value="LOADING">Proceed</button>
  </div>
  <div>
    <button @click="submitForm" type="submit" value="SEAL">Seal</button>
  </div>
  <div>
    <button @click="submitForm" type="submit" value="VENT">Vent</button>
  </div>
  <div>
    <button @click="submitForm" type="submit" value="REJECT">Reject</button>
  </div>

  <button>
    <router-link to="/lab-results/">Back</router-link>
  </button>
</template>
