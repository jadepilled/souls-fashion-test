// Function to update the outfit simulator content in the collapsible panel
function updateOutfitSimulatorContent() {
    const outfits = JSON.parse(localStorage.getItem("outfits")) || Array(10).fill({});
    const content = document.getElementById("outfitSimulatorContent");
    content.innerHTML = "";

    outfits.forEach((outfit, index) => {
        const outfitDiv = document.createElement("div");
        outfitDiv.classList.add("outfit");
        outfitDiv.textContent = `Preset ${index + 1}`;
        
        for (const itemType in outfit) {
            const itemDiv = document.createElement("div");
            itemDiv.textContent = `${itemType}: ${outfit[itemType].name}`;
            outfitDiv.appendChild(itemDiv);
        }
        content.appendChild(outfitDiv);
    });
}

// Function to toggle the display of the Outfit Simulator panel
function toggleOutfitSimulator() {
    const content = document.getElementById("outfitSimulatorContent");
    content.style.display = content.style.display === "none" ? "block" : "none";
}

// Clear all outfits function
function clearOutfits() {
    localStorage.setItem("outfits", JSON.stringify(Array(10).fill({})));
    updateOutfitSimulatorContent();
}
