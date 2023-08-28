from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import asyncio
import datetime
import pytz  # Add this import for working with timezones
from info import ADMINS, LOG_CHANNEL


# Convert UTC time to Indian Timezone
def get_indian_time():
    utc_now = datetime.datetime.now(pytz.utc)
    indian_timezone = pytz.timezone("Asia/Kolkata")
    return utc_now.astimezone(indian_timezone)

# Your existing code here...

# Modify the send_log_message function
async def send_log_message(chat_id):
    while True:
        indian_now = get_indian_time()
        if indian_now.hour == 02 and indian_now.minute == 20:
            message = f"This is a daily log message. Current Indian Time: {indian_now.strftime('%Y-%m-%d %H:%M:%S')}"
            await bot.send_message(LOG_CHANNEL, message)
        await asyncio.sleep(60)  # Sleep for 1 minute

        # Check if the task needs to be stopped
        if chat_id not in active_tasks:
            break

# Dictionary to keep track of active tasks
active_tasks = {}

@Client.on_message(filters.private & filters.user(ADMINS) & filters.command("Reporting"))
async def start_command_handler(_, message):
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Start Reporting", callback_data="start_log"),
                InlineKeyboardButton("Stop Reporting", callback_data="stop_log"),
            ],
            [
                InlineKeyboardButton("Cancel", callback_data="cancel_log"),
            ]
        ]
    )
    await message.reply("Log message sending started. Click 'Stop' to stop.", reply_markup=keyboard)

@Client.on_callback_query(filters.user(ADMINS))
async def callback_handler(_, query: CallbackQuery):
    chat_id = query.message.chat.id
    data = query.data

    if data == "start_log":
        if chat_id not in active_tasks:
            active_tasks[chat_id] = asyncio.create_task(send_log_message(chat_id))
            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Stop Reporting", callback_data="stop_log"),
                        InlineKeyboardButton("Cancel", callback_data="cancel_log"),
                    ]
                ]
            )
            await query.message.edit_text("Log message sending started. Click 'Stop' to stop.", reply_markup=keyboard)
    
    elif data == "stop_log":
        if chat_id in active_tasks:
            active_tasks[chat_id].cancel()
            del active_tasks[chat_id]
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Start Reporting", callback_data="start_log"),
                    InlineKeyboardButton("Cancel", callback_data="cancel_log"),
                ]
            ]
        )
        await query.message.edit_text("Log message sending stopped.", reply_markup=keyboard)
    
    elif data == "cancel_log":
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Start Reporting", callback_data="start_log"),
                    InlineKeyboardButton("Stop Reporting", callback_data="stop_log"),
                ]
            ]
        )
        await query.message.edit_text("Log message sending canceled.", reply_markup=keyboard)


