import os

import logging

class Config:                                                                   

    API_ID = int(os.environ.get("API_ID", "24720215"))

    API_HASH = os.environ.get("API_HASH", "c0d3395590fecba19985f95d6300785e")       

    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5858006797:AAHvD6U81nTd40oK5r_PSq0Q0HUWy__GVoI")

    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")

    OWNER_ID = os.environ.get("OWNER_ID", "6295565062")                             

    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://Nischaybot:Nischaybot@cluster0.thf9kzz.mongodb.net/?retryWrites=true&w=majority")  

    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")

    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')

    SESSION = os.environ.get("SESSION", "BQAKX3q_K-r2THsb_Ie78f7BRLZtIfVlPfC5sh5uEXE31mropah2BDnGyyZl5vBt99Ky9fh_ymCYDYxqTYUDb8nIwRg9MxStsd-OqNGqQXP3bCMMdgJ1aXYvtjoAXxc36BAkui8gu5ImmH6hh3Xhxog1SeE-nuOOKFnu89yAJJcHYKnVqJO4Av60RGta0NCkbhhukkwS7wuzxZaA_rVrTyQeo5_UlDV6Lm6duA9lmd3Pa6uo-LmgpAxnsFg_edm4ceZsOIxaKhCdGgcCow6UiTN9kMaur186C5YQQP-tpvD3c3Bb8JqJQ9qUCuvTaBHtGIbJXS94isgpvR1QZ382NeU5AAAAAXc-swYA")   

    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001553031624"))

    BOT_USERNAME= os.environ.get("BOT_USERNAME", "NY_Forward_robot")

def LOGGER(name: str) -> logging.Logger:

    return logging.getLogger(name)
