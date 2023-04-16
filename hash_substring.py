# python3

def read_input():
    izvele = input()

    if "I" in izvele:
        pattern, text = input().rstrip(), input().rstrip()
        if 1 <= len(pattern) <= len(text) <= (5 * 10**5):
            return (pattern, text)

    elif "F" in izvele:
        with open("./tests/06", mode='r') as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
        if 1 <= len(pattern) <= len(text) <= (5 * 10**5):
            return (pattern, text)

def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    pattern_hash, text_hash = hash(pattern), hash(text[:len(pattern)])
    text_length, pattern_length = len(text), len(pattern)
    occurances = []

    for i in range(text_length - pattern_length + 1):
        if text_hash == pattern_hash and text[i:i+pattern_length] == pattern:
            occurances.append(i)
        if i < text_length - pattern_length:
            text_hash = hash(text[i+1:i+pattern_length+1])

    return occurances


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
