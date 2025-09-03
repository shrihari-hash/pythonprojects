import datetime

entry = input("What did you learn:").strip()
rating = input("⭐ Rate your productivity today(1-10) :").strip()
now = datetime.datetime.now()
date_str = now.strftime("%Y-%m-%d - %I:%M %p")
journal_entry = f"\n 🗓️{date_str}\n{entry}"
if rating:
    journal_entry += f"\n Productivity Rating: {rating}\n"
journal_entry += "\n" + "-" *50

with open("Learning_journal.txt","a",encoding="utf-8") as f:
    f.write(journal_entry)

print("\n Your journal file has been saved to the txt file")

