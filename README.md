# Python Flake

A simple Python project with code quality checks (flake8 and black) set up to run on pull requests to the main branch.

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`

## Development Workflow

1. Make changes to the code
2. Run formatters locally: `black .`
3. Run linters locally: `flake8 .`
4. Create a pull request to the main branch
5. GitHub Actions will automatically check your code with flake8 and black

## Code Quality Tools

- **flake8**: A Python linter that checks for style guide enforcement
- **black**: An uncompromising code formatter for Python

Both tools run automatically on pull requests to ensure code quality. 