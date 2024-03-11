def count_words(text):
    words = text.split()
    return len(words)


def count_letters(text):
    count = {}
    for char in text:
        if char.lower() not in count:
            count[char.lower()] = 1
        else:
            count[char.lower()] += 1
    return count


def sort_on_count(dict):
    return dict["count"]


def main():
    with open("./books/frankenstein.txt") as f:
        text = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{count_words(text)} words found in the document")

        letter_count = count_letters(text)
        letter_list = []
        for k, v in letter_count.items():
            if k.isalpha():
                letter_list.append({"letter": k, "count": v})

        letter_list.sort(reverse=True, key=sort_on_count)
        for count in letter_list:
            char = count["letter"]
            char_count = count["count"]
            print(f"The {char} character was found {char_count} times")


main()
