from ex2 import fetcher
from datetime import datetime

CALL_COUNT = 10


def benchmark(num):
    """
    Совершает num прогонов переданной функции и выводит в консоль время каждого прогона и среднее время всех прогонов

    :param num: число итераций
    :return: функцию обёртку
    """

    def wrapper(func):
        # put your code here
        def wrapped(*args, **kwargs):
            total_time = 0
            for i in range(num):
                start_time = datetime.now()
                func(*args, **kwargs)
                end_time = datetime.now()
                total_time += (end_time.microsecond - start_time.microsecond)
                print(f'Execution time for iteration number {i} is: {end_time.microsecond - start_time.microsecond} ms')
            print(f'Average execution time for {num} iterations is: {total_time / num} ms')
        return wrapped

    return wrapper


@benchmark(CALL_COUNT)
def fetch_page(url):
    fetcher.get(url)
