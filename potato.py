# potato.py

import random

# List of scientifically questionable potato emotions
potato_emotions = [
    "Happy",
    "Sad",
    "Mildly Confused",
    "Existential Dread",
    "Overwhelming Joy",
    "Spicy",
    "Quantumly Uncertain",
    "Contemplating the Meaning of Fries"
]

def predict_potato_mood():
    return random.choice(potato_emotions)

if __name__ == "__main__":
    print("🔮 Analyzing Potato Quantum Field...")
    print(f"Today's potato is feeling: {predict_potato_mood()}.")
