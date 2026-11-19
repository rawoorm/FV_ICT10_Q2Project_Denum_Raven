from pyscript import document

# Predefined members for each grade level
grade7 = {
    "ALICE BLUE",
    "ANITA BATH",
    "BILLY SPARKS",
    "ELLE VATOR"
}

grade8 = {
    "PAIGE TURNER",
    "JOE KERR",
    "FRANCISCO PORTERO"
}

grade9 = {
    "JUANITO LAKARIN",
    "JUSTIN CASE",
    "TAM NGUYEN"
}

grade10 = {
    "LIGAYA ANONUEVO",
    "SHELTON COOPER",
    "RESTYUTO FRUTO"
}

# Combine all grade-level sets into one master set
all_members = grade7 | grade8 | grade9 | grade10


# Function to add a new club member
def add_member(event=None):
    global all_members

    # Get the first and last name
    first = document.getElementById("first_name").value.strip()
    last = document.getElementById("last_name").value.strip()

    # Combine and format the full name
    new_member = (first + " " + last).upper().strip()

    # Add the new member using set union
    all_members = all_members | {new_member}

    # Sort and join all members alphabetically
    members_list = "<br>".join(sorted(all_members))

    # Display the complete member list
    document.getElementById("members").innerHTML = f"{members_list}"

    # Display the total number of members
    document.getElementById("total").innerHTML = f"TOTAL MEMBERS: {len(all_members)}"

    # Display confirmation message
    document.getElementById("message").innerHTML = f"Successfully added: {new_member}"