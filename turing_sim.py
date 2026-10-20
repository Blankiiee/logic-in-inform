BLANK = "_"

PARITY = """
q0 1 -> q1 1 R
q1 1 -> q0 1 R
q0 _ -> halt _ S
q1 _ -> loop _ R
loop _ -> loop _ R
"""


def parse_program(text):
    rules = {}
    for line in text.strip().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        left, right = line.split("->")
        state, symbol = left.split()
        new_state, new_symbol, move = right.split()
        rules[(state, symbol)] = (new_state, new_symbol, move)
    return rules


def run(rules, word, max_steps=1000):
    tape = dict(enumerate(word))
    head, state, steps = 0, "q0", 0
    while state != "halt":
        if steps >= max_steps:
            return "limit", steps
        symbol = tape.get(head, BLANK)
        if (state, symbol) not in rules:
            return "stuck", steps
        state, tape[head], move = rules[(state, symbol)]
        head += {"R": 1, "L": -1, "S": 0}[move]
        steps += 1
    return "halt", steps


def main():
    rules = parse_program(PARITY)
    print("Вплив кількості одиниць n на роботу машини (ліміт 1000 кроків):")
    for n in range(0, 9):
        status, steps = run(rules, "1" * n)
        if status == "halt":
            print("n = %d: зупинилась, кількість кроків: %d" % (n, steps))
        else:
            print("n = %d: ліміт кроків (%d) вичерпано, зупинки не видно" % (n, steps))
    print("Вплив ліміту кроків (n = 100):")
    for limit in (50, 1000):
        status, steps = run(rules, "1" * 100, limit)
        if status == "halt":
            print("ліміт %d: зупинилась, кількість кроків: %d" % (limit, steps))
        else:
            print("ліміт %d: ліміт вичерпано, зупинки не видно" % limit)


if __name__ == "__main__":
    main()
