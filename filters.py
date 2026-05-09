# filters.py
import re
from collections import defaultdict

# Regex patterns
link_pattern = re.compile(r"(https?://\S+)")
nsfw_pattern = re.compile(r"(porn|xxx|sex|nude)", re.IGNORECASE)

# Flood control
user_messages = defaultdict(list)

# Ban tracking
admin_ban_count = defaultdict(int)