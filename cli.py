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
    click.echo("1. Generate QR Code and STL")
    click.echo("2. Exit")

    while True:
        choice = click.prompt("Enter your choice (1 or 2)", type=int)

        if choice == 1:
            click.echo("\nYou selected: Generate QR Code and STL")
            generate()  # Call the generate command
            break
        elif choice == 2:
            click.echo("\nExiting the program. Goodbye!")
            break
        else:
            click.echo("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    show_start_screen()