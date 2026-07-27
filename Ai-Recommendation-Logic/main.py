# ===========================
# AI Recommendation System
# ===========================

# Dataset
items = {
    "Avengers": ["action", "superhero"],
    "John Wick": ["action", "thriller"],
    "Interstellar": ["space", "sci-fi"],
    "Harry Potter": ["fantasy", "magic"],
    "The Notebook": ["romance", "drama"],
    "Inception": ["sci-fi", "thriller"],
    "Frozen": ["animation", "family"],
    "Coco": ["animation", "family"],
    "Titanic": ["romance", "drama"],
    "Batman": ["action", "superhero"]
}

print("=" * 45)
print("      AI RECOMMENDATION SYSTEM")
print("=" * 45)

print("\nAvailable Interests:")
print("action")
print("superhero")
print("thriller")
print("space")
print("sci-fi")
print("fantasy")
print("magic")
print("romance")
print("drama")
print("animation")
print("family")

# User Input
user_interest = input("\nEnter your favorite interest: ").lower()

recommendations = []

# Matching Logic
for item, categories in items.items():

    if user_interest in categories:
        recommendations.append(item)

print("\n" + "=" * 45)

if recommendations:
    print("Recommended for you:\n")

    for movie in recommendations:
        print("✔", movie)

else:
    print("Sorry!")
    print("No recommendation found.")

print("=" * 45)