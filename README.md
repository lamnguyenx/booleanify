# Booleanify

Inspired by Pydantic's boolean, Booleanify is a Python package that provides a simple utility for converting strings representing boolean values into actual boolean values.

## Installation

You can install Booleanify using pip:

\`\`\`bash
pip install booleanify
\`\`\`

## Usage

To use Booleanify in your Python code, simply import the \`booleanify\` function and pass a string representing a boolean value to it. The function will return the corresponding boolean value.

\`\`\`python
from booleanify import booleanify

result = booleanify("T")
print(result)  # Output: True

result = booleanify("false")
print(result)  # Output: False
\`\`\`

Booleanify supports the following string representations for boolean values:

| Input  | Output |
|--------|--------|
| 1      | True   |
| '1'    | True   |
| 'on'   | True   |
| 't'    | True   |
| 'true' | True   |
| 'y'    | True   |
| 'yes'  | True   |
| 0      | False  |
| 'off'  | False  |
| 'f'    | False  |
| 'false'| False  |
| 'n'    | False  |
| 'no'   | False  |

## Contribution

If you have any suggestions, improvements, or issues regarding Booleanify, feel free to open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
