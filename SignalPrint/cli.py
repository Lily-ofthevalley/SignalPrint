import click
from SignalPrint.commands.generate import generate
from SignalPrint.commands.generate_custom import generate_custom

WELCOME_ART = r"""
 _____ _                   _______     _       _   
/  ___(_)                 | | ___ \   (_)     | |  
\ `--. _  __ _ _ __   __ _| | |_/ / __ _ _ __ | |_ 
 `--. \ |/ _` | '_ \ / _` | |  __/ '__| | '_ \| __|
/\__/ / | (_| | | | | (_| | | |  | |  | | | | | |_ 
\____/|_|\__, |_| |_|\__,_|_\_|  |_|  |_|_| |_|\__|
          __/ |                                    
         |___/                                     
"""

@click.group()
def cli():
    """Welcome to SignalPrint type [SignalPrint start] to start the program."""
    pass

cli.add_command(generate)
cli.add_command(generate_custom)

@cli.command()
def start():
    """Display the start screen and handle user input."""
    click.clear()

    # Display ASCII Art
    click.secho(WELCOME_ART, fg='cyan', bold=True)

    # Welcome Message
    click.secho("=============================================", fg='blue', bold=True)
    click.secho("🎉 Welcome to the SignalPrint CLI Wizard! 🎉", fg='cyan', bold=True)
    click.secho("=============================================", fg='blue', bold=True)

    #Menu options
    click.echo("\nPlease choose an option:\n")
    click.secho("1. Automatically Generate QrCode Sign", fg='cyan')
    click.secho("2. Manually Generate QrCode Sign", fg='cyan')
    click.secho("3. Exit", fg='red')

    while True:
        choice = click.prompt("\nEnter your choice (1, 2 or 3)", type=int)

        if choice == 1:
            click.clear()
            click.secho(WELCOME_ART, fg='cyan', bold=True)

            click.secho("================================================", fg='blue', bold=True)
            click.secho("You selected: Automatically Generate QrCode Sign", fg='cyan', bold=True)
            click.secho("================================================", fg='blue', bold=True)
            cli(args=["generate"])
            break
        elif choice == 2:
            click.clear()
            click.secho(WELCOME_ART, fg='cyan', bold=True)

            click.secho("================================================", fg='blue', bold=True)
            click.secho("You selected: Manually Generate QrCode Sign", fg='cyan', bold=True)
            click.secho("================================================", fg='blue', bold=True)
            cli(args=["generate_custom"])
            break
        elif choice == 3:
            click.clear()
            click.secho("\nExiting the program. Goodbye!", fg='red', bold=True)
            break
        else:
            click.echo("Invalid choice. Please enter 1, 2 or 3.")

if __name__ == "__main__":
    start()