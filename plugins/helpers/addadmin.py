from pyrogram import Client, filters
from pyrogram.types import ChatMember, ChatPrivileges
from info import *

# Define the add_admins command handler
@Client.on_message(filters.command("add_admins") & filters.user(ADMINS))
async def add_admins(client, message):
    if len(message.command) != 3:
        await message.reply("Usage: /add_admins <user_id> <channel_id>")
        return

    user_id = int(message.command[1])
    channel_id = int(message.command[2])
    
    try:
        # Create a ChatMember object with status ADMINISTRATOR
        admin_member = ChatMember(
            status=enums.ChatMemberStatus.ADMINISTRATOR,
            user=None,  # You can provide user information here if needed
            chat=None,  # You can provide chat information here if needed
            can_be_edited=False,  # Customize as needed
            privileges=ChatPrivileges(),  # Customize permissions as needed
        )

        await client.promote_chat_member(channel_id, user_id, admin_member)

        await message.reply(f"Admin with user ID {user_id} added to the channel with custom privileges.")
    except Exception as e:
        await message.reply(f"An error occurred: {str(e)}")
