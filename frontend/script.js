document.getElementById('fetchBtn').addEventListener('click', async () => {
    const userId = 1; // Example user
    const response = await fetch(`/recommendations/${userId}`);
    const data = await response.json();

    const recDiv = document.getElementById('recommendations');
    recDiv.innerHTML = `<p>Recommended Movies: ${data.recommendations}</p>`;
});