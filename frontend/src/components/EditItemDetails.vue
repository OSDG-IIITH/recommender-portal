<template>
  <v-list rounded dense flat>
    <v-subheader>Edit More Information</v-subheader>
    <v-list-item>
      <v-list-item-content>
        <EditItemCommonForm :post="post" @editCommonSubmit="editCommonSubmit" />
      </v-list-item-content>
    </v-list-item>
    <v-list-item>
      <v-list-item-content>
        <EditItemSpecificForm :post="post" @editSpecificSubmit="editSpecificSubmit" />
      </v-list-item-content>
    </v-list-item>
  </v-list>
</template>

<script>
import EditItemCommonForm from "@/components/EditItemCommonForm";
import EditItemSpecificForm from "@/components/EditItemSpecificForm";

export default {
  name: "EditItemDetails",
  props: {
    post: Object,
    editmode: Boolean
  },
  data() {
    return {
      commonValid: true,
      specificValid: true,
      editFormData: {}
    };
  },
  components: {
    EditItemCommonForm,
    EditItemSpecificForm
  },
  methods: {
    editCommonSubmit: function(data) {
      this.editFormData = JSON.parse(data);
    },
    editSpecificSubmit: async function(data) {
      this.editFormData = {
        ...this.editFormData,
        ...JSON.parse(data)
      }
      console.log(this.editFormData);
      this.$emit("mode", false);
      this.editFormData = {};
    },
    cancel: function() {
      this.editFormData = {};
    }
  }
};
</script>
