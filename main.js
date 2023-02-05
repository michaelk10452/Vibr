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
        const { data } = await axios.post('/api/upload', formData);
        this.responseData = data;
      }
    }
  });
  

// var app = new Vue({
//     el: '#app',
//     data: {
//       responseData: ''
//     },
//     methods: {
//       uploadFile: function(event) {
//         this.selectedFile = event.target.files[0]
//       },
//       submitFile: function() {
//         if (!this.selectedFile) {
//           alert('Please select a file to upload.')
//           return
//         }
  
//         let formData = new FormData()
//         formData.append('file', this.selectedFile)
//         axios.post('http://localhost:5000/upload', formData).then(response => {
//           this.responseData = response.data
//         }).catch(error => {
//           console.error(error)
//         })
//       }
//     }
//   })
  




//     el: '#app',
//     methods: {
//       uploadFile() {
//         this.selectedFile = this.$refs.fileInput.files[0];
//       },
//       async submitFile() {
//         if (!this.selectedFile) {
//           alert("Please select a file to upload");
//           return;
//         }
//         const formData = new FormData();
//         formData.append('file', this.selectedFile);
        
//         try {
//           const response = await axios.post('http://10.8.2.207:5000/', formData, {
//             headers: {
//               'Content-Type': 'multipart/form-data'
//             }
//           });
          
//           console.log(response.data);
//         } catch (error) {
//           console.error(error);
//         }
//       }
//     }
//   });
  