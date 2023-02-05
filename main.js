const app = new Vue({
    el: '#app',
    data: {
      responseData: null,
      file: null,
      isRequesting: false
    },
    methods: {

      uploadFile(event) {
      
        this.file = event.target.files[0];
        this.responseData = null;
      
      },
      
      async submitFile() {
      
        if (!this.file) {
          alert("Please upload a file before submitting");
          return;
        }
      
        const formData = new FormData();
      
        formData.append('file', this.file);
      
        this.isRequesting = true;

        const { data } = await axios.post('https://vibr.herokuapp.com/upload', formData);
      
        this.isRequesting = false;

        console.log(typeof data);
      
        this.responseData = data;
      
        console.log(this.responseData)
      
      }
      
    }
  });