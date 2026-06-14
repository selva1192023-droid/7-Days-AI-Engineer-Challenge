import random

quotes = [
    "Success comes from consistency.",
    "Learn something new every day.",
    "AI is transforming the future.",
    "Small progress is still progress.",
    "The best way to predict the future is to create it."
]

print("🤖 AI Quote Generator")
print("-" * 30)

quote = random.choice(quotes)

print("\nGenerated Quote:")
print(f'"{quote}"')
