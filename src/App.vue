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
  </div>
</template>

<script>
export default {
  name: "App",
  components: {},
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
</style>
