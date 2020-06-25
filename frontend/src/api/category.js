import api from "./helper";

export default {
    async getCategories() {
        return await api
            .get("/api/core/categories", { json: false, auth: true })
            .then(res => {
                console.log(res);
                return res.data;
            })
            .then(categories => {
                if (!categories.success) throw new Error(categories.error);
                console.log(categories);
                return categories;
            })
            .catch(err => {
                throw err.isAxiosError ? err.response.data : err;
            });
    }
};
