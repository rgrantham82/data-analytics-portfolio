---
layout: default
title: "Projects"
permalink: /projects/
---

<!-- Filter Buttons -->
<section class="filters-section section">
  <div class="container">
    <h2>Filter Projects</h2>
    <div class="filters">
      <button class="filter-btn" data-filter="All">All</button>
      <button class="filter-btn" data-filter="SQL">SQL</button>
      <button class="filter-btn" data-filter="Machine Learning">Machine Learning</button>
      <button class="filter-btn" data-filter="AI">AI</button>
      <button class="filter-btn" data-filter="Forecasting">Forecasting</button>
      <button class="filter-btn" data-filter="Clustering">Clustering</button>
      <button class="filter-btn" data-filter="Data Visualization">Data Visualization</button>
      <button class="filter-btn" data-filter="Predictive Analytics">Predictive Analytics</button>
      <button class="filter-btn" data-filter="Credit Risk">Credit Risk</button>
      <button class="filter-btn" data-filter="Crime Analysis">Crime Analysis</button>
      <!-- Add more buttons based on your tags -->
    </div>
  </div>
</section>

<!-- Search Bar -->
<section class="search-section section">
  <div class="container">
    <h2>Search Projects</h2>
    <div class="search-container">
      <input type="text" id="searchInput" placeholder="Search projects...">
    </div>
  </div>
</section>

<!-- Projects Grid -->
<section class="projects-section section">
  <div class="container">
    <h2>My Projects</h2>
    <div class="projects-grid">
      {% for project in site.data.projects.items %}
        <div class="project-card" data-tags="{{ project.tags | replace: ', ', ' ' | downcase }}">
          <img src="{{ project.image | relative_url }}" alt="{{ project.title }} Screenshot" class="project-image {{ project.image_ratio }}">
          <div class="project-content">
            <h3>{{ project.title }}</h3>
            <h4>{{ project.subtitle }}</h4>
            <p>{{ project.description }}</p>
            <div class="project-tags">
              {% for tag in project.tags | split: ", " %}
                <span class="tag">{{ tag }}</span>
              {% endfor %}
            </div>
            <a href="{{ project.link | relative_url }}" class="btn" target="_blank" rel="noopener noreferrer">{{ project.link_text }}</a>
          </div>
        </div>
      {% endfor %}
    </div>
  </div>
</section>

<!-- No Results Message -->
<section class="no-results-section section" style="display: none;">
  <div class="container">
    <h2>No Projects Found</h2>
    <p>Try adjusting your search or filter criteria to find the projects you're looking for.</p>
  </div>
</section>

<!-- JavaScript for Filtering and Searching -->
<script>
  document.addEventListener('DOMContentLoaded', () => {
    const filterButtons = document.querySelectorAll('.filter-btn');
    const projectCards = document.querySelectorAll('.project-card');
    const searchInput = document.getElementById('searchInput');
    const noResultsSection = document.querySelector('.no-results-section');

    // Function to filter projects
    const filterProjects = (filter) => {
      let anyVisible = false;
      projectCards.forEach(card => {
        const tags = card.getAttribute('data-tags');
        if (filter === 'All' || tags.includes(filter.toLowerCase())) {
          card.style.display = 'block';
          anyVisible = true;
        } else {
          card.style.display = 'none';
        }
      });
      noResultsSection.style.display = anyVisible ? 'none' : 'block';
    };

    // Function to search projects
    const searchProjects = (query) => {
      let anyVisible = false;
      projectCards.forEach(card => {
        const title = card.querySelector('h3').textContent.toLowerCase();
        const tags = card.querySelector('.project-tags').textContent.toLowerCase();
        if (title.includes(query) || tags.includes(query)) {
          card.style.display = 'block';
          anyVisible = true;
        } else {
          card.style.display = 'none';
        }
      });
      noResultsSection.style.display = anyVisible ? 'none' : 'block';
    };

    // Event listeners for filter buttons
    filterButtons.forEach(button => {
      button.addEventListener('click', () => {
        const filter = button.getAttribute('data-filter');
        filterButtons.forEach(btn => btn.classList.remove('active'));
        button.classList.add('active');
        filterProjects(filter);
      });
    });

    // Event listener for search input
    searchInput.addEventListener('keyup', () => {
      const query = searchInput.value.trim().toLowerCase();
      if (query === '') {
        // If search is empty, show all projects based on current filter
        const activeFilter = document.querySelector('.filter-btn.active');
        const filter = activeFilter ? activeFilter.getAttribute('data-filter') : 'All';
        filterProjects(filter);
      } else {
        // Search across all projects
        projectCards.forEach(card => {
          const title = card.querySelector('h3').textContent.toLowerCase();
          const tags = card.querySelector('.project-tags').textContent.toLowerCase();
          if (title.includes(query) || tags.includes(query)) {
            card.style.display = 'block';
          } else {
            card.style.display = 'none';
          }
        });
        // Show or hide the no results message
        const visibleCards = Array.from(projectCards).filter(card => card.style.display === 'block');
        noResultsSection.style.display = visibleCards.length > 0 ? 'none' : 'block';
      }
    });

    // Initialize with 'All' filter active
    const allButton = document.querySelector('.filter-btn[data-filter="All"]');
    if (allButton) {
      allButton.classList.add('active');
    }
  });
</script>
