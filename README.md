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