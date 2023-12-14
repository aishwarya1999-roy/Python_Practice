from geopy.distance import great_circle

# Define your list of places with their names and coordinates (latitude, longitude).
places = [
    {"name": "Barisha Club Puja", "location": (22.48143265613953, 88.31286168170489)},
    {"name": "Behala Sree Sangha", "location": (22.498065811239726, 88.3200640393802)},
    {"name": "Suruchi Sangha", "location": (22.50924134520332, 88.33403852959287)},
    # Add more places as needed.
]

# Function to calculate distance between two coordinates.
def calculate_distance(coord1, coord2):
    return great_circle(coord1, coord2).kilometers

# Function to sort places based on distance from a reference point.
def sort_places_by_distance(reference_coord, place_list):
    return sorted(place_list, key=lambda place: calculate_distance(reference_coord, place['location']))

# Example: Sorting places based on the reference location (e.g., user's current location).
reference_location = (22.52490423627308, 88.34609923095552)
sorted_places = sort_places_by_distance(reference_location, places)

# Now, 'sorted_places' is a list of places sorted by distance.
for place in sorted_places:
    print(f"{place['name']}: {calculate_distance(reference_location, place['location'])} kilometers")
