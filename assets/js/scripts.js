// assets/js/scripts.js

document.addEventListener('DOMContentLoaded', () => {
    const contactForm = document.querySelector('.contact-form');
    const successMessage = document.querySelector('.success-message');
    const errorMessage = document.querySelector('.error-message');
    const submitButton = document.querySelector('.contact-form button[type="submit"]');
    const inputFields = document.querySelectorAll('.contact-form input, .contact-form textarea');
    
    // Scroll Animation
    const scrollElements = document.querySelectorAll('.animate-on-scroll');
    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate');
            }
        });
    }, { threshold: 0.5 });

    scrollElements.forEach(el => observer.observe(el));

    // Real-time Form Validation
    const validateField = (field) => {
        const errorContainer = field.nextElementSibling;
        if (field.required && !field.value.trim()) {
            field.classList.add('invalid');
            if (errorContainer) {
                errorContainer.textContent = `${field.name} is required.`;
            }
            return false;
        } else {
            field.classList.remove('invalid');
            if (errorContainer) {
                errorContainer.textContent = '';
            }
            return true;
        }
    };

    inputFields.forEach(field => {
        field.addEventListener('input', () => validateField(field));
    });

    if (contactForm) {
        contactForm.addEventListener('submit', async function(event) {
            event.preventDefault(); // Prevent default form submission

            let isValid = true;
            inputFields.forEach(field => {
                if (!validateField(field)) {
                    isValid = false;
                }
            });

            if (!isValid) {
                if (errorMessage) {
                    errorMessage.style.display = 'block';
                    errorMessage.innerText = 'Please correct the highlighted fields before submitting.';
                }
                return;
            }

            // Disable the submit button to prevent multiple submissions
            if (submitButton) {
                submitButton.disabled = true;
                submitButton.textContent = 'Sending...';
            }

            // Collect form data
            const formData = new FormData(contactForm);
            const data = Object.fromEntries(formData.entries());

            // Prepare data to send (assuming JSON endpoint)
            const jsonData = JSON.stringify(data);

            try {
                const response = await fetch(contactForm.action, {
                    method: contactForm.method,
                    headers: {
                        'Content-Type': 'application/json',
                        'Accept': 'application/json'
                    },
                    body: jsonData
                });

                if (response.ok) {
                    // Display success message
                    if (successMessage) {
                        successMessage.style.display = 'block';
                        successMessage.innerText = 'Thank you! Your message has been sent successfully.';
                    }

                    // Hide error message
                    if (errorMessage) {
                        errorMessage.style.display = 'none';
                    }

                    // Reset form fields
                    contactForm.reset();
                } else {
                    const errorData = await response.json();
                    // Display error message from server
                    if (errorMessage) {
                        errorMessage.style.display = 'block';
                        errorMessage.innerText = errorData.message || 'Oops! There was a problem submitting your form.';
                    }

                    // Hide success message
                    if (successMessage) {
                        successMessage.style.display = 'none';
                    }
                }
            } catch (error) {
                console.error('Error:', error);
                // Display generic error message
                if (errorMessage) {
                    errorMessage.style.display = 'block';
                    errorMessage.innerText = 'An unexpected error occurred. Please try again later.';
                }

                // Hide success message
                if (successMessage) {
                    successMessage.style.display = 'none';
                }
            } finally {
                // Re-enable the submit button
                if (submitButton) {
                    submitButton.disabled = false;
                    submitButton.textContent = 'Send Message';
                }
            }
        });
    }

    // Smooth Scrolling for Anchor Links
    const anchorLinks = document.querySelectorAll('a[href^="#"]');
    anchorLinks.forEach(link => {
        link.addEventListener('click', (event) => {
            event.preventDefault();
            const targetId = link.getAttribute('href').slice(1);
            const targetElement = document.getElementById(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    // Back-to-Top Button
    const backToTopButton = document.querySelector('.back-to-top');
    if (backToTopButton) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 300) {
                backToTopButton.style.display = 'block';
            } else {
                backToTopButton.style.display = 'none';
            }
        });

        backToTopButton.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }
});
