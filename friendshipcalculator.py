def friendship_score(name1,name2):
      name1,name2 = name1.lower(),name2.lower()
      score = 0 
      shared_letter = set(name1)&set(name2)
      vowels = set('aeiou')

      score = score+len(shared_letter)*5
      score = score+len(vowels&shared_letter)*10
      return min(score,100)


def run_friendship_calculator():
      print("❤️ Friendship Compatibility Calculator ❤️")
      name1 = input("Enter the first Name:")
      name2 = input("Enter the second name:")
      border = "*"*80
      score = friendship_score(name1 , name2)
      print(f"\n {border}\n Friend_Ship Score is {score}\n{border} ")
      if score > 90:
        print("Soul-sync achieved. If this were a game, you'd be unlocking legendary status.🏆")
      elif score > 80:
        print("You're not just compatible—you complement each other like code and coffee.☕")
      elif score > 70:
       print("This connection has potential—like peanut butter and jelly, but with extra sparkle. ✨")
      elif score > 60:
       print("You two vibe like a playlist that never skips. 🎶")
      elif score > 50:
       print("Something's clicking... maybe it's the start of something beautiful.")
      else:
       print("Both are good friends 💖")

      


while True:
           
           run_friendship_calculator()
           value = input("Do you want to check more friend type (y/n)->").lower()
           if value!=('y'):
                   break
                   
         



