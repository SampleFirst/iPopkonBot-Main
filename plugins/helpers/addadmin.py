from pyrogram import Client, filters
from pyrogram.types import ChatPermissions
from info import *


# Use the `on_message` decorator to handle commands
@Client.on_message(filters.command("add_admin") & filters.user(ADMINS))
async def add_admin(client, message):
    try:
        # Extract the chat ID and user ID from the message text
        chat_id, user_id = map(int, message.text.split()[1:])
    except (ValueError, IndexError):
        await message.reply("Invalid command format. Use /add_admin <chat_id> <user_id>")
        return

    # Create chat permissions with almost admin privileges
    permissions = ChatPermissions(
        can_send_messages=True,
        can_send_media_messages=True,
        can_send_polls=True,
        can_send_other_messages=True,
        can_add_web_page_previews=True,
        can_change_info=True,
        can_invite_users=True,
        can_pin_messages=True
    )

    # Promote the user to admin with the defined permissions
    await client.promote_chat_member(
        chat_id=chat_id,
        user_id=user_id,
        permissions=permissions,
    )

    await message.reply(f"User {user_id} has been promoted to admin in chat {chat_id}")
    
