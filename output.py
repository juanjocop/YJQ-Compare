# output.py
from rich.console import Console
from rich.table import Table
from rich import print

console = Console()

def mostrar_resultado(diff):
    if not diff:
        console.print("[green]No hay diferencias entre los archivos.[/green]")
        return

    table = Table(title="Diferencias entre archivos")

    table.add_column("Tipo de Diferencia", style="cyan", no_wrap=True)
    table.add_column("Detalles", style="magenta")

    for tipo, detalles in diff.items():
        table.add_row(tipo, str(detalles))

    console.print(table)
