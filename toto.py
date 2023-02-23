import sys
from contextlib import redirect_stderr

def find_pair1(number, k):
    seen = {}
    for i, num in enumerate(number):
        diff = k - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return [0,0]

def find_pair(numbers, k):
    seen = {}
    for i, num in enumerate(numbers):
        diff = k - num
        if diff in seen:
            return sorted([seen[diff], i]) # trier les index
        seen[num] = i
    return [0, 0]


def count_frequencies(words):
    word_f = {}
    for word in words:
        if word not in word_f:
            word_f[word]=1
        else:
            word_f[word]+=1
    sorted_word_f = sorted(word_f.items())
    return [freq for word, freq in sorted_word_f]

def test_count_frequencies():
    words = ['apple', 'banana', 'cherry', 'apple', 'cherry', 'cherry']
    freq_list = count_frequencies(words)
    assert freq_list == [2, 1, 3], f"Expected [2, 1, 3], but got {freq_list}"

def main():
    n = int(input("n: "))
    x = int(input("x: "))
    words = []
    for i in range(n):
        words.append(input())
    with redirect_stderr(sys.stderr):
        counts = count_frequencies(words)
    for i in range(x):
        print(counts[i])


def test_find_pair():
    numbers = [1, 5, 7, 3, 8, 2]
    k = 10
    expected_output = [1, 4]
    output = find_pair(numbers, k)
    print(output) # imprimer la sortie de la fonction
    assert output == expected_output, f"Expected {expected_output}, but got {output}"


if __name__ == "__main__":
   # test_count_frequencies()
    test_find_pair()
    main()

