---
layout: default
title: "Home"
permalink: /
---

<!-- Hero Section -->
<section class="hero-section">
  <div class="container">
    <h1>Welcome to My Data Analytics Portfolio</h1>
    <p>I'm Robert Grantham, a passionate Data Analyst dedicated to transforming data into actionable insights.</p>
    <a href="#about" class="btn">Learn More About Me</a>
  </div>
</section>

<!-- About Section -->
<section class="about-section section">
  <div class="container">
    <h2>About Me</h2>
    <p>
      With a strong foundation in statistics, machine learning, and data visualization, I specialize in analyzing complex datasets to uncover meaningful patterns and drive informed decision-making. My expertise spans SQL, Python, R, Tableau, and more, enabling me to deliver comprehensive data solutions.
    </p>
    <a href="/about/" class="btn">View My Resume</a>
  </div>
</section>

<!-- Featured Projects Section -->
<section class="featured-projects-section section">
  <div class="container">
    <h2>Featured Projects</h2>
    <div class="projects-grid">
      {% assign featured_projects = site.data.projects.items | limit: 3 %}
      {% for project in featured_projects %}
        <div class="project-card">
          <img src="{{ project.image }}" alt="{{ project.title }} Screenshot" class="project-image {{ project.image_ratio }}">
          <div class="project-content">
            <h3>{{ project.title }}</h3>
            <h4>{{ project.subtitle }}</h4>
            <p>{{ project.description | truncatewords: 20 }}</p>
            <div class="project-tags">
              {% for tag in project.tags | split: ", " %}
                <span class="tag">{{ tag }}</span>
              {% endfor %}
            </div>
            <a href="{{ project.link }}" class="btn" target="_blank">{{ project.link_text }}</a>
          </div>
        </div>
      {% endfor %}
    </div>
    <div class="view-all">
      <a href="/projects/" class="btn">View All Projects</a>
    </div>
  </div>
</section>

<!-- Contact Section -->
<section class="contact-section section">
  <div class="container">
    <h2>Get in Touch</h2>
    <p>
      I'm always open to discussing new projects, opportunities, or just to say hello. Feel free to reach out through the contact form below or connect with me on LinkedIn.
    </p>
    <a href="/contact/" class="btn">Contact Me</a>
  </div>
</section>
