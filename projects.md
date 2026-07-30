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
      <button class="filter-btn active" type="button" data-filter="All">All</button>
      {%- comment -%}
        Filter buttons are generated from the tags actually present in
        _data/projects.yml, so they can never drift out of sync with the cards.
      {%- endcomment -%}
      {% assign tag_string = "" %}
      {% for project in site.data.projects.items %}
        {% assign tag_string = tag_string | append: project.tags | append: ", " %}
      {% endfor %}
      {% assign all_tags = tag_string | split: ", " | uniq | sort %}
      {% for tag in all_tags %}
        <button class="filter-btn" type="button" data-filter="{{ tag }}">{{ tag }}</button>
      {% endfor %}
    </div>
  </div>
</section>

<!-- Search Bar -->
<section class="search-section section">
  <div class="container">
    <h2>Search Projects</h2>
    <div class="search-container">
      <label class="visually-hidden" for="searchInput">Search projects</label>
      <input type="search" id="searchInput" placeholder="Search projects...">
    </div>
  </div>
</section>

<!-- Projects Grid -->
<section class="projects-section section">
  <div class="container">
    <h2>My Projects</h2>
    <div class="projects-grid">
      {% for project in site.data.projects.items %}
        {% assign tag_list = project.tags | split: ", " %}
        <div class="project-card" data-tags="{{ tag_list | join: '|' | downcase }}">
          {% if project.image %}
            <img src="{{ project.image | relative_url }}"
                 alt="Screenshot from the {{ project.title }} project"
                 class="project-image" loading="lazy">
          {% endif %}
          <div class="project-content">
            <h3>{{ project.title }}</h3>
            <h4>{{ project.subtitle }}</h4>
            <p>{{ project.description }}</p>
            <div class="project-tags">
              {% for tag in tag_list %}
                <span class="tag">{{ tag }}</span>
              {% endfor %}
            </div>
            {% assign is_external = project.link | slice: 0, 4 %}
            <a href="{{ project.link | relative_url }}" class="btn"
               {% if is_external == "http" %}target="_blank" rel="noopener noreferrer"{% endif %}>{{ project.link_text }}</a>
          </div>
        </div>
      {% endfor %}
    </div>
  </div>
</section>

<!-- No Results Message -->
<section class="no-results-section section" hidden>
  <div class="container">
    <h2>No Projects Found</h2>
    <p>Try adjusting your search or filter criteria to find the projects you're looking for.</p>
  </div>
</section>

<!-- Filtering and Searching -->
<script>
  document.addEventListener('DOMContentLoaded', () => {
    const filterButtons = document.querySelectorAll('.filter-btn');
    const projectCards = Array.from(document.querySelectorAll('.project-card'));
    const searchInput = document.getElementById('searchInput');
    const noResultsSection = document.querySelector('.no-results-section');

    let activeFilter = 'All';
    let activeQuery = '';

    // Filter and search compose: a card must satisfy both to stay visible.
    const applyFilters = () => {
      let visibleCount = 0;

      projectCards.forEach(card => {
        const tags = (card.dataset.tags || '').split('|');
        const title = card.querySelector('h3').textContent.toLowerCase();
        const text = card.textContent.toLowerCase();

        const matchesFilter =
          activeFilter === 'All' || tags.includes(activeFilter.toLowerCase());
        const matchesQuery =
          activeQuery === '' || title.includes(activeQuery) || text.includes(activeQuery);

        const visible = matchesFilter && matchesQuery;
        card.classList.toggle('is-hidden', !visible);
        if (visible) visibleCount += 1;
      });

      if (noResultsSection) noResultsSection.hidden = visibleCount > 0;
    };

    filterButtons.forEach(button => {
      button.addEventListener('click', () => {
        activeFilter = button.dataset.filter;
        filterButtons.forEach(btn => btn.classList.toggle('active', btn === button));
        applyFilters();
      });
    });

    if (searchInput) {
      searchInput.addEventListener('input', () => {
        activeQuery = searchInput.value.trim().toLowerCase();
        applyFilters();
      });
    }

    applyFilters();
  });
</script>
