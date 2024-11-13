// shrink header when scroll
const header = document.querySelector('header');
window.addEventListener('scroll', () => {
    if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
        header.classList.add('shrink');
    } else {
        header.classList.remove('shrink');
    }
})

document.addEventListener('DOMContentLoaded', function() {
    const scrollBtn = document.getElementById('scrollTopBtn');
    
    scrollBtn.addEventListener('click', function(e) {
        e.preventDefault();
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const downloadButtons = document.querySelectorAll('.btn-download');
    
    downloadButtons.forEach(button => {
      button.addEventListener('click', function(e) {
        // Prevent default action
        e.preventDefault();
        
        // Show loading state
        const originalText = this.textContent;
        this.innerHTML = `
          <svg class="animate-spin" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="12" cy="12" r="10"></circle>
            <path d="M16 12a4 4 0 1 1-8 0"></path>
          </svg>
          Descargando...
        `;
        
        // Simulate download (replace with actual download logic if needed)
        setTimeout(() => {
          // Restore original text and redirect
          this.innerHTML = originalText;
          window.location.href = this.href;
        }, 1500);
      });
    });
  });

  document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.btn-wraper button').forEach(button => {
        button.addEventListener('click', function() {
            const cakeId = this.getAttribute('data-cake-id');  // Obtén el ID del pastel
            const url = this.getAttribute('data-url');  // Obtén la URL base de `add_to_cart`

            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')  // Obtiene el token CSRF correctamente
                },
                body: JSON.stringify({ cake_id: cakeId, quantity: 1 })  // Asegúrate de enviar `cake_id` como JSON
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert(data.message);
                } else {
                    alert("Failed to add cake to cart.");
                }
            })
            .catch(error => console.error('Error:', error));
        });
    });
});

// Función para obtener el token CSRF desde las cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
