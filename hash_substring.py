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
    prime_numbers = 31  
    pattern_hash = 0  
    text_hash = 0   
    repeat = []

    for i in range(pattern_length):
        pattern_hash = (pattern_hash << 1) + ord(pattern[i])
        text_hash = (text_hash << 1) + ord(text[i])

    for i in range(text_length - pattern_length + 1):
        if pattern_hash == text_hash and pattern == text[i:i+pattern_length]:
            repeat.append(i)

        if i < text_length - pattern_length:
            text_hash = ((text_hash - ord(text[i]) * (prime_numbers ** (pattern_length - 1))) << 1) + ord(text[i+pattern_length])

    return repeat

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

