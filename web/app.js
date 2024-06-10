document.getElementById('prediction-form').addEventListener('submit', async function(e) {
    e.preventDefault();

    const formData = {
        Lattitude: parseFloat(document.getElementById('latitude').value),
        Longitude: parseFloat(document.getElementById('longitude').value),
        number_of_bedrooms: parseInt(document.getElementById('bedrooms').value),
        number_of_bathrooms: parseFloat(document.getElementById('bathrooms').value),
        living_area: parseInt(document.getElementById('living_area').value),
        lot_area: parseInt(document.getElementById('lot_area').value),
        number_of_floors: parseFloat(document.getElementById('floors').value),
        waterfront_present: parseInt(document.getElementById('waterfront').value),
        number_of_views: parseInt(document.getElementById('views').value),
        condition_of_the_house: parseInt(document.getElementById('condition').value),
        grade_of_the_house: parseInt(document.getElementById('grade').value),
        area_of_the_house_excluding_basement: parseInt(document.getElementById('house_area').value),
        area_of_the_basement: parseInt(document.getElementById('basement_area').value),
        built_year: parseInt(document.getElementById('built_year').value),
        renovation_year: parseInt(document.getElementById('renovation_year').value),
        postal_code: parseInt(document.getElementById('postal_code').value),
        living_area_renov: parseInt(document.getElementById('living_area_renov').value),
        lot_area_renov: parseInt(document.getElementById('lot_area_renov').value),
        number_of_schools_nearby: parseInt(document.getElementById('schools_nearby').value),
        distance_from_the_airport: parseInt(document.getElementById('airport_distance').value)
    };

    try {
        const response = await fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });

        const result = await response.json();
        document.getElementById('result').innerText = `Predicted Price: ${result.predicted_price}`;
    } catch (error) {
        document.getElementById('result').innerText = 'Error: Unable to get prediction';
        console.error('Error:', error);
    }
});
