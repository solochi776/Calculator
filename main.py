#the entry files
import typer

app = typer.Typer()
@app.command()
def version(version: str):
    print(f"xyra calculator version pre:0.1")


if __name__ == "__main__":
    app()
