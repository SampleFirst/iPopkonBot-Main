from pyrogram import Client, filters
from pyrogram.types import ChatPermissions
from pyrogram.errors import UserAdminInvalid

from info import ADMINS

# Updated extract_user function to extract user details
def get_user_details(message):
    if message.reply_to_message:
        user = message.reply_to_message.from_user
    else:
        user = message.from_user

    user_id = user.id
    user_first_name = user.first_name

    return user_id, user_first_name

@Client.on_message(filters.command("promote_user") & filters.user(ADMINS))
async def promote_user(client, message):
    is_admin = message.from_user and message.from_user.id in ADMINS

    if not is_admin:
        await message.reply_text(
            "Attention: Admin Privileges Required\n\n"
            "Dear member,\n\n"
            "However, to access this, we kindly request that you ensure you have admin privileges within our group."
        )
        return

    user_id, user_first_name = get_user_details(message)

    # Define the chat permissions for the promoted user
    permissions = ChatPermissions(
        can_send_messages=True,
        can_send_media_messages=True,
        can_send_other_messages=True,
        can_send_polls=True,
        can_add_web_page_previews=True,
        can_change_info=True,
        can_invite_users=True,
        can_pin_messages=True
    )

    try:
        await message.chat.promote_chat_member(
            user_id, 
            can_send_messages=True,
            can_send_media_messages=True,
            can_send_other_messages=True,
            can_send_polls=True,
            can_add_web_page_previews=True,
            can_change_info=True,
            can_invite_users=True,
            can_pin_messages=True
        )
    except UserAdminInvalid:
        await message.reply_text(
            "Unable to promote the user. Please make sure the user is a member of the group and try again."
        )
    except Exception as error:
        await message.reply_text(str(error))
    else:
        await message.reply_text(
            f"✨ {user_first_name} has been promoted to an admin with enhanced permissions! 🎉"
        )
        

@Client.on_message(filters.command("demote_user") & filters.user(ADMINS))
async def demote_user(client, message):
    is_admin = message.from_user and message.from_user.id in ADMINS

    if not is_admin:
        await message.reply_text(
            "Admin privileges are required to demote users."
        )
        return

    user_id, user_first_name = get_user_details(message)

    try:
        await client.restrict_chat_member(
            chat_id=message.chat.id,
            user_id=user_id,
            permissions=ChatPermissions()
        )

        await message.reply_text(
            f"🔥 {user_first_name} has been demoted to a regular member!"
        )
    except Exception as error:
        await message.reply_text(str(error))
        
