
 <!-- JS SCRIPT -->

      const cardTitles = document.querySelectorAll('.card-title');
      cardTitles.forEach(cardTitle => {
        cardTitle.addEventListener('click', () => {
          const cardText = cardTitle.nextElementSibling;
          if (cardText.style.display === 'none') {
            cardText.style.display = 'block';
          } else {
            cardText.style.display = 'none';
          }
        });
      });
