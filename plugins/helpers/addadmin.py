from pyrogram import Client, filters
from pyrogram.types import ChatPrivileges
import asyncio
from info import ADMINS 


# Define the add_admins command handler
@Client.on_message(filters.command("add_admins") & filters.user("ADMINS"))
async def add_admins_command(client, message):
    try:
        # Get the chat ID and user ID from the message text
        chat_id = message.chat.id
        user_id = message.text.split(" ")[1]

        # Promote the user to admin with desired privileges
        privileges = ChatPrivileges(
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

        result = await client.promote_chat_member(chat_id, user_id, privileges)

        if result:
            await message.reply("User has been added as an admin.")
        else:
            await message.reply("Failed to add user as an admin.")

    except Exception as e:
        await message.reply(f"An error occurred: {str(e)}")
 
