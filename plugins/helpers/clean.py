from pyrogram import Client, filters
from pyrogram.types import Message
from info import *

# Define a command handler to listen for admin commands
@Client.on_message(filters.command("clean") & filters.user(ADMINS))
async def delete_all_messages(client, message: Message):
    try:
        # Check if the command has an argument (chat_id)
        if len(message.command) != 2:
            await message.reply_text("Please provide a valid chat ID.")
            return

        # Get the chat ID from the command message
        chat_id = int(message.command[1])

        # Get the list of messages in the chat
        chat = await client.get_chat(chat_id)
        messages = await client.get_history(chat.id)

        # Iterate through the messages and delete them
        for msg in messages:
            await client.delete_messages(chat.id, msg.message_id)

        # Send a confirmation message
        await message.reply_text(f"All messages in chat {chat_id} have been deleted.")
    except Exception as e:
        # Handle any errors
        await message.reply_text(f"An error occurred: {str(e)}")
