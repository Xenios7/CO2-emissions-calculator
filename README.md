# 🌍 CO2 Emissions Calculator

## 📖 Overview
The **CO2 Emissions Calculator** is a web application that helps users estimate their carbon footprint based on **transportation, energy consumption, and diet choices**. The goal of this project is to promote awareness of carbon emissions and encourage sustainable habits.

## 🚀 Features
- 🌱 Calculate **CO2 emissions** from **transport, energy usage, and diet**.
- 📊 Displays **individual emission breakdown**.
- 📉 Provides **suggestions to reduce emissions**.
- 📡 Built with **Flask**, **PostgreSQL**, and **JavaScript**.
- 🎨 Responsive UI with **HTML, CSS, and JavaScript**.

## 🖥️ Demo
> 🚀 **[Live Demo (if deployed)](https://your-deployment-link.com)**  
> 🎥 **[Demo Video (if applicable)](https://your-video-link.com)**

## 🏗️ Tech Stack
| Technology    | Usage |
|--------------|------------------------------------------------|
| **Python (Flask)** | Backend API & Web Server |
| **PostgreSQL** | Database for storing user data |
| **HTML, CSS, JavaScript** | Frontend & UI design |
| **Bootstrap** | Responsive design |
| **Matplotlib** | Visualization of CO2 breakdown |

## 📸 Screenshots
### 🌱 Home Page
![Home Page](screenshots/home.png)
### 📊 Results Page
![Results Page](screenshots/results.png)

## 🛠️ Installation & Setup
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/Xenios7/CO2-emissions-calculator.git
cd CO2-emissions-calculator
```

### **2️⃣ Create a Virtual Environment**
```sh
python3 -m venv myenv
source myenv/bin/activate  # On macOS/Linux
myenv\Scripts\activate     # On Windows
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Set Up Database**
- Ensure **PostgreSQL** is running.
- Create a database:
```sh
psql -U your_username -d postgres
CREATE DATABASE carbon_footprint;
\q
```
- Apply schema:
```sh
psql -U your_username -d carbon_footprint -f database/schema.sql
psql -U your_username -d carbon_footprint -f database/seed_data.sql
```

### **5️⃣ Run the App**
```sh
python app.py
```
The app should now be running on **`http://127.0.0.1:5000`**.

---

## 🎯 How It Works
1. Enter **transport type, distance, energy usage, and diet choice**.
2. Click **"Calculate"** to compute **your total CO2 footprint**.
3. View results in **detailed breakdown + improvement tips**.
4. Get **visualized data** for a better understanding.

---

## 🛠️ Contributing
Feel free to contribute to this project! To contribute:
1. **Fork** the repo
2. **Create** a new branch (`git checkout -b feature-new-feature`)
3. **Commit** changes (`git commit -m "Added new feature"`)
4. **Push** to GitHub (`git push origin feature-new-feature`)
5. Open a **Pull Request**

---
### **🔗 Connect With Me**
**📌 GitHub**: [Xenios7](https://github.com/Xenios7)  
**📌 LinkedIn**: [Your LinkedIn](https://linkedin.com/in/yourname)  
**📌 Email**: xenios04@gmail.com  
