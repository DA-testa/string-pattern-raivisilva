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
    p_len = len(pattern)
    t_len = len(text)
    prime = 101 
    p_hash = 0  
    t_hash = 0   
    occurances = []

    for i in range(p_len):
        p_hash += ord(pattern[i]) * pow(prime, i)
        t_hash += ord(text[i]) * pow(prime, i)

    for i in range(t_len - p_len + 1):
        if p_hash == t_hash and pattern == text[i:i+p_len]:
            occurances.append(i)

        if i < t_len - p_len:
            t_hash = (t_hash - ord(text[i]) * pow(prime, 0)) // prime
            t_hash += ord(text[i+p_len]) * pow(prime, p_len-1)

    return occurances

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

