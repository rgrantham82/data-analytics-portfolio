---
layout: default
title: "Contact"
permalink: /contact/
---

# Contact Me

I'm always open to discussing new projects, opportunities, or just to connect. Send a note using the form below, or reach out on [LinkedIn]({{ site.author.linkedin }}).

<!-- Feedback banners. These are always present in the DOM and revealed by
     assets/js/scripts.js after the form submits. -->
<div class="form-message success-message" role="status" aria-live="polite" hidden></div>
<div class="form-message error-message" role="alert" aria-live="assertive" hidden></div>

<form action="https://formspree.io/f/mbjnwpgb" method="POST" class="contact-form">
  <div class="form-group">
    <label for="name">Name <span class="required">(required)</span></label>
    <input type="text" id="name" name="name" placeholder="Your Name" autocomplete="name" required>
    <div class="field-error" aria-live="polite"></div>
  </div>

  <div class="form-group">
    <label for="email">Email <span class="required">(required)</span></label>
    <input type="email" id="email" name="_replyto" placeholder="Your Email" autocomplete="email" required>
    <div class="field-error" aria-live="polite"></div>
  </div>

  <div class="form-group">
    <label for="subject">Subject <span class="required">(required)</span></label>
    <input type="text" id="subject" name="subject" placeholder="Subject" required>
    <div class="field-error" aria-live="polite"></div>
  </div>

  <div class="form-group">
    <label for="message">Message <span class="required">(required)</span></label>
    <textarea id="message" name="message" rows="5" placeholder="Your Message" required></textarea>
    <div class="field-error" aria-live="polite"></div>
  </div>

  <!-- Honeypot Field (Spam Protection) -->
  <input type="text" name="_gotcha" tabindex="-1" autocomplete="off" style="display:none">

  <button type="submit" class="btn">Send Message</button>
</form>

## Direct Contact

- **LinkedIn:** [Connect with me on LinkedIn]({{ site.author.linkedin }})
- **GitHub:** [{{ site.author.github | split: "/" | last }}]({{ site.author.github }})
