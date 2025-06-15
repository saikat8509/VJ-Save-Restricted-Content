import os
from urllib.parse import quote_plus

# Bot token from @BotFather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "23584757"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "ac9926d2cb8acc38413f5e93881fd514")

# Your Owner / Admin ID for Broadcast
ADMINS = int(os.environ.get("ADMINS", "7616562927"))

# MongoDB credentials
MONGO_USERNAME = os.environ.get("MONGO_USERNAME", "creazysaikat")
MONGO_PASSWORD = os.environ.get("MONGO_PASSWORD", "Saikat9735")
MONGO_CLUSTER = os.environ.get("MONGO_CLUSTER", "cluster0.y2ku5.mongodb.net")

# Encode username and password
encoded_username = quote_plus(MONGO_USERNAME)
encoded_password = quote_plus(MONGO_PASSWORD)

# Use standard mongodb:// URI to avoid SRV DNS issues
DB_URI = os.environ.get("DB_URI", f"mongodb://{encoded_username}:{encoded_password}@{MONGO_CLUSTER}:27017/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# Target channel ID or username for forwarding content
TARGET_CHANNEL = os.environ.get("TARGET_CHANNEL", "")  # e.g., "-1001234567890" or "@YourChannel"

# Enable/disable error messages in personal chats
ERROR_MESSAGE = bool(os.environ.get("ERROR_MESSAGE", True))
