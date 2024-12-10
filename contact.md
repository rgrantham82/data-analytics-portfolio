---
layout: default
title: "Contact"
permalink: /contact/
---

<!-- Contact Page Section -->
<section class="contact-page-section section">
  <div class="container">
    <h1>Contact Me</h1>
    <p>
      I'm always open to discussing new projects, opportunities, or just to connect. Please feel free to reach out using the form below or connect with me on LinkedIn.
    </p>
    
    <!-- Contact Form -->
    <form action="https://formspree.io/f/mbjnwpgb" method="POST" class="contact-form">
      <div class="form-group">
        <label for="name">Name<span class="required">*</span></label>
        <input type="text" id="name" name="name" placeholder="Your Name" required>
      </div>
      
      <div class="form-group">
        <label for="email">Email<span class="required">*</span></label>
        <input type="email" id="email" name="_replyto" placeholder="Your Email" required>
      </div>
      
      <div class="form-group">
        <label for="subject">Subject<span class="required">*</span></label>
        <input type="text" id="subject" name="subject" placeholder="Subject" required>
      </div>
      
      <div class="form-group">
        <label for="message">Message<span class="required">*</span></label>
        <textarea id="message" name="message" rows="5" placeholder="Your Message" required></textarea>
      </div>
      
      <!-- Honeypot Field (Spam Protection) -->
      <input type="text" name="_gotcha" style="display:none">
      
      <!-- Submit Button -->
      <button type="submit" class="btn">Send Message</button>
    </form>
    
    <!-- Success Message -->
    {% if page.success %}
    <div class="success-message">
      <p>Your message has been sent successfully! I'll get back to you soon.</p>
    </div>
    {% endif %}
    
    <!-- Error Message -->
    {% if page.error %}
    <div class="error-message">
      <p>There was an error sending your message. Please try again later.</p>
    </div>
    {% endif %}
    
    <!-- Contact Information -->
    <div class="contact-info">
      <h2>Or Reach Me Directly</h2>
      <p>
        <strong>Email:</strong> <a href="mailto:robertgrantham40@gmail.com">robertgrantham40@gmail.com</a><br>
        <strong>Phone:</strong> <a href="tel:5122003563">512-200-3563</a><br>
        <strong>LinkedIn:</strong> <a href="{{ site.author.linkedin }}" target="_blank">Connect with me on LinkedIn</a>
      </p>
    </div>
  </div>
</section>
