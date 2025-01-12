from utils import list_notes, preview_note_in_browser, save_note, load_note, delete_note
from rich.console import Console
from rich.markdown import Markdown

console = Console()

def main_menu():
    console.print("[bold blue]Markdown Note-Taking App[/bold blue]")
    console.print("1. Create a new note")
    console.print("2. View a note")
    console.print("3. List all notes")
    console.print("4. Delete a note")
    console.print("5. Exit")

    choice = input("Enter your choice: ")
    return choice

def create_note():
    title = input("Enter note title: ")
    content = input("Write your note (Markdown supported):\n")
    save_note(title, content)
    console.print("[green]Note saved successfully![/green]")

def view_note():
    title = input("Enter note title to view: ")
    content = load_note(title)
    if content:
        console.print(Markdown(content))
    else:
        console.print("[red]Note not found![/red]")

def list_all_notes():
    notes = list_notes()
    if notes:
        console.print("[bold]Available Notes:[/bold]")
        for note in notes:
            console.print(f"- {note}")
    else:
        console.print("[yellow]No notes available.[/yellow]")

def delete_note_menu():
    title = input("Enter note title to delete: ")
    delete_note(title)
    console.print("[green]Note deleted successfully![/green]")
    
def preview_note():
    title = input("Enter note title to preview: ")
    result = preview_note_in_browser(title)
    console.print(result)

def main():
    while True:
        choice = main_menu()
        if choice == "1":
            create_note()
        elif choice == "2":
            view_note()
        elif choice == "3":
            list_all_notes()
        elif choice == "4":
            delete_note_menu()
        elif choice == "5":
             preview_note()
        elif choice == "6":
            console.print("[bold green]Goodbye![/bold green]")
            break
        else:
            console.print("[red]Invalid choice! Please try again.[/red]")

if __name__ == "__main__":
    main()
