# Agent Scaffolder

A Python tool to automatically create project structures from text file descriptions.

## Features

- Create complete project directory structures from a simple text file
- Automatically generates placeholder files
- Supports nested directory structures
- Easy-to-use command-line interface

## Installation

```bash
pip install -e .
```

Or using Poetry:

```bash
poetry install
```

## Usage

```bash
python src/scaffolder.py <structure_file> <destination>
```

### Example

```bash
python src/scaffolder.py example.txt ./my_new_project
```

This will create a project structure based on the `example.txt` file in the `./my_new_project` directory.

## Structure File Format

The structure file should use a tree-like format:

```
project_name/
├── src/
│   ├── __init__.py
│   ├── main.py
├── tests/
│   ├── __init__.py
│   ├── test_main.py
├── README.md
└── setup.py
```

## Requirements

- Python 3.9+

## License

See LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

**Other Languages:**
- [हिंदी (Hindi)](README.hi.md)
- [Français (French)](README.fr.md)
