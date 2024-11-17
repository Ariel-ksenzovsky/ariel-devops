import speedtest
import csv
import time
from datetime import datetime

def log_internet_speed():
    # File name for the CSV file
    csv_filename = 'internet_speed.csv'

    # Check if the CSV file exists, and if not, create it with headers
    try:
        with open(csv_filename, 'r') as file:
            # Check if file is empty
            pass
    except FileNotFoundError:
        # If file doesn't exist, create and write the header row
        with open(csv_filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "Download Speed (Mbps)", "Upload Speed (Mbps)"])

    # Initialize the speedtest client
    st = speedtest.Speedtest()

    # Run the test every 5 minutes
    while True:
        # Get current timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Perform the speed test for download and upload speeds
        download_speed = st.download() / 1_000_000  # Convert from bits/s to Mbps
        upload_speed = st.upload() / 1_000_000  # Convert from bits/s to Mbps

        # Write the results to the CSV file
        with open(csv_filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, round(download_speed, 2), round(upload_speed, 2)])

        print(f"Logged data: {timestamp} - Download: {round(download_speed, 2)} Mbps, Upload: {round(upload_speed, 2)} Mbps")

        # Sleep for 5 minutes before taking the next measurement
        time.sleep(300)  # 300 seconds = 5 minutes

# Call the function to log internet speed
log_internet_speed()

    