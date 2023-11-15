"""
ADVANCED PYTHON 

Task - create a function that sets a random target time for the user. if the user clicks the enter button, the elapsed time is showm
the respective response is shown as per the elapsed time and target time difference

"""
import time
import random

def waiting_game():
    target = random.randint(2,4)
    print("\n Your target time is ", target," seconds")

    input('---------- PRESS ENTER TO BEGIN -------------')
    start = time.perf_counter()

    input(f'\n.... Press enter again after {target} seconds.........')
    elapsed = time.perf_counter-start

    print(f'\n Elapsed time : {elapsed :.3f} seconds')

    if elapsed==target:
        print('(Unbelievable! Perfect timing!)')
    elif elapsed<target:
        print(f'({target-elapsed :.3f} seconds too fast)')
    else:
        print(f'({elapsed-target :.3f} seconds too slow)')
