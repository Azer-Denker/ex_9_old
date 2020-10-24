async function onChosen(event) {
    event.preventDefault();
    let chosenBtn = event.target;
    let url = chosenBtn.href;

    try {
        let response = await makeRequest(url, 'POST');
        let data = await response.text();
        console.log(data);
        const counter = chosenBtn.parentElement.getElementsByClassName('counter')[0];
        counter.innerText = data;
    }
    catch (error) {
        console.log(error);
    }

    chosenBtn.classList.add('hidden');
    const unlikeBtn = chosenBtn.parentElement.getElementsByClassName('not_chosen')[0];
    unlikeBtn.classList.remove('hidden');
}

async function onUnlike(event) {
    event.preventDefault();
    let not_chosenBtn = event.target;
    let url = unot_chosenBtn.href;

    try {
        let response = await makeRequest(url, 'DELETE');
        let data = await response.text();
        console.log(data);
        const counter = not_chosenBtn.parentElement.getElementsByClassName('counter')[0];
        counter.innerText = data;
    }
    catch (error) {
        console.log(error);
    }

    not_chosenBtn.classList.add('hidden');
    const chosenBtn = not_chosenBtn.parentElement.getElementsByClassName('chosen')[0];
    chosenBtn.classList.remove('hidden');
}

window.addEventListener('load', function() {
    const chosenButtons = document.getElementsByClassName('chosen');
    const not_chosenButtons = document.getElementsByClassName('not_chosen');

    for (let btn of chosenButtons) {btn.onclick = onchosen}
    for (let btn of not_chosenButtons) {btn.onclick = onNot_Chosen}
});
