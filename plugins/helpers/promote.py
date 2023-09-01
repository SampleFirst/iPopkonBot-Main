from pyrogram import Client, filters
from pyrogram.types import ChatPermissions
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

    try:
        await message.chat.promote_member(user_id)
    except Exception as error:
        await message.reply_text(str(error))
    else:
        await message.reply_text(f"✨ {user_first_name} has been promoted to an admin! 🎉"
        )

@Client.on_message(filters.command("demote_users") & filters.user(ADMINS))
async def promote_user(client, message):
    is_admin = message.from_user and message.from_user.id in ADMINS

    if not is_admin:
        await message.reply_text(
            "Attention: Admin Privileges Required\n\n"
            "Dear member,\n\n"
            "To access this, we kindly request that you ensure you have admin privileges within our group."
        )
        return

    user_id, user_first_name = get_user_details(message)

    try:
        await message.chat.restrict_member(user_id, ChatPermissions())
    except Exception as error:
        await message.reply_text(str(error))
    else:
        await message.reply_text(f"🔥 {user_first_name} has been demoted to a regular member!"
        )

