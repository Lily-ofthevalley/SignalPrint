import click
from commands.generate import generate

@click.group()
def cli():
    """Main CLI entry point."""
    pass

cli.add_command(generate)

def show_start_screen():
    """Display the start screen and handle user input."""
    click.clear()
    click.echo("====================================")
    click.echo("Welcome to the SignalPrint CLI Tool!")
    click.echo("====================================")
    click.echo("\nPlease choose an option:")
    click.echo("1. Automatically Generate QR Code and STL")
    click.echo("2. Generate QR Code and STL for Custom Wifi (COMING SOON)")
    click.echo("3. Exit")

    while True:
        choice = click.prompt("Enter your choice (1, 2 or 3)", type=int)

        if choice == 1:
            click.clear()
            click.echo("\nYou selected: Generate QR Code and STL")
            click.echo("======================================")
            generate()
            break
        elif choice == 2:
            click.clear()
            click.echo("\nExiting the program. Goodbye!")
            click.echo("=============================")
            break
        elif choice == 3:
            click.clear()
            click.echo("\nExiting the program. Goodbye!")
            click.echo("=============================")
            break
        else:
            click.echo("Invalid choice. Please enter 1, 2 or 3.")

if __name__ == "__main__":
    show_start_screen()