<template>
    <div class="column is-3">
      <div class="card">
        <div class="card-image">
          <figure class="image">
            <img :src="product.get_thumbnail" alt="Product Thumbnail" />
          </figure>
        </div>
  
        <div class="card-content">
          <h3 class="is-size-4 mb-2">{{ product.name }}</h3>
          <p class="is-size-6 has-text-grey mb-4">${{ product.price }}</p>
        </div>
  
        <footer class="card-footer">
          <router-link :to="product.get_absolute_url" class="card-footer-item button is-dark">View details</router-link>
        </footer>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'ProductBox',
    props: {
      product: {
        type: Object,
        required: true
      }
    }
  };
  </script>
  
  <style scoped>
  .column {
    display: flex;
    justify-content: center; /* Centers the cards horizontally */
  }
  
  .card {
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 1.5rem;
    border: 1px solid #ccc; /* Optional: Add a border for visual separation */
  }
  
  .card-content {
    flex-grow: 1;
  }
  
  .card-footer {
    justify-content: center;
  }
  
  .mb-2 {
    margin-bottom: 0.5rem;
  }
  
  .mb-4 {
    margin-bottom: 1rem;
  }
  </style>