import datetime
import requests
name = input("enter your name:-").strip()
age = int(input("enter your age:-"))
city=input("enter your city:-").strip()
profession = input("enter your profession:-").strip()
favourite_hobby = input("enter your favourite hobby:-").strip()
intro_message = (
    f"Hello! my name is {name},\n" 
    f"I'm {age} years old and live in {city}\n"
    f"I work as a {profession}\n"
    f"and I absolutely enjoy {favourite_hobby}\n"
    f"in my free time "
    f"Nice to meet you! \n"
)

current_date = datetime.date.today().isoformat()
intro_message=intro_message+f"\n Logged on: {current_date}"
border = "*" *80
final_output = f"{border}\n{intro_message}\n{border}"
print("\n"+final_output)

