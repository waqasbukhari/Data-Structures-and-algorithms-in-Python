from random import shuffle

def insertion_sort(seq):
    for i in range(1, len(seq)):
        cur = i
        for j in range(i-1, -1,-1):
            if seq[cur] < seq[j]:
                seq[j], seq[cur] = seq[cur], seq[j]
                cur = j

if __name__ == "__main__":
    A = list(range(100))
    shuffle(A)
    print(A)
    print()
    insertion_sort(A)
