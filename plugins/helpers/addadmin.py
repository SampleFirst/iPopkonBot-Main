from pyrogram import Client, filters
from pyrogram.types import ChatPrivileges
from info import *


# Define the add_admins command handler
@Client.on_message(filters.command("add_admins") & filters.user(ADMINS))
async def add_admins(client, message):
    try:
        # Get the chat ID and user ID from the message text
        chat_id = message.chat.id
        user_id = int(message.text.split(" ")[1])

        # Define desired chat permissions for the new admin
        privileges = chat_privileges(
            can_change_info=True,
            can_post_messages=True,
            can_edit_messages=True,
            can_delete_messages=True,
            can_restrict_members=True,
            can_invite_users=True,
            can_pin_messages=True,
            can_promote_members=True,
            can_manage_video_chats=True,
            can_manage_chat=True
        )

        # Promote the user to admin with desired permissions
        await client.promote_chat_member(chat_id, user_id, ChatPrivileges=privileges)

        await message.reply("User has been added as an admin.")
    except Exception as e:
        await message.reply(f"An error occurred: {str(e)}")
