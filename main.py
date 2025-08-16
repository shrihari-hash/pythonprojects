from gtts import gTTS
import os

def main():
    print("Welcome to Robospeaker (gTTS version)")

    while True:
        text = input("Enter text to speak (or 'q' to quit): ")
        if text.lower() == 'q':
            break

        tts = gTTS(text)
        tts.save("voice.mp3")
        os.system("start voice.mp3")


if __name__ == "__main__":
    main()


