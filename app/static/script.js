document.addEventListener('DOMContentLoaded', () => {
    const urlForm = document.getElementById('url-form');
    const originalUrlInput = document.getElementById('original-url');
    const shortUrlInput = document.getElementById('short-url');
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
        // Select the shortened URL for copying
        shortUrlInput.select();
        // Use document.execCommand for broader browser compatibility
        document.execCommand('copy');
        copiedModal.show();
      });
    });
  });
  