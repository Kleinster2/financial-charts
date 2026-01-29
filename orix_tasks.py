"""Script to add ORIX data and generate comparison chart"""
import subprocess
import sys
import time
import os

# Step 1: Download ORIX data
print("=" * 60)
print("Step 1: Downloading ORIX (IX) data...")
print("=" * 60)
result1 = subprocess.run([sys.executable, "download_single_ticker.py", "IX"], 
                         cwd=r"C:\Users\klein\financial-charts",
                         capture_output=True, text=True, timeout=120)
print("STDOUT:", result1.stdout)
print("STDERR:", result1.stderr)
print("Return code:", result1.returncode)
print()

# Step 2: Start Flask server in background
print("=" * 60)
print("Step 2: Starting Flask API server...")
print("=" * 60)
server_process = subprocess.Popen([sys.executable, "charting_app/app.py"],
                                  cwd=r"C:\Users\klein\financial-charts",
                                  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(f"Server started with PID: {server_process.pid}")

# Wait for server to start
print("Waiting for server to start...")
time.sleep(5)

# Step 3: Generate chart using Python requests
print()
print("=" * 60)
print("Step 3: Generating chart...")
print("=" * 60)

try:
    import urllib.request
    import ssl
    
    url = "http://localhost:5000/api/chart/lw?tickers=IX,SMFG,MFG,MUFG&normalize=true&primary=IX&start=2020-01-01&show_title=false"
    output_path = r"C:\Users\klein\financial-charts\investing\attachments\orix-vs-peers.png"
    
    # Create attachments directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Download with SSL context that allows us to connect
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req, context=ctx, timeout=60) as response:
        data = response.read()
        with open(output_path, 'wb') as f:
            f.write(data)
    
    file_size = os.path.getsize(output_path)
    print(f"Chart saved to: {output_path}")
    print(f"File size: {file_size} bytes")
    
except Exception as e:
    print(f"Error generating chart: {e}")
    import traceback
    traceback.print_exc()

# Step 4: Stop the server
print()
print("=" * 60)
print("Step 4: Stopping server...")
print("=" * 60)
server_process.terminate()
try:
    server_process.wait(timeout=5)
except:
    server_process.kill()
print("Server stopped")

print()
print("=" * 60)
print("SUMMARY")
print("=" * 60)
