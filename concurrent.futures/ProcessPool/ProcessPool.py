from multiprocessing import get_all_start_methods, get_start_method
from concurrent.futures import ProcessPoolExecutor

result = get_all_start_methods()

print(result)

print(get_start_method())

pool = ProcessPoolExecutor()
print(pool._max_workers)