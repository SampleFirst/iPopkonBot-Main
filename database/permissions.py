# Create a new file named 'permissions.py'
# Define the ChatPermissions class with the appropriate attributes

class ChatPermissions:
    def __init__(
        self,
        can_change_info=None,
        can_post_messages=None,
        can_edit_messages=None,
        can_delete_messages=None,
        can_invite_users=None,
        can_restrict_members=None,
        can_pin_messages=None,
        can_promote_members=None,
        can_send_messages=None,
        can_send_media_messages=None,
        can_send_polls=None,
        can_send_other_messages=None,
        can_add_web_page_previews=None,
    ):
        self.can_change_info = can_change_info
        self.can_post_messages = can_post_messages
        self.can_edit_messages = can_edit_messages
        self.can_delete_messages = can_delete_messages
        self.can_invite_users = can_invite_users
        self.can_restrict_members = can_restrict_members
        self.can_pin_messages = can_pin_messages
        self.can_promote_members = can_promote_members
        self.can_send_messages = can_send_messages
        self.can_send_media_messages = can_send_media_messages
        self.can_send_polls = can_send_polls
        self.can_send_other_messages = can_send_other_messages
        self.can_add_web_page_previews = can_add_web_page_previews
