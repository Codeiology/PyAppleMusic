import subprocess
import colorama
from colorama import Fore, Back, Style, init
init()
import sys
import os
import time
import signal
user_interrupt_occured = False
def user_interrupt(signal, frame):
	global user_interrupt_occured
	user_interrupt_occured = True
	print("")
	print("Program stopped.")
	print("")
	sys.exit()
signal.signal(signal.SIGINT, user_interrupt)
def type_text(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.001)
    print("")
def type_text_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print("")
def loading_screen(message):
    print(message, end="")
    spinner = ["|", "/", "-", "\\"]
    start_time = time.time()
    i = 0
    while True:
        if time.time() - start_time > 3:
            print("\b \b" * (len(message) + 1), end="")
            break
        print(f"\b{spinner[i%4]}", end="", flush=True)
        i += 1
        time.sleep(0.05)
def play():
	name = prompt[len("play "):]
	script = f'tell application "Music" to play track  "{name}"'
	result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
	if result.returncode == 0:
		type_text_slow(Fore.GREEN + "Playing... " + Fore.RESET)
	else:
		print(Fore.RED + f"Song not found in library: {name}." + Fore.RESET)
def pause():
	script = 'tell application "Music" to pause'
	subprocess.run(['osascript', '-e', script])
def search(search_term):
	script = f'tell application "Music" to get the name of (every track whose name contains "{search_term}")'
	result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
	output = result.stdout.strip().split(', ')
	if output == ['']:
		type_text_slow(Fore.RED + "No results. Searches queries must be 100% accurate." + Fore.RESET)
	else:
		outputclean = str.join(", ", output)
		print("")
		print(outputclean)
		print("")
os.system("clear")
logo = '''

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⡿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣠⣤⣤⣤⣀⣀⠈⠋⠉⣁⣠⣤⣤⣤⣀⡀⠀⠀
⠀⢠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀
⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀    APPLE MUSIC
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀    by Taj Entabi
⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀ 
⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁    
⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀  
⠀⠀⠀⠈⠙⢿⣿⣿⣿⠿⠟⠛⠻⠿⣿⣿⣿⡿⠋

'''
type_text(logo)
while True:
	prompt = input("applemusic> ")
	if prompt == "help":
		ins = '''
		
APPLE MUSIC

play <songname> = Play a song from the Apple Music Library
search <query> = Search for a song in your library
exit = exit

'''
		type_text(ins)
	elif prompt.startswith("play"):
		play()
	elif prompt == "pause":
		pause()
	elif prompt.startswith("search"):
		query = prompt[len("search "):]
		search(query)
	elif prompt == "exit":
		print("")
		print("")
		sys.exit()
	else:
		print(Fore.RED + "Invalid command. Type, 'help' to see available commands." + Fore.RESET)
if user_interrupt_ocurred:
	sys.exit(0)