let materialSelect = document.getElementById('material-select');
let materialTable = document.getElementById('display-info');

if (window.location.href === 'http://localhost:5000/') {
    materialTable.style.display = 'none';
}

materialSelect.addEventListener('change', function() {
    if (materialSelect.value === 'PLA') {
        document.location.href = '/PLA'
    } else if (materialSelect.value === 'ABS') {
        document.location.href = '/ABS'
    } else {
        document.location.href = '/'
    }
});
