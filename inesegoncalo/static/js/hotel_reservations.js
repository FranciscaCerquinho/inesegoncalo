function generateHotelReservationsCSV() {
    $.getJSON('/api/to_csv/hotel_reservations',
        function (data) {
            downloadHotelReservationsFile('/static/data/csv/hotel_reservations.csv');
        });
}

function downloadHotelReservationsFile(filename) {
    const link = document.createElement("a");
    link.download = 'hotel_reservations.csv';
    link.style.display = "none";
    link.href = filename;

    document.body.appendChild(link);
    link.click();

    setTimeout(() => {
        URL.revokeObjectURL(link.href);
        link.parentNode.removeChild(link);
    }, 0);
}

