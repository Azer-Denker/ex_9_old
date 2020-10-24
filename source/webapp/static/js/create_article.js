async function addPhoto(event) {
    event.preventDefault();
    let response = await makeRequest(BASE_API_URL + 'photo/create/', 'POST', {
        title: document.getElementById('id_title').value,
        text: document.getElementById('id_text').value
    });
    let data = await response.json();
    console.log(data.pk);
    window.location.href = `${BASE_URL}photo/${data.pk}/`;
}


window.addEventListener('load', function() {
    const form = document.forms['photo_create_form'];
    form.onsubmit = addPhoto;
});
