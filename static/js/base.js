window.addEventListener('load', function() {

	// setTimeout to simulate the delay from a real page load
	setTimeout(lazyLoad, 1000);

});

function lazyLoad() {
	var card_images = document.querySelectorAll('.card-image');

	// loop over each card image
	card_images.forEach(function(card_image) {
		var image_url = card_image.getAttribute('data-image-full');
		var content_image = card_image.querySelector('img');

		// change the src of the content image to load the new high res photo
		content_image.src = image_url;

		// listen for load event when the new photo is finished loading
		content_image.addEventListener('load', function() {
			// swap out the visible background image with the new fully downloaded photo
			card_image.style.backgroundImage = 'url(' + image_url + ')';
			// add a class to remove the blur filter to smoothly transition the image change
			card_image.className = card_image.className + ' is-loaded';
		});

	});

}


        const menuBtn = document.querySelector(".menu-icon span");
        const searchBtn = document.querySelector(".search-icon");
        const cancelBtn = document.querySelector(".cancel-icon");
        const items = document.querySelector(".nav-items");
        const form = document.querySelector("form");
        menuBtn.onclick = ()=>{
          items.classList.add("active");
          menuBtn.classList.add("hide");
          searchBtn.classList.add("hide");
          cancelBtn.classList.add("show");
        }
        cancelBtn.onclick = ()=>{
          items.classList.remove("active");
          menuBtn.classList.remove("hide");
          searchBtn.classList.remove("hide");
          cancelBtn.classList.remove("show");
          form.classList.remove("active");
          cancelBtn.style.color = "#ff3d00";
        }
        searchBtn.onclick = ()=>{
          form.classList.add("active");
          searchBtn.classList.add("hide");
          cancelBtn.classList.add("show");
        }