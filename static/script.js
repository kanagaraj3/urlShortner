document.addEventListener('DOMContentLoaded', () => {
    const urlForm = document.getElementById('url-form');
    const originalUrlInput = document.getElementById('original-url');
    const shortUrlInput = document.getElementById('short-url');
    const clearButton = document.getElementById('clear-button');
    const copiedModal = new bootstrap.Modal(document.getElementById('copiedModal'));

    urlForm.addEventListener('submit', (event) => {
        event.preventDefault();

        const originalUrl = originalUrlInput.value;
        fetch('/shorten', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `original_url=${encodeURIComponent(originalUrl)}`,
        })
        .then(response => response.json())
        .then(data => {
            shortUrlInput.value = data.short_url;
        });
    });

    clearButton.addEventListener('click', () => {
        originalUrlInput.value = '';
        shortUrlInput.value = '';
    });

    shortUrlInput.addEventListener('click', () => {
        shortUrlInput.select();
        document.execCommand('copy');
        copiedModal.show();
    });
});
