<template>
    <v-stepper v-model="stepNum" vertical>
        <v-overlay :absolute="true" :value="overlay">
            <v-progress-circular indeterminate size="64"></v-progress-circular>
        </v-overlay>
        <h3 class="pa-2 ma-1 text-center text-sm-left text-overline">Add {{ sheetType }}</h3>
        <v-stepper-step editable :complete="stepNum > 1" step="1" :rules="[() => this.commonValid]">
            Compulsory <small>Common details</small>
        </v-stepper-step>
        <v-stepper-content step="1">
            <ItemCommonForm
                :isValid="commonValid"
                @continue="commonSubmit"
                @next="goToSpecific"
                @cancel="cancel"
            />
        </v-stepper-content>

        <v-stepper-step editable step="2" :rules="[() => this.specificValid]">
            Optional <small>Extra details</small>
        </v-stepper-step>
        <v-stepper-content step="2">
            <ItemSpecificForm
                :sheetType="sheetType"
                :isCommonValid="!commonValid"
                @continue="specificSubmit"
                @previous="goToCommon"
                @cancel="cancel"
            />
        </v-stepper-content>
    </v-stepper>
</template>

<script>
import ItemCommonForm from '@/components/ItemCommonForm';
import ItemSpecificForm from '@/components/ItemSpecificForm';

export default {
    name: 'AddItemSheet',
    components: {
        ItemCommonForm,
        ItemSpecificForm
    },
    props: {
        stepNum: Number,
        closeSheet: Function,
        sheetType: String
    },
    data() {
        return {
            overlay: false,
            commonValid: true,
            specificValid: true,
            formData: {}
        };
    },
    methods: {
        goToCommon: function(currentValid, changeSection = true) {
            this.specificValid = currentValid;
            if (changeSection) this.stepNum = 1;
        },
        goToSpecific: function(currentValid, changeSection = true) {
            this.commonValid = currentValid;
            if (changeSection) this.stepNum = 2;
        },
        commonSubmit: function(data) {
            // get back data
            this.formData = JSON.parse(data);
        },

        specificSubmit: async function(data) {
            this.formData = {
                ...this.formData,
                ...JSON.parse(data)
            };

            // start loading
            this.overlay = true;

            // call the action
            await this.$store.dispatch('items/addItem', {
                // so as to remove __ob__
                ...JSON.parse(JSON.stringify(this.formData)),
                category: this.sheetType
            });

            // stop loading
            this.overlay = false;

            // close the sheet
            this.formData = {};
            this.closeSheet();
        },
        cancel: function() {
            this.formData = {};
            this.closeSheet();
        }
    }
};
</script>
