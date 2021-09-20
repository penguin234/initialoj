<template>
  <div class="content">
    <div class="content flex justify-between items-center">
      <div class="text-xl font-bold">코딩테스트 연습 문제</div>
    </div>
    <div class="content">
      <list-cont :list-content="listContent"/>
    </div>
  </div>
</template>

<script>
import ListCont from '../components/List/index.vue';

export default {
  name: 'ListContent',
  components: { ListCont },
  data() {
    return {
      listContent: [],
    };
  },
  created() {
    this.$axios.get('http://3.115.176.201/problems')
      .then((res) => {
        this.listContent = res.data.problems;
      });
  },
};
</script>
