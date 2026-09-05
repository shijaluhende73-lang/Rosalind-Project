def hamming_distance(s, t):
    return sum(1 for a, b in zip(s, t) if a != b)
with open('rosalind_hamm.txt') as f:
    lines = [line.strip() for line in f if line.strip()]
s = lines[0]
t = lines[1]
print(hamming_distance(s, t))