from flask import Flask, request, jsonify, render_template, send_file
import os
import plotly.graph_objects as go

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
        if not request.is_json:
            return jsonify({"error": "Request must be JSON"}), 415

        data = request.get_json()

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

        results = calculate_emissions(transport_type, distance, energy_usage, diet_type)

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

    try:
        transport = float(transport)
        energy = float(energy)
        diet = float(diet)
        total = float(total)
    except ValueError:
        return jsonify({"error": "Invalid values for emissions"}), 400

    recommendations = generate_recommendations(total)

    return render_template("results.html",
                           transport_emissions=transport,
                           energy_emissions=energy,
                           diet_emissions=diet,
                           total_emissions=total,
                           recommendations=recommendations)

# --- Helper Functions ---
def calculate_emissions(transport_type, distance, energy_usage, diet_type):
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
    if total_emissions < 10:
        return "Great job! Your carbon footprint is low. Keep using sustainable transport and renewable energy!"
    elif total_emissions < 30:
        return "Your carbon footprint is moderate. Consider reducing energy consumption and carpooling."
    else:
        return "Your carbon footprint is high. Try using public transport, renewable energy, and a plant-based diet!"

# --- Plotly Pie Chart Route ---
@app.route('/generate_pie_chart')
def generate_pie_chart():
    """
    Generate and save an interactive 2D pie chart using Plotly.
    """
    try:
        print("✅ Generating Pie Chart...")

        # Retrieve values dynamically from the request
        transport = float(request.args.get("transport", 0))
        energy = float(request.args.get("energy", 0))
        diet = float(request.args.get("diet", 0))

        labels = ['Transportation', 'Energy Usage', 'Diet']
        values = [transport, energy, diet]

        # Create interactive Pie Chart using Plotly
        fig = go.Figure(data=[go.Pie(
            labels=labels,
            values=values,
            pull=[0.1, 0.1, 0.1],  # Slightly separate each section
            hoverinfo='label+value+percent',
            textinfo='percent+label',
            marker=dict(colors=['#ff9999', '#66b3ff', '#99ff99'])  # Custom colors
        )])

        fig.update_layout(
            title='Carbon Footprint Breakdown',
            title_x=0.5,  # Center the title
            showlegend=True
        )

        # Save the chart as an HTML file
        os.makedirs("static", exist_ok=True)
        chart_path = os.path.join("static", "carbon_footprint_pie.html")
        fig.write_html(chart_path)

        print(f"✅ Pie Chart Saved at {chart_path}")
        return send_file(chart_path, mimetype='text/html')

    except Exception as e:
        print(f"❌ Error: {e}")
        return str(e), 500

# --- Run App ---
if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
