<template>
  <div>
    <monaco-editor ref="editor" style="height: 300px; width: 100%"/>
    <div class="mt-4">
      <div class="flex justify-between items-center  border-b border-t py-2">
        <div class="font-extrabold">실행결과</div>
        <button class="ml-3 bg-blue-200 py-2 px-5 rounded-lg" @click="submitCode">제출</button>
      </div>
      <div class="content" style="height: 200px">
        <div v-if="loading">채점중...</div>
        <div v-else class="flex justify-start items-center gap-4">
          <div :class="result ? 'text-green-600' : result===false ? 'text-red-600' : ''">
            {{ result === true ? '성공' : result === false ? '실패' : '실행 결과가 여기에 표시됩니다.' }}
          </div>
          <div>{{ resultDesc }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'result',
  props: {
    id: {
      type: Number,
      default: null,
    },
    langVal: {
      type: Number,
      default: null,
    },
    lang: {
      type: String,
      default: null,
    },
    darkMode: {
      type: Boolean,
      default: null,
    },
  },
  watch: {
    darkMode(v) {
      if (v) {
        this.$refs.editor.changeTheme('vs-dark');
      } else {
        this.$refs.editor.changeTheme('vs');
      }
    },
    lang(v) {
      if (v != null) {
        if (v === 'c++') this.$refs.editor.updateOptions('c');
        else this.$refs.editor.updateOptions(v);
      }
    },
  },
  data() {
    return {
      result: null,
      resultDesc: null,
      detailContent: null,
      loading: false,
    };
  },
  methods: {
    submitCode() {
      this.loading = true;
      this.inputCode = this.$refs.editor.getValue();
      this.$axios.post('http://3.115.176.201/judge', {
        proNum: this.id,
        langtype: this.langVal,
        code: this.inputCode,
      })
        .then((res) => {
          this.result = res.data.result;
          this.resultDesc = this.setResultDesc(res.data.resultDesc);
          this.loading = false;
        });
    },
    setResultDesc(e) {
      switch (e) {
        case 1:
          return '컴파일 에러';
        case 2:
          return '런타임 에러';
        case 3:
          return '오답';
        default:
          return '';
      }
    },
  },
};
</script>

<style scoped>

</style>
