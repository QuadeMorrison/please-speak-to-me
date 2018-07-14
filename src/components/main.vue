<template lang="pug">
  div
    link(rel="stylesheet" href="https://use.fontawesome.com/releases/v5.1.0/css/all.css" integrity="sha384-lKuwvrZot6UHsBSfcMvOkWwlCMgc0TaWr+30HWe3a4ltaBwTZhyTEggF5tJv8tbt" crossorigin="anonymous")
    transition(name='fade' mode='out-in')
      input(v-if='!loading' autofocus type='text' @keyup.enter='onSubmit' v-model='text'
            placeholder='please speak with me')
      RiseLoader#loader(v-else :color='"#1271ED"')
    .audio(v-for="(link, i) in audioLinks")
      #face(:style='"background: " + colors[i % colors.length]')
        i.fas.fa-user-circle
      #content
        audio(controls)
          source(:src="link")
</template>

<script>
import RiseLoader from 'vue-spinner/src/RiseLoader.vue'

export default {
  name: 'Main',
  components: {
    RiseLoader
  },
  data () {
    return {
      text: '',
      loading: false,
      audioLinks: [],
      colors: ['#ef5350', 'yellowgreen', '#FFEE58', '#26A69A']
    }
  },
  methods: {
    sleep(ms) {
      return new Promise(resolve => setTimeout(resolve, ms));
    },
    async onSubmit() {
      this.loading = true;
      await this.sleep(2000)
      this.audioLinks.push(0)
      url = encodeURI(`/voice?query=${this.text}`)
      let res = await this.$http.get(url)
      this.loading = false
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

input {
  text-align: center;
  border: none;
  display: block;
  font-size: 45px;
  border-bottom: 4px #35A4ED solid;
  height: 60px;
  width: 80%;
  margin: 50px auto;
}

#face {
  width: 70px;
  height: 70px;
  background: yellowgreen;
  font-size: 55px;
  text-align: center;
  vertical-align: center;
  color: white;
  display: inline-block;
  border-radius: 100px;
  margin-bottom: 10px;
}

#content {
  position: relative;
  display: inline-block;
  margin-left: 10px;
  top: 5px;
}

*:focus {
    outline: none;
}

#loader {
  margin: 72px;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s
}

.fade-enter,
.fade-leave-to
{
  opacity: 0
}

</style>
