# interface.py
from rich.prompt import Prompt
from rich.panel import Panel
from utils import console
from setup import setup_server
from server_controls import start_server, stop_server

def main_menu():
    """Display the main menu and handle user input."""
    menu_content = (
        "[bold]1.[/bold] Set Up Server\n"
        "[bold]2.[/bold] Start Server\n"
        "[bold]3.[/bold] Stop Server\n"
        "[bold]4.[/bold] Exit"
    )
    panel = Panel(menu_content, title="[bold]Sikko's Minecraft Server CLI[/bold]", border_style="blue")
    console.print(panel)

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