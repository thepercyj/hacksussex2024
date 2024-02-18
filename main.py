import time
from datetime import datetime
from board import *
import psutil


GridWidth = 11
GridHeight = 5


def get_memory_footprint():
    process = psutil.Process()
    memory_usage = process.memory_info().rss  # Get the memory usage in bytes
    memory_usage_mb = memory_usage / (1024 * 1024)  # Convert bytes to megabytes
    return memory_usage_mb


Pieces = [
    " A  \n" +
    " A  \n" +
    "AA  \n",

    " B  \n" +
    "BB  \n" +
    "BB  \n",

    " C  \n" +
    " C  \n" +
    " C  \n" +
    "CC  \n",

    " D  \n" +
    " D  \n" +
    "DD  \n" +
    " D  \n",

    " E  \n" +
    " E  \n" +
    "EE  \n" +
    "E   \n",

    "F   \n" +
    "FF  \n",

    "  G \n" +
    "  G \n" +
    "GGG \n",

    "  H \n" +
    " HH \n" +
    "HH  \n",

    "I I \n" +
    "III \n",

    "J   \n" +
    "JJ  \n" +
    "J   \n",

    " KK  \n" +
    "KK  \n",

    " L  \n" +
    "LL  \n" +
    " LL \n"
]


def main():
    start_time = time.time()
    answer = Kanoodle.findAllSolutions(Pieces, GridWidth, GridHeight)
    end_time = time.time()

    if answer:
        current_date = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename = f'output_{current_date}.txt'
        print("Type of answer is", answer)
        with open(filename, 'w') as file:
            for solution in answer:
                for row in solution:
                    file.write(''.join(row) + '\n')
                file.write('\n')
        print("Time taken: " + (str((end_time - start_time) * 1000)) + "ms")
        memory_usage = get_memory_footprint()
        print("Memory footprint:", memory_usage, "MB")


if __name__ == "__main__":
    main()
