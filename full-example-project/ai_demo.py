"""
ai_demo.py - Simple AI Demo

A quick demonstration of how to use the AI service.
Run this file to see the AI generate a poem!

Run this file with: python3 ai_demo.py (or python ai_demo.py on Windows)
"""

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
