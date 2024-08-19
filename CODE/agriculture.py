import json
import os

CROP_DATA_FILE = 'crop_data.json'
CODE_DIR = os.path.join(os.path.dirname(__file__), 'DATA')
file_path = os.path.join(CODE_DIR, CROP_DATA_FILE)

def initialize_file():
    os.makedirs(CODE_DIR, exist_ok=True)
    if not os.path.isfile(file_path):
        with open(file_path, 'w') as file:
            json.dump([], file)

def load_data():
    if not os.path.isfile(file_path):
        return []
    with open(file_path, 'r') as file:
        return json.load(file)

def save_data(data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def add_crop_data():
    crop_data = load_data()

    crop_name = input("Enter the crop name: ").strip()
    soil_type = input("Enter the soil type: ").strip()
    disease = input("Enter the disease affecting the crop (if any): ").strip()
    date = input("Enter the date of observation (YYYY-MM-DD): ").strip()

    new_crop = {
        'crop_name': crop_name,
        'soil_type': soil_type,
        'disease': disease if disease else "No disease reported",
        'date': date
    }

    crop_data.append(new_crop)
    save_data(crop_data)
    print(f"Crop data for {crop_name} added successfully.")

def provide_recommendations():
    crop_data = load_data()
    soil_type = input("Enter the soil type to get crop recommendations: ").strip()

    recommendations = [crop for crop in crop_data if crop['soil_type'] == soil_type]

    if recommendations:
        print(f"Crop recommendations for soil type '{soil_type}':")
        for crop in recommendations:
            print(f" - {crop['crop_name']} (Disease: {crop['disease']}, Date: {crop['date']})")
    else:
        print("No data for crop recommendation for this soil.")

def list_all_crops():
    crop_data = load_data()

    if crop_data:
        print("All crops in the database:")
        for crop in crop_data:
            print(f" - {crop['crop_name']} (Soil Type: {crop['soil_type']}, Disease: {crop['disease']}, Date: {crop['date']})")
    else:
        print("No crop data available.")

initialize_file()

while True:
    print("\nCrop Management System")
    print("1. Add Crop Data")
    print("2. Provide Crop Recommendations")
    print("3. List All Crops")
    print("4. Exit")
    choice = input("Enter your choice: ").strip()

    if choice == '1':
        add_crop_data()
    elif choice == '2':
        provide_recommendations()
    elif choice == '3':
        list_all_crops()
    elif choice == '4':
        print("Exiting the system.")
        break
    else:
        print("Invalid choice. Please try again.")
