# server_controls.py
import subprocess
from utils import console

def start_server():
    """Start the Minecraft server."""
    console.print("[bold green]Starting server...[/bold green]")
    subprocess.run(["java", "-Xmx6G", "-Xms1G", "-XX:SoftMaxHeapSize=5G",
                    "-XX:+UnlockExperimentalVMOptions", "-XX:+UseZGC", "-jar", 
                    "server.jar", "--nogui"])

def stop_server():
    """Stop the Minecraft server."""
    console.print("[bold red]Stopping server...[/bold red]")
    subprocess.run(["stop"], input=b"stop\n", shell=True)