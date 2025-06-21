# welcome_ai_journey.py

def get_ai_message(level):
    level = level.strip().lower()

    if level == "beginner":
        return {
            "title": "Welcome, Beginner!",
            "message": (
                "You're in exactly the right place. I'm learning too, one step at a time.\n\n"
                "Would you like to start exploring basic concepts like:\n"
                "- Large Language Models (LLMs)\n"
                "- Prompt engineering\n"
                "- A short history of AI\n\n"
                "👉 Start here: https://example.com/start-here"
            )
        }

    elif level == "intermediate":
        return {
            "title": "Hello, Explorer!",
            "message": (
                "Nice! You’ve already started exploring.\n\n"
                "Would you like to dive into:\n"
                "- Practical applications of AI\n"
                "- Comparing AI tools\n"
                "- Reflections on AI and society\n\n"
                "👉 Explore next: https://example.com/next-steps"
            )
        }

    elif level == "just curious":
        return {
            "title": "Hi there, Curious Mind!",
            "message": (
                "Curiosity is the best starting point.\n\n"
                "Want to try:\n"
                "- What AI is and how it works?\n"
                "- Why people are excited (or nervous) about it?\n"
                "- Fun ways to experiment with AI tools?\n\n"
                "👉 Try this: https://example.com/curious-path"
            )
        }

    else:
        return {
            "title": "Welcome!",
            "message": "Thanks for stopping by. Feel free to explore and learn at your own pace."
        }


# Main interactive script
if __name__ == "__main__":
    name = input("What’s your name? ").strip()

    if name.lower() == "harry":
        print(f"\n🚀 Behold! The visionary AI Builder {name} has arrived — time to build greatness! 🚀\n")
    else:
        print(f"\nWelcome, {name}! Ready to explore the world of possibilities together?\n")

    print("How would you describe your experience with AI?")
    print("1 - Beginner")
    print("2 - Intermediate")
    print("3 - Just Curious")

    choice = input("Enter the number that best describes you (1/2/3): ").strip()
    level_map = {"1": "beginner", "2": "intermediate", "3": "just curious"}
    level = level_map.get(choice, "other")

    result = get_ai_message(level)

    print(f"\n{result['title']}\n")
    print(result['message'])

    print("\nThanks for visiting. No matter where you are on your path, I wish you curiosity, courage, and a bit of fun as you explore the world of AI.")
    print("Let’s keep moving forward and see what we can build together.")
