<template>
    <div class="container">
      <h1>Movies</h1>
      <div class="movies-container" style="max-height: 600px">
        <div class="movie-card" v-for="movie in movies" :key="movie.id">
          <div class="poster">
            <img :src="movie.poster" :alt="movie.title" class="card-img img-fluid" />
          </div>
          <div class="m-body">
            <h5 class="m-title">{{ movie.title }}</h5>
            <p class="m-description">{{ movie.description }}</p>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from "vue";
  
  let movies = ref([]);
  
  async function fetchMovies() {
    try {
      const response = await fetch("/api/v1/movies", {
        method: "GET",
      });
      const data = await response.json();
      movies.value = data.movies;
    } catch (error) {
      console.error('Error:', error);
    }
  }
  
  onMounted(fetchMovies);
  </script>
  
  <style scoped>
  .movies-container {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
  }
  
  .movie-card {
    flex: 0 0 calc(33.33% - 20px); 
    border: 1px solid #ccc;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    display: flex; 
  }
  
  .poster {
    width: 100%; 
    display: flex;
    justify-content: flex-end; 
  }
  
  .m-body {
    width: 60%; 
    padding: 10px;
  }
  
  .m-title {
    margin-bottom: 5px;
  }
  
  .m-description {
    font-size: 14px;
  }
  </style>
  