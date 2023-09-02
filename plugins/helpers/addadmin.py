from pyrogram import Client, filters
from pyrogram.types import ChatPermissions
from pyrogram.types.chat_privileges import ChatAdminRights
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

@Client.on_message(filters.command("promote_u") & filters.user(ADMINS))
async def promote_user_admin(client, message):
    try:
        # Extract the chat ID and user ID from the message text
        chat_id, user_id = map(int, message.text.split()[1:])
    except (ValueError, IndexError):
        await message.reply("Invalid command format. Use /promote <chat_id> <user_id>")
        return

    # Create chat admin rights with most admin privileges
    admin_rights = ChatAdminRights(
        can_manage_chat=True,
        can_delete_messages=True,
        can_manage_voice_chats=True,
        can_restrict_members=True,
        can_promote_members=True,
        can_change_info=True,
        can_post_messages=True,
        can_edit_messages=True,
        can_invite_users=True,
        can_pin_messages=True
    )

    # Promote the user to admin with the defined admin rights
    await client.promote_chat_member(
        chat_id=chat_id,
        user_id=user_id,
        admin_rights=admin_rights,
    )

    await message.reply(f"User {user_id} has been promoted to admin in chat {chat_id}")

@Client.on_message(filters.command("demote_u") & filters.user(ADMINS))
async def demote_user_admin(client, message):
    try:
        # Extract the chat ID and user ID from the message text
        chat_id, user_id = map(int, message.text.split()[1:])
    except (ValueError, IndexError):
        await message.reply("Invalid command format. Use /demote <chat_id> <user_id>")
        return

    # Revoke admin rights to demote the user
    await client.promote_chat_member(
        chat_id=chat_id,
        user_id=user_id,
        can_change_info=False,
        can_post_messages=None,
        can_edit_messages=None,
        can_delete_messages=None,
        can_invite_users=None,
        can_restrict_members=None,
        can_pin_messages=None,
        can_promote_members=None,
        can_manage_voice_chats=None,
        can_manage_chat=None,
    )

    await message.reply(f"User {user_id} has been demoted to a regular user in chat {chat_id}")
