# Alert Viewer

A lightweight Flask-based tool that receives alerts through a webhook endpoint and displays them in a simple, web-based viewer.  
This can be useful for testing alert payloads, webhook integrations, or visualizing incoming data from monitoring systems.

---

# Features
- Simple REST webhook (`/webhook`) to receive alert payloads via POST requests  
- Web interface (`/alerts`) to view received alerts in a formatted table  
- Pretty-printed JSON output for easier debugging and readability  
- Runs locally using Flask — no database or external dependency required  

---

# Getting Started

### 1. Clone the repository

git clone https://github.com/<your-username>/flask-alert-viewer.git

cd flask-alert-viewer


### 2. Install dependencies
pip install flask

### 3. Run the application
python app.py
