document.addEventListener("DOMContentLoaded", () => {
    const menuToggle = document.getElementById("menu-toggle");
    const navMenu = document.getElementById("nav-menu");

    if (menuToggle && navMenu) {
        menuToggle.addEventListener("click", () => {
            const isOpen = navMenu.classList.toggle("active");
            menuToggle.setAttribute("aria-expanded", String(isOpen));
        });

        navMenu.querySelectorAll("a").forEach((link) => {
            link.addEventListener("click", () => {
                navMenu.classList.remove("active");
                menuToggle.setAttribute("aria-expanded", "false");
            });
        });
    }

    const contactForm = document.querySelector(".contact-form");
    if (contactForm) {
        contactForm.addEventListener("submit", (event) => {
            const requiredFields = contactForm.querySelectorAll("[required]");
            let hasError = false;

            requiredFields.forEach((field) => {
                if (!field.value.trim()) {
                    hasError = true;
                    field.setAttribute("aria-invalid", "true");
                } else {
                    field.removeAttribute("aria-invalid");
                }
            });

            const email = contactForm.querySelector('input[type="email"]');
            if (email && email.value.trim() && !email.checkValidity()) {
                hasError = true;
                email.setAttribute("aria-invalid", "true");
            }

            if (hasError) {
                event.preventDefault();
                alert("Please fill out the required fields with valid details.");
            }
        });
    }

    const galleryButtons = Array.from(document.querySelectorAll("[data-lightbox-src]"));
    const lightbox = document.getElementById("lightbox");
    const lightboxImage = lightbox ? lightbox.querySelector(".lightbox-image") : null;
    const closeButton = lightbox ? lightbox.querySelector(".lightbox-close") : null;
    const prevButton = lightbox ? lightbox.querySelector(".lightbox-prev") : null;
    const nextButton = lightbox ? lightbox.querySelector(".lightbox-next") : null;
    let currentIndex = 0;

    function showImage(index) {
        if (!lightbox || !lightboxImage || galleryButtons.length === 0) {
            return;
        }

        currentIndex = (index + galleryButtons.length) % galleryButtons.length;
        const activeButton = galleryButtons[currentIndex];
        lightboxImage.src = activeButton.dataset.lightboxSrc;
        lightboxImage.alt = activeButton.dataset.lightboxAlt || "";
        lightbox.classList.add("active");
        lightbox.setAttribute("aria-hidden", "false");
        document.body.style.overflow = "hidden";
    }

    function closeLightbox() {
        if (!lightbox || !lightboxImage) {
            return;
        }

        lightbox.classList.remove("active");
        lightbox.setAttribute("aria-hidden", "true");
        lightboxImage.src = "";
        document.body.style.overflow = "";
    }

    galleryButtons.forEach((button, index) => {
        button.addEventListener("click", () => showImage(index));
    });

    if (closeButton) {
        closeButton.addEventListener("click", closeLightbox);
    }

    if (prevButton) {
        prevButton.addEventListener("click", () => showImage(currentIndex - 1));
    }

    if (nextButton) {
        nextButton.addEventListener("click", () => showImage(currentIndex + 1));
    }

    if (lightbox) {
        lightbox.addEventListener("click", (event) => {
            if (event.target === lightbox) {
                closeLightbox();
            }
        });
    }

    document.addEventListener("keydown", (event) => {
        if (!lightbox || !lightbox.classList.contains("active")) {
            return;
        }

        if (event.key === "Escape") {
            closeLightbox();
        }

        if (event.key === "ArrowLeft") {
            showImage(currentIndex - 1);
        }

        if (event.key === "ArrowRight") {
            showImage(currentIndex + 1);
        }
    });
});
