import psycopg2

class DatabaseHandler:
    def __init__(self):
        # Connect to PostgreSQL
        self.conn = psycopg2.connect(
            host="localhost",
            database="your_database",
            user="your_user",
            password="your_password"
        )
        self.cursor = self.conn.cursor()

    def get_user_data(self, user_id):
        # Fetch user data from PostgreSQL based on user_id
        query = f"SELECT user_data FROM user_table WHERE user_id = {user_id};"
        self.cursor.execute(query)
        user_data = self.cursor.fetchone()
        return user_data[0] if user_data else None

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
