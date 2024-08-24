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

document.getElementById('countryDropdown').addEventListener('change', function() {
    if (this.value) {
        this.style.color = '#000'; 
    } else {
        this.style.color = '#808080';
    }
});

// List of countries with coordinates
var countries = [
    { country: "United States", lat: 37.0902, lon: -95.7129, value: 50 },
    { country: "Canada", lat: 56.1304, lon: -106.3468, value: 30 },
    { country: "Brazil", lat: -14.2350, lon: -51.9253, value: 20 },
    { country: "Australia", lat: -25.2744, lon: 133.7751, value: 25 },
    { country: "India", lat: 20.5937, lon: 78.9629, value: 40 },
    { country: "China", lat: 35.8617, lon: 104.1954, value: 60 },
    { country: "Germany", lat: 51.1657, lon: 10.4515, value: 45 },
    { country: "South Africa", lat: -30.5595, lon: 22.9375, value: 35 },
    { country: "Russia", lat: 61.5240, lon: 105.3188, value: 55 },
    { country: "Japan", lat: 36.2048, lon: 138.2529, value: 65 },
    { country: "United Kingdom", lat: 55.3781, lon: -3.4360, value: 50 },
    { country: "France", lat: 46.6034, lon: 1.8883, value: 45 },
    { country: "Italy", lat: 41.8719, lon: 12.5674, value: 40 },
    { country: "Spain", lat: 40.4637, lon: -3.7038, value: 35 },
    { country: "Mexico", lat: 23.6345, lon: -102.5528, value: 25 },
    { country: "Indonesia", lat: -0.7893, lon: 113.9213, value: 20 },
    { country: "Saudi Arabia", lat: 23.8859, lon: 45.0792, value: 30 },
    { country: "Turkey", lat: 38.9637, lon: 35.2433, value: 35 },
    { country: "Argentina", lat: -38.4161, lon: -63.6167, value: 20 },
    { country: "Egypt", lat: 26.8206, lon: 30.8025, value: 25 },
    { country: "Iran", lat: 32.4279, lon: 53.6880, value: 30 },
    { country: "Thailand", lat: 15.8700, lon: 100.9925, value: 25 },
    { country: "Vietnam", lat: 14.0583, lon: 108.2772, value: 20 },
    { country: "Poland", lat: 51.9194, lon: 19.1451, value: 40 },
    { country: "Netherlands", lat: 52.1326, lon: 5.2913, value: 45 },
    { country: "Sweden", lat: 60.1282, lon: 18.6435, value: 40 },
    { country: "Belgium", lat: 50.8503, lon: 4.3517, value: 35 },
    { country: "Switzerland", lat: 46.8182, lon: 8.2275, value: 50 },
    { country: "Austria", lat: 47.5162, lon: 14.5501, value: 40 },
    { country: "Norway", lat: 60.4720, lon: 8.4689, value: 35 },
    { country: "Ireland", lat: 53.4129, lon: -8.2439, value: 30 },
    { country: "Portugal", lat: 39.3999, lon: -8.2245, value: 25 },
    { country: "New Zealand", lat: -40.9006, lon: 174.8860, value: 20 },
    { country: "South Korea", lat: 35.9078, lon: 127.7669, value: 55 },
    { country: "Singapore", lat: 1.3521, lon: 103.8198, value: 60 },
    { country: "Malaysia", lat: 4.2105, lon: 101.9758, value: 25 },
    { country: "Philippines", lat: 12.8797, lon: 121.7740, value: 20 },
    { country: "Pakistan", lat: 30.3753, lon: 69.3451, value: 30 },
    { country: "Bangladesh", lat: 23.6858, lon: 90.3563, value: 25 },
    { country: "Colombia", lat: 4.5709, lon: -74.2973, value: 20 },
    { country: "Chile", lat: -35.6751, lon: -71.5430, value: 25 },
    { country: "Peru", lat: -9.1900, lon: -75.0152, value: 20 }
];
