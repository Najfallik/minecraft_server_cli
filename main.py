# main.py
import time
from interface import main_menu

if __name__ == "__main__":
    while True:
        main_menu()
        time.sleep(1)  # Add a small delay to prevent high CPU usage