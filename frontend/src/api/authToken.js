import axios from "axios";

export const setAuthToken = token => {
    axios.defaults.headers.common["Authorization"] = token;
};

export const removeAuthToken = () => {
    delete axios.defaults.headers.common["Authorization"];
};
