-- schema.sql

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE activities (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    transport_type VARCHAR(50),
    distance_km FLOAT,
    energy_usage_kwh FLOAT,
    diet_type VARCHAR(50),
    total_emissions FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
