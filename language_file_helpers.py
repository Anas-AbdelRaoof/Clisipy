import sys
from rich import print
import os


# Mapping of supported language names (keys) to their file extensions (values).
# Keys should be lowercase and may include common aliases (e.g. "js" and "javascript").
# Values include the leading dot (".py", ".js") so they can be compared directly
# against the value returned from os.path.splitext(filename)[1].
# Keep this dictionary updated when you add/remove supported languages.
languages_extensions = {
    "python": ".py",
    "c++": ".cpp",
    "cpp": ".cpp",
    "c": ".c",
    "java": ".java",
    "ruby": ".rb",
    "c#": ".cs",
    "cs": ".cs",
    "csharp": ".cs",
    "php": ".php",
    "rust": ".rs",
    "go": ".go",
    "golang": ".go",
    "lua": ".lua",
    "swift": ".swift",
    "kotlin": ".kt",
    "dart": ".dart",
    "gdscript": ".gd",
    "js": ".js",
    "javascript": ".js",
    "zig": ".zig",
    "julia": ".jl",
    "f#": ".fs",
    "fsharp": ".fs",
    # Cython extension should include the leading dot like the others
    "cython": ".pyx",
}  # Notice: the languages names were lower() before this dictionary


def check_lang(language_name, language_file):
    """
    Validate that the given filename matches the expected file extension for the
    provided programming language name.

    Parameters
    - language_name: str
        Name of the programming language (e.g. "python", "javascript"). This
        function normalizes to lower-case before lookup, so callers may use any
        case.

    - language_file: str
        The filename to check (e.g. "example.py"). The function inspects the
        file extension and compares it with the expected extension for the
        language.

    Returns
    - True if the language is supported and the file has the expected
      extension.
    - False otherwise (and prints a helpful message explaining the mismatch).

    Behavior notes / implementation details
    - We use os.path.splitext to extract the file extension because it is
      robust to filenames with multiple dots (e.g. "archive.tar.gz").
    - The language lookup is case-insensitive (we call .lower() on the input
      language name prior to checking the dictionary).
    - The languages_extensions dictionary stores extensions with a leading dot
      so we can compare directly to the result of os.path.splitext.
    """

    # Normalize the language name so lookups are case-insensitive and match
    # the dictionary keys which are all lower-case.
    language_key = language_name.lower()

    try:
        # Expected extension for the provided language name. If the language is
        # not present in the mapping a KeyError will be raised and handled
        # below.
        expected_extension = languages_extensions[language_key]

        # Use os.path.splitext to safely extract the extension from the
        # filename (includes the leading dot or empty string if none).
        _, file_extension = os.path.splitext(language_file)

        # If the file extension doesn't match what we expect for the language,
        # print a helpful, colorized message and return False.
        if file_extension != expected_extension:
            # Construct a suggested filename by replacing the current
            # extension (if any) with the expected one. If the filename had no
            # extension we simply append the expected extension.
            if file_extension:
                suggested_name = language_file[:-len(file_extension)] + expected_extension
            else:
                suggested_name = language_file + expected_extension

            # Rich-formatted output to inform the user of the mismatch and show
            # a suggested filename that would be correct for the given
            # programming language.
            print(
                f"""
[red]File <[italic blue]{language_file}[/italic blue]> is not [italic blue]{language_name.title()}[/italic blue] file[/red]
[green]Did you mean <[yellow]{suggested_name}[/yellow]>?[/green]
                """
            )
            return False

    except KeyError:
        # The requested language is not present in the mapping of supported
        # languages. Inform the user and return False.
        print(
            f"[red]Language [italic blue]{language_name.title()}[/italic blue] is not allowed or not a recognized language[/red]"
        )
        return False

    # If we reach here, the language exists in the mapping and the file's
    # extension matched the expected one.
    return True
