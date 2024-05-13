#!/bin/bash

# Install dependencies
pip install Flask requests

# Start Flask server in the background
python app.py &

# Configure port forwarding
# Replace 5000 with the port number your Flask app is running on
codespace-port-forward 5000
