/**
 * Get user information, likes, ratings, etc
 */

import axios from "axios";

export default {
  getUsers() {
    return new Promise(async (resolve, reject) => {
      try {
        const config = {
          headers: {
            "Content-Type": "application/json",
            Authorization:
              "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Imd1cmtpcmF0LnNpbmdoQHN0dWRlbnRzLmlpaXQuYWMuaW4ifQ.my7VTpp7glcJLaW-64679UULOah3Cx2pXo_X-7O8iJE"
          }
        };
        const _res = await axios.get("/api/core/users", config);
        resolve(_res.data);
      } catch (err) {
        reject(err);
      }
    });
  },

  getCurrentUser() {
    return new Promise(async (resolve, reject) => {
      try {
        const config = {
          headers: {
            "Content-Type": "application/json",
            Authorization:
              "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Imd1cmtpcmF0LnNpbmdoQHN0dWRlbnRzLmlpaXQuYWMuaW4ifQ.my7VTpp7glcJLaW-64679UULOah3Cx2pXo_X-7O8iJE"
          }
        };
        const _res = await axios.get("/api/user/me", config);
        resolve(_res.data);
      } catch (err) {
        reject(err);
      }
    });
  },

  getRating(ratingId) {},

  getLikes(userId) {}
};
