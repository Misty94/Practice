
function openPopup() {
    document.getElementById('popupContainer').style.display='block';
    // document.getElementById('overlay').style.display='none'; This made it regular - the popup appeared, but nothing was blurred.
    document.getElementById('overlay').style.display='block'; // This made the background behind the popup blurred!!!
}

function closePopup() {
    document.getElementById('popupContainer').style.display='none';
    document.getElementById('overlay').style.display='none';
}