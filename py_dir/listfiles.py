import os
from settings.config import settingslog_path
from rich.console import Console
from rich.table import Table

style = ""

console = Console(width=100)

lslog = [file for file in os.listdir(settingslog_path) if file.endswith('.log')]
file_count = len(lslog)
table = Table()
lslog = lslog.__str__()

with console.pager():
    if file_count > 0:
        table.add_column("Logfiles", style = "green", justify="center")
        table.add_row(lslog)
        console.print(table)

    else:
        console.print("No files found!", style=style, justify="right")
