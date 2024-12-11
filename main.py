
def count_character(file):
    count_dict = {}
    new_string = file.lower()

    for char in new_string:
        if char.isalpha():
            if char in count_dict:
                count_dict[char] += 1
            else:
                count_dict[char] = 1
    return count_dict

def create_report(file):
    dict = count_character(file)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(file)} words found in the document")
    print("")
    for key in dict:
        print(f"The '{key}' character was found {dict[key]} times")
    print('--- End Report ---')


def count_words(file):
    return len(file.split())


def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()

    create_report(file_contents)

    


main()
