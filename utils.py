import os
import markdown
import webbrowser

NOTES_DIR = "notes"
os.makedirs(NOTES_DIR, exist_ok=True)

def list_notes():
    """List all Markdown notes in the notes directory."""
    return [f for f in os.listdir(NOTES_DIR) if f.endswith(".md")]

def save_note(title, content):
    """Save a new note or update an existing one."""
    filepath = os.path.join(NOTES_DIR, f"{title}.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

def load_note(title):
    """Load the content of a specific note."""
    filepath = os.path.join(NOTES_DIR, f"{title}.md")
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    return None

def delete_note(title):
    """Delete a specific note."""
    filepath = os.path.join(NOTES_DIR, f"{title}.md")
    if os.path.exists(filepath):
        os.remove(filepath)

def preview_note_in_browser(title):
    """Render a Markdown note as HTML and open it in the browser."""
    filepath = os.path.join(NOTES_DIR, f"{title}.md")
    if not os.path.exists(filepath):
        return "Note not found!"
    
    # Read the Markdown file
    with open(filepath, "r", encoding="utf-8") as f:
        md_content = f.read()
    
    # Convert Markdown to HTML
    html_content = markdown.markdown(md_content)

    # Create a temporary HTML file
    temp_html_file = "preview.html"
    with open(temp_html_file, "w", encoding="utf-8") as f:
        f.write(f"""
        <html>
        <head>
            <title>{title}</title>
        </head>
        <body>
            {html_content}
        </body>
        </html>
        """)

    # Open the HTML file in the default web browser
    webbrowser.open(f"file://{os.path.abspath(temp_html_file)}")
    return "Preview opened in your browser!"
