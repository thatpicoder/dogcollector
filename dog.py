import time
import random
import sys

if sys.platform == "win32":
    import msvcrt

    def get_key():
        if msvcrt.kbhit():
            return msvcrt.getch().decode('utf-8').lower()
        return None

else:
    import select
    import termios
    import tty

    def get_key():
        dr, _, _ = select.select([sys.stdin], [], [], 0)
        if dr:
            return sys.stdin.read(1).lower()
        return None

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    tty.setcbreak(fd)

levels = ['common', 'uncommon', 'rare', 'legendary', 'godly', "bitetheapple's best friend"]
weights = [50, 30, 15, 4, 1, 0.1]

names = {
    'common': ['max', 'buddy', 'charlie', 'rocky', 'bella'],
    'uncommon': ['luna', 'oliver', 'lucy', 'cooper', 'mia'],
    'rare': ['bailey', 'daisy', 'finn', 'hazel', 'ivy'],
    'legendary': ['jasper', 'lily', 'marcus', 'penelope', 'quentin'],
    'godly': ['seraphina', 'thorin', 'uriel', 'vivian', 'zara'],
    "bitetheapple's best friend": ['betty']
}

last_collect_time = 0
cooldown = 10
counts = {level: 0 for level in levels}

print("dog collector, made by bitetheapple")
print("press 'c' to collect a dog. 10 second cooldown.")

try:
    while True:
        key = get_key()

        if key == 'c':
            current_time = time.time()

            if current_time - last_collect_time >= cooldown:
                level = random.choices(levels, weights=weights)[0]
                name = random.choice(names[level])

                print(f"\nyou have collected a {level} dog named {name}!")
                counts[level] += 1

                for lvl in levels:
                    print(f"{lvl}: {counts[lvl]}")

                last_collect_time = current_time
            else:
                remaining = cooldown - (current_time - last_collect_time)
                print(f"\nthere is {remaining:.1f} seconds left on your cooldown!")

        time.sleep(0.1)

finally:
    if sys.platform != "win32":
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)