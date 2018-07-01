<template lang="pug">
  div
    input(autofocus type='text' @keyup.enter="onSubmit" v-model='text'
          placeholder='please speak with me')
    button(@click="onSubmit") Submit
    audio(controls='true' :src="audio")
    span
      | Icons made by&nbsp
      a(href="http://www.freepik.com" title="Freepik") Freepik
      | &nbspfrom&nbsp
      a(href="https://www.flaticon.com/" title="Flaticon") www.flaticon.com
      | &nbspis licensed by&nbsp
      a(href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0" target="_blank") CC 3.0 BY
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      text: '',
      audio: ''
    }
  },
  methods: {
    onSubmit() {
      console.log("Submitting!")
      this.$http.post('/voice', {
        text: this.text
      }).then((response) => {
        this.audio = response
        console.log('Give me the data')
      })
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

*:focus {
    outline: none;
}

</style>
