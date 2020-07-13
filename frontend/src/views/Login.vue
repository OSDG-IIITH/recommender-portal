<template>
    <div class="login">
        Login....
    </div>
</template>

<script>
import userStore from "../api/users";

export default {
    name: "login",
    created() {
        const ticket = this.$route.query.ticket;
        console.log(ticket);
        if (ticket) {
            this.$store.dispatch("getToken", { ticket });
        }
        this.$router.push("/");
    }
};
</script>
