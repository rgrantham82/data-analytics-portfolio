```markdown
---
layout: default
title: "Contact"
permalink: /contact/
---

# Contact Me

I'm always open to discussing new projects, opportunities, or just to connect. Please feel free to reach out using the form below or connect with me on LinkedIn.

**Contact Form**

<form action="https://formspree.io/f/mbjnwpgb" method="POST" class="contact-form">
- **Name** (required):  
  `<input type="text" id="name" name="name" placeholder="Your Name" required>`  
- **Email** (required):  
  `<input type="email" id="email" name="_replyto" placeholder="Your Email" required>`  
- **Subject** (required):  
  `<input type="text" id="subject" name="subject" placeholder="Subject" required>`  
- **Message** (required):  
  `<textarea id="message" name="message" rows="5" placeholder="Your Message" required></textarea>`

*(Honeypot Field for Spam Protection)*  
`<input type="text" name="_gotcha" style="display:none">`

**Submit Button:**  
`<button type="submit" class="btn">Send Message</button>`

If the form submission is successful (based on `page.success`):
```
{% if page.success %}
<div class="success-message">
  <p>Your message has been sent successfully! I'll get back to you soon.</p>
</div>
{% endif %}
```

If there's an error sending the message (based on `page.error`):
```
{% if page.error %}
<div class="error-message">
  <p>There was an error sending your message. Please try again later.</p>
</div>
{% endif %}
```

**Or Reach Me Directly**

**Email:** [robertgrantham40@gmail.com](mailto:robertgrantham40@gmail.com)  
**Phone:** [512-200-3563](tel:5122003563)  
**LinkedIn:** [Connect with me on LinkedIn]({{ site.author.linkedin }})  
```
