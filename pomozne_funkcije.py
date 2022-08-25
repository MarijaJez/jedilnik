import hashlib
import random


def hashSHA256(s):
    h = hashlib.sha256(s.encode("utf8"))
    return h.hexdigest()


def izberi(obtezen_seznam, koliko):
    izbrani = []
    while koliko:
        izbira = random.choice(obtezen_seznam)
        while izbira in obtezen_seznam:
            obtezen_seznam.remove(izbira)
        izbrani.append(izbira)
        koliko -= 1

    return izbrani