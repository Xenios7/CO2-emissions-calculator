import matplotlib.pyplot as plt

def get_user_input():
    """
    Get user input for transportation, energy usage, and diet type.
    Ensures valid inputs are provided.
    """
    print("Welcome to the Carbon Footprint Calculator!")
    
    transport_options = {'car', 'bus', 'train'}
    diet_options = {'vegan', 'vegetarian', 'meat-based'}

    # Validate transportation type
    while True:
        transport_type = input("Enter transportation type (car, bus, train): ").lower()
        if transport_type in transport_options:
            break
        print("Invalid choice! Please enter car, bus, or train.")

    # Validate numeric inputs
    while True:
        try:
            distance = float(input("Enter distance traveled (in km): "))
            if distance < 0:
                raise ValueError("Distance must be non-negative.")
            break
        except ValueError:
            print("Invalid input! Please enter a valid number for distance.")

    while True:
        try:
            energy_usage = float(input("Enter energy consumption (in kWh): "))
            if energy_usage < 0:
                raise ValueError("Energy usage must be non-negative.")
            break
        except ValueError:
            print("Invalid input! Please enter a valid number for energy usage.")

    # Validate diet type
    while True:
        diet_type = input("Enter diet type (vegan, vegetarian, meat-based): ").lower()
        if diet_type in diet_options:
            break
        print("Invalid choice! Please enter vegan, vegetarian, or meat-based.")

    return transport_type, distance, energy_usage, diet_type


def calculate_transport_emissions(transport_type, distance):
    """
    Calculate emissions from transportation based on type and distance.
    """
    factors = {'car': 0.21, 'bus': 0.10, 'train': 0.05}  # CO2 emissions per km (in kg)
    return factors.get(transport_type, 0) * distance


def calculate_energy_emissions(energy_usage):
    """
    Calculate emissions from energy usage based on kWh consumed.
    """
    factor = 0.5  # Average CO2 emissions per kWh (in kg)
    return energy_usage * factor


def calculate_diet_emissions(diet_type):
    """
    Calculate emissions from food choices based on diet type.
    """
    factors = {'vegan': 2.0, 'vegetarian': 3.0, 'meat-based': 7.0}  # Daily CO2 emissions (in kg)
    return factors.get(diet_type, 0)


def display_results(transport_emissions, energy_emissions, diet_emissions):
    """
    Display the calculated emissions and total carbon footprint.
    """
    total_emissions = transport_emissions + energy_emissions + diet_emissions
    print("\n--- Your Carbon Footprint ---")
    print(f"Transportation: {transport_emissions:.2f} kg CO2")
    print(f"Energy Usage: {energy_emissions:.2f} kg CO2")
    print(f"Food Choices: {diet_emissions:.2f} kg CO2")
    print(f"Total Emissions: {total_emissions:.2f} kg CO2")

    print("\nTo reduce your footprint, consider:")
    print("- Using public transport, carpooling, or electric vehicles.")
    print("- Reducing energy consumption with energy-efficient appliances.")
    print("- Switching to a plant-based or low-carbon diet.")


def visualize_emissions(transport, energy, diet):
    """
    Visualize the carbon footprint breakdown using a pie chart.
    """
    labels = ['Transportation', 'Energy Usage', 'Diet']
    values = [transport, energy, diet]
    
    # Ensure there's at least some data for a pie chart
    if sum(values) == 0:
        print("No emissions recorded to visualize.")
        return

    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99'])
    plt.title("Carbon Footprint Breakdown")
    plt.show()


def main():
    """
    Main function to run the Carbon Footprint Calculator.
    """
    transport_type, distance, energy_usage, diet_type = get_user_input()
    
    transport_emissions = calculate_transport_emissions(transport_type, distance)
    energy_emissions = calculate_energy_emissions(energy_usage)
    diet_emissions = calculate_diet_emissions(diet_type)
    
    display_results(transport_emissions, energy_emissions, diet_emissions)
    visualize_emissions(transport_emissions, energy_emissions, diet_emissions)


if __name__ == "__main__":
    main()
