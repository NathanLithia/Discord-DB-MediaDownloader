import requests
import time
import ctypes

def main():
    Downloader(DiscoverLines())

def DiscoverLines():
    lines = 0
    with open("links.txt") as file:
        print("Starting Discovery Process")
        for line in file:
            ctypes.windll.kernel32.SetConsoleTitleW(f"Scanning Files: {lines}")
            lines = lines+1
        return lines

def Downloader(lines):
    filenum = 1
    with open("links.txt") as file:
        print("Starting Downloading Process")
        for line in file:
            ctypes.windll.kernel32.SetConsoleTitleW(f"Downloading file: {filenum}/{lines}")
            print(line)
            if line.startswith('https://'):
                r = requests.get(line.rstrip("\n"), allow_redirects=True)
                fixpass0 = line.lstrip("https://cdn.discordapp.com/attachments/").rstrip("\n")
                fixpass1 = fixpass0.replace('/', '.')
                fixpass2 = fixpass1.replace(':', ';')
                open(f"./files/{fixpass2}", 'wb').write(r.content)
                filenum = filenum+1
                time.sleep(0.1)
            else:
                print(f"Bad Link: {filenum}/{lines} {line}")

main()