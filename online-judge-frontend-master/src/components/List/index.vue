<template>
  <div class="border-2 rounded-2xl p-4">
    <div class="grid grid-cols-3 gap-2 place-items-stretch">
      <div v-for="item in listContent" :key="item.proNum" :value="item.proNum"
           class=" h-16 pt-4 m-3 border-t-2  font-bold
            text-xl cursor-pointer hover:text-blue-500"
           @click="clickItem(item.proNum)"
      >
        <span class="border-t-4 border-blue-500 pt-4 pr-2">{{ item.proTitle }}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'index',
  props: {
    listContent: {
      type: Array,
      default: null,
    },
  },
  methods: {
    clickItem(id) {
      this.$router.push(`/${id}`);
    },
    // clickItem(num) {
    //   this.$router.push(`/${num}`);
    // },
  },
};
</script>

<style scoped>

</style>
