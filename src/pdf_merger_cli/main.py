import typer
from pathlib import Path
from PyPDF2 import PdfMerger
from typing import List

app = typer.Typer()

@app.command()
def merge(
    input_paths: List[Path] = typer.Argument(..., help="Paths PDF to merge"),
    output_path: Path = typer.Option(..., "--output", "-o", help="Output files"),
    ordered: bool = typer.Option(False, "--ordered", "-r", help="Use input order, or alphabetical order")
):
    """Merge multiple PDF files into a single PDF file."""
    merger = PdfMerger()

    if not ordered:
        input_paths = sorted(input_paths, key=lambda p: p.name)

    for path in input_paths:
        if not path.exists():
            typer.echo(f"File not found: {path}")
            raise typer.Exit(1)
        merger.append(str(path))

    merger.write(str(output_path))
    merger.close()
    typer.echo(f"✅ Created {output_path}")

if __name__ == "__main__":
    app()
