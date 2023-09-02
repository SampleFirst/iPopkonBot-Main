from pyrogram import Client, filters, enums
from pyrogram.types import ChatMember, ChatPrivileges
from info import *

# Define the add_admins command handler
@Client.on_message(filters.command("add_admins") & filters.user(ADMINS))
async def add_admins(client, message):
    if len(message.command) != 3:
        await message.reply("Usage: /add_admins user_id channel_id")
        return

    user_id = int(message.command[1])
    channel_id = int(message.command[2])
    
    try:
        # Get the user and chat objects
        user = await client.get_users(user_id)
        chat = await client.get_chat(channel_id)

        # Create a ChatMember object with custom privileges
        admin_member = ChatMember(
            status=enums.ChatMemberStatus.ADMINISTRATOR,
            user=user,
            chat=chat,
            can_be_edited=True,
            can_promote_members=True  # Set the privilege directly
        )

        # Promote the user to an administrator
        await client.promote_chat_member(channel_id, user_id, admin_member)

        await message.reply(f"Admin with user ID {user_id} added to the channel with custom privileges and can be edited.")
    except Exception as e:
        await message.reply(f"An error occurred: {str(e)}")
