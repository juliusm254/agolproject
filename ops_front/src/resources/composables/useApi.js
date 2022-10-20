import { ref } from "vue";
import axios from "axios";
import { useRoute } from "vue-router";

const safetyList = ref([]);
const safetyInspectionList = ref([]);
const labInspectionList = ref([]);
const labResultsList = ref([]);
const labResultsDetail = ref([]);
const trailer = ref("");
const truck = ref("");

export const useApi = () => {


    const route = useRoute();
    const orderid = ref(route.params.id);


    const getPrintSafetyList = async () => {
        const response = await axios.get(`/printsafety/`);
        safetyList.value = response.data
    };

    const getSafetyInspectionList = async () => {
        const response = await axios.get(`/checklist/`);
        safetyInspectionList.value = response.data
    };

    const getLabInspectionList = async () => {
        const response = await axios.get(`/lab-inspection/`);
        labInspectionList.value = response.data

    };

    const getLabResultsList = async () => {
        const response = await axios.get(`/lab-results/`);
        labResultsList.value = response.data
    };

    const getLabResultsDetail = async () => {
        let response = await axios.get(`/lab-results/${orderid.value}`);
        console.log(response.data);
        labResultsDetail.value = response.data[0];
    };

    const getTruck = async () => {
        const response = await axios.get(`/order/${orderid.value}`);
        console.log(response.data);    
        truck.value = response.data.truck_details.registration;
        trailer.value = response.data.trailer_details.registration;    
    };
    
    
    // getSafetyList();
    // getLabResultsList();    
    return {safetyList,
            safetyInspectionList,
            labInspectionList,
            labResultsList,
            labResultsDetail,
            truck,
            trailer,
            orderid,
            getPrintSafetyList,
            getSafetyInspectionList,
            getLabResultsDetail,
            getLabInspectionList,
            getLabResultsList,
            getTruck
    };
};