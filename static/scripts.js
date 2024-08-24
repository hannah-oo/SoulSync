document.getElementById('countryDropdown').addEventListener('change', function() {
    if (this.value) {
        this.style.color = '#000'; // Change text color to black when a value is selected
    } else {
        this.style.color = '#808080'; // Default color for placeholder
    }
});

