import asyncio
from datetime import datetime
from pyrogram import Client, filters
from info import *


@Client.on_message(filters.command("set_calendar") & filters.user("ADMINS"))
async def set_calendar(client, message):
    try:
        # Extract the date and time from the command message
        command_parts = message.text.split(" ")
        if len(command_parts) != 3:
            await message.reply("Invalid command format. Use: set_calendar time date")
            return
        
        time_str = command_parts[1]
        date_str = command_parts[2]
        datetime_str = f"{date_str} {time_str}"
        
        # Convert the datetime string to a datetime object
        scheduled_datetime = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")
        
        # Calculate the time until the scheduled message
        current_time = datetime.now()
        time_difference = (scheduled_datetime - current_time).total_seconds()
        
        if time_difference <= 0:
            await message.reply("The scheduled time has already passed.")
        else:
            # Sleep until the scheduled time
            await asyncio.sleep(time_difference)
            
            # Send the scheduled message
            await message.reply("It's time! Your scheduled message is being sent now.")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
