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
    const reviewForm = document.querySelector('.review-form');
    const ratingInput = document.querySelector('input[name="rating"]');
  
    if (reviewForm && ratingInput) {
      const ratingStars = document.createElement('div');
      ratingStars.classList.add('rating-stars');
      
      // Create star rating interface with custom star characters
      const starCharacters = {
        empty: '☆',
        filled: '★'
      };
  
      for (let i = 1; i <= 5; i++) {
        const star = document.createElement('span');
        star.innerHTML = starCharacters.empty;
        star.classList.add('star');
        star.dataset.value = i;
        
        // Add hover animation
        star.addEventListener('mouseover', function() {
          this.style.transform = 'scale(1.2)';
        });
        
        star.addEventListener('mouseout', function() {
          this.style.transform = 'scale(1)';
        });
        
        ratingStars.appendChild(star);
      }
  
      // Insert stars before the hidden input
      ratingInput.parentNode.insertBefore(ratingStars, ratingInput);
      ratingInput.style.display = 'none';
  
      // Handle star rating clicks
      ratingStars.addEventListener('click', function(e) {
        if (e.target.classList.contains('star')) {
          const value = e.target.dataset.value;
          ratingInput.value = value;
          updateStars(value);
          
          // Add click animation
          e.target.style.transform = 'scale(0.8)';
          setTimeout(() => {
            e.target.style.transform = 'scale(1)';
          }, 100);
        }
      });
  
      // Handle star rating hover
      ratingStars.addEventListener('mouseover', function(e) {
        if (e.target.classList.contains('star')) {
          const value = e.target.dataset.value;
          updateStars(value, true);
        }
      });
  
      // Reset stars on mouseout
      ratingStars.addEventListener('mouseout', function() {
        updateStars(ratingInput.value);
      });
  
      function updateStars(value, isHover = false) {
        const stars = ratingStars.querySelectorAll('.star');
        stars.forEach((star, index) => {
          if (index < value) {
            star.innerHTML = starCharacters.filled;
            star.classList.add('filled');
            if (isHover) {
              star.style.transform = 'scale(1.1)';
            }
          } else {
            star.innerHTML = starCharacters.empty;
            star.classList.remove('filled');
            if (isHover) {
              star.style.transform = 'scale(1)';
            }
          }
        });
      }
  
      // Initialize with any existing value
      if (ratingInput.value) {
        updateStars(ratingInput.value);
      }
    }
  
    // Add smooth scroll for review section links
    document.querySelectorAll('a[href="#reviews"]').forEach(anchor => {
      anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector('#reviews').scrollIntoView({
          behavior: 'smooth'
        });
      });
    });
  });