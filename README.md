# 🤖 FMAnalyzerBot

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Telegram Bot](https://img.shields.io/badge/Telegram-Bot-blue.svg?logo=telegram)](https://core.telegram.org/bots)
[![Status: Active Development](https://img.shields.io/badge/Status-Active%20Development-green.svg)]()

AI-powered Telegram bot for cryptocurrency trading analysis featuring real-time MEXC market data, ClickHouse data warehouse, VectorBT backtesting engine, machine learning predictions, and agentic AI system.

> 🚀 **Production-ready Python fintech platform** for algorithmic trading research and automation.

---

## 📋 Table of Contents

- [Features](#-features)
- [Architecture](#-architecture)
- [Demo](#-demo)
- [Quick Start](#-quick-start)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Project Roadmap](#-project-roadmap)
- [Technology Stack](#-technology-stack)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## ✨ Features

### Current Features (Phase 1 ✅)

- 🤖 **Telegram Bot Interface**
  - Webhook mode for instant responses (<100ms latency)
  - Natural language command processing
  - Real-time notifications and alerts
  - Multi-user support

- 🔄 **CI/CD Pipeline**
  - Automated deployments via Bitbucket Pipelines
  - Zero-downtime updates
  - Production-grade infrastructure (Nginx, SSL, systemd)

### In Development (Phase 2 🔄)

- 📊 **MEXC Data Pipeline**
  - Real-time market data ingestion (5-minute intervals)
  - Historical data download (18+ months)
  - Support for multiple cryptocurrencies
  - Trade-by-trade data for order flow analysis

- 🗄️ **ClickHouse Data Warehouse**
  - Optimized columnar storage (10x compression)
  - Lightning-fast aggregation queries (<100ms)
  - Materialized views for multiple timeframes (1h, 4h, 1d)
  - 2+ years data retention

### Coming Soon (Phases 3-6 📅)

- 📈 **VectorBT Backtesting Engine**
  - Vectorized strategy testing (100x faster)
  - Pre-built strategies (MA crossover, RSI, MACD, Bollinger Bands)
  - Parameter optimization
  - Performance metrics (Sharpe ratio, max drawdown, win rate)

- 🤖 **Machine Learning Models**
  - LSTM price prediction
  - Sentiment analysis (news + social media)
  - Pattern recognition (chart patterns)
  - Risk assessment models

- 🧠 **Agentic AI System**
  - Market Analysis Agent
  - Sentiment Analysis Agent
  - Risk Management Agent
  - Signal Generation Agent
  - Research Agent
  - Orchestrated via LangChain + OpenRouter

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────┐
│              USER INTERFACE (Telegram)              │
│   Natural language commands & real-time alerts      │
└─────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────┐
│          DATA LAYER (MEXC + ClickHouse)             │
│  • Real-time market data from MEXC API              │
│  • Historical data warehouse (ClickHouse)           │
│  • 5-minute candles → Multiple timeframes           │
└─────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────┐
│         ANALYSIS LAYER (VectorBT + ML)              │
│  • Backtesting engine (VectorBT)                    │
│  • Technical indicators (RSI, MACD, etc.)           │
│  • ML models for price prediction                   │
└─────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────┐
│        AI LAYER (Agentic AI System)                 │
│  • Multiple specialized agents                       │
│  • Sentiment analysis agent                          │
│  • Risk management agent                             │
│  • Signal generation agent                           │
│  • Orchestrated via LangChain                       │
└─────────────────────────────────────────────────────┘
```

### System Components

```
fmanalyzerbot/
├── bot.py                      # Main Telegram bot
├── config/
│   ├── settings.py            # Centralized configuration
│   └── clickhouse_schema.sql # Database schema
├── services/
│   ├── mexc_client.py        # MEXC API wrapper
│   ├── clickhouse_client.py  # Database connector
│   ├── data_pipeline.py      # ETL logic
│   └── vectorbt_engine.py    # Backtesting (Phase 3)
├── handlers/
│   ├── market_commands.py    # /analyze, /price
│   └── backtest_commands.py  # /backtest, /optimize
├── models/                    # ML models (Phase 4)
├── agents/                    # Agentic AI (Phase 5)
└── scripts/
    ├── download_historical.py
    └── sync_live_data.py
```

---

## 🎥 Demo

### Current Bot Interface

```
User: /start

Bot: 🤖 Welcome to FMAnalyzerBot!

I'm your AI-powered crypto trading assistant.

Commands:
/start - Show this message
/ping - Health check
/analyze [SYMBOL] - Market analysis (coming soon)
```

### Coming Soon: AI Analysis

```
User: /analyze SOLUSDT

Bot: 📊 SOL/USDT Analysis
━━━━━━━━━━━━━━━━
Price: $145.32 (+2.3%)

Technical: BULLISH 📈
• RSI: 65 (Neutral)
• MACD: Bullish crossover
• Support: $140 | Resistance: $150

Sentiment: POSITIVE 😊
• News score: 7.5/10
• Social: Trending #4

Signal: BUY 🟢
Confidence: 78%
Entry: $143-$147
```

*(Screenshots coming soon)*

---

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- Telegram account
- MEXC account (for API access)
- ClickHouse Cloud account (free trial available)

### 1. Clone the Repository

```bash
git clone https://github.com/mohsinds/fmanalyzerbot.git
cd fmanalyzerbot
```

### 2. Create Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment

```bash
cp .env.example .env
nano .env  # Edit with your credentials
```

Required environment variables:
```bash
TELEGRAM_BOT_TOKEN=your_bot_token_from_botfather
CLICKHOUSE_HOST=your_instance.clickhouse.cloud
CLICKHOUSE_PASSWORD=your_password
```

### 5. Run the Bot

```bash
# Polling mode (for development)
python bot.py

# Webhook mode (for production)
python bot.py --webhook
```

### 6. Test in Telegram

Open Telegram, search for your bot, and send `/start`!

---

## 📦 Installation

### Development Setup (Local)

```bash
# 1. Clone repository
git clone https://github.com/mohsinds/fmanalyzerbot.git
cd fmanalyzerbot

# 2. Set up environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure
cp .env.example .env
# Edit .env with your credentials

# 5. Initialize database
python scripts/init_database.py

# 6. Download historical data (optional)
python scripts/download_historical.py

# 7. Run bot
python bot.py
```

### Production Deployment (Server)

**Recommended:** AlmaLinux 9 / Ubuntu 22.04 / Debian 12

```bash
# 1. Install system dependencies
sudo dnf install python3 python3-pip nginx certbot  # AlmaLinux
# OR
sudo apt install python3 python3-pip nginx certbot  # Ubuntu/Debian

# 2. Clone and setup
git clone https://github.com/mohsinds/fmanalyzerbot.git /opt/fmab
cd /opt/fmab
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 3. Configure systemd service
sudo cp deploy/fmab.service /etc/systemd/system/
sudo systemctl enable fmab
sudo systemctl start fmab

# 4. Setup Nginx + SSL (webhook mode)
sudo cp deploy/nginx.conf /etc/nginx/sites-available/fmab
sudo ln -s /etc/nginx/sites-available/fmab /etc/nginx/sites-enabled/
sudo certbot --nginx -d api.yourdomain.com
sudo systemctl restart nginx

# 5. Verify
sudo systemctl status fmab
sudo journalctl -u fmab -f
```

### Docker Deployment (Coming Soon)

```bash
docker pull mohsinds/fmanalyzerbot:latest
docker run -d --env-file .env mohsinds/fmanalyzerbot
```

---

## ⚙️ Configuration

### Environment Variables

Create `.env` file with the following:

```bash
# ===== Telegram Bot =====
TELEGRAM_BOT_TOKEN=123456789:AAH_your_token_from_botfather
WEBHOOK_URL=https://api.yourdomain.com/webhook  # For webhook mode
PORT=8443  # For webhook mode
ENV=production  # or development

# ===== MEXC API =====
MEXC_API_KEY=optional_for_public_data
MEXC_SECRET_KEY=optional_for_public_data

# ===== ClickHouse =====
CLICKHOUSE_HOST=your-instance.clickhouse.cloud
CLICKHOUSE_PORT=8443
CLICKHOUSE_USER=default
CLICKHOUSE_PASSWORD=your_password
CLICKHOUSE_DATABASE=fmanalyzer

# ===== AI / ML (Phase 4+) =====
OPENROUTER_API_KEY=your_openrouter_key
OPENAI_API_KEY=your_openai_key  # For embeddings

# ===== Data Pipeline =====
PRIMARY_SYMBOL=SOLUSDT
KLINE_INTERVAL=5m
SYNC_INTERVAL_SECONDS=300
```

### ClickHouse Schema

Initialize database schema:

```bash
python scripts/init_database.py
```

Or manually execute:

```bash
clickhouse-client --host your-host --secure \
  --user default --password your_password \
  --query "$(cat config/clickhouse_schema.sql)"
```

---

## 💡 Usage

### Telegram Bot Commands

#### Current Commands (Phase 1)

```
/start - Welcome message and bot introduction
/help - Show all available commands
/ping - Health check (verify bot is running)
```

#### Data Commands (Phase 2)

```
/download [SYMBOL] - Download latest market data
/status - Show database statistics
/query [SYMBOL] [TIMEFRAME] - Query historical data
```

#### Analysis Commands (Phase 3-4)

```
/analyze [SYMBOL] - AI-powered market analysis
/predict [SYMBOL] - Price prediction
/sentiment [SYMBOL] - Sentiment analysis
/backtest [STRATEGY] [SYMBOL] - Run backtest
/optimize [STRATEGY] - Optimize strategy parameters
```

#### Trading Commands (Phase 5-6)

```
/signal [SYMBOL] - Trading signal with confidence score
/risk [POSITION] - Risk assessment for position
/portfolio - View portfolio performance
/alert [SYMBOL] [CONDITION] - Set price alert
```

### Python API Usage

```python
from services.mexc_client import MEXCClient
from services.clickhouse_client import ClickHouseClient

# Initialize clients
mexc = MEXCClient()
ch = ClickHouseClient()

# Download historical data
klines = mexc.get_historical_klines(
    symbol="SOLUSDT",
    interval="5m",
    start_date=datetime(2024, 1, 1),
    end_date=datetime.now()
)

# Store in ClickHouse
ch.insert_klines("SOLUSDT", klines)

# Query data
df = ch.query_klines(
    symbol="SOLUSDT",
    start_date="2024-01-01",
    end_date="2024-12-31",
    interval="1d"
)
```

### VectorBT Strategy Example (Phase 3)

```python
import vectorbt as vbt
from services.clickhouse_client import ClickHouseClient

# Load data
ch = ClickHouseClient()
data = ch.query_klines("SOLUSDT", "2024-01-01", "2024-12-31", "1h")

# Define strategy
fast_ma = vbt.MA.run(data['close'], 20)
slow_ma = vbt.MA.run(data['close'], 50)

entries = fast_ma.ma_crossed_above(slow_ma)
exits = fast_ma.ma_crossed_below(slow_ma)

# Backtest
portfolio = vbt.Portfolio.from_signals(
    data['close'],
    entries,
    exits,
    init_cash=10000,
    fees=0.001
)

# Results
print(f"Total Return: {portfolio.total_return():.2%}")
print(f"Sharpe Ratio: {portfolio.sharpe_ratio():.2f}")
print(f"Max Drawdown: {portfolio.max_drawdown():.2%}")
```

---

## 🗺️ Project Roadmap

### ✅ Phase 1: Foundation (Completed)
**Timeline: Weeks 1-2**

- [x] Telegram bot setup (polling mode)
- [x] CI/CD pipeline (Bitbucket Pipelines)
- [x] Migration to webhooks (production-ready)
- [x] Server infrastructure (Nginx, SSL, systemd)
- [x] Open-source repository setup

### 🔄 Phase 2: Data Pipeline (In Progress)
**Timeline: Weeks 3-4**

- [x] MEXC API integration
- [x] ClickHouse schema design
- [ ] Historical data download (18 months)
- [ ] Real-time data sync (cron job every 5 min)
- [ ] Data quality validation
- [ ] Commands: `/download`, `/status`, `/query`

### 📊 Phase 3: Backtesting Engine (Next)
**Timeline: Weeks 5-6**

- [ ] VectorBT integration
- [ ] Pre-built strategies (MA, RSI, MACD, BB)
- [ ] Custom strategy builder
- [ ] Performance metrics dashboard
- [ ] Parameter optimization engine
- [ ] Commands: `/backtest`, `/optimize`, `/compare`

### 🤖 Phase 4: Machine Learning Models
**Timeline: Weeks 7-9**

- [ ] LSTM price prediction model
- [ ] Sentiment analysis (news + social media)
- [ ] Pattern recognition (chart patterns)
- [ ] Risk assessment model
- [ ] Model training pipeline
- [ ] Commands: `/predict`, `/sentiment`, `/forecast`

### 🧠 Phase 5: Agentic AI System
**Timeline: Weeks 10-14**

- [ ] LangChain integration
- [ ] OpenRouter API setup
- [ ] Market Analysis Agent
- [ ] Sentiment Analysis Agent
- [ ] Risk Management Agent
- [ ] Signal Generation Agent
- [ ] Research Agent
- [ ] Agent orchestration
- [ ] Commands: `/analyze`, `/signal`, `/risk`, `/research`

### 🚀 Phase 6: Production Features
**Timeline: Ongoing**

- [ ] Multi-user portfolio tracking
- [ ] Custom alerts system
- [ ] Subscription tiers (free/premium)
- [ ] Web dashboard (React + FastAPI)
- [ ] Paper trading mode
- [ ] Real broker integration (via CCXT)
- [ ] Multi-asset support (stocks, forex)
- [ ] Mobile app (React Native)

---

## 🛠️ Technology Stack

### Core Technologies

| Component | Technology | Version |
|-----------|-----------|---------|
| **Programming Language** | Python | 3.9+ |
| **Bot Framework** | python-telegram-bot | 20.7 |
| **Data Source** | MEXC API | v3 |
| **Database** | ClickHouse Cloud | Latest |
| **Backtesting** | VectorBT | 0.26 |
| **ML Framework** | TensorFlow | 2.15 |
| **AI Orchestration** | LangChain | 0.1+ |
| **LLM Provider** | OpenRouter | Latest |
| **Web Server** | Nginx | 1.24+ |
| **Process Manager** | systemd | - |

### Dependencies

```txt
# Core
python-telegram-bot[webhooks]==20.7
python-dotenv==1.0.1

# Data Pipeline
requests==2.31.0
pandas==2.1.4
numpy==1.26.3
clickhouse-connect==0.7.0
ccxt==4.2.0

# Backtesting
vectorbt==0.26.0
ta-lib==0.4.28

# Machine Learning
tensorflow==2.15.0
scikit-learn==1.4.0
transformers==4.36.0

# Agentic AI
langchain==0.1.0
openai==1.10.0
chromadb==0.4.20
```

### Infrastructure

```yaml
Production:
  Server: Hetzner Cloud CX21 (2 vCPU, 4GB RAM)
  OS: AlmaLinux 9.4
  Web Server: Nginx (reverse proxy)
  SSL: Let's Encrypt (auto-renewal)
  Process Manager: systemd
  Database: ClickHouse Cloud (managed)
  CI/CD: Bitbucket Pipelines

Development:
  IDE: PyCharm / VS Code
  Version Control: Git + GitHub
  Testing: pytest
  Code Quality: black + flake8
```

---

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) first.

### How to Contribute

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes**
   ```bash
   # Write code
   # Add tests
   # Update documentation
   ```
4. **Commit your changes**
   ```bash
   git commit -m "Add amazing feature"
   ```
5. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
6. **Open a Pull Request**

### Contribution Areas

- 🐛 **Bug Fixes**: Report or fix bugs
- 📊 **Trading Strategies**: New VectorBT strategies
- 🤖 **AI Agents**: Additional specialized agents
- 📈 **Technical Indicators**: New indicators
- 📝 **Documentation**: Improve docs and tutorials
- 🌍 **Translations**: Internationalization
- 🎨 **UI/UX**: Web dashboard improvements
- ✅ **Tests**: Increase test coverage

### Code Style

We use:
- **black** for code formatting
- **flake8** for linting
- **mypy** for type checking

Run before committing:
```bash
black .
flake8 .
mypy .
pytest
```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**TL;DR:** You can use, modify, and distribute this software freely, even for commercial purposes. Just include the original license and copyright notice.

---

## 👤 Contact

**Mohsin DS**  
Principal Full-Stack Software Engineer | Founder @ Dimensional Sys Inc.

- 💼 LinkedIn: [linkedin.com/in/mohsinds](https://linkedin.com/in/mohsinds)
- 🐦 Twitter: [@mohsinds](https://twitter.com/mohsinds)
- 📧 Email: mohsin@dimensionalsys.com
- 🌐 Website: [dimensionalsys.com](https://dimensionalsys.com)
- 💬 Telegram Bot: [@fmanalyzer_bot](https://t.me/fmanalyzer_bot)

---

## 🙏 Acknowledgments

- **Telegram Bot API** - Excellent bot framework
- **MEXC Exchange** - Free historical data access
- **ClickHouse** - Lightning-fast analytics database
- **VectorBT Community** - Backtesting inspiration
- **LangChain** - Agent framework
- **Open Source Community** - For making this possible

---

## 📊 Project Stats

![GitHub stars](https://img.shields.io/github/stars/mohsinds/fmanalyzerbot?style=social)
![GitHub forks](https://img.shields.io/github/forks/mohsinds/fmanalyzerbot?style=social)
![GitHub issues](https://img.shields.io/github/issues/mohsinds/fmanalyzerbot)
![GitHub pull requests](https://img.shields.io/github/issues-pr/mohsinds/fmanalyzerbot)
![Last commit](https://img.shields.io/github/last-commit/mohsinds/fmanalyzerbot)

---

## 🌟 Support the Project

If you find this project useful, please:

- ⭐ **Star this repository**
- 🍴 **Fork and contribute**
- 📢 **Share with others**
- 🐛 **Report bugs**
- 💡 **Suggest features**

---

<div align="center">

**Built with ❤️ by developers, for traders**

[Documentation](https://github.com/mohsinds/fmanalyzerbot/wiki) • [Report Bug](https://github.com/mohsinds/fmanalyzerbot/issues) • [Request Feature](https://github.com/mohsinds/fmanalyzerbot/issues)

</div>