# tensor-networks

A repository for tracking my study of tensor networks.

## Setup

This project uses [uv](https://docs.astral.sh/uv/) for package management and follows a src layout structure.

### Prerequisites

Install uv:
```bash
pip install uv
```

### Installation

1. Clone the repository
2. Sync dependencies:
```bash
uv sync
```

### Usage

Run Python scripts with uv:
```bash
uv run python script.py
```

Import the package:
```python
from tensor_networks import hello
print(hello())
```

### Development

Add dependencies:
```bash
uv add <package-name>
```

Add development dependencies:
```bash
uv add --dev <package-name>
```

Run commands in the virtual environment:
```bash
uv run <command>
```

### Code Quality Tools

This project uses several tools to maintain code quality:

**Linting and Formatting with Ruff:**
```bash
uv run ruff check src/ tests/      # Check for issues
uv run ruff check --fix src/ tests/  # Auto-fix issues
uv run ruff format src/ tests/      # Format code
```

**Type Checking with mypy:**
```bash
uv run mypy src/
```

**Testing with pytest:**
```bash
uv run pytest                  # Run all tests
uv run pytest -v               # Verbose output
uv run pytest tests/test_file.py  # Run specific test file
```

**Pre-commit Hooks:**

Pre-commit hooks are configured to run automatically before each commit. To install them:
```bash
uv run pre-commit install
```

To run pre-commit checks manually:
```bash
uv run pre-commit run --all-files
```
