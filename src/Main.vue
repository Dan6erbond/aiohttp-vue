<template>
  <div>
    <h1 class="text-center">System Processes</h1>
    <br />
    <b-list-group>
      <b-list-group-item
        :to="'/processes/' + proc.pid"
        v-for="proc in processes"
        :key="proc.pid"
      >{{ proc.name }}</b-list-group-item>
    </b-list-group>
  </div>
</template>

<script>
export default {
  name: "App",
  components: {},
  data: function () {
    return {
      processes: [],
    };
  },
  created: function () {
    fetch("/api/processes")
      .then((response) => response.json())
      .then((json) => (this.processes = json));
  },
};
</script>
