# Real-Time Data Pipeline

A complete lightweight pipeline for real-time market data ingestion, storage, processing, analytics, anomaly detection, and dashboard visualization.  
The project uses the BTC/USDT price from the Binance public API and provides:

- Real-time data ingestion  
- Local SQLite storage  
- Feature engineering (returns, volatility, z-score)  
- Diagnostics and anomaly detection  
- A simple baseline trading signal  
- A real-time Streamlit dashboard  

---

## 🚀 Features

### Real-Time Ingestion
- Fetches BTC/USDT price from Binance
- Adjustable refresh interval (1 second by default)
- Robust error handling

### Storage
- Local SQLite database  
- Append-only architecture  
- Full historical loading for analytics  

### Analytics
- Price returns  
- Rolling volatility  
- Z-score (distance from rolling mean)  
- Automatic feature computation  

### Alerts
- High positive/negative deviation (z > 3 or z < -3)
- Volatility spikes
- Alerts displayed in the dashboard

### Baseline Signal
- **Buy** if z < -1  
- **Sell** if z > 1  
- **Neutral** otherwise  

### Streamlit Dashboard
- Live price display  
- Current trading signal  
- Time-series charts (price, return, volatility, z-score)  
- Real-time alerts  

---

## 🧱 Project Structure

```
RealTime Data Pipeline
│
├── dashboard/
│   └── app.py                 # Streamlit dashboard
│
├── data_pipeline/
│   ├── fetcher.py             # Fetch BTC/USDT price
│   ├── processor.py           # Compute analytics features
│   ├── scheduler.py           # Real-time loop
│   └── storage.py             # SQLite storage
│
├── diagnostics/
│   ├── analytics.py           # Full analytics pipeline
│   └── alerts.py              # Anomaly detection
│
└── models/
    └── baseline_signal.py     # Simple trading signal
```

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/realtime-data-pipeline.git
cd realtime-data-pipeline
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Pipeline

Open **Terminal 1** and start the pipeline:

```bash
python data_pipeline/scheduler.py
```

This will:
- Initialize the database  
- Start saving real-time prices every second  

---

## 📊 Launching the Dashboard

Open **Terminal 2**:

```bash
streamlit run dashboard/app.py
```

Your browser will open automatically with the dashboard.

---

## ⏹️ Stop the Pipeline and the Dashboard

To stop the pipeline and the dashboard, you **must manually kill both terminals using `CTRL + C`**.  
This is required because both processes run continuously in real time.

---

## 📝 Example Outputs

- Live BTC/USDT price  
- Baseline signal (buy / sell / neutral)  
- Time-series charts (price, return, volatility, z-score)  
- Alerts such as:  
  - *High positive deviation (z > 3)*  
  - *High negative deviation (z < -3)*  
  - *Volatility spike detected*  

---

## ⚙️ Configuration

You can customize:
- Pipeline refresh interval → `scheduler.py → run_pipeline(sleep_seconds=1)`
- API endpoint → `fetcher.py → API_URL`
- Rolling windows → `processor.py`
- Alert thresholds → `alerts.py`

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

---

## 📄 License

MIT License.
