<template>
  <div id="app">
    <h1 class="text-center">Your Bots</h1>
    <br />
    <b-container>
      <b-row class>
        <b-col class="col-auto mb-4" v-for="n in 3" :key="n">
          <b-card title="Bot Name" class="bot-card">
            <b-card-text>
              <b-container class="p-0">
                <b-row>
                  <b-col class="col-8">
                    This is a wider card with supporting text below as a natural lead-in to additional content.
                    This content is a little bit longer.
                  </b-col>
                  <b-col class="col-4 text-center">
                    <b-avatar class="my-4" size="3.5rem"></b-avatar>
                  </b-col>
                </b-row>
              </b-container>
            </b-card-text>
          </b-card>
        </b-col>
      </b-row>
    </b-container>
    <h2>Websocket Responses</h2>
    <div v-if="systemUsage" class="resource-monitor card">
      <b>Process Name</b>
      {{systemUsage.name}}
      <br />
      <br />
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
  name: "App",
  components: {},
  data: function () {
    return {
      connection: null,
      socketMsgs: [],
      systemUsage: null,
    };
  },
  created: function () {
    const wsUrl = window.location.host + "/ws/0";

    this.connection = new WebSocket("ws://" + wsUrl);

    this.connection.onmessage = (event) => {
      this.socketMsgs.push(event);
      this.systemUsage = JSON.parse(event.data);
      console.log(event);
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
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin: 60px 20px;
}

.bot-card {
  min-width: 300px !important;
  width: 40vw;
  min-height: 250px !important;
  border-radius: 5px;
  transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
  cursor: pointer;

  &:hover {
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.12), 0 5px 5px rgba(0, 0, 0, 0.12);
  }
}

.resource-monitor {
  max-width: 450px;
  padding: 10px;
}
</style>
