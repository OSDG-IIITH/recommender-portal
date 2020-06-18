/**
 * Item handling API routes
 */
import axios from "axios";

export default {
  // get all items of category
  getItems(categoryId) {
    return new Promise(async (resolve, reject) => {
      try {
        const _res = await axios.get(`/api/${categoryId}`);
        resolve(_res.data);
      } catch (err) {
        reject(err);
      }
    });
  },
  searchItem() {},

  // get item with id itemId in category
  getItem(categoryId, itemId) {
    return new Promise(async (resolve, reject) => {
      try {
        const _res = await axios.get(`/api/${categoryId}/${itemId}`);
        resolve(_res.data);
      } catch (err) {
        reject(err);
      }
    });
  },

  // Add item in category
  addItem(categoryId, data) {
    return new Promise(async (resolve, reject) => {
      try {
        const config = {
          headers: {
            "Content-Type": "application/json",
            Authorization:
              "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Imd1cmtpcmF0LnNpbmdoQHN0dWRlbnRzLmlpaXQuYWMuaW4ifQ.my7VTpp7glcJLaW-64679UULOah3Cx2pXo_X-7O8iJE"
          }
        };
        const body = JSON.stringify(data);
        const _res = await axios.post(`/api/${categoryId}`, body, config);
        resolve(_res.data);
      } catch (err) {
        reject(err);
      }
    });
  },

  // Update item with itemId in category
  updateItem(categoryId, itemId, data) {
    return new Promise(async (resolve, reject) => {
      try {
        const config = {
          headers: {
            "Content-Type": "application/json",
            Authorization:
              "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Imd1cmtpcmF0LnNpbmdoQHN0dWRlbnRzLmlpaXQuYWMuaW4ifQ.my7VTpp7glcJLaW-64679UULOah3Cx2pXo_X-7O8iJE"
          }
        };

        const body = JSON.stringify(data);
        const _res = await axios.patch(
          `/api/${categoryId}/${itemId}`,
          body,
          config
        );
        resolve(_res.data);
      } catch (err) {
        reject(err);
      }
    });
  },

  // Rate item
  rateItem(categoryId, itemId, rating) {
    return new Promise(async (resolve, reject) => {
      try {
        const config = {
          headers: {
            "Content-Type": "application/json",
            Authorization:
              "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Imd1cmtpcmF0LnNpbmdoQHN0dWRlbnRzLmlpaXQuYWMuaW4ifQ.my7VTpp7glcJLaW-64679UULOah3Cx2pXo_X-7O8iJE"
          }
        };

        const body = JSON.stringify({ rating });
        const _res = await axios.post(
          `/api/${categoryId}/rate/${itemId}`,
          body,
          config
        );
        resolve(_res.data);
      } catch (err) {
        reject(err);
      }
    });
  },

  //Like item if like the value 1 else its -1
  likeItem(categoryId, itemId, value) {
    return new Promise(async (resolve, reject) => {
      try {
        const config = {
          headers: {
            "Content-Type": "application/json",
            Authorization:
              "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Imd1cmtpcmF0LnNpbmdoQHN0dWRlbnRzLmlpaXQuYWMuaW4ifQ.my7VTpp7glcJLaW-64679UULOah3Cx2pXo_X-7O8iJE"
          }
        };

        const body = JSON.stringify({ value });
        const _res = await axios.post(
          `/api/user/like/${categoryId}/${itemId}`,
          body,
          config
        );
        resolve(_res.data);
      } catch (err) {
        reject(err);
      }
    });
  }
};
