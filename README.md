# Binance Futures Testnet Trading Bot

A Python-based CLI trading bot for Binance Futures Testnet that supports MARKET and LIMIT orders with logging, validation, and error handling.

---

## Features

- Place MARKET orders
- Place LIMIT orders
- BUY and SELL support
- Input validation
- Structured logging
- Exception handling
- Binance Futures Testnet integration
- Command Line Interface (CLI)

---

## Project Structure

```text
trading_bot/

bot/
│
├── __init__.py
├── client.py
├── orders.py
├── validators.py
├── logging_config.py
├── cli.py
│
├── .env
├── README.md
├── requirements.txt
└── logs.txt
```

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone <your-github-repo-url>
cd trading_bot
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure API Keys

Create `.env` file:

```env
API_KEY=your_api_key
SECRET_KEY=your_secret_key
```

---

## Binance Futures Testnet

Testnet Base URL:

https://testnet.binancefuture.com

---

## Run Examples

### MARKET Order

```bash
python bot/cli.py BTCUSDT BUY MARKET 0.001
```

---

### LIMIT Order

```bash
python bot/cli.py BTCUSDT BUY LIMIT 0.001 50000
```

---

## Sample Output

```text
===== ORDER REQUEST SUMMARY =====

Symbol      : BTCUSDT
Side        : BUY
Order Type  : MARKET
Quantity    : 0.001

===== ORDER RESPONSE =====

Order ID      : 123456
Status        : FILLED
Executed Qty  : 0.001

Order placed successfully
```

---

## Logging

Logs are stored in:

```text
logs.txt
```

---

## Assumptions

- Uses Binance Futures Testnet only
- LIMIT orders require price argument
- Internet connection required
- Testnet account must contain virtual balance

---

## Technologies Used

- Python 3
- python-binance
- Click
- python-dotenv
- Logging module
