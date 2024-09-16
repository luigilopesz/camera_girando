from camera_girando.getcamera import *
import os
from rich.console import Console
import typer

app = typer.Typer()
console = Console()

@app.command('info')
def print_info(custom_message : str = ""):
    """
    Print information about the module
    """
    console.print('')
    console.print("CAMERA: python main.py run", '\n')
    console.print("COMANDOS: 'w' / 'a' / 's' / 'd' -> move a imagem em 2D", '\n')
    console.print("COMANDOS: 'q' / 'e' -> rotaciona a imagem", '\n')
    console.print("COMANDOS: 'z' / 'x' -> cisalhamento da imagem", '\n')
    console.print("COMANDOS: 'espaco' reseta a camera ao normal", '\n')
    console.print("QUIT: aperte '1' para sair", '\n')
    console.print(f"Author: camera_girando.__author__")
    console.print(f"Version: camera_girando.__version__")
    if custom_message != "":
        console.print(f"Custom message: {custom_message}")

@app.command('run')
def run():
    """
    APS 3 de LUIGI LOPES
    """
    camera()
