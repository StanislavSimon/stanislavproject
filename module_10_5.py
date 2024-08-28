import datetime
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        for line in file:
            if line.strip():
                all_data.append(line.strip())



if __name__ == '__main__':
    filenames = [f'./file{number}.txt' for number in range(1, 5)]


    start = datetime.datetime.now()
    print(f"Начало линейного выполнения: {start}")

    for filename in filenames:
        read_info(filename)
    end = datetime.datetime.now()
    linear_execution = end - start
    print(f'Конец линейного выполнения: {end}')
    print(f'Линейное выполнение заняло: {linear_execution}')


    start = datetime.datetime.now()
    print(f"Начало многопроцессного выполнения: {start}")

    with Pool() as pool:
        pool.map(read_info, filenames)

    end = datetime.datetime.now()
    multiprocessing_execution = end - start
    print(f'Конец многопроцессного выполнения: {end}')
    print(f'Многопроцессное выполнение заняло: {multiprocessing_execution}')


