<template>
  <div id="app">
    <p v-if="showWarning" id="warning">Expected txt file.</p>
    <input
      v-on:input="onInput"
      id="upload-file" type="file"
    />
    <article>{{fileContent}}</article>
  </div>
</template>

<script>
export default {
  name: 'app',
  components: {
  },
  data: function() {
    return {
      showWarning: false,
      fileContent: '',
    };
  },
  methods: {
    //<events>
    onInput: function(evt) {
      this.readFile(evt.target.files[0])
        .then((result) => {
          this.printFile(result);
        })
        .catch(() => {
          this.showWarning = true;

          let hideWarning = setInterval(() => {
            this.showWarning = false;
            clearInterval(hideWarning);
          }, 3000);
        })
        .finally(() => evt.target.value = "");
    },
    //</events>

    //<file handler>
    readFile: function(file) {
      const reader = new FileReader();

      if (!(/^text.*/).test(file.type)) {
        return Promise.reject();
      }

      reader.readAsText(file);
      return new Promise((res) => {
        reader.onload = (() => { res(reader.result); });
      });
    },
    printFile: function(text) {
      this.fileContent = text;
    },
    //</file handler>
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 60px;
}

input {
  text-align: center;
}
</style>
