<template>
  <div>
    <h2>
      System Usage
      <small v-if="systemProcess" class="text-muted">{{ systemProcess.name }}</small>
    </h2>
    <div v-if="systemUsage" class="resource-monitor card">
      <span v-if="systemProcess">
        <b>Process Executable</b>
        {{systemProcess.exe}}
        <br />
        <br />
      </span>
      <b>CPU Usage</b>
      {{cpuPercent}}%
      <b-progress :value="cpuPercent" max="100" show-progress animated></b-progress>
      <br />
      <b>Memory Usage</b>
      {{memory}} MB / {{memoryPercent}}%
      <b-progress :value="memoryPercent" max="100" show-progress animated></b-progress>
    </div>
  </div>
</template>

<script>
export default {
  data: function () {
    return {
      systemProcess: null,
      connection: null,
      socketMsgs: [],
      systemUsage: null,
    };
  },
  created: function () {
    fetch("/api/processes/" + this.$route.params.pid)
      .then((response) => response.json())
      .then((json) => (this.systemProcess = json));

    const wsUrl = window.location.host + "/ws/" + this.$route.params.pid;

    this.connection = new WebSocket("ws://" + wsUrl);

    this.connection.onmessage = (event) => {
      this.socketMsgs.push(event);
      this.systemUsage = JSON.parse(event.data);
    };
  },
  computed: {
    cpuPercent: function () {
      if (this.systemUsage) {
        return new Intl.NumberFormat().format(this.systemUsage.cpu);
      } else {
        return 0;
      }
    },
    memory: function () {
      if (this.systemUsage) {
        return new Intl.NumberFormat().format(this.systemUsage.memory);
      } else {
        return 0;
      }
    },
    memoryPercent: function () {
      if (this.systemUsage) {
        return new Intl.NumberFormat().format(this.systemUsage.memory_percent);
      } else {
        return 0;
      }
    },
  },
};
</script>

<style lang="scss" scoped>
.resource-monitor {
  max-width: 450px;
  padding: 10px;
}
</style>
