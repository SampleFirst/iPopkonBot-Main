import time  # Import the 'time' module separately
import datetime
from pyrogram import Client, filters
from info import ADMINS 

@Client.on_message(filters.command("showtime") & filters.user(ADMINS))
def show_time(client, message):
    chat_id = message.chat.id

    while True:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        client.send_message(chat_id, f"Current Date and Time: {current_time}")
        time.sleep(1)  # Use the 'time' module for sleep
