/**
 * Item handling API routes
 */
import api from "./helper";
import { config } from "shelljs";

export default {
    // get all items of category
    async getItems(categoryId) {
        return await api
            .get(`/api/${categoryId}`, {
                json: false
            })
            .then(res => res.data)
            .then(items => {
                if (!items.success) throw new Error(items.error);
                return items;
            })
            .catch(err => {
                throw err.isAxiosError ? err.response.data : err;
            });
    },

    // get item with id itemId in category
    async getItem(categoryId, itemId) {
        return await api
            .get(`/api/${categoryId}/${itemId}`, {
                json: false
            })
            .then(res => res.data)
            .then(item => {
                if (!item.success) throw new Error(item.error);
                return item;
            })
            .catch(err => {
                throw err.isAxiosError ? err.response.data : err;
            });
    },

    // Add item in category
    async addItem(categoryId, data) {
        return await api
            .post(`/api/${categoryId}`, {
                body: JSON.stringify(data),
                json: true
            })
            .then(res => res.data)
            .then(item => {
                if (!item.success) throw new Error(item.error);
                return item;
            })
            .catch(err => {
                throw err.isAxiosError ? err.response.data : err;
            });
    },

    // Update item with itemId in category
    async updateItem(categoryId, itemId, data) {
        return await api
            .patch(`/api/${categoryId}/${itemId}`, {
                body: JSON.stringify(data),
                json: true
            })
            .then(res => res.data)
            .then(item => {
                if (!item.success) throw new Error(item.error);
                return item;
            })
            .catch(err => {
                throw err.isAxiosError ? err.response.data : err;
            });
    },

    // Rate item
    async rateItem(categoryId, itemId, rating) {
        return await api
            .post(`/api/${categoryId}/rate/${itemId}`, {
                body: JSON.stringify({ rating }),
                json: true
            })
            .then(res => res.data)
            .then(rate => {
                if (!rate.success) throw new Error(rate.error);
                return rate;
            })
            .catch(err => {
                throw err.isAxiosError ? err.response.data : err;
            });
    },

    //Like item if like the value 1 else its -1
    async likeItem(categoryId, itemId, value) {
        return await api
            .post(`/api/user/like/${categoryId}/${itemId}`, {
                body: JSON.stringify({ value }),
                json: true
            })
            .then(res => res.data)
            .then(like => {
                if (!like.success) throw new Error(like.error);
                return like;
            })
            .catch(err => {
                throw err.isAxiosError ? err.response.data : err;
            });
    }
};
