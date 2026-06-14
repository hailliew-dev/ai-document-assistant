# define a clean_text function that takes a string and returns that string cleaned of
# extra whitespace in the beginning, middle, and end of the string, and newlines
# preserve capitalization and punctuation

def clean_text(text: str) -> str:
    return ' '.join(text.split())

def word_count(text: str) -> int:
    return len(text.split())

if __name__ == "__main__":
    print("Hello world")
    print(repr(clean_text("Hello world")))
    print(word_count("Hello world"))

    print('')

    print(" Hello world ")
    print(repr(clean_text(" Hello world ")))
    print(word_count(" Hello world "))

    print("")

    print("Hello   world")
    print(repr(clean_text("Hello   world")))
    print(word_count("Hello   world"))

    print("")

    print("")
    print(repr(clean_text("")))
    print(word_count(""))

    print('')

    print("   ")
    print(repr(clean_text("   ")))
    print(word_count("   "))

    print('')

    print("one two three four five")
    print(repr(clean_text("one two three four five")))
    print(word_count("one two three four five"))

    print('')

    print("Hello\nworld")
    print(repr(clean_text("Hello\nworld")))
    print(word_count("Hello\nworld"))

    print('')

    print("Hello\tworld")
    print(repr(clean_text("Hello\tworld")))
    print(word_count("Hello\tworld"))

    print('')

    print("Python")
    print(repr(clean_text("Python")))
    print(word_count("Python"))

    print('')

    print(" ChatGPT is awesome! ")
    print(repr(clean_text(" ChatGPT is awesome! ")))
    print(word_count(" ChatGPT is awesome! "))