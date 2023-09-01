from pyrogram import Client, filters
from pyrogram.types import ChatPermissions
from info import *

# Updated extract_user function to extract user details
def get_user_details(message):
    if message.reply_to_message:
        user = message.reply_to_message.from_user
        user_id = user.id
        user_first_name = user.first_name
    else:
        user_id = message.from_user.id
        user_first_name = message.from_user.first_name
    return user_id, user_first_name

@Client.on_message(filters.command("promote"))
async def promote_user(_, message):
    is_admin = message.from_user and message.from_user.id in ADMINS

    if not is_admin:
        await message.reply_text(
            "Attention: Admin Privileges Required\n\n"
            "Dear member,\n\n"
            "However, to access this, we kindly request that you ensure you have admin privileges within our group."
        )
        return

    user_id, user_first_name = get_user_details(message)
    if not user_id:
        await message.reply_text("You don't seem to be referring to a user.")
        return
        
    try:
        # Use the promote_member method to promote the user to admin with necessary permissions
        await message.chat.promote_member(
            user_id=user_id,
            can_change_info=True,
            can_post_messages=True,
            can_edit_messages=True,
            can_delete_messages=True,
            can_invite_users=True,
            can_restrict_members=True,
            can_pin_messages=True,
            can_promote_members=True
        )
   
    except Exception as error:
        await message.reply_text(str(error))
    else:
        await message.reply_text(
            f"✨ {user_first_name} has been promoted to an admin! 🎉"
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
        
