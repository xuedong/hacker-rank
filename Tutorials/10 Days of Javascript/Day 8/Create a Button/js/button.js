var button = document.createElement('Button');

button.id = 'btn';
button.innerHTML = '0';
document.body.appendChild(button);

button.onclick = function() {
    button.innerHTML++;
}

