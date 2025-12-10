# Import our AI service
from ai_service import call_ai


def main():
    """Ask the AI to write a poem about Python."""

    print("")
    print("=" * 50)
    print("AI Poetry Demo")
    print("=" * 50)
    print("")
    print("Asking the AI to write a poem...")
    print("(This may take a moment)")
    print("")

    # Create our prompt
    prompt = "Write a short, fun rhyming poem about the Python programming language. Keep it under 8 lines."

    # Call the AI
    response = call_ai(prompt)

    # Check if we got a response
    if response is None:
        print("Could not get a response. Check your API key in the .env file.")
        return

    # Display the poem
    print("-" * 50)
    print("")
    print(response)
    print("")
    print("-" * 50)


# Run main() when this file is executed directly
if __name__ == "__main__":
    main()


# ============================================================
# DISCUSSION QUESTIONS
# ============================================================
# While you wait for others to catch up, think about:
#
# 1. Look at the code in this file - what do you think call_ai(prompt) does?
#
# 2. What would happen if you changed the prompt to ask for something different?
#    (Try it!)
#
# 3. Where do you think the call_ai function actually lives?
#    (Hint: look at the import at the top)
#
# 4. What do you think happens inside call_ai? How does your code "talk" to
#    the AI?
#
# 5. Why do we check "if response is None"? What could go wrong?
