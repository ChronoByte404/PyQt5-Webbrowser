import os

print("Attempting universal installation scripts.")

os.system("python3 -m pip install PyQt5")
os.system("python3 -m pip install PyQtwebEngine")

print("Attempting Windows script.")

os.system("pip install PyQt5")
os.system("pip install PyQtwebEngine")

print("Done.")
