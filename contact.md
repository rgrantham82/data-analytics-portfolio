---
layout: default
title: "Contact"
permalink: /contact/
---

# Contact Me

I'm always open to discussing new projects, opportunities, or just to connect. Please fill out the form below or reach out directly via email or LinkedIn.

<form action="https://formspree.io/f/mbjnwpgb" method="POST" class="contact-form">
  <div class="form-group">
    <label for="name">Name <span class="required">(required)</span></label>
    <input type="text" id="name" name="name" placeholder="Your Name" required>
  </div>

  <div class="form-group">
    <label for="email">Email <span class="required">(required)</span></label>
    <input type="email" id="email" name="_replyto" placeholder="Your Email" required>
  </div>

  <div class="form-group">
    <label for="subject">Subject <span class="required">(required)</span></label>
    <input type="text" id="subject" name="subject" placeholder="Subject" required>
  </div>

  <div class="form-group">
    <label for="message">Message <span class="required">(required)</span></label>
    <textarea id="message" name="message" rows="5" placeholder="Your Message" required></textarea>
  </div>

  <!-- Honeypot Field (Spam Protection) -->
  <input type="text" name="_gotcha" style="display:none">

  <!-- Submit Button -->
  <button type="submit" class="btn">Send Message</button>
</form>

<!-- Success and Error Messages -->
{% if page.success %}
<div class="success-message">
  <p>Your message has been sent successfully! I'll get back to you soon.</p>
</div>
{% endif %}

{% if page.error %}
<div class="error-message">
  <p>There was an error sending your message. Please try again later.</p>
</div>
{% endif %}

## Direct Contact

- **Email:** [robertgrantham40@gmail.com](mailto:robertgrantham40@gmail.com)  
- **Phone:** [512-200-3563](tel:5122003563)  
- **LinkedIn:** [Connect with me on LinkedIn]({{ site.author.linkedin }})

If the form fails, try again later or use one of the direct contact methods above.
