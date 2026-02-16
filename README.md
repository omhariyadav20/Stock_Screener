# Stock Analyzer

A Streamlit-based web application for analyzing and comparing stocks with real-time market data, technical indicators, and optional AI-powered insights.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Project Structure](#project-structure)
3. [How It Works](#how-it-works)
4. [Installation & Setup](#installation--setup)
5. [Running the App](#running-the-app)
6. [Features](#features)
7. [Configuration](#configuration)
8. [File Descriptions](#file-descriptions)
9. [Technical Details](#technical-details)

---

## Project Overview

**Stock Analyzer** is a stock market analysis tool that helps users:
- Compare multiple stocks side-by-side
- View technical indicators (RSI, moving averages, trends)
- Display candlestick charts for daily and intraday data
- Get AI-powered analysis (optional, with OpenAI API key)
- View corporate fundamentals (P/E ratio, dividend yield, sector, etc.)

The app uses **Streamlit** for the UI, **yfinance** for stock data, and **OpenAI** for optional AI analysis.

---

## Project Structure

```
stocks_analyise/
├── app.py                   # Main Streamlit entry point (home page)
├── data.py                  # Stock data fetching & technical analysis
├── requirements.txt         # Python dependencies
├── users.json              # User credentials (auth removed, unused)
├── generate_hash.py        # Script to generate password hashes
├── check_syntax.py         # Syntax validation script
├── test_auth.py            # Authentication test script
├── test_data.py            # Data module test script
│
├── lib/
│   ├── __init__.py         # Makes lib a Python package
│   ├── app.py              # Alternative app configuration (unused currently)
│   ├── auth.py             # Authentication logic (auth removed)
│   └── llm.py              # OpenAI API integration
│
├── pages/
│   ├── 1_Compare.py        # Multi-stock comparison page
│   ├── 2_Deep_Dive.py      # Single stock deep analysis page
│
└── README.md               # This file
```

---

## How It Works

### Application Flow

```
1. User opens app.py
   ↓
2. Homepage displays (lib/app.py)
   - Shows "Stock Analyzer" title
   - Navigation hints to pages
   ↓
3. User selects page from sidebar:
   
   Option A: Compare Stocks (pages/1_Compare.py)
   ├─ Enter tickers (AAPL, MSFT, GOOGL, etc.)
   ├─ Fetch historical + intraday data (data.py)
   ├─ Compute technical indicators (RSI, MA20/50/200)
   ├─ Display comparison table + charts
   └─ Optional: Generate AI analysis (lib/llm.py)
   
   Option B: Deep Dive (pages/2_Deep_Dive.py)
   ├─ Enter single ticker
   ├─ Fetch 6mo-5yr historical data
   ├─ Show fundamentals (JSON format)
   ├─ Show technical metrics (dataframe)
   ├─ Display daily + intraday charts
   └─ Optional: Run deep AI analysis
```

### Data Flow

#### 1. **Data Fetching** (`data.py`)
```python
# Using yfinance library
yf.Ticker(ticker).history(period="1y", interval="1d")
  ↓
# Returns DataFrame with OHLCV (Open, High, Low, Close, Volume)
```

#### 2. **Technical Analysis** (`data.py`)
```python
Compute for each ticker:
├─ RSI (Relative Strength Index) - momentum indicator
├─ Moving Averages (MA20, MA50, MA200) - trend direction
├─ Trend Slope (60-day polyfit) - trend strength
└─ Last Close Price - current market value
```

#### 3. **Fundamental Data** (`data.py`)
```python
yf.Ticker(ticker).info or get_info()
  ↓
Extract:
├─ Company name, sector, industry
├─ Market cap, P/E ratios
├─ Dividend yield
├─ 52-week high/low
└─ Beta (volatility measure)
```

#### 4. **AI Analysis** (`lib/llm.py`)
```
If OpenAI key configured:
├─ Build detailed prompt with:
│  ├─ Fundamentals summary
│  ├─ 120 latest daily candles
│  ├─ 60 latest intraday candles
│  └─ Technical metrics
├─ Send to OpenAI API
├─ Parse JSON response
└─ Display verdict + analysis

If no key:
  └─ Show "OpenAI key not configured" message
```

---

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- OpenAI API key (optional, for AI analysis)

### Step 1: Install Dependencies

```powershell
cd C:\Users\Dell\stocks_analyise
pip install -r requirements.txt
```

**Dependencies included:**
- `streamlit` - Web UI framework
- `yfinance` - Stock data (Yahoo Finance)
- `pandas` - Data manipulation
- `numpy` - Numerical computing
- `python-dotenv` - Environment variable loading
- `passlib[bcrypt]` - Password hashing (legacy)
- `openai` - OpenAI API client

### Step 2: Configure OpenAI (Optional)

**Option A: Using Streamlit secrets file (Recommended)**

1. Create directory:
```powershell
mkdir C:\Users\Dell\.streamlit -Force
```

2. Create file `C:\Users\Dell\.streamlit\secrets.toml`:
```toml
OPENAI_API_KEY = "sk-your-actual-key-here"
```

**Option B: Using environment variable**

```powershell
$env:OPENAI_API_KEY = "sk-your-actual-key-here"
```

**Get your OpenAI API key:**
- Visit https://platform.openai.com/api-keys
- Sign in or create account
- Create new API key and copy it

---

## Running the App

### Start the Streamlit Server

```powershell
cd C:\Users\Dell\stocks_analyise
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

### Navigation

1. **Home Page** (app.py)
   - Overview of the app
   - Navigation instructions

2. **Compare Page** (pages/1_Compare.py)  
   - Enter multiple tickers (comma-separated)
   - View side-by-side comparison table
   - See charts for each stock
   - Generate AI analysis for all stocks

3. **Deep Dive Page** (pages/2_Deep_Dive.py)
   - Analyze one stock in detail
   - View fundamentals as JSON
   - See technical metrics
   - View daily + intraday charts
   - Get detailed AI analysis

---

## Features

### ✅ Core Features

| Feature | Description | File |
|---------|-------------|------|
| **Multi-Stock Comparison** | Compare up to 10+ stocks simultaneously | `pages/1_Compare.py` |
| **Technical Indicators** | RSI, Moving Averages (MA20, MA50, MA200), Trend slope | `data.py` |
| **Candlestick Data** | Daily & intraday OHLCV data | `data.py` |
| **Fundamentals** | P/E, dividend yield, market cap, sector, industry | `data.py` |
| **Charts** | Line charts for daily/intraday closes | `pages/*.py` |
| **Deep Analysis** | Detailed 1-stock breakdown | `pages/2_Deep_Dive.py` |
| **AI Analysis** | Optional OpenAI-powered insights | `lib/llm.py` |

### ⚙️ Technical Features

- **Caching**: Streamlit `@st.cache_data` for fast data retrieval (TTL: 60s intraday, 6h fundamentals)
- **Responsive UI**: Wide layout with columns for side-by-side display
- **Error Handling**: Graceful fallbacks when data unavailable
- **Optional AI**: Works fine without OpenAI key (AI analysis just shows message)

---

## Configuration

### Environment Variables

```bash
OPENAI_API_KEY      # OpenAI API key (optional for AI analysis)
USERS_FILE          # Path to users.json (default: "users.json", unused)
```

### Streamlit Config

Default settings in Streamlit:
- **Page layout**: Wide
- **Page title**: "Stock App"
- **Theme**: Default

---

## File Descriptions

### Root Level Files

| File | Purpose |
|------|---------|
| `app.py` | **Main Entry Point** - Streamlit runs this to start the app. Contains home page UI. |
| `data.py` | **Stock Data Module** - Fetches data from yfinance, computes technical indicators. |
| `requirements.txt` | **Dependencies** - Lists all Python packages needed. Install with: `pip install -r requirements.txt` |
| `users.json` | **User Data** (Legacy) - Contains hashed passwords. Unused now (auth removed). |
| `generate_hash.py` | **Password Hash Generator** - Script to create bcrypt hashes. Legacy/unused. |
| `check_syntax.py` | **Validation Tool** - Compiles all .py files to check for syntax errors. |
| `test_auth.py` | **Auth Test** - Tests authentication logic (legacy, auth removed). |
| `test_data.py` | **Data Test** - Tests data fetching and technical analysis functions. |
| `README.md` | **Documentation** - This file. Explains the entire project. |

### Library Files (`lib/`)

| File | Purpose |
|------|---------|
| `__init__.py` | **Package Marker** - Makes `lib/` a Python package. |
| `auth.py` | **Authentication** - Verify user login (unused, auth removed). |
| `app.py` | **App Config** - Alternative app UI (currently unused). |
| `llm.py` | **OpenAI Integration** - Calls OpenAI API for stock analysis. |

### Page Files (`pages/`)

| File | Purpose |
|------|---------|
| `1_Compare.py` | **Compare Multiple Stocks** - User enters tickers, app displays comparison table, charts, and optional AI analysis. |
| `2_Deep_Dive.py` | **Deep Dive Single Stock** - User enters one ticker, app shows fundamentals, technicals, charts, and detailed AI analysis. |

---

## Technical Details

### Stock Data Source

**yfinance** fetches from Yahoo Finance:
```python
yf.Ticker("AAPL").history(period="1y", interval="1d")
# Returns: DataFrame with Date (index), Open, High, Low, Close, Volume, Adj Close
```

### Technical Indicators Explained

#### **RSI (Relative Strength Index)**
- **Formula**: `100 - (100 / (1 + RS))` where `RS = avg_gain / avg_loss`
- **Range**: 0-100
- **Interpretation**:
  - RSI > 70 = "Overbought" (may pull back)
  - RSI < 30 = "Oversold" (may bounce)
  - RSI 30-70 = Neutral

#### **Moving Averages (MA)**
- **MA20**: Average of last 20 closing prices
- **MA50**: Average of last 50 closing prices
- **MA200**: Average of last 200 closing prices
- **Interpretation**: Price above MA = Uptrend, Price below MA = Downtrend

#### **Trend Slope**
- **Calculation**: `np.polyfit(x, close_prices[-60:], 1)[0]` (60-day linear fit)
- **Positive slope**: Upward trend
- **Negative slope**: Downward trend

### AI Analysis Process

1. **Build Prompt** (`build_prompt()`)
   - Combines fundamentals, technical metrics, and recent price action
   - Sends structured data to OpenAI

2. **OpenAI Call** (`analyze_with_openai()`)
   - Uses OpenAI Responses API
   - Model: `gpt-4.1-mini` (configurable)
   - Request timeout: ~30 seconds

3. **Response Handling**
   - If successful: Parse and display JSON
   - If no key: Show "OpenAI key not configured" message
   - If API error: Show friendly error message (app doesn't crash)

### Caching Strategy

```python
@st.cache_data(ttl=60, show_spinner=False)
def fetch_history(ticker, period, interval):
    # Cache for 60 seconds (1 min) for intraday
    
@st.cache_data(ttl=6 * 60 * 60, show_spinner=False)
def fetch_fundamentals(ticker):
    # Cache for 6 hours for company info
```

**Why?** Yahoo Finance has rate limits. Caching reduces API calls and speeds up the app.

### Error Handling

```python
# Data unavailable
└─ Returns empty dict or None; UI shows "No data." message

# OpenAI not configured
└─ Returns {"error": "..."} dict; UI shows warning message

# Network error
└─ catch Exception; return fallback dict; UI continues

# No match found
└─ Filter results; warn user; app doesn't crash
```

---

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'lib.auth'"
**Solution**: Ensure `lib/__init__.py` exists. If not:
```powershell
New-Item -Path "lib\__init__.py" -Force
```

### Issue: "StreamlitSecretNotFoundError: No secrets found"
**Solution**: This is normal if no OpenAI key is set. The app still works; AI analysis just won't run. To fix, add your key as shown in [Configuration](#configuration).

### Issue: "TypeError: argument of type 'NoneType' is not iterable"
**Solution**: Updated code gracefully handles missing/None responses. If you see this, restart the app:
```powershell
streamlit run app.py
```

### Issue: "No data." in charts
**Cause**: Ticker not found or Yahoo Finance has no data for that ticker.
**Solution**: Try a major ticker like AAPL, MSFT, GOOGL to test.

### Issue: "OpenAI analysis unavailable"
**Cause**: No API key configured, or OpenAI API returned an error.
**Solution**: Add your OpenAI key (see [Configuration](#configuration)) or check your API quota at https://platform.openai.com/account/usage/limits.

---

## Performance Tips

1. **Use shorter periods** for faster data fetch:
   - Daily: Use "1y" or "2y" instead of "5y"
   - Intraday: Use "5d" or "7d" instead of longer periods

2. **Compare fewer stocks** at once:
   - 3-5 stocks = fast comparison
   - 10+ stocks = slower, more network time

3. **Cache works best** if you're looking at the same stocks repeatedly:
   - First load: slow (fetches from Yahoo)
   - Subsequent loads (within TTL): instant

4. **AI analysis is optional**:
   - Without OpenAI key: instant results
   - With OpenAI key: takes ~5-10s per stock

---

## Development Notes

### Adding a New Page

1. Create file `pages/3_Your_Page.py` (Streamlit auto-discovers numbered pages)
2. Import needed modules:
   ```python
   import streamlit as st
   import pandas as pd
   from data import fetch_history, compute_technicals
   from lib.llm import analyze_with_openai
   ```
3. Write Streamlit UI code
4. Run `python check_syntax.py` to validate

### Modifying Technical Indicators

All indicators are in `data.py` function `compute_technicals()`:
- Edit `compute_rsi()` to change RSI logic
- Edit moving average calculations
- Add new indicators and return them in the dict

### Updating Dependencies

If you add/update packages:
```powershell
pip freeze > requirements.txt
```

---

## License & Credits

- **yfinance**: Data from Yahoo Finance API
- **Streamlit**: Web app framework
- **OpenAI**: AI analysis (optional)
- **pandas**: Data handling

---

## Summary

**Stock Analyzer** is a complete stock analysis platform combining:
- Real-time market data ✓
- Technical analysis ✓
- Fundamental data ✓
- AI-powered insights ✓ (optional)

Simply run `streamlit run app.py` and start analyzing!

For questions or issues, check the [Troubleshooting](#troubleshooting) section above.
