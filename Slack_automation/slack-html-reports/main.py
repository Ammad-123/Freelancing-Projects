
import time
import logging
from datetime import datetime
from app.orchestrator import ReportOrchestrator

# -------------------------
# Setup logging 
# -------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)

def main():
    logger.info("🚀 Automation Bot Started")
    logger.info("Waiting 1 minute before sending the report... ⏳")
    
    time.sleep(60)  # Wait for 1 minute

    try:
        logger.info("Starting ReportOrchestrator...")
        ReportOrchestrator().run()
        logger.info("✅ Report sent successfully!")
    except Exception as e:
        logger.error(f"❌ Failed to send report: {e}")

    logger.info("Automation run completed. Bot is still alive for demonstration purposes.")

if __name__ == "__main__":
    main()
