from pyrogram import Client, filters
from pyrogram.types import ChatPrivileges
from pyrogram.errors import UserAdminInvalid
from info import *

# Define your custom privileges
privileges = ChatPrivileges(
    can_manage_chat=True,             # Replace with your desired permissions
    can_delete_messages=True,
    can_manage_video_chats=True,
    can_restrict_members=True,
    can_promote_members=True,
    can_change_info=True,
    can_post_messages=True,
    can_edit_messages=True,
    can_invite_users=True,
    can_pin_messages=True,
    is_anonymous=False  # Adjust as needed
)

# Define the add_admins command handler
@Client.on_message(filters.command("add_admins") & filters.user(ADMINS))
async def add_admins(client, message):
    if len(message.command) != 3:
        await message.reply("Usage: /add_admin <user_id> <channel_id>")
        return

    user_id = int(message.command[1])
    channel_id = int(message.command[2])

    try:
        await client.add_chat_members(
            channel_id,
            user_id,
            privileges
        )
        await message.reply(f"Admin with user ID {user_id} added to the channel with custom privileges.")
    except UserAdminInvalid:
        await message.reply("Invalid user ID or user is already an admin.")
    except Exception as e:
        await message.reply(f"An error occurred: {str(e)}")
