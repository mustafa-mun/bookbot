# count words in text
def count_word(text):
    l = text.split()
    return len(l)
# count letters
def count_letters(text):
    output = {}
    for s in text:
        # Include if character is letter
        if(s.isalpha()):
            str = s.lower()
        if str in output:
            output[str] += 1
        else:
            output[str] = 1
    # sort the output on descending order
    sorted_output = sorted(output.items(), key=lambda x: x[1], reverse=True)
    # convert sorted output to dictionary again
    converted = dict(sorted_output)
    return converted
        

with open("books/frankenstein.txt") as file:
    file_contents = file.read()
    print(count_letters(file_contents))
