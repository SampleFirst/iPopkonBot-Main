import time
import datetime
from pyrogram import Client, filters
from info import ADMINS

@Client.on_message(filters.command("showtime") & filters.user(ADMINS))
def show_time(client, message):
    chat_id = message.chat.id
    current_message = None

    while True:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if current_message is not None:
            try:
                client.edit_message_text(chat_id, current_message.message_id, f"Current Date and Time:\n{current_time}")
            except Exception as e:
                print(f"Error editing message: {e}")
        else:
            current_message = client.send_message(chat_id, f"Current Date and Time:\n{current_time}")
        
        time.sleep(1)
