from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# --- Constants ---
TRANSPORT_FACTORS = {'car': 0.21, 'bus': 0.10, 'train': 0.05}  # kg CO2 per km
DIET_FACTORS = {'vegan': 2.0, 'vegetarian': 3.0, 'meat-based': 7.0}  # kg CO2 per day
ENERGY_FACTOR = 0.5  # kg CO2 per kWh

# --- Homepage ---
@app.route("/")
def home():
    return render_template("index.html")

# --- Calculation Route ---
@app.route("/calculate", methods=["POST"])
def calculate():
    try:
        # Ensure request is JSON
        if not request.is_json:
            return jsonify({"error": "Request must be JSON"}), 415

        data = request.get_json()

        # Extract input values and validate them
        transport_type = data.get("transport_type", "").lower()
        distance = data.get("distance")
        energy_usage = data.get("energy_usage")
        diet_type = data.get("diet_type", "").lower()

        if not transport_type or not diet_type or distance is None or energy_usage is None:
            return jsonify({"error": "Missing required fields"}), 400

        try:
            distance = float(distance)
            energy_usage = float(energy_usage)
        except ValueError:
            return jsonify({"error": "Invalid number format"}), 400

        # Calculate emissions
        results = calculate_emissions(transport_type, distance, energy_usage, diet_type)

        # Redirect to results page with calculated values
        return jsonify(results)

    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

# --- Results Route ---
@app.route("/results")
def results():
    transport = request.args.get("transport", 0)
    energy = request.args.get("energy", 0)
    diet = request.args.get("diet", 0)
    total = request.args.get("total", 0)

    # Generate recommendations based on emissions
    recommendations = generate_recommendations(float(total))

    return render_template("results.html",
                           transport_emissions=transport,
                           energy_emissions=energy,
                           diet_emissions=diet,
                           total_emissions=total,
                           recommendations=recommendations)

# --- Helper Functions ---
def calculate_emissions(transport_type, distance, energy_usage, diet_type):
    """Calculates the carbon footprint for transport, energy, and diet."""
    transport_emissions = TRANSPORT_FACTORS.get(transport_type, 0) * distance
    energy_emissions = energy_usage * ENERGY_FACTOR
    diet_emissions = DIET_FACTORS.get(diet_type, 0)
    total_emissions = transport_emissions + energy_emissions + diet_emissions

    return {
        "transport_emissions": round(transport_emissions, 2),
        "energy_emissions": round(energy_emissions, 2),
        "diet_emissions": round(diet_emissions, 2),
        "total_emissions": round(total_emissions, 2)
    }

def generate_recommendations(total_emissions):
    """Provides recommendations based on total carbon footprint."""
    if total_emissions < 10:
        return "Great job! Your carbon footprint is low. Keep using sustainable transport and renewable energy!"
    elif total_emissions < 30:
        return "Your carbon footprint is moderate. Consider reducing energy consumption and carpooling."
    else:
        return "Your carbon footprint is high. Try using public transport, renewable energy, and a plant-based diet!"

# --- Run App ---
if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)

