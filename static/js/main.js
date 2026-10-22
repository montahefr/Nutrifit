
document.addEventListener("DOMContentLoaded", () => {
    // Mobile navigation
    const menuButton = document.querySelector(".menu-toggle");
    const navLinks = document.querySelector(".nav-links");

    if (menuButton && navLinks) {
        menuButton.addEventListener("click", () => {
            const isOpen = menuButton.getAttribute("aria-expanded") === "true";

            menuButton.setAttribute("aria-expanded", String(!isOpen));
            navLinks.classList.toggle("is-open", !isOpen);
        });

        navLinks.querySelectorAll("a").forEach((link) => {
            link.addEventListener("click", () => {
                navLinks.classList.remove("is-open");
                menuButton.setAttribute("aria-expanded", "false");
            });
        });
    }

    // Show or hide password
    document.querySelectorAll("[data-toggle-password]").forEach((button) => {
        button.addEventListener("click", () => {
            const input = document.getElementById(
                button.dataset.togglePassword
            );

            if (!input) return;

            const show = input.type === "password";
            input.type = show ? "text" : "password";
            button.textContent = show ? "Hide" : "Show";
            button.setAttribute(
                "aria-label",
                show ? "Hide password" : "Show password"
            );
        });
    });

    // Dismiss Django messages
    document.querySelectorAll(".message-close").forEach((button) => {
        button.addEventListener("click", () => {
            const message = button.closest(".message");
            if (message) message.remove();
        });
    });

    // Client-side confirmation for registration
    const registerForm = document.querySelector(
        'form[action$="/register/"]'
    );

    if (registerForm) {
        registerForm.addEventListener("submit", (event) => {
            const password = document.getElementById("password");
            const confirmPassword = document.getElementById("confirm_password");

            if (
                password &&
                confirmPassword &&
                password.value !== confirmPassword.value
            ) {
                event.preventDefault();
                confirmPassword.setCustomValidity("Passwords do not match.");
                confirmPassword.reportValidity();
            }
        });

        const confirmPassword = document.getElementById("confirm_password");

        if (confirmPassword) {
            confirmPassword.addEventListener("input", () => {
                confirmPassword.setCustomValidity("");
            });
        }
    }
});
