import asyncio
from pyrogram import Client, filters, enums


@Client.on_message(filters.command("purge") & (filters.group | filters.channel))
async def purge(client, message):
    if message.chat.type not in (enums.ChatType.SUPERGROUP, enums.ChatType.CHANNEL):
        return

    is_admin = message.from_user and message.from_user.id in ADMINS

    if not is_admin:
        await message.reply_text(
            "Attention: Admin Privileges Required\n\n"
            "Dear member,\n\n"
            "However, to access this, we kindly request that you ensure you have admin privileges within our group."
        )
        return

    status_message = await message.reply_text("...", quote=True)
    await message.delete()
    message_ids = []
    count_deletions = 0

    if message.reply_to_message:
        async for a_message in client.iter_history(
            chat_id=message.chat.id,
            from_message_id=message.reply_to_message.message_id,
            reverse=True,
        ):
            message_ids.append(a_message.message_id)
            if len(message_ids) >= 100:
                await client.delete_messages(
                    chat_id=message.chat.id,
                    message_ids=message_ids,
                    revoke=True,
                )
                count_deletions += len(message_ids)
                message_ids = []

    if len(message_ids) > 0:
        await client.delete_messages(
            chat_id=message.chat.id,
            message_ids=message_ids,
            revoke=True,
        )
        count_deletions += len(message_ids)

    await status_message.edit_text(f"Deleted {count_deletions} messages")
    await asyncio.sleep(5)
    await status_message.delete()
