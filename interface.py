# interface.py
from rich.prompt import Prompt
from rich.panel import Panel
from utils import console
from setup import setup_server
from server_controls import start_server, stop_server

def main_menu():
    """Display the main menu and handle user input."""
    console.print(Panel("[bold]Minecraft Server Interface[/bold]", title="Welcome", border_style="blue"))
    console.print("1. Set Up Server")
    console.print("2. Start Server")
    console.print("3. Stop Server")
    console.print("4. Exit")

    choice = Prompt.ask("Choose an option", choices=["1", "2", "3", "4"])

    if choice == "1":
        setup_server()
    elif choice == "2":
        start_server()
    elif choice == "3":
        stop_server()
    elif choice == "4":
        console.print("Exiting...", style="bold blue")
        exit()