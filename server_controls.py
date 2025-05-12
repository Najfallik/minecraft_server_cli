# server_controls.py
import subprocess
from utils import console
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.live import Live
from threading import Thread

console_output = Console()
player_list = Console()
command_input = Console()

layout = Layout()

layout.split_column(
    Layout(name="main", ratio=2),
    Layout(name="bottom", ratio=1)
)

layout["main"].split_row(
    Layout(Panel("Console Output", title="Console"), name="console"),
    Layout(name="right")
)

layout["right"].split_column(
    Layout(Panel("Player List", title="Players"), name="players"),
    Layout(Panel("Command Input", title="Input"), name="input")
)

server_process_instance = None  # Global variable to track the server process

def start_server():
    """Start the Minecraft server with a 2-column interface."""
    global server_process_instance
    console.print("[bold green]Starting server...[/bold green]")
    
    def server_process():
        global server_process_instance
        server_process_instance = subprocess.Popen(
            ["java", "-Xmx6G", "-Xms1G", "-XX:SoftMaxHeapSize=5G",
             "-XX:+UnlockExperimentalVMOptions", "-XX:+UseZGC", "-jar", 
             "server.jar", "--nogui"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE,  # Allow sending input to the process
            text=True
        )
        for line in server_process_instance.stdout:
            console_output.print(line.strip())
        for line in server_process_instance.stderr:
            console_output.print(line.strip(), style="bold red")
    
    def live_interface():
        with Live(layout, refresh_per_second=10):
            while True:
                layout["console"].update(Panel(console_output.export_text(), title="Console"))
                layout["players"].update(Panel("Player list here", title="Players"))
                layout["input"].update(Panel("Command input here", title="Input"))
    
    Thread(target=server_process, daemon=True).start()
    Thread(target=live_interface, daemon=True).start()

def stop_server():
    """Stop the Minecraft server."""
    global server_process_instance
    if server_process_instance and server_process_instance.stdin:
        console.print("[bold red]Stopping server...[/bold red]")
        try:
            server_process_instance.stdin.write("stop\n")
            server_process_instance.stdin.flush()
            server_process_instance.wait()  # Wait for the process to terminate
            console.print("[bold green]Server stopped successfully.[/bold green]")
        except Exception as e:
            console.print(f"[bold red]Error stopping server: {e}[/bold red]")
    else:
        console.print("[bold yellow]Server is not running.[/bold yellow]")