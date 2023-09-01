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

@Client.on_message(filters.command("promote_user") & filters.user(ADMINS))
async def promote_user(client, message):
    is_admin = message.from_user and message.from_user.id in ADMINS
    
    chat = message.chat
    user_id = get_user_details(message)

    if not user_id:
        await message.reply_text("You don't seem to be referring to a user.")
        return

    try:
        user_member = await client.get_chat_member(chat.id, user_id)
        if user_member.status == 'administrator' or user_member.status == 'creator':
            await message.reply_text("How am I meant to promote someone that's already an admin?")
            return
    
        if user_id == (await client.get_me()).id:
            await message.reply_text("I can't promote myself! Get an admin to do it for me.")
            return
    
        # Set the same permissions as the bot - bot can't assign higher permissions than itself!
        bot_member = await client.get_chat_member(chat.id, (await client.get_me()).id)
        permissions = {
            "can_change_info": bot_member.can_change_info,
            "can_post_messages": bot_member.can_post_messages,
            "can_edit_messages": bot_member.can_edit_messages,
            "can_delete_messages": bot_member.can_delete_messages,
            "can_restrict_members": bot_member.can_restrict_members,
            "can_pin_messages": bot_member.can_pin_messages,
            "can_promote_members": bot_member.can_promote_members,
        }
    
        await client.promote_chat_member(chat.id, user_id, **permissions)
        await message.reply_text(
            f"✨ {user_first_name} has been promoted to an admin! 🎉"
        )
    except Exception as error:
        await message.reply_text(str(error))


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
        
