def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)

def num_words():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
    print(len(words))
 
def chars():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        lower_contents = file_contents.lower()
        letters = lower_contents
        dict = {}
        for letter in letters:
            if letter not in dict:
                dict[letter] = 1
            else:
                dict[letter] += 1
    print(dict)

def report():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        word_count = len(words)
        lower_contents = file_contents.lower()
        letters = lower_contents
        dict = {}
        for letter in letters:
            if letter not in dict and letter.isalpha():
                dict[letter] = 1
            elif letter.isalpha():
                dict[letter] += 1
        list = []
        for letter, count in dict.items():
            list.append({"letter": letter, "count": count})
        def sort(list):
            return list["count"]
        list.sort(reverse=True, key=sort)
    
    print("---Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in this document")
    for dict in list:
        print(f"The '{dict["letter"]}' character was found '{dict["count"]}' times")

    print("--- End report ---")
    
report()
