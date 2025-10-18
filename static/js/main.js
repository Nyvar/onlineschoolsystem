function loadPage(pageName) {
    alert("halooo")
fetch(`/instructors/load/${pageName}/`)
    .then(response => response.text())
    .then(html => {
    document.getElementById('main-content').innerHTML = html;
    })
    .catch(error => {
    console.error('Error loading page:', error);
    });
}