<template>
<div class="container">
 <form id="movieForm" @submit.prevent="saveMovie">
  <div class="form-group mb-3">
    <label for="title" class="form-label">Movie Title</label>
    <br>
    <input type="text" name="title" class="form-control" style="width: 500px;"/>
  </div> 
  <div class="form-group mb-3">
    <label for="description" class="form-label">Movie Description</label>
    <br>
    <textarea name="description" class="form-control" style="width: 500px; height: 200px;"> </textarea>
  </div> 
  <div class="form-group mb-3">
    <label for="poster" class="form-label">Movie Poster</label>
    <br>
    <input type="file" name="poster" class="form-control"/>
  </div>
  <div>
    <button type="submit" class="btn btn-primary">Submit</button>
  </div>
 </form>
</div>
</template>

<script setup>
import { ref, onMounted } from "vue";
    let csrf_token = ref("");
    let success = ref("");
    let errors = ref([]);

    function saveMovie(){
        console.log(csrf_token)
        let movieForm = document.getElementById('movieForm');
        let form_data = new FormData(movieForm);
        fetch("/api/v1/movies", {
            method: 'POST',
            body: form_data,
            headers: {
                'X-CSRFToken': csrf_token.value
            }
            })
            .then(function (response) {
                return response.json();
              }
            })
            .then(function (data) {
                if (data.errors) {
                errors.value = data.errors;
                return;
                }
                success.value = data.message;
                errors.value = [];
                console.log(data);
            })
                .catch(function (error) {
                  console.error(error);
            });
    }

    function getCsrfToken() {
      fetch("/api/v1/csrf-token")
        .then((res) => res.json())
        .then((data) => {
          csrf_token.value = data.csrf_token;
        })
        .catch((error) => {
          console.log(error);
        });
    }

    onMounted(async() => {
       await getCsrfToken();
    });

</script>