class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
OWNER_ID = "7524407228"
sudo_users = ["2054990632", "6606949931" , "6590287973" ,"6839571494" ,"1648076207"]
GROUP_ID = "-1001720134719"
TOKEN = "7500848496:AAG_qEjAZkzRCODLnjjDj7kg6tqyJjQVv00"
mongo_url = "mongodb+srv://wangling01:wangling@cluster0.trgu2ty.mongodb.net/?retryWrites=true&w=majority"
PHOTO_URL =  ["https://graph.org/file/f10bec6ec695bba69037d.jpg","https://graph.org/file/bdac0dcb5d841263a8866.jpg","https://telegra.ph/file/75e758e6e47453d301fcd.jpg","https://telegra.ph/file/75e758e6e47453d301fcd.jpg","https://telegra.ph/file/dba87ad2a7d957588b8de.jpg","https://telegra.ph/file/765c9474d372cf40621da.jpg","https://telegra.ph/file/1e55c00d0be79b7ca614d.jpg"]
SUPPORT_CHAT = "testbotarea"
UPDATE_CHAT = "bot_support_arena"
BOT_USERNAME = "Testjdjdjdjdbot"
CHARA_CHANNEL_ID = "-1002109838600"
api_id = "12380656"
api_hash = "d927c13beaaf5110f25c505b7c071273"
    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
