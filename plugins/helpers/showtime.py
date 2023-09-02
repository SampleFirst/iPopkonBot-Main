import time
import datetime
from pyrogram import Client, filters
from info import ADMINS

# Define a global variable to track whether the loop should continue
should_continue = True

@Client.on_message(filters.command("showtime") & filters.user(ADMINS))
async def show_time(client, message):
    global should_continue  # Declare should_continue as a global variable
    chat_id = message.chat.id
    sent_message = await client.send_message(chat_id, "Initializing...")  # Initial message

    while should_continue:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        await client.edit_message_text(chat_id, sent_message.message_id, f"Current Date and Time: {current_time}")
        time.sleep(1)

@Client.on_message(filters.command("stopshowtime") & filters.user(ADMINS))
async def stop_show_time(client, message):
    global should_continue  # Declare should_continue as a global variable
    should_continue = False
    await client.send_message(message.chat.id, "Stopped updating time.")
