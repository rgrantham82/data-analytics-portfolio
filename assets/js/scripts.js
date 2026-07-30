// assets/js/scripts.js

document.addEventListener('DOMContentLoaded', () => {
  /* -------------------------------------------------------
     Back-to-Top Button
     ------------------------------------------------------- */
  const backToTopButton = document.querySelector('.back-to-top');

  if (backToTopButton) {
    const toggleBackToTop = () => {
      backToTopButton.hidden = window.scrollY <= 300;
    };

    toggleBackToTop();
    window.addEventListener('scroll', toggleBackToTop, { passive: true });

    backToTopButton.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  /* -------------------------------------------------------
     Smooth Scrolling for in-page Anchor Links

     The skip link is deliberately excluded: hijacking it would
     scroll the page without moving keyboard focus, which defeats
     the purpose of having a skip link at all.
     ------------------------------------------------------- */
  document.querySelectorAll('a[href^="#"]:not(.skip-link)').forEach(link => {
    link.addEventListener('click', (event) => {
      const targetId = link.getAttribute('href').slice(1);
      if (!targetId) return;

      const targetElement = document.getElementById(targetId);
      if (!targetElement) return;

      event.preventDefault();
      targetElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
      targetElement.setAttribute('tabindex', '-1');
      targetElement.focus({ preventScroll: true });
    });
  });

  /* -------------------------------------------------------
     Contact Form
     ------------------------------------------------------- */
  const contactForm = document.querySelector('.contact-form');
  if (!contactForm) return;

  const successMessage = document.querySelector('.success-message');
  const errorMessage = document.querySelector('.error-message');
  const submitButton = contactForm.querySelector('button[type="submit"]');
  const inputFields = contactForm.querySelectorAll('input:not([type="hidden"]), textarea');

  const showMessage = (el, text) => {
    if (!el) return;
    el.textContent = text;
    el.hidden = false;
  };

  const hideMessage = (el) => {
    if (!el) return;
    el.hidden = true;
  };

  // Prefer an explicit label over the raw input name (e.g. "_replyto")
  const fieldLabel = (field) => {
    const label = contactForm.querySelector(`label[for="${field.id}"]`);
    if (label) return label.firstChild.textContent.trim();
    return field.name;
  };

  const validateField = (field) => {
    const errorContainer = field.parentElement
      ? field.parentElement.querySelector('.field-error')
      : null;

    let message = '';
    if (field.required && !field.value.trim()) {
      message = `${fieldLabel(field)} is required.`;
    } else if (field.type === 'email' && field.value.trim() && !field.checkValidity()) {
      message = 'Please enter a valid email address.';
    }

    field.classList.toggle('invalid', Boolean(message));
    if (errorContainer) errorContainer.textContent = message;
    return !message;
  };

  inputFields.forEach(field => {
    field.addEventListener('blur', () => validateField(field));
    field.addEventListener('input', () => {
      if (field.classList.contains('invalid')) validateField(field);
    });
  });

  contactForm.addEventListener('submit', async (event) => {
    event.preventDefault();
    hideMessage(successMessage);
    hideMessage(errorMessage);

    let isValid = true;
    inputFields.forEach(field => {
      if (!validateField(field)) isValid = false;
    });

    if (!isValid) {
      showMessage(errorMessage, 'Please correct the highlighted fields before submitting.');
      return;
    }

    if (submitButton) {
      submitButton.disabled = true;
      submitButton.textContent = 'Sending...';
    }

    try {
      const response = await fetch(contactForm.action, {
        method: contactForm.method,
        headers: { 'Accept': 'application/json' },
        body: new FormData(contactForm)
      });

      if (response.ok) {
        showMessage(successMessage, 'Thank you! Your message has been sent successfully.');
        contactForm.reset();
        inputFields.forEach(field => {
          field.classList.remove('invalid');
          const errorContainer = field.parentElement
            ? field.parentElement.querySelector('.field-error')
            : null;
          if (errorContainer) errorContainer.textContent = '';
        });
      } else {
        let detail = '';
        try {
          const data = await response.json();
          detail = (data.errors || []).map(e => e.message).join(' ') || data.error || '';
        } catch (_) { /* response was not JSON */ }
        showMessage(errorMessage, detail || 'Sorry — there was a problem sending your message. Please try again.');
      }
    } catch (error) {
      console.error('Contact form error:', error);
      showMessage(errorMessage, 'An unexpected error occurred. Please try again later.');
    } finally {
      if (submitButton) {
        submitButton.disabled = false;
        submitButton.textContent = 'Send Message';
      }
    }
  });
});
