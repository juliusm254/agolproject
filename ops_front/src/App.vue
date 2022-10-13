<template>
  <div id="nav">
    <router-link to="/orderscan">Scan Order</router-link> |
    <router-link to="/">Home</router-link> |
    <router-link to="/safety-inspection">Safety Inspection</router-link> |
    <router-link to="/print-safety">Print Safety Inspection</router-link> |
    <router-link to="/lab-inspection">LabInspection</router-link> |
    <router-link to="/lab-results">Lab Results</router-link> |
    <router-link to="/lab-vent">Lab Vent</router-link> |
    <router-link to="/lab-seal">Lab Seal</router-link> |
    <router-link to="/loading">Loading</router-link> |
    
    <router-link to="/about">About</router-link> |
    
    <router-link to="/login">Login</router-link> |
  </div>
  <router-view />
  <the-loader v-if="isLoading" ></the-loader>
  <!-- <TheLoader v-if="isLoading" /> -->
</template>

<script>
// import TheNavigation from './components/TheNavigation.vue';
import TheLoader from './components/TheLoader.vue';
import { mapState } from 'vuex';
export default {
    name: 'App',
    computed: {
        ...mapState("loading", {
            isLoading: (state) => state.isLoading,
        }),
    },
    components: {
        // TheNavigation,
        TheLoader,
    },
};
</script>

<style>

</style>
