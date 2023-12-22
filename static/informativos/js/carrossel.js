$(document).ready(function () {
  const carrossel = $('.carrossel');
  const prevButton = $('.prev-button');
  const nextButton = $('.next-button');
  const dotsContainer = $('.dots-container');

  let currentIndex = 0;

  function updateCarousel() {
    carrossel.css('transform', `translateX(${-currentIndex * 100}%)`);
    updateDots();
  }

  function updateDots() {
    dotsContainer.children().removeClass('active');
    dotsContainer.children().eq(currentIndex).addClass('active');
  }

  function nextSlide() {
    currentIndex = (currentIndex + 1) % carrossel.children().length;
    updateCarousel();
  }

  function prevSlide() {
    currentIndex = (currentIndex - 1 + carrossel.children().length) % carrossel.children().length;
    updateCarousel();
  }

  // Adiciona eventos de clique aos botões
  prevButton.click(prevSlide);
  nextButton.click(nextSlide);

  for (let i = 0; i < carrossel.children().length; i++) {
    dotsContainer.append('<span class="dot"></span>');
  }

  dotsContainer.on('click', '.dot', function () {
    currentIndex = $(this).index();
    updateCarousel();
  });

  setInterval(nextSlide, 7000);
  
});