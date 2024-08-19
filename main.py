# Simple Crop and Soil Management System

# Function to recommend a crop based on soil pH, rainfall, and temperature
def recommend_crop(ph, rainfall, temperature):
    if 6.0 <= ph <= 7.5 and 500 <= rainfall <= 1000 and 15 <= temperature <= 25:
        return "Wheat"
    elif 5.5 <= ph <= 6.5 and 1000 <= rainfall <= 2000 and 20 <= temperature <= 30:
        return "Rice"
    elif 6.0 <= ph <= 7.0 and 600 <= rainfall <= 1200 and 20 <= temperature <= 30:
        return "Maize"
    else:
        return "No suitable crop found for the given conditions."

# Function to provide basic soil management advice
def soil_management(soil_type):
    if soil_type.lower() == "sandy":
        return "Add organic matter to improve nutrient and water retention."
    elif soil_type.lower() == "clay":
        return "Consider raised beds to improve drainage. Add organic matter."
    elif soil_type.lower() == "loamy":
        return "This is ideal soil. Maintain fertility with organic matter."
    elif soil_type.lower() == "silt":
        return "Manage drainage carefully and add organic matter to improve structure."
    else:
        return "No advice available for this soil type."

# Function to identify a simple disease based on a single symptom
def identify_disease(symptom):
    if symptom.lower() == "yellow leaves":
        return "Nitrogen Deficiency"
    elif symptom.lower() == "wilting":
        return "Root Rot"
    elif symptom.lower() == "stunted growth":
        return "Phosphorus Deficiency"
    elif symptom.lower() == "leaf spots":
        return "Leaf Spot Disease"
    else:
        return "No disease identified for the given symptom."

# Main function to interact with the user
def main():
    print("Welcome to the Simple Crop and Soil Management System")

    # Collect user inputs
    soil_type = input("Enter your soil type (Sandy, Clay, Loamy, Silt): ")
    ph = float(input("Enter the soil pH: "))
    rainfall = float(input("Enter the annual rainfall (in mm): "))
    temperature = float(input("Enter the average temperature (in °C): "))
    symptom = input("Enter observed symptom in crops (e.g., Yellow Leaves): ")

    # Recommend a crop
    crop = recommend_crop(ph, rainfall, temperature)
    print(f"\nRecommended crop: {crop}")

    # Provide soil management advice
    advice = soil_management(soil_type)
    print(f"Soil management advice: {advice}")

    # Identify a disease
    disease = identify_disease(symptom)
    print(f"Identified disease: {disease}")

if __name__ == "__main__":
    main()