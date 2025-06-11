# Find first non-repeating character in a string.
from collections import Counter
def find(string):
    freq=Counter(string)
    # freq=dict(freq)     # freq=dict(freq) not needed because its already a dictionary like object
    for s in string:
        if freq[s]==1:
            return s
    return -1
print(find("aagbbcecdd"))