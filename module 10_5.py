import time
from multiprocessing import Pool


def read_info(name):
    with open(name, 'r') as f:
        lines = []
        while True:
            line = f.readline().strip()
            if not line:
                break
            lines.append(line)


def main():
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    start_time = time.perf_counter()
    for filename in filenames:
        _ = read_info(filename)
    linear_time = time.perf_counter() - start_time
    print(f"Линейное выполнение: {linear_time}")

    if __name__ == '__main__':
        pool = Pool()
        start_time = time.perf_counter()
        res = pool.map(read_info, filenames)
        multi_process_time = time.perf_counter() - start_time
        print(f"Многопроцессное выполнение: {multi_process_time}")


if __name__ == '__main__':
    main()
