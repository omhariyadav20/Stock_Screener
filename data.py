from typing import Dict, Any, Optional
import numpy as np
import pandas as pd
import yfinance as yf
import streamlit as st


def compute_rsi(close: pd.Series, period: int = 14) -> pd.Series:
    delta = close.diff()
    gain = delta.clip(lower=0).rolling(period).mean()
    loss = (-delta.clip(upper=0)).rolling(period).mean()
    rs = gain / loss.replace(0, np.nan)
    return 100 - (100 / (1 + rs))


def compute_technicals(hist: pd.DataFrame) -> Dict[str, Any]:
    if hist is None or hist.empty or "Close" not in hist:
        return {}

    close = hist["Close"].dropna()
    if close.empty:
        return {}

    out: Dict[str, Any] = {}
    out["last_close"] = float(close.iloc[-1])
    out["ma20"] = float(close.rolling(20).mean().iloc[-1]) if len(close) >= 20 else None
    out["ma50"] = float(close.rolling(50).mean().iloc[-1]) if len(close) >= 50 else None
    out["ma200"] = float(close.rolling(200).mean().iloc[-1]) if len(close) >= 200 else None

    rsi = compute_rsi(close, 14)
    out["rsi14"] = float(rsi.iloc[-1]) if len(rsi.dropna()) else None

    if len(close) >= 60:
        y = close.iloc[-60:].values
        x = np.arange(len(y))
        out["trend_slope_60"] = float(np.polyfit(x, y, 1)[0])
    else:
        out["trend_slope_60"] = None

    return out


@st.cache_data(ttl=60, show_spinner=False)
def fetch_history(ticker: str, period: str, interval: str) -> pd.DataFrame:
    t = yf.Ticker(ticker)
    return t.history(period=period, interval=interval, auto_adjust=False)


@st.cache_data(ttl=6 * 60 * 60, show_spinner=False)
def fetch_fundamentals(ticker: str) -> Dict[str, Any]:
    t = yf.Ticker(ticker)
    info: Dict[str, Any] = {}
    try:
        info = t.get_info()
    except Exception:
        try:
            info = t.info
        except Exception:
            info = {}

    keys = [
        "shortName", "sector", "industry",
        "marketCap", "trailingPE", "forwardPE",
        "priceToBook", "dividendYield",
        "profitMargins", "operatingMargins",
        "revenueGrowth", "earningsGrowth",
        "beta",
        "fiftyTwoWeekHigh", "fiftyTwoWeekLow",
        "currency",
    ]
    return {k: info.get(k) for k in keys}


def build_summary_row(ticker: str,
                      fundamentals: Dict[str, Any],
                      tech_daily: Dict[str, Any],
                      tech_intra: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "ticker": ticker,
        "name": fundamentals.get("shortName"),
        "sector": fundamentals.get("sector"),
        "industry": fundamentals.get("industry"),
        "marketCap": fundamentals.get("marketCap"),
        "trailingPE": fundamentals.get("trailingPE"),
        "forwardPE": fundamentals.get("forwardPE"),
        "divYield": fundamentals.get("dividendYield"),
        "52wHigh": fundamentals.get("fiftyTwoWeekHigh"),
        "52wLow": fundamentals.get("fiftyTwoWeekLow"),
        "last_close_daily": tech_daily.get("last_close"),
        "ma20": tech_daily.get("ma20"),
        "ma50": tech_daily.get("ma50"),
        "ma200": tech_daily.get("ma200"),
        "rsi14": tech_daily.get("rsi14"),
        "last_price_intraday": tech_intra.get("last_close"),
    }
