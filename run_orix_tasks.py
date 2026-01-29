#!/usr/bin/env python3
"""
Script to add ORIX Corporation (IX) data to the database and generate a price comparison chart.

This script:
1. Downloads ORIX ADR (NYSE: IX) data from yfinance and adds it to the database
2. Starts the Flask API server in a background process
3. Generates a price comparison chart (IX vs Japanese bank peers)
4. Verifies the output file was created

Usage:
    python run_orix_tasks.py

Requirements:
    - Virtual environment at .venv with all dependencies installed
    - market_data.db exists in the financial-charts directory
"""

import subprocess
import sys
import time
import os
from pathlib import Path

# Configuration
PROJECT_DIR = Path(r"C:\Users\klein\financial-charts")
DB_PATH = PROJECT_DIR / "market_data.db"
OUTPUT_PATH = PROJECT_DIR / "investing" / "attachments" / "orix-vs-peers.png"
PYTHON_EXE = PROJECT_DIR / ".venv" / "Scripts" / "python.exe"
SERVER_URL = "http://localhost:5000"

def step1_download_data():
    """Download ORIX (IX) data from yfinance and add to database."""
    print("=" * 60)
    print("Step 1: Downloading ORIX (IX) data...")
    print("=" * 60)
    
    result = subprocess.run(
        [str(PYTHON_EXE), "download_single_ticker.py", "IX"],
        cwd=str(PROJECT_DIR),
        capture_output=True,
        text=True,
        encoding='utf-8',
        errors='replace'
    )
    
    print(result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)
    
    if result.returncode != 0:
        print(f"ERROR: Failed to download IX data (exit code: {result.returncode})")
        return False
    
    print("✓ Data download completed successfully")
    return True

def step2_start_server():
    """Start the Flask API server in a background process."""
    print()
    print("=" * 60)
    print("Step 2: Starting Flask API server...")
    print("=" * 60)
    
    # Start server in background
    process = subprocess.Popen(
        [str(PYTHON_EXE), "charting_app/app.py"],
        cwd=str(PROJECT_DIR),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        creationflags=subprocess.CREATE_NEW_CONSOLE  # Windows: create new console window
    )
    
    print(f"Server started with PID: {process.pid}")
    print("Waiting for server to initialize...")
    time.sleep(5)  # Give server time to start
    
    return process

def step3_generate_chart():
    """Generate the price comparison chart via API request."""
    print()
    print("=" * 60)
    print("Step 3: Generating chart...")
    print("=" * 60)
    
    # Create output directory if it doesn't exist
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    
    # Build chart URL
    chart_url = (
        f"{SERVER_URL}/api/chart/lw"
        f"?tickers=IX,SMFG,MFG,MUFG"
        f"&normalize=true"
        f"&primary=IX"
        f"&start=2020-01-01"
        f"&show_title=false"
    )
    
    print(f"Requesting chart from: {chart_url}")
    
    try:
        # Try using urllib first (no external dependencies)
        import urllib.request
        import ssl
        
        # Create SSL context that allows us to connect
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        
        req = urllib.request.Request(chart_url)
        with urllib.request.urlopen(req, context=ctx, timeout=60) as response:
            data = response.read()
            with open(OUTPUT_PATH, 'wb') as f:
                f.write(data)
        
        print(f"✓ Chart saved to: {OUTPUT_PATH}")
        return True
        
    except Exception as e:
        print(f"urllib failed: {e}")
        
        # Fallback: try requests if available
        try:
            import requests
            response = requests.get(chart_url, timeout=60)
            response.raise_for_status()
            with open(OUTPUT_PATH, 'wb') as f:
                f.write(response.content)
            print(f"✓ Chart saved to: {OUTPUT_PATH}")
            return True
        except ImportError:
            print("requests library not available")
        except Exception as e2:
            print(f"requests failed: {e2}")
        
        # Final fallback: try curl via subprocess
        try:
            result = subprocess.run(
                ["curl", chart_url, "-o", str(OUTPUT_PATH)],
                capture_output=True,
                text=True,
                timeout=60
            )
            if result.returncode == 0:
                print(f"✓ Chart saved to: {OUTPUT_PATH}")
                return True
        except FileNotFoundError:
            print("curl not available")
        except Exception as e3:
            print(f"curl failed: {e3}")
    
    return False

def step4_verify():
    """Verify the output file was created and has content."""
    print()
    print("=" * 60)
    print("Step 4: Verification")
    print("=" * 60)
    
    if OUTPUT_PATH.exists():
        file_size = OUTPUT_PATH.stat().st_size
        if file_size > 0:
            print(f"✓ SUCCESS: Chart file created")
            print(f"  Path: {OUTPUT_PATH}")
            print(f"  Size: {file_size:,} bytes ({file_size / 1024:.1f} KB)")
            return True
        else:
            print(f"✗ ERROR: File exists but is empty (0 bytes)")
            return False
    else:
        print(f"✗ ERROR: File not found at {OUTPUT_PATH}")
        return False

def main():
    """Main execution function."""
    print("ORIX Corporation Data Download and Chart Generation")
    print("=" * 60)
    print()
    
    # Check prerequisites
    if not PYTHON_EXE.exists():
        print(f"ERROR: Python executable not found at {PYTHON_EXE}")
        print("Please ensure the virtual environment is set up correctly.")
        return 1
    
    if not DB_PATH.exists():
        print(f"WARNING: Database not found at {DB_PATH}")
        print("The download script may create it automatically.")
    
    # Step 1: Download data
    if not step1_download_data():
        return 1
    
    # Step 2: Start server
    server_process = step2_start_server()
    
    try:
        # Step 3: Generate chart
        if not step3_generate_chart():
            print("\n✗ Chart generation failed")
            return 1
        
        # Step 4: Verify
        if not step4_verify():
            return 1
        
    finally:
        # Cleanup: Stop the server
        print()
        print("=" * 60)
        print("Cleanup: Stopping Flask server...")
        print("=" * 60)
        server_process.terminate()
        try:
            server_process.wait(timeout=5)
            print("✓ Server stopped")
        except subprocess.TimeoutExpired:
            server_process.kill()
            print("✓ Server killed (forced)")
    
    print()
    print("=" * 60)
    print("ALL TASKS COMPLETED SUCCESSFULLY")
    print("=" * 60)
    print(f"Chart saved to: {OUTPUT_PATH}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
