def word_counter(text):
    """
    Count the number of words in the given text.

    Parameters:
    text (str): The input text to count words from.

    Returns:
    int: The number of words in the text.
    """
    # Remove any leading/trailing whitespace
    text = text.strip()

    # Split the text into words based on whitespace
    words = text.split()

    # Count the number of words
    word_count = len(words)

    return word_count

if __name__ == "__main__":
    # Display a user-friendly prompt
    print("Welcome to the Word Counter!")
    print("Please enter a sentence or paragraph to count the words.")

    # Get the text input from the user
    text = input("Enter the text: ").strip()

    # Check if the input is empty
    if not text:
        print("Error: No input provided. Please enter some text.")
    else:
        # Count the words in the text
        count = word_counter(text)

        # Display the word count
        print(f"The number of words in the given text is: {count}")
