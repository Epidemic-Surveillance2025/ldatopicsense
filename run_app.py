
import os
from pyngrok import ngrok
import subprocess

# Set up ngrok authentication
ngrok_auth_token = "cr_2yNPfSzYXH2wtTnhZiKaJqsRm9D"
ngrok.set_auth_token(ngrok_auth_token)

# Start the Streamlit app and create a tunnel
public_url = ngrok.connect(addr='8501', proto='http')
print(f"Streamlit app is running at: {public_url}")

# Start the Streamlit app
subprocess.Popen(["streamlit", "run", "app.py"])

# Keep the notebook running
input("Press Enter to stop the Streamlit app...")
ngrok.kill()