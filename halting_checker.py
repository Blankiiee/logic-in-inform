import os
import subprocess
import sys
import time

TIMEOUT = 10


def check_program(path, timeout=TIMEOUT):
    if not os.path.exists(path):
        return "файл не знайдено"
    start = time.time()
    try:
        result = subprocess.run([sys.executable, path], capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        return "не завершилась за %d с (невідомо, чи завершиться взагалі)" % timeout
    elapsed = time.time() - start
    if result.returncode == 0:
        return "завершилась за %.1f с" % elapsed
    return "завершилась з помилкою (код %d)" % result.returncode


if __name__ == "__main__":
    for program in sys.argv[1:]:
        print("%s: %s" % (program, check_program(program)))
