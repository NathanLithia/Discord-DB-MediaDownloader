import os
from csv import reader
import time
DesiredFiles = ('.png', '.jpg', '.jpeg', '.webp', '.PNG', '.JPG', '.JPEG', '.WEBP')
savedata = open("links.txt", "w")
newline = "\n"
debug = False
for MessageInstance in os.listdir('./messages'):
    if MessageInstance.endswith(".json"):
        pass
    else:
        print(MessageInstance)
        for MessageFolder in os.listdir(f"./messages/{MessageInstance}"):
            if MessageFolder.endswith(".json"):
                pass
            else:
                print("   ", MessageFolder)
                if MessageFolder.endswith('.csv'):
                    print("      ","Contents:")
                    with open(f"./messages/{MessageInstance}/{MessageFolder}",encoding="utf8") as read_obj:
                        csv_reader = reader(read_obj)
                        for row in csv_reader:
                            for data in row:
                                if data.endswith(DesiredFiles):
                                    print(data)
                                    if debug == True:
                                        savedata.write(f"{data.replace(' http',f'{newline}http')}\n")
                                        savedata.write(f"{data}\n\n")
                                    else:
                                        savedata.write(f"{data.replace(' http',f'{newline}http')}\n")
savedata.close()
