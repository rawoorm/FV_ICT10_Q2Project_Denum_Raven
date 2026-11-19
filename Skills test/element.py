from pyscript import document

# Dictionary containing the non-metal elements
# Each element has its name, symbol, atomic number, and atomic mass
elements = {
    "H": ('Hydrogen', 'H', 1, 1.008),
    "He": ('Helium', 'He', 2, 4.0026),
    "C": ('Carboon', 'C', 6, 12.011),
    "N": ('Nitrogen', 'N', 7, 14.007),
    "O": ('Oxygen', 'O', 8, 15.999),
    "F": ('Fluorine', 'F', 9, 18.998),
    "Ne": ('Neon', 'Ne', 10, 20.180),
    "P": ('Phosphorus', 'P', 15, 30.974),
    "S": ('Sulfur', 'S', 16, 32.06),
    "Cl": ('Chlorine', 'Cl', 17, 35.45),
    "Ar": ('Argon', 'Ar', 18, 39.948),
    "Se": ('Selenium', 'Se', 34, 78.971),
    "Br": ('Bromine', 'Br', 35, 79.904),
    "Kr": ('Krypton', 'Kr', 36, 83.798),
    "I": ('Iodine', 'I', 53, 126.904),
    "Xe": ('Xenon', 'Xe', 54, 131.293),
    "Rn": ('Radon', 'Rn', 86, 222)
}


# Function that runs when the search button is clicked
def search_element(event):

    # Get the user's input from the HTML text box
    # strip() removes unnecessary spaces
    # capitalize() fixes the capitalization of element symbols
    element1 = document.getElementById("element1").value.strip().capitalize()

    # Search for the entered symbol in the dictionary
    # If the symbol does not exist, display "Element not found"
    result = elements.get(
        element1,
        ('Element not found', '-', '-', '-')
    )

    # Display the element name in the HTML
    document.getElementById("element").innerText = result[0]

    # Display the chemical symbol in the HTML
    document.getElementById("symbol").innerText = result[1]

    # Display the atomic number in the HTML
    document.getElementById("atomicnumber").innerText = str(result[2])

    # Display the atomic mass in the HTML
    document.getElementById("atomicmass").innerText = str(result[3])
