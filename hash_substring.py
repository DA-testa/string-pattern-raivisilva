# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    izvele = input()

    if "I" in izvele:
        pattern = input().rstrip()
        text = input().rstrip()
        return (pattern, text)

    elif "F" in izvele:
        with open("./tests/06", mode='r') as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
            return (pattern, text)
    

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    pattern_length = len(pattern)
    text_length = len(text)
    if pattern_length > text_length:
        return []
    pattern_hash = hash(pattern)
    text_hash = hash(text[:pattern_length])
    occurrences = []
    for i in range(text_length - pattern_length + 1):
        if text_hash == pattern_hash and text[i:i+pattern_length] == pattern:
            occurrences.append(i)
        if i < text_length - pattern_length:
            text_hash = text_hash - hash(text[i]) + hash(text[i+pattern_length])

    return occurrences

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

