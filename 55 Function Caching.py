# import time
# from functools import lru_cache
#
# @lru_cache(maxsize=256 )
#
#
# def some_work(n):
#     # Some task taking n seconds
#     time.sleep(n)
#     return n
#
# if __name__ == '__main__':
#     print("Now running some work")
#     some_work(3)
#     print("done... Calling Again")
#     some_work(3)
#     print("called Again")

import time
from functools import lru_cache

@lru_cache(maxsize=int(input('how many cache data you want ? \n')))
def run_cache(n):
    print('cache run')
    time.sleep(n)
    time.sleep(5)
    print('file run again')
run_cache(3)
