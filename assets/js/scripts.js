// assets/js/scripts.js

document.addEventListener('DOMContentLoaded', () => {
    const contactForm = document.querySelector('.contact-form');
    const successMessage = document.querySelector('.success-message');
    const errorMessage = document.querySelector('.error-message');
    const submitButton = document.querySelector('.contact-form button[type="submit"]');

    if (contactForm) {
        contactForm.addEventListener('submit', async function(event) {
            event.preventDefault(); // Prevent default form submission

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
});
