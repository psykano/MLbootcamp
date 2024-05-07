document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');

    form.addEventListener('submit', function(event) {
        const categoriesInput = document.querySelector('input[name="categories"]').value;
        const valuesInput = document.querySelector('input[name="values"]').value;

        if (!isValidInput(categoriesInput) || !isValidInput(valuesInput)) {
            alert('Make sure both categories and values are comma-separated lists.');
            
            // Prevent form from submitting
            event.preventDefault();
        }
    });

    // Checks if input is not empty and contains at least one comma
    function isValidInput(input) {
        return input.trim() !== '' && input.includes(',');
    }
});