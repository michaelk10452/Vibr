const app = new Vue({
    el: '#app',
    data: {
      responseData: null,
      file: null
    },
    methods: {
      uploadFile(event) {
        this.file = event.target.files[0];
      },
      async submitFile() {
        if (!this.file) {
          alert("Please upload a file before submitting");
          return;
        }
        const formData = new FormData();
        formData.append('file', this.file);
        const { data } = await axios.post('https://vibr.herokuapp.com//upload', formData);
        console.log(typeof data);
        this.responseData = data;
        console.log(data)
      }
    }
  });