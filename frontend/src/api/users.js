import api from "./helper";

export default {
    async getUsers() {
        return await api
            .get(`/api/core/users`, {
                json: false
            })
            .then(res => res.data)
            .then(users => {
                if (!users.success) throw new Error(users.error);
                return users;
            })
            .catch(err => {
                throw err.isAxiosError ? err.response.data : err;
            });
    },

    async getCurrentUser() {
        return await api
            .get(`/api/user/me`, {
                json: false
            })
            .then(res => res.data)
            .then(user => {
                if (!user.success) throw new Error(user.error);
                return user;
            })
            .catch(err => {
                throw err.isAxiosError ? err.response.data : err;
            });
    },
    async login(ticket) {
        return await api
            .get(`/api/core/login?ticket=${ticket}`, {
                json: false
            })
            .then(res => res.data)
            .then(token => {
                if (!token.success) throw new Error(token.error);
                return token;
            })
            .catch(err => {
                throw err.isAxiosError ? err.response.data : err;
            });
    }
};
