"""
Bot konfiguratsiyasi
"""

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Bot sozlamalari"""
    
    def __init__(self):
        self.BOT_TOKEN = os.getenv('BOT_TOKEN', '')
        
        if not self.BOT_TOKEN:
            raise ValueError(
                "BOT_TOKEN muhit o'zgaruvchisida topilmadi! "
                ".env faylini yaratib, BOT_TOKEN ni kiriting."
            )

