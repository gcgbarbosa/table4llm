import bleach


def read_file_to_variable(file_path: str):
    """
    Reads the content of a text file and stores it in a variable.

    Args:
        file_path (str): The path to the text file.

    Returns:
        str: The content of the file as a string.

    Raises:
        FileNotFoundError: If the file does not exist.
        IOError: If there is an error reading the file.
    """

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        return content
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {file_path} was not found.")
    except IOError as e:
        raise IOError(f"An error occurred while reading the file: {e}")


def clean_html(html_input: str) -> str:
    """
    Cleans and sanitizes an HTML string by allowing only specific tags and attributes.

    Args:
        html_input (str): The HTML string to be sanitized.

    Returns:
        str: The sanitized HTML string with disallowed tags and attributes removed.
    """

    allowed_tags = [
        "table",
        "thead",
        "tbody",
        "tfoot",
        "tr",
        "td",
        "th",
        "colgroup",
        "col",
    ]
    allowed_attrs = {"*": ["rowspan", "colspan", "span"]}

    # Sanitize HTML
    clean_html = bleach.clean(
        html_input, tags=allowed_tags, attributes=allowed_attrs, strip=True
    )

    # Replace &nbsp; with space
    clean_html = clean_html.replace("&nbsp;", " ")

    return clean_html


if __name__ == "__main__":
    html_file = read_file_to_variable("out.html")
    cleaned_html = clean_html(html_file)

    print(cleaned_html)
