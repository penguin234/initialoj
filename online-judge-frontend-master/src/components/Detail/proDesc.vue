<template>
  <div class="divide-y">
    <div class="mb-4">
      <div class="mb-3 font-extrabold">문제설명</div>
      <div>{{ proDesc }}</div>
    </div>
    <div>
      <div class="mt-4 mb-3 font-extrabold">입출력 예시</div>
      <div class="mt-2">
        <table class="border-collapse border border-gray-800">
          <thead>
          <tr>
            <th class="border border-gray-600 py-2 px-5">입력</th>
            <th class="border border-gray-600 py-2 px-5">출력</th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="(item, idx) in testCases" :key="idx" :value="idx">
            <td class="border border-gray-600 py-2 px-5">{{ item.inputEx }}</td>
            <td class="border border-gray-600 py-2 px-5">{{ item.outputEx }}</td>
          </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'proDesc',
  props: {
    detailContent: {
      type: Object,
      default: null,
    },
  },
  data() {
    return {
      proDesc: null,
      testCases: null,
    };
  },
  watch: {
    detailContent: {
      immediate: true,
      deep: true,
      handler(v) {
        if (v != null) {
          this.proDesc = v.proDesc;
          this.testCases = v.testCases;
        }
      },
    },
  },
};
</script>

<style scoped>

</style>
