<template>
  <div id="app">
    <p v-if="showWarning" id="warning">Expected txt file.</p>
    <input
      v-on:input="onInput"
      id="upload-file" type="file"
    />
    <ColoredDoc
      v-if="fileContent.length > 0"
      v-bind:text="fileContent"
    />
  </div>
</template>

<script>
import ColoredDoc from './components/Colored-Doc'

export default {
  name: 'app',
  components: {
    ColoredDoc,
  },
  data: () => {
    return {
      showWarning: false,
      fileContent: '',
    };
  },
  methods: {
    //<events>
    onInput: function(evt) {
      this.fileContent = '';
      this.readFile(evt.target.files[0])
        .then((result) => {
          this.processFile(result);
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
    processFile: function(text) {
      fetch('http://127.0.0.1:5000/word-freq', {
        method: 'POST',
        header: {
          'Content-Type': 'text/plain',
        },
        body: text,
      }).then(res => res.text())
      .then((text) => this.fileContent = JSON.parse(text.replace('\n', '<br/>')));
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
