<template>
  <div id="app">
    <b-navbar type="dark" variant="dark">
      <b-navbar-brand tag="h1" class="mb-0" to="/">Resource Monitor</b-navbar-brand>
    </b-navbar>
    <b-container fluid class="content">
      <router-view></router-view>
    </b-container>
  </div>
</template>

<style lang="scss" scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

.content {
  padding: 30px 40px;
}
</style>
