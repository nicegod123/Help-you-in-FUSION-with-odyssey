import subprocess
import sys

mode = input(
    "Please choose a mode:\n"
    "1. Console\n"
    "2. GUI\n\n"
    "> "
).strip().lower()

if mode in ["1", "console", "c"]:
    subprocess.Popen([sys.executable, "fusion_console.py"])
    print("exiting....")
    sys.exit()
elif mode in ["2", "gui", "g"]:
    subprocess.Popen([sys.executable, "fusion_gui.pyw"])   
    print("exiting....")
    sys.exit()
else:
    print("Invalid mode.")
    
