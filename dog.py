import msvcrt
import time
import random

levels = ['common', 'uncommon', 'rare', 'legendary', 'godly', 'bitetheapple\'s best friend']
weights = [50, 30, 15, 4, 1, 0.1]
names = {
    'common': ['max', ' buddy', 'charlie', 'rocky', 'bella'],
    'uncommon': ['luna', 'oliver', ' lucy', 'cooper', 'mia'],
    'rare': ['bailey', 'daisy', 'finn', 'hazel', 'ivy'],
    'legendary': ['jasper', 'lily', 'marcus', 'penelope', 'quentin'],
    'godly': ['seraphina', 'thorin', 'uriel', 'vivian', 'zara'],
    'bitetheapple\'s best friend': ['betty']
}
last_collect_time = 0
cooldown = 10
counts = {level: 0 for level in levels}
print("dog collector, made by bitetheapple")
print("press 'c' to collect a dog. 10 second cooldown.")

while True:
    if msvcrt.kbhit():
        key = msvcrt.getch().decode('utf-8').lower()
        if key == 'c':
            current_time = time.time()
            if current_time - last_collect_time >= cooldown:
                level = random.choices(levels, weights=weights)[0]
                name = random.choice(names[level])
                print(f"you have collected a {level} dog named {name}!")
                counts[level] += 1
                for lvl in levels:
                    print(f"{lvl}: {counts[lvl]}")
                last_collect_time = current_time
            else:
                remaining = cooldown - (current_time - last_collect_time)
                print(f"there is {remaining:.1f} seconds left on your cooldown!")
    time.sleep(0.1)