# Code Saver

`code_saver` is a lightweight command-line tool for organizing, storing, and retrieving code snippets. It lets you easily add, search, and list code snippets through an interactive terminal interface.

## Features

- Save and organize code snippets with a title and description.
- Search snippets by title, description, or content.
- List all saved snippets in a readable format, including their code.
- Copy snippet code to the clipboard directly from search or list results.
- Fully portable and customizable storage location for snippets.

## Installation

### 1. Clone or Download the Script

Save the `code_saver` script to your local machine.

### 2. Make the Script Executable

Make sure the script has executable permissions:

```bash
chmod +x code_saver
```

### 3. Move the Script to a Directory in `$PATH`

To make `code_saver` accessible globally from any terminal session, copy it to a directory included in your `$PATH`. For example:

```bash
sudo cp code_saver.py /usr/local/bin/
```

Alternatively, if you want to use a custom directory, you can:

1. Create a directory for your scripts (if not already created):
   ```bash
   mkdir -p ~/scripts
   ```
2. Copy the script to this directory:
   ```bash
   cp code_saver.py ~/scripts/
   ```
3. Add the directory to your `$PATH` by editing your shell configuration file (e.g., `~/.bashrc` or `~/.zshrc`):
   ```bash
   echo 'export PATH="$PATH:~/scripts"' >> ~/.bashrc
   ```
4. Reload the shell configuration:
   ```bash
   source ~/.bashrc
   ```

## Usage

Once installed, you can invoke the `code_saver` command from anywhere in your terminal.

### Example Usage

#### 1. Adding a Snippet

```bash
$ code_saver
Code Saver
1. Add a snippet
2. Search snippets
3. List all snippets
4. Exit

Enter your choice (1-4): 1
Enter a title for the snippet: Hello World in Python
Enter a short description: Basic Python Hello World example
Enter the code snippet: print("Hello, World!")

Snippet added successfully!
```

#### 2. Searching Snippets

```bash
$ code_saver
Code Saver
1. Add a snippet
2. Search snippets
3. List all snippets
4. Exit

Enter your choice (1-4): 2
Enter a search term: Python

Found 1 snippet(s):
1. Hello World in Python
   Basic Python Hello World example
   Code:
   print("Hello, World!")

Enter the number of the snippet to copy: 1
Snippet 'Hello World in Python' copied to clipboard!
```

#### 3. Listing All Snippets

```bash
$ code_saver
Code Saver
1. Add a snippet
2. Search snippets
3. List all snippets
4. Exit

Enter your choice (1-4): 3

Stored Snippets (1):
1. Hello World in Python
   Basic Python Hello World example
   Code:
   print("Hello, World!")

Enter the number of the snippet to copy: 1
Snippet 'Hello World in Python' copied to clipboard!
```

#### 4. Adding More Complex Snippets

You can also add complex code snippets like multi-line functions or classes:

```bash
$ code_saver
Code Saver
1. Add a snippet
2. Search snippets
3. List all snippets
4. Exit

Enter your choice (1-4): 1
Enter a title for the snippet: Factorial Function in Python
Enter a short description: Python function to calculate factorial using recursion
Enter the code snippet: 
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

Snippet added successfully!
```

When listing or searching, this snippet will appear just like any other and can be copied to the clipboard for use.

## Customizing the Snippets File Location

When you first run `code_saver`, you'll be prompted to specify where the snippets should be stored. If no input is given, the default location (`~/snippets.json`) will be used. You can provide a custom path at runtime.

## License

This project is open source and available under the MIT License.

---

Enjoy using `code_saver` to keep all your code snippets organized!
