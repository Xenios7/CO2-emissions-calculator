-- seed_data.sql

-- Insert sample users
INSERT INTO users (name, email, password) VALUES 
('John Doe', 'john.doe@example.com', 'hashedpassword1'),
('Jane Smith', 'jane.smith@example.com', 'hashedpassword2');

-- Insert sample activities
INSERT INTO activities (user_id, transport_type, distance_km, energy_usage_kwh, diet_type, total_emissions) VALUES
(1, 'car', 15.5, 10.2, 'meat-based', 25.7),
(2, 'bus', 20.0, 8.0, 'vegetarian', 12.4);
