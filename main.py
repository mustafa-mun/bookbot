# count words in text
def count_words(text):
    l = text.split()
    return len(l)
# count letters
def count_letters(text):
    output = {}
    for s in text:
        # make characters lowercase
        str = s.lower()
        # include only if character is letter
        if(s.isalpha()):
            if str in output:
                # character is found, add +1 to it's count
                output[str] += 1
            else:
                # character is not found, make it's count 1
                output[str] = 1
    # sort the output on descending order
    sorted_output = sorted(output.items(), key=lambda x: x[1], reverse=True)
    # convert sorted output to dictionary again
    converted = dict(sorted_output)
    return converted
        
path = "books/frankenstein.txt"
# open file
with open(path) as file:
    # read the file
    file_contents = file.read()
    print(f"--- Begin report of {path} ---")
    # print word count of the file
    print(f"{count_words(file_contents)} words found in the document\n")
    letter_dict = count_letters(file_contents)
    # print letter count of the file
    for char in letter_dict:
        print(f"The '{char}' character was found {letter_dict[char]} times")
    print("--- End report ---")
