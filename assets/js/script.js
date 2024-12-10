// assets/js/scripts.js

document.addEventListener('DOMContentLoaded', () => {
    const contactForm = document.querySelector('.contact-form');
    const successMessage = document.querySelector('.success-message');
    const errorMessage = document.querySelector('.error-message');

    contactForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission

        const formData = new FormData(contactForm);
        const data = Object.fromEntries(formData);

        fetch(contactForm.action, {
            method: contactForm.method,
            headers: {
                'Accept': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => {
            if (response.ok) {
                successMessage.style.display = 'block';
                errorMessage.style.display = 'none';
                contactForm.reset();
            } else {
                response.json().then(data => {
                    if (data.errors) {
                        errorMessage.innerHTML = data.errors.map(error => `<p>${error.message}</p>`).join('');
                    } else {
                        errorMessage.innerHTML = '<p>An error occurred. Please try again later.</p>';
                    }
                    errorMessage.style.display = 'block';
                    successMessage.style.display = 'none';
                });
            }
        })
        .catch(error => {
            console.error('Error:', error);
            errorMessage.innerHTML = '<p>An error occurred. Please try again later.</p>';
            errorMessage.style.display = 'block';
            successMessage.style.display = 'none';
        });
    });
});
