import random

music_library = {
    "happy": ["Blinding Lights- by The Weeknd","Shape of You -by Ed Sheeran","Levitating-by Dua Lipa","Stay- by The Kid LAROI & Justin Bieber","Good 4 U- by Olivia Rodrigo"],
     "sad": ["Someone Like You - Adele", "Fix You - Coldplay", "Let Her Go - Passenger"],
    "angry": ["Breaking the Habit - Linkin Park", "Smells Like Teen Spirit - Nirvana", "Killing in the Name - RATM"],
    "relaxed": ["Weightless - Marconi Union", "Sunset Lover - Petit Biscuit", "Ocean Eyes - Billie Eilish"]
}


mood_emojis = {
    "happy": "😄",
    "sad": "😢",
    "angry": "😡",
    "relaxed": "😌"
}

print("🎵 Welcome to Mood-Based Music Suggester 🎵")
print("Available moods: happy, sad, angry, relaxed")

mood = input("How are you feeling today? (Type your mood): ").lower()

if mood in music_library:
    print(f"\nYour mood: {mood_emojis[mood]} ({mood})\n")
    

    suggestions = random.sample(music_library[mood], 2)
    
    print("🎶 Here are some songs you might enjoy:\n")
    for song in suggestions:
        print(f"👉 {song}")
else:
    print("\nSorry, I don't have songs for that mood yet.")

print("\nThanks for using Mood-Based Music Suggester! 🎧")
