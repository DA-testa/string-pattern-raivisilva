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
    pattern_length, text_length = len(pattern), len(text)
    prime_number, pattern_hash, text_hash, repetitions = 101, 0, 0, []

    for i in range(pattern_length):
        pattern_hash += ord(pattern[i]) * pow(prime_number, i)
        text_hash += ord(text[i]) * pow(prime_number, i)

    for i in range(text_length - pattern_length + 1):
        if pattern_hash == text_hash and pattern == text[i:i+pattern_length]:
            repetitions.append(i)

        if i < text_length - pattern_length:
            text_hash = (
                text_hash - ord(text[i]) * pow(prime_number, 0)) // prime_number
            text_hash += ord(text[i+pattern_length]) * \
                pow(prime_number, pattern_length-1)

    return repetitions


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
