// On sélectionne le bouton et la zone de texte
const bouton = document.getElementById('btn-cagnotter');
const affichageCagnotte = document.getElementById('montant-cagnotte');

// On écoute le clic sur le bouton
bouton.addEventListener('click', () => {
    
    // On envoie une requête POST invisible à notre API Flask
    fetch('/api/cagnotte?montant=50&devise=euro', { method: 'GET' })
        .then(response => response.json()) // On transforme la réponse en JSON
        .then(data => {
            // On met à jour le texte à l'écran avec la nouvelle valeur reçue de Flask
            affichageCagnotte.textContent = data.cagnotte + data.devise;
        })
        .catch(error => console.error("Erreur avec l'API :", error))
        
});
