# Table4LLM

Table4LLM is a tool designed to convert HTML tables into a
format that is consumable by Large Language Models (LLMs).
It provides both a web-based interface and a Python-based
backend for cleaning and sanitizing HTML table data.

## Features

- **Web Interface**: Paste HTML table data into a web interface,
  preview the cleaned table, and get sanitized HTML output.
- **Python Backend**: Use the Python script to clean and sanitize HTML tables programmatically.
- **HTML Sanitization**: Ensures that only specific tags and attributes are allowed,
  making the output safe and clean.

## Requirements

- Python 3.12 or higher
- Dependencies listed in `pyproject.toml`:
  - `bleach>=6.2.0`
