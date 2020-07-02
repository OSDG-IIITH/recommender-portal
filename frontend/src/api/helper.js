import axios from "axios";

function getConfig(payload) {
    const config = {
        headers: {
            "Content-Type": "application/json",
            Authorization: process.env.AUTH_TOKEN
        }
    };
    if (!payload.auth) delete config.headers.Authorization;
    if (!payload.json) delete config.headers["Content-Type"];
    return config;
}

export default {
    get(url, payload) {
        return axios.get(url, getConfig(payload));
    },
    post(url, payload) {
        return axios.post(url, payload.body, getConfig(payload));
    },
    put(url, payload) {
        return axios.put(url, payload.body, getConfig(payload));
    },
    patch(url, payload) {
        return axios.patch(url, payload.body, getConfig(payload));
    }
};
