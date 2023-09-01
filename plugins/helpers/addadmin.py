from pyrogram import Client, filters
from pyrogram.types import ChatMember
from info import *

# Define the add_admins command handler
@Client.on_message(filters.command("add_admins") & filters.user(ADMINS))
async def add_admins(client, message):
    if len(message.command) != 3:
        await message.reply("Usage: /add_admins <user_id> <channel_id>")
        return

    user_id = int(message.command[1])
    channel_id = int(message.command[2])

    try:
        # Get the bot's member information in the chat
        bot_member = await client.get_chat_member(chat.id, bot.id)

        # Promote the user to admin with custom privileges
        await client.promote_chat_member(
            chat_id=channel_id,
            user_id=user_id,
            can_change_info=bot_member.can_change_info,
            can_post_messages=bot_member.can_post_messages,
            can_edit_messages=bot_member.can_edit_messages,
            can_delete_messages=bot_member.can_delete_messages,
            can_invite_users=bot_member.can_invite_users,
            can_restrict_members=bot_member.can_restrict_members,
            can_pin_messages=bot_member.can_pin_messages,
            can_promote_members=bot_member.can_promote_members
        )

        await message.reply(f"Admin with user ID {user_id} added to the channel with custom privileges.")
    except Exception as e:
        await message.reply(f"An error occurred: {str(e)}")
