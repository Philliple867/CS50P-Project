def main():
    word = input("Input: ")
    print(shorten(word))

def shorten(word):
    # This function removes vowels (a, e, i, o, u) regardless of case
    vowels = "aeiouAEIOU"
    result = ""
    for char in word:
        if char not in vowels:
            result += char
    return result

if __name__ == "__main__":
    main()
