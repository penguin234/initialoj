<template>
  <div id="container"
       ref="container"
  />
</template>

<script>
import * as monaco from 'monaco-editor';

export default {
  name: 'monacoEditor',
  data() {
    return {
      editor: null,
    };
  },
  computed: {},
  mounted() {
    this.editor = monaco.editor.create(this.$refs.container, {
      value: '',
      language: 'python',
      theme: 'vs',
      // theme: 'vs-dark',
      automaticLayout: true,
      tabSize: 2,
    });
  },
  methods: {
    getValue() {
      return this.editor.getValue();
    },
    changeTheme(type) {
      this.editor.updateOptions({ theme: type });
    },
    updateOptions(lang) {
      monaco.editor.setModelLanguage(this.editor.getModel(), lang);
    },
  },
};
</script>

<style scoped lang="scss">

</style>
