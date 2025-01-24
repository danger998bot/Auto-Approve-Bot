from os import environ

API_ID = int(environ.get("API_ID", "25325861"))
API_HASH = environ.get("API_HASH", "d945b8c295a892802530fe808bde0d76")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

AUTH_CHANNEL = int(environ.get("AUTH_CHANNEL", "-1002354912335"))
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002431971886"))
ADMINS = int(environ.get("ADMINS", "7830741296"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "mongodb+srv://sibasundar826:3MWd1ecA55pC1hZM@cluster0.ferdl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = environ.get("DB_NAME", "autoacceptbot")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', True))
