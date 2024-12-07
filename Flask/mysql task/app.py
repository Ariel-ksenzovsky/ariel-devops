from flask import Flask, render_template, jsonify
import random
import os
import mysql.connector
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables from .env
load_dotenv()

# Database configuration
db_config = { 
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME')
}

@app.route('/')
def display_images():
    try:
        # Establish a database connection
        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor()

        # SQL query to retrieve image URLs
        query = "SELECT url FROM images"
        cursor.execute(query)

        # Fetch the list of image URLs
        images = cursor.fetchall()
        
        # Shuffle the images randomly
        random.shuffle(images)

        # Close the cursor and connection
        cursor.close()
        cnx.close()

        if images:
            # Pass only the URL (the first element of the tuple)
            return render_template('index.html', image=images[0][0])
        else:
            return "No images found.", 404
    
    except mysql.connector.Error as err:
        app.logger.error(f"Database error: {err}")
        return f"Database error: {err}", 500
    
    except Exception as e:
        app.logger.error(f"Unexpected error: {e}")
        return f"Internal server error: {e}", 500

if __name__ == "__main__":
    port = int(os.getenv('FLASK_PORT', 5000))
    app.run(host="0.0.0.0", port=port)
