import sys
import time
import os

PINK = "\033[95m"
BLUE = "\033[94m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

lyrics = [
    f"{PINK}💗 <Kisi Ne Na Kiya Hai Jaisa Ishq Tera Mera>...{RESET}",
    f"{BLUE}🎤 <Me Daudta Aata Hoon Koi Naam Le Jo Tera>...{RESET}",
    f"{CYAN}💞 <Kisi Ne Na Kiya Hai Jaisa Ishq Tera Mera>...{RESET}",
    f"{GREEN}🌙 <Mere Ghamon Ki Raat Ka Tu Ujla Savera>...{RESET}",
    f"{YELLOW}✨ <Rhne Do Na Nashe Me>...{RESET}",
    f"{PINK}✮.✮.˙♡{RESET}"
]

delays = [0.2, 0.2, 0.2, 0.2, 1.5, 4.2]

os.system("cls")

print("~" * 60)
print("✨ HALKA HALKA SONG LYRICS ✨".center(60))
print("~" * 60)
print()

def type_line(line):
    for char in line:
        print(char, end="", flush=True)
        time.sleep(0.07)
    print()

time.sleep(2)

for i in range(len(lyrics)):
    type_line(lyrics[i])
    time.sleep(delays[i])
