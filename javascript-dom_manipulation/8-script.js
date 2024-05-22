document.addEventListener("DOMContentLoaded", (event) => {
    const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
    const hello = document.getElementById('hello');
    
    fetch(apiUrl)
        .then((response) => {
            return response.json()
        })
    
        .then((data) => {
            const salut = data.hello;
            const str = document.createElement('p');
            str.textContent = salut;
            hello.appendChild(str);
        })});
