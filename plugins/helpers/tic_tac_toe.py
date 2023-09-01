import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Callback


# Define the game state
game = {
    "board": ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
    "current_player": 1,  # Player 1 starts
    "players": [None, None],  # To store player IDs
}

# Helper function to check for a win
def check_win(board, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6],  # Diagonals
    ]

    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True

    return False

# Start command to initiate the game
@Client.on_message(filters.command("tic_tac_toe") & filters.user(ADMINS))
def start_tic_tac_toe_game(client, message):
    chat_id = message.chat.id
    game["players"][game["current_player"] - 1] = chat_id

    markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("1", callback_data="1"), 
                InlineKeyboardButton("2", callback_data="2"), 
                InlineKeyboardButton("3", callback_data="3")
            ],
            [
                InlineKeyboardButton("4", callback_data="4"), 
                InlineKeyboardButton("5", callback_data="5"), 
                InlineKeyboardButton("6", callback_data="6")
            ],
            [
                InlineKeyboardButton("7", callback_data="7"), 
                InlineKeyboardButton("8", callback_data="8"), 
                InlineKeyboardButton("9", callback_data="9")
            ],
        ]
    )

    client.send_message(chat_id, "Player 1, it's your turn.", reply_markup=markup)

# Callback function to handle user moves
@Client.on_callback_query()
def handle_callback(client, query):
    chat_id = query.message.chat.id
    player = game["current_player"]
    move = int(query.data)

    if chat_id != game["players"][player - 1]:
        return  # Ignore moves from other players

    if game["board"][move - 1] == str(move):
        game["board"][move - 1] = "X" if player == 1 else "O"

        if check_win(game["board"], "X" if player == 1 else "O"):
            client.send_message(chat_id, f"Player {player} wins! Game over.")
            return
        elif all(cell != str(cell) for cell in game["board"]):
            client.send_message(chat_id, "It's a draw! Game over.")
            return

        game["current_player"] = 3 - player  # Switch players
        client.edit_message_text(chat_id, query.message.message_id, f"Player {game['current_player']}, it's your turn.")



