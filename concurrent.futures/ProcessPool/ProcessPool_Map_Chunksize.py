from hashlib import sha512
from concurrent.futures import ProcessPoolExecutor
from time import time
from math import ceil



def load_words(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.readlines()


def hash_words(word):
    hash_object = sha512()
    byte_data = word.encode('utf-8')
    hash_object.update(byte_data)
    return hash_object.hexdigest()

def test_chunksize(words, size):
    time1 = time()
    with ProcessPoolExecutor(max_workers=6) as Executor:
        exec = set(Executor.map(hash_words, words, chunksize=size))
    time2 = time()
    total = time2 - time1
    print(f'{size}: {total:.3f} seconds')


def main():
    path = '/usr/share/dict/words.pre-dictionaries-common'
    words = load_words(path)
    print(f'Loaded {len(words)} words from {path}')
    base = ceil(len(words) / 4)
    sizes = [base, 100000, 50000, 10000, 5000, 1000, 500]
    for size in sizes:
        test_chunksize(words, size)

if __name__ == '__main__':
    main()

