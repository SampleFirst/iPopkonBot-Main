import os
from pyrogram import Client, filters
from pyrogram.types import Message, User
from info import LOG_CHANNEL, ADMINS
from database.users_chats_db import db


@Client.on_message(filters.new_chat_members)
async def welcome(bot, message):
    chat_id = message.chat.id
    group_name = message.chat.title
    username = message.from_user.username if message.from_user else None
    user_id = message.from_user.id if message.from_user else None
    
    await db.add_event("new_chat_members", chat_id, user_id)  # Store the event in the database
    
    log_text = f"#NEWMEMBER\nGroup Name: {group_name}\n"
    
    if username:
        log_text += f"Username: {username}\n"
    if user_id:
        log_text += f"User ID: {user_id}\n"
    
    await bot.send_message(LOG_CHANNEL, text=log_text)

@Client.on_message(filters.left_chat_member)
async def goodbye(bot, message):
    chat_id = message.chat.id
    group_name = message.chat.title
    username = message.from_user.username if message.from_user else None
    user_id = message.from_user.id if message.from_user else None
    
    await db.add_event("left_chat_member", chat_id, user_id)  # Store the event in the database
    
    log_text = f"#LEFTMEMBER\nGroup Name: {group_name}\n"
    
    if username:
        log_text += f"Username: {username}\n"
    if user_id:
        log_text += f"User ID: {user_id}\n"
    
    await bot.send_message(LOG_CHANNEL, text=log_text)

@Client.on_message(filters.command("chat_info") & filters.user(ADMINS))
async def chat_info_command(_, message):
    chat_id = message.chat.id
    new_members = await db.get_all_events("new_chat_members", chat_id)  # Retrieve new chat member events
    left_members = await db.get_all_events("left_chat_member", chat_id)  # Retrieve left chat member events
    total_new_members = len(new_members)
    total_left_members = len(left_members)
    total_members = total_new_members - total_left_members
    chat_info_text = f"Chat ID: {chat_id}\nTotal Members: {total_members}\nTotal New Members: {total_new_members}\nTotal Left Members: {total_left_members}"
    
    await app.send_message(message.chat.id, text=chat_info_text)
