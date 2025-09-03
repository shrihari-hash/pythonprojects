import time 
import winsound



while True:
    try:
        seconds = int(input("⏱️ enter the time in seconds: "))
        if seconds<1:
            print("Please enter a number greater than 0")
            continue
        break
    except ValueError:
        print("Invalid input Please enter a whole number")

print("\n🔔 Timer started....")
# div mode operator is a special kind of built in method 
# gives quotient and remaninder when reamaning is divided by 60
# mins holds the remainder value and the secs holds the quotient value 
for remaning in range(seconds,0,-1):
    mins,secs = divmod(remaning,60)
    time_formate = f"{mins:02}:{secs:02}"
    print(f"⏱️ Time left: {time_formate} ",end="\r")
    time.sleep(1)

print("\n Time's up! Take a break or move to next task.")

winsound.Beep(1000, 500)
