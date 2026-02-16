"""Top-level Streamlit entrypoint.

Run with: `streamlit run app.py` from the project root.
This file is the Streamlit script so the `pages/` directory is discovered
automatically by Streamlit.
"""
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.set_page_config(page_title="Stock App", layout="wide")
st.title("📈 Stock Analyzer")

with st.sidebar:
    st.header("Navigation")
    st.write("Use the Streamlit Pages on the left:")
    st.write("- **Compare**: Multi-stock comparison")
    st.write("- **Deep Dive**: Single stock analysis")
    st.divider()
    st.caption("v1.0 - No authentication required")

# Welcome section
st.markdown("""
# Welcome to Stock Analyzer

A comprehensive tool for stock market analysis combining real-time data, technical indicators, and AI-powered insights.
""")

# Key Features
st.header("✨ Key Features")
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("📊 Compare Stocks")
    st.write("Analyze multiple stocks side-by-side with technical metrics and charts.")

with col2:
    st.subheader("🔍 Deep Dive")
    st.write("Detailed analysis of individual stocks with fundamentals and technicals.")

with col3:
    st.subheader("🤖 AI Analysis")
    st.write("Optional Google Gemini-powered insights (requires API key).")

# Project Overview
with st.expander("📖 Project Overview", expanded=False):
    st.markdown("""
    **Stock Analyzer** is a Streamlit-based web application for analyzing and comparing stocks with:
    
    - **Real-time market data** from Yahoo Finance
    - **Technical indicators** (RSI, Moving Averages, Trend analysis)
    - **Fundamental metrics** (P/E ratios, dividend yield, market cap)
    - **Interactive charts** for daily and intraday price movements
    - **Optional AI analysis** using Google Gemini (requires API key)
    
    ### How It Works
    1. Select a page from the sidebar (Compare or Deep Dive)
    2. Enter stock ticker(s) (e.g., AAPL, MSFT, GOOGL)
    3. View technical and fundamental data
    4. Generate AI analysis (optional)
    """)

# Technical Indicators
with st.expander("📐 Technical Indicators Explained", expanded=False):
    st.markdown("""
    ### RSI (Relative Strength Index)
    - **Range**: 0-100
    - **RSI > 70**: Overbought (may pull back)
    - **RSI < 30**: Oversold (may bounce)
    - **Formula**: `100 - (100 / (1 + RS))` where `RS = avg_gain / avg_loss`
    
    ### Moving Averages
    - **MA20**: Average of last 20 closing prices (short-term trend)
    - **MA50**: Average of last 50 closing prices (medium-term trend)
    - **MA200**: Average of last 200 closing prices (long-term trend)
    - **Price > MA**: Uptrend • **Price < MA**: Downtrend
    
    ### Trend Slope
    - **Positive slope**: Upward trend
    - **Negative slope**: Downward trend
    - **Calculated over**: Last 60 trading days
    """)

# Getting Started
with st.expander("🚀 Getting Started", expanded=False):
    st.markdown("""
    ### Step 1: Compare Multiple Stocks
    1. Click **Compare** in the left sidebar
    2. Enter tickers (comma-separated): `AAPL,MSFT,GOOGL`
    3. View comparison table, charts, and technical metrics
    4. (Optional) Click "Generate Analysis" for AI insights
    
    ### Step 2: Deep Dive into One Stock
    1. Click **Deep Dive** in the left sidebar
    2. Enter a single ticker: `AAPL`
    3. View fundamentals, technicals, and charts
    4. (Optional) Click "Run Deep Analysis" for detailed AI analysis
    
    ### Step 3: Enable Gemini AI Analysis (Optional)
    1. Get a Gemini API key from: https://aistudio.google.com/app/apikey
    2. Open `.env` file in project root
    3. Replace `paste-your-API-key-here` with your actual key:
       ```
       GEMINI_API_KEY = "your-actual-key-here"
       ```
    4. Restart the app
    5. AI analysis will now work on both pages
    """)

# File Structure
with st.expander("📁 Project File Structure", expanded=False):
    st.markdown("""
    ```
    stocks_analyise/
    ├── app.py                    # Main entry point (this file)
    ├── data.py                   # Stock data & technical analysis
    ├── requirements.txt          # Dependencies
    ├── README.md                 # Full documentation
    │
    ├── lib/
    │   ├── __init__.py
    │   ├── auth.py               # Auth (unused - removed)
    │   ├── app.py                # Alt app config
    │   └── llm.py                # OpenAI integration
    │
    └── pages/
        ├── 1_Compare.py          # Multi-stock comparison
        └── 2_Deep_Dive.py        # Single stock analysis
    ```
    """)

# Data Sources
with st.expander("📊 Data Sources", expanded=False):
    st.markdown("""
    ### Yahoo Finance (yfinance)
    - **Stock prices**: OHLCV (Open, High, Low, Close, Volume)
    - **Fundamentals**: P/E ratio, market cap, sector, dividend
    - **History**: Up to 5 years of daily/intraday data
    
    ### Google Gemini (Optional)
    - **Model**: gemini-pro
    - **Input**: Company fundamentals + recent price action
    - **Output**: JSON analysis with verdict, strengths, risks, technical insights
    
    ### Caching
    - **Market data**: Cached for 60 seconds (1 min)
    - **Fundamentals**: Cached for 6 hours
    - Improves speed & reduces API rate limit hits
    """)

# Configuration
with st.expander("⚙️ Configuration & Setup", expanded=False):
    st.markdown("""
    ### Install Dependencies
    ```bash
    pip install -r requirements.txt
    ```
    
    ### Enable Gemini (Optional)
    
    **Option 1: Using .env file (Recommended)**
    1. Open `.env` file in project root
    2. Add your Gemini API key:
       ```
       GEMINI_API_KEY = "your-key-here"
       ```
    3. Restart app
    
    **Option 2: Streamlit Secrets**
    1. Create: `C:\\Users\\Dell\\.streamlit\\secrets.toml`
    2. Add: `GEMINI_API_KEY = "your-key"`
    3. Restart app
    
    **Get Gemini API Key**: https://aistudio.google.com/app/apikey
    (Free tier available)
    
    ### Run the App
    ```bash
    cd C:\\Users\\Dell\\stocks_analyise
    streamlit run app.py
    ```
    """)

# Troubleshooting
with st.expander("🔧 Troubleshooting", expanded=False):
    st.markdown("""
    ### "No data." in charts
    - Ticker may not exist or have no data
    - Try a major ticker: AAPL, MSFT, GOOGL
    
    ### Gemini not working
    - Check if API key is in `.env` file or Streamlit secrets
    - Visit https://aistudio.google.com/app/apikey to generate/verify key
    - App works fine without Gemini (AI analysis just won't run)
    
    ### Slow data fetching
    - Use shorter periods (1y instead of 5y)
    - Compare fewer stocks at once
    - Data is cached—subsequent loads are fast
    
    ### "ModuleNotFoundError"
    - Run: `pip install -r requirements.txt`
    - Ensure you're in correct directory: `C:\\Users\\Dell\\stocks_analyise`
    """)

# Footer
st.divider()
st.markdown("""
<div style='text-align: center'>
    <p>📚 <b>Full Documentation:</b> See <code>README.md</code> in project root</p>
    <p style='color: gray; font-size: 12px'>Stock Analyzer v1.0 | Data from Yahoo Finance | AI powered by Google Gemini</p>
</div>
""", unsafe_allow_html=True)
