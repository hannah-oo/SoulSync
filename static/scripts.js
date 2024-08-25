let selectedHashtags = [];

function selectHashtag(element) {
    if (selectedHashtags.length < 3 || element.classList.contains('selected')) {
        element.classList.toggle('selected');
        const text = element.textContent;

        if (element.classList.contains('selected')) {
            selectedHashtags.push(text);
        } else {
            selectedHashtags = selectedHashtags.filter(tag => tag !== text);
        }
    }
    const proceedButton = document.getElementById('proceed');
    if (selectedHashtags.length === 3) {
        proceedButton.disabled = false;
        proceedButton.classList.add('active');
    } else {
        proceedButton.disabled = true;
        proceedButton.classList.remove('active');
    }
}

document.getElementById('proceed').addEventListener('click', () => {
    fetch('/save_rec_hashtags', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ hashtags: selectedHashtags }),
    })
    .then(response => response.json())
});

document.getElementById('countryDropdown').addEventListener('change', function() {
    if (this.value) {
        this.style.color = '#000'; 
    } else {
        this.style.color = '#808080';
    }
});