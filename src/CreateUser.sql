CREATE TABLE user_table (
    user_id SERIAL PRIMARY KEY,
    user_name VARCHAR(255),
    user_data JSONB
);
