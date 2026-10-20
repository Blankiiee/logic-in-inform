def fibonacci(n):
    a, b = 0, 1
    seq = []
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq


def find_period(seq):
    for p in range(1, len(seq) // 2 + 1):
        if all(seq[i] == seq[i + p] for i in range(len(seq) - p)):
            return p
    return None


def has_recurrence(seq):
    return all(seq[i] == seq[i - 1] + seq[i - 2] for i in range(2, len(seq)))


def tricky(n):
    seq = [x % 10 for x in fibonacci(n)]
    for i in range(1000, n):
        seq[i] = 7
    return seq


def main():
    seq = fibonacci(200)
    print("Рекурентне співвідношення a(n) = a(n-1) + a(n-2):", has_recurrence(seq))
    for m in (2, 3, 10):
        print("Період залишків за модулем %d: %s" % (m, find_period([x % m for x in seq])))
    print("Відношення сусідніх членів: %.10f" % (seq[-1] / seq[-2]))
    print("Золотий перетин:           %.10f" % ((1 + 5 ** 0.5) / 2))
    last_digits = [x % 10 for x in fibonacci(1200)]
    print("Останні цифри, 200 членів: період", find_period(last_digits[:200]))
    print("Послідовність tricky, 200 членів: період", find_period(tricky(200)))
    print("Останні цифри, 1200 членів: період", find_period(last_digits))
    print("Послідовність tricky, 1200 членів: період", find_period(tricky(1200)))


if __name__ == "__main__":
    main()
