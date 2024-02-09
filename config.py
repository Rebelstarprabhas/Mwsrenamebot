# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "25188430")

API_HASH = os.environ.get("API_HASH", "bb109bec058bcc4927dc59dde7088436")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6256178441:AAHNzoTTKCr21lRU4-GnSYnjgcc9MGFmqsk") 

FORCE_SUB = os.environ.get("FORCE_SUB", "Mws_Files") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "prabhas")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://prabhas:prabhas@prabhas.ek96nec.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/bad2719e7e70e4496fd3a.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1345691152').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
