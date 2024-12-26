const lengthUnits = ["millimeter", "centimeter", "meter", "kilometer", "inch", "foot", "yard", "mile"];
const weightUnits = ["milligram", "gram", "kilogram", "ounce", "pound"];
const temperatureUnits = ["Celsius", "Fahrenheit", "Kelvin"];

function populateSelectBoxes() {
    const fromSelect = document.getElementById("fromSelect");
    const toSelect = document.getElementById("toSelect");
    const unitType = document.getElementById("fromUnit").value;

    fromSelect.innerHTML = '';
    toSelect.innerHTML = '';

    let units = [];
    switch (unitType) {
        case "length":
            units = lengthUnits;
            break;
        case "weight":
            units = weightUnits;
            break;
        case "temperature":
            units = temperatureUnits;
            break;
    }

    units.forEach(unit => {
        const optionFrom = document.createElement("option");
        optionFrom.value = unit;
        optionFrom.textContent = unit;
        
        const optionTo = document.createElement("option");
        optionTo.value = unit;
        optionTo.textContent = unit;

        fromSelect.appendChild(optionFrom);
        toSelect.appendChild(optionTo);
    });
}

function convert() {
    const value = parseFloat(document.getElementById("valueInput").value);
    const fromUnit = document.getElementById("fromSelect").value;
    const toUnit = document.getElementById("toSelect").value;
    const resultElement = document.getElementById("result");

    let convertedValue;

    if (fromUnit === toUnit) {
        convertedValue = value;
    } else if (lengthUnits.includes(fromUnit) && lengthUnits.includes(toUnit)) {
        convertedValue = convertLength(value, fromUnit, toUnit);
    } else if (weightUnits.includes(fromUnit) && weightUnits.includes(toUnit)) {
        convertedValue = convertWeight(value, fromUnit, toUnit);
    } else if (temperatureUnits.includes(fromUnit) && temperatureUnits.includes(toUnit)) {
        convertedValue = convertTemperature(value, fromUnit, toUnit);
    } else {
        convertedValue = "Conversion not supported.";
    }

    resultElement.textContent = convertedValue;
}

function convertLength(value, fromUnit, toUnit) {
    const lengthConversions = {
        "millimeter": 0.001,
        "centimeter": 0.01,
        "meter": 1,
        "kilometer": 1000,
        "inch": 0.0254,
        "foot": 0.3048,
        "yard": 0.9144,
        "mile": 1609.34,
    };

    const meters = value * lengthConversions[fromUnit];
    return meters / lengthConversions[toUnit];
}

function convertWeight(value, fromUnit, toUnit) {
    const weightConversions = {
        "milligram": 0.001,
        "gram": 1,
        "kilogram": 1000,
        "ounce": 28.3495,
        "pound": 453.592,
    };

    const grams = value * weightConversions[fromUnit];
    return grams / weightConversions[toUnit];
}

function convertTemperature(value, fromUnit, toUnit) {
    if (fromUnit === "Celsius") {
        if (toUnit === "Fahrenheit") return (value * 9/5) + 32;
        if (toUnit === "Kelvin") return value + 273.15;
    } else if (fromUnit === "Fahrenheit") {
        if (toUnit === "Celsius") return (value - 32) * 5/9;
        if (toUnit === "Kelvin") return (value - 32) * 5/9 + 273.15;
    } else if (fromUnit === "Kelvin") {
        if (toUnit === "Celsius") return value - 273.15;
        if (toUnit === "Fahrenheit") return (value - 273.15) * 9/5 + 32;
    }
    
    return value; // If conversion is not needed
}

document.getElementById("fromUnit").addEventListener("change", populateSelectBoxes);
window.onload = populateSelectBoxes;