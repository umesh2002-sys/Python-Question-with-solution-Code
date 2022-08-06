import time
import random

def waiting_game():
    target = random.randint(2, 4)
    print(f'\nYour target tome os {target} seconds')

    input(' --- Press Enter to Begin--- ')
    # perf_counter function always returns the float value of time in seconds
    start = time.perf_counter()

    input(f'\n ...Please Enter again after {target} seconds ...')
    elapsed = time.perf_counter() - start

    print('\n Elapsed time: {0:.2f} seconds'.format(target))
    if elapsed == target:
        print('Unbelievable! Perfect timing!')
        print('Great work')
    elif elapsed < target:
        timing = target - elapsed
        print('{0:.0f} seconds is too fast.'.format(timing))
    else:
        timing = elapsed - target
        print('{0:.3f} second is too slow'.format(timing))


if __name__ == "__main__":
    waiting_game()
