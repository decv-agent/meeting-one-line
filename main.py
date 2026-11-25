import os
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write("This meeting could have been an email, and the email just says: approved.")
