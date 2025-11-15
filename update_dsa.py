import os
import re
from datetime import datetime

DSA_FOLDER = "dsa"
README_FILE = "README.md"

# Get all folders like day_01, day_02 ...
folders = [f for f in os.listdir(DSA_FOLDER) if f.startswith("day_")]

# Sort by number
folders.sort(key=lambda x: int(x.split("_")[1]))

streak = len(folders)
last_problem = folders[-1] if folders else "None"
total_solved = streak

# Read README
with open(README_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the updating values
content = re.sub(r"🔥 \*\*Current Streak:\*\*.*",
                 f"🔥 **Current Streak:** {streak} days", content)

content = re.sub(r"📅 \*\*Last Problem:\*\*.*",
                 f"📅 **Last Problem:** {last_problem}", content)

content = re.sub(r"📁 \*\*Total Problems Solved:\*\*.*",
                 f"📁 **Total Problems Solved:** {total_solved}", content)

# Write updated README
with open(README_FILE, "w", encoding="utf-8") as f:
    f.write(content)

print("DSA Streak Updated!")
