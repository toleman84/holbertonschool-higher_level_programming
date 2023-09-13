const request = new XMLHttpRequest();
request.open('GET', 'https://hellosalut.stefanbohacek.dev/?lang=fr');
request.setRequestHeader('Accept', 'application/json');
request.send();
request.addEventListener('load', function() {
    if (request.status === 200) {
        const data = JSON.parse(request.responseText);
        const hello = data.hello;
        document.getElementById('hello').innerHTML = hello;
    } else {
        console.error('An error occurred while fetching the data:', request.status);
    }
});
