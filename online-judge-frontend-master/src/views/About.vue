<template>
  <div class="content" @click="langFlag=false">
    <div class="content">
      <div class="flex justify-between items-end border-b-4 pb-3">
        <div class="text-xl font-bold">
          <span class="cursor-pointer hover:text-blue-600" @click="goHome">
            코딩테스트 연습 문제
          </span>
          > {{ title }}
        </div>
        <div class="flex items-center">
          <div class="cursor-pointer bg-gray-600 text-white font-medium
        rounded-lg px-3 py-1"
               @click.stop="openLanguage"
          >
            {{ language }} ▾
          </div>
          <div v-if="langFlag"
               style="position: fixed; top: 52px; right: 20px; z-index: 99"
               class="shadow-2xl p-3 bg-white">
            <div v-for="item in langList" :value="item.value" :key="item.value"
                 class="hover:text-blue-600 font-medium p-1 cursor-pointer"
                 @click="selectLang(item)"
            >
              {{ item.label }}
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="flex justify-between">
      <pro-desc class="w-1/2 content" :detailContent="detailContent"/>
      <div class="bg-gray-200 text-gray-200">.</div>
      <div class="w-1/2 content">
        <result-cont :id="id" :langVal="langVal"
                     :lang="language" :darkMode="darkMode"/>
      </div>
    </div>
  </div>
</template>

<script>
import ProDesc from '../components/Detail/proDesc.vue';
import ResultCont from '../components/Detail/result.vue';

export default {
  name: 'index',
  components: {
    ProDesc,
    ResultCont,
  },
  data() {
    return {
      id: null,
      detailContent: null,
      inputCode: null,
      resultContent: null,
      loading: false,
      title: null,
      darkMode: false,
      language: 'python',
      langVal: 1,
      langFlag: false,
      langList: [
        {
          label: 'python',
          value: 1,
        },
        {
          label: 'c++',
          value: 2,
        },
        {
          label: 'c',
          value: 3,
        },
        {
          label: 'java',
          value: 4,
        },
      ],

      colors: ['#bababa'],
    };
  },
  created() {
    this.id = parseInt(this.$route.params.id, 10);
    this.$axios.get(`http://3.115.176.201/problem/${this.id}`)
      .then((res) => {
        this.title = res.data.proTitle;
        this.detailContent = res.data;
      });
  },
  methods: {
    selectLang(e) {
      this.language = e.label;
      this.langVal = e.value;
      this.langFlag = false;
    },
    openLanguage() {
      this.langFlag = !this.langFlag;
    },
    goHome() {
      this.$router.push('/');
    },
  },
};
</script>

<style scoped>
.cc {
  color: #bababa;
}
</style>
