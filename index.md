---
layout: default
title: "Home"
permalink: /
---

<!-- Hero Section -->
<section class="hero-section section">
  <div class="container">
    <h1>Welcome to My Data Analytics Portfolio</h1>
    <p>I'm Robert Grantham, a passionate Data Analyst dedicated to transforming data into actionable insights.</p>
    <a href="#about" class="btn">Learn More About Me</a>
  </div>
</section>

<!-- About Preview Section -->
<section class="about-preview-section section" id="about">
  <div class="container">
    <h2>About Me</h2>
    <p>
      With a strong foundation in data migration, visualization, and system optimization, I specialize in leveraging SQL, Python, and ETL processes to deliver effective data-driven solutions. My expertise lies in managing complex datasets, ensuring data integrity, and collaborating with cross-functional teams to support business intelligence initiatives.
    </p>
    <a href="/about/" class="btn">Read More</a>
  </div>
</section>

<!-- Featured Projects Section -->
<section class="featured-projects-section section">
  <div class="container">
    <h2>Featured Projects</h2>
    <div class="projects-grid">
      {% assign featured_projects = site.data.projects.items | limit: 3 %}
      {% for project in featured_projects %}
        <div class="project-card" data-tags="{{ project.tags | replace: ', ', ' ' | downcase }}">
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

<!-- Testimonials Section (Optional) -->
<section class="testimonials-section section">
  <div class="container">
    <h2>What Others Say</h2>
    <div class="testimonials-grid">
      <div class="testimonial-card">
        <p>"Robert's expertise in data analytics is unparalleled. His ability to translate complex data into actionable insights has been invaluable to our projects."</p>
        <h4>- Jane Doe, Senior Manager at ABC Corp</h4>
      </div>
      <div class="testimonial-card">
        <p>"Working with Robert was a pleasure. His attention to detail and commitment to excellence ensured the success of our data-driven initiatives."</p>
        <h4>- John Smith, Data Scientist at DEF Solutions</h4>
      </div>
      <!-- Add more testimonials as needed -->
    </div>
  </div>
</section>

<!-- Contact Preview Section -->
<section class="contact-preview-section section">
  <div class="container">
    <h2>Get in Touch</h2>
    <p>
      I'm always open to discussing new projects, opportunities, or just to connect. Feel free to reach out through the contact form below or connect with me on LinkedIn.
    </p>
    <a href="/contact/" class="btn">Contact Me</a>
  </div>
</section>
