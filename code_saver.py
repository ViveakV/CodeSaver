#!/usr/bin/env python3

import json
import os
import pyperclip

CONFIG_FILE = os.path.join(os.path.expanduser("~"), ".snippet_config.json")

# Function to get the file path from the user
def get_snippets_file_path():
    """Prompt the user for the location to store snippets on first run."""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as config:
            return json.load(config).get("snippets_file", "snippets.json")

    default_path = os.path.join(os.path.expanduser("~"), "snippets.json")
    print(f"Default snippets file location: {default_path}")
    custom_path = input("Enter a custom path or press Enter to use the default: ").strip()

    snippets_file = os.path.abspath(custom_path) if custom_path else default_path

    # Save the chosen path to the config file
    with open(CONFIG_FILE, "w") as config:
        json.dump({"snippets_file": snippets_file}, config)

    return snippets_file

# Prompt user for file location on first run
SNIPPETS_FILE = get_snippets_file_path()

# Ensure the snippets file exists
if not os.path.exists(SNIPPETS_FILE):
    with open(SNIPPETS_FILE, "w") as file:
        json.dump([], file)

def load_snippets():
    """Load snippets from the JSON file."""
    with open(SNIPPETS_FILE, "r") as file:
        return json.load(file)

def save_snippets(snippets):
    """Save snippets to the JSON file."""
    with open(SNIPPETS_FILE, "w") as file:
        json.dump(snippets, file, indent=4)

def add_snippet():
    """Add a new code snippet."""
    title = input("Enter a title for the snippet: ").strip()
    description = input("Enter a short description: ").strip()
    code = input("Enter the code snippet: ").strip()

    snippet = {
        "title": title,
        "description": description,
        "code": code
    }

    snippets = load_snippets()
    snippets.append(snippet)
    save_snippets(snippets)

    print("Snippet added successfully!\n")

def copy_snippet_to_clipboard(snippets):
    """Copy a selected snippet's code to the clipboard."""
    try:
        choice = int(input("Enter the number of the snippet to copy: ").strip())
        if 1 <= choice <= len(snippets):
            snippet = snippets[choice - 1]
            pyperclip.copy(snippet['code'])
            print(f"Snippet '{snippet['title']}' copied to clipboard!\n")
        else:
            print("Invalid number. Please try again.\n")
    except ValueError:
        print("Invalid input. Please enter a number.\n")

def search_snippets():
    """Search for snippets by title or description."""
    query = input("Enter a search term: ").strip().lower()
    snippets = load_snippets()

    results = [s for s in snippets if query in s["title"].lower() or query in s["description"].lower()]

    if results:
        print(f"\nFound {len(results)} snippet(s):\n")
        for i, snippet in enumerate(results, start=1):
            print(f"{i}. {snippet['title']}\n   {snippet['description']}\n   Code:\n{snippet['code']}\n")
        copy_snippet_to_clipboard(results)
    else:
        print("\nNo snippets found.\n")

def list_snippets():
    """List all stored snippets."""
    snippets = load_snippets()

    if snippets:
        print(f"\nStored Snippets ({len(snippets)}):\n")
        for i, snippet in enumerate(snippets, start=1):
            print(f"{i}. {snippet['title']}\n   {snippet['description']}\n Code:\n{snippet['code']}\n")
        copy_snippet_to_clipboard(snippets)
    else:
        print("\nNo snippets stored yet.\n")

def main():
    """Main menu for the Code Snippet Organizer."""
    while True:
        print("\nCode Snippet Organizer")
        print("1. Add a snippet")
        print("2. Search snippets")
        print("3. List all snippets")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_snippet()
        elif choice == "2":
            search_snippets()
        elif choice == "3":
            list_snippets()
        elif choice == "4":
            print("Byeeeeeeeeeee!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
