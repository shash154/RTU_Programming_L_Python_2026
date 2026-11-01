def analyze_sentence(sentence, word):
    """Return (number_of_words, word_found), ignoring case.

    >>> analyze_sentence("The quick brown fox", "QUICK")
    (4, True)
    >>> analyze_sentence("The quick brown fox", "dog")
    (4, False)
    >>> analyze_sentence("", "a")
    (0, False)
    """
    words = sentence.split()
    found = word.lower() in [w.lower() for w in words]
    return (len(words), found)


if __name__ == "__main__":
    s = input("Sentence: ")
    w = input("Word to look for: ")
    count, found = analyze_sentence(s, w)
    print(f"{count} words, found: {found}")