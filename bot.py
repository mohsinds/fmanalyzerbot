import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Configuration
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL", "https://fmabapi.finnmetrics.com/webhook")
PORT = int(os.getenv("PORT", 8443))
ENV = os.getenv("ENV", "production")


# Command handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Welcome message"""
    await update.message.reply_text(
        "🤖 *FMAnalyzerBot is Live!*\n\n"
        "Mode: Webhook\n"
        "Commands:\n"
        "/start - Show this message\n"
        "/ping - Health check\n"
        "/analyze - Market analysis (coming soon)",
        parse_mode="Markdown"
    )


async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Health check"""
    await update.message.reply_text(f"✅ pong | ENV: {ENV} | Mode: Webhook")


async def analyze(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Future: Market analysis placeholder"""
    await update.message.reply_text(
        "📊 Market analysis feature coming soon!\n\n"
        "Will integrate:\n"
        "• MEXC API\n"
        "• Sentiment Analysis\n"
        "• ClickHouse Data Warehouse\n"
        "• VectorBT Backtesting"
    )


async def post_init(application: Application) -> None:
    """Set webhook after application initialization"""
    await application.bot.set_webhook(url=WEBHOOK_URL)
    logger.info(f"✅ Webhook set to: {WEBHOOK_URL}")


def main():
    """Start the bot in webhook mode"""
    if not TOKEN:
        raise RuntimeError("TELEGRAM_BOT_TOKEN is missing in .env")

    logger.info(f"🚀 Starting FMAnalyzerBot in webhook mode...")
    logger.info(f"📡 Webhook URL: {WEBHOOK_URL}")
    logger.info(f"🔌 Listening on 0.0.0.0:{PORT}")

    # Build application
    application = Application.builder().token(TOKEN).post_init(post_init).build()

    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("ping", ping))
    application.add_handler(CommandHandler("analyze", analyze))

    # Start webhook
    application.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path="webhook",
        webhook_url=WEBHOOK_URL,
        drop_pending_updates=True
    )


if __name__ == "__main__":
    main()