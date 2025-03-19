# setup.py
import os
import subprocess
import time
import requests
from rich.progress import Progress
from utils import console

def download_server_jar(url, save_path):
    """Download the Minecraft server JAR file."""
    console.print(f"[bold green]Downloading server JAR from {url}...[/bold green]")
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get("content-length", 0))

    with Progress() as progress:
        task = progress.add_task("[cyan]Downloading...", total=total_size)
        with open(save_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)
                progress.update(task, advance=len(chunk))

    console.print(f"[bold green]Server JAR downloaded to {save_path}[/bold green]")
    return

def run_initial_server_setup(server_jar):
    """Run the server for the first time to generate files."""
    console.print("[bold yellow]Running server for the first time...[/bold yellow]")
    process = subprocess.Popen(["java", "-Xmx1G", "-Xms1G", "-jar", server_jar, "nogui"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(10)  # Wait for the server to generate files
    process.terminate()
    console.print("[bold green]Initial setup complete![/bold green]")
    return

def accept_eula():
    """Accept the EULA by modifying the eula.txt file."""
    eula_path = "eula.txt"
    if os.path.exists(eula_path):
        with open(eula_path, "r") as f:
            content = f.read()
        content = content.replace("eula=false", "eula=true")
        with open(eula_path, "w") as f:
            f.write(content)
        console.print("[bold green]EULA accepted![/bold green]")
    else:
        console.print("[bold red]eula.txt not found![/bold red]")
        return

def setup_server():
    """Main function to set up the Minecraft server."""
    server_jar_url = "https://piston-data.mojang.com/v1/objects/4707d00eb834b446575d89a61a11b5d548d8c001/server.jar"
    server_jar_path = "server.jar"

    if not os.path.exists(server_jar_path):
        download_server_jar(server_jar_url, server_jar_path)

    run_initial_server_setup(server_jar_path)
    accept_eula()

    console.print("[bold green]Minecraft server setup complete![/bold green]")