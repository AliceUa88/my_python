function updateRatingStars(ratingDiv) {
  const rating = parseFloat(ratingDiv.getAttribute('data-rating')) || 0;
  const stars = ratingDiv.querySelectorAll('.star');
 
  stars.forEach((star, index) => {
    const starNumber = index + 1;
   
    if (rating >= starNumber) {
      star.classList.add('full');
      star.style.background = 'none';
    } else if (rating > starNumber - 1) {
      const fillPercent = (rating - (starNumber - 1)) * 100;
      star.style.background = `linear-gradient(90deg, #ffc107 ${fillPercent}%, #ddd ${fillPercent}%)`;
      star.style.webkitBackgroundClip = 'text';
      star.style.webkitTextFillColor = 'transparent';
      star.style.backgroundClip = 'text';
    } else {
      star.classList.remove('full');
      star.style.background = 'none';
    }
  });
}


document.addEventListener('DOMContentLoaded', function() {
document.querySelectorAll('.rating').forEach(updateRatingStars);
});
