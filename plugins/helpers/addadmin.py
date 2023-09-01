from pyrogram import Client, filters
from pyrogram.types import ChatMember
from info import *

# Define the add_admins command handler
@@Client.on_message(filters.command("add_admins") & filters.user(ADMINS))
async def add_admins(client, message):
    is_admin = message.from_user and message.from_user.id in ADMINS

    if len(message.command) != 3:
        await message.reply("Usage: /add_admin user_id channel_id")
        return

    user_id = int(message.command[1])
    channel_id = int(message.command[2])

    try:
        await client.promote_chat_member(
            chat_id=channel_id,
            user_id=user_id,
            is_admin=True,
            can_change_info=True,
            can_post_messages=True,
            can_edit_messages=True,
            can_delete_messages=True,
            can_invite_users=True,
            can_restrict_members=True,
            can_pin_messages=True,
            can_promote_members=True
        )
        await message.reply(f"Admin with user ID {user_id} added to the channel with custom privileges.")
    except Exception as e:
        await message.reply(f"An error occurred: {str(e)}")

