import ast
import logging
from pathlib import Path
from typing import Any, Dict, List, Union


class DocstringExtractor:
    """Extract docstrings and type information from Python files in a directory."""

    def __init__(self, directory: str):
        """
        Initialize the DocstringExtractor.

        Args:
            directory (str): Path to the directory containing Python files
        """
        self.directory = Path(directory)
        self.setup_logging()

    def setup_logging(self):
        """Configure logging for the extractor."""
        logging.basicConfig(
            level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
        )
        self.logger = logging.getLogger(__name__)

    def get_python_files(self) -> List[Path]:
        """
        Find all Python files in the directory and its subdirectories.

        Returns:
            List[Path]: List of paths to Python files
        """
        return list(self.directory.rglob("*.py"))

    def get_type_annotation(self, node: ast.AST) -> str:
        """
        Convert AST type annotation to string representation.

        Args:
            node (ast.AST): AST node containing type annotation

        Returns:
            str: String representation of the type
        """
        if isinstance(node, ast.Name):
            return node.id
        elif isinstance(node, ast.Subscript):
            value = self.get_type_annotation(node.value)
            slice_value = self.get_type_annotation(node.slice)
            return f"{value}[{slice_value}]"
        elif isinstance(node, ast.Constant):
            return str(node.value)
        elif isinstance(node, ast.List):
            elements = [self.get_type_annotation(elt) for elt in node.elts]
            return f"[{', '.join(elements)}]"
        elif isinstance(node, ast.Tuple):
            elements = [self.get_type_annotation(elt) for elt in node.elts]
            return f"({', '.join(elements)})"
        elif isinstance(node, ast.BinOp):
            # Handle Union types (X | Y in Python 3.10+)
            if isinstance(node.op, ast.BitOr):
                left = self.get_type_annotation(node.left)
                right = self.get_type_annotation(node.right)
                return f"Union[{left}, {right}]"
        return "Any"

    def extract_function_info(
        self, node: Union[ast.FunctionDef, ast.AsyncFunctionDef]
    ) -> Dict[str, Any]:
        """
        Extract function information including docstring, arguments, and return type.

        Args:
            node (Union[ast.FunctionDef, ast.AsyncFunctionDef]): Function AST node

        Returns:
            Dict[str, Any]: Dictionary containing function information
        """
        info = {
            "docstring": ast.get_docstring(node),
            "args": {},
            "return_type": None,
            "is_async": isinstance(node, ast.AsyncFunctionDef),
        }

        # Get return type annotation
        if node.returns:
            info["return_type"] = self.get_type_annotation(node.returns)

        # Get argument types
        for arg in node.args.args:
            if arg.annotation:
                info["args"][arg.arg] = self.get_type_annotation(arg.annotation)
            else:
                info["args"][arg.arg] = "Any"

        return info

    def extract_class_info(self, node: ast.ClassDef) -> Dict[str, Any]:
        """
        Extract class information including docstring and methods.

        Args:
            node (ast.ClassDef): Class AST node

        Returns:
            Dict[str, Any]: Dictionary containing class information
        """
        info = {"docstring": ast.get_docstring(node), "methods": {}}

        for item in node.body:
            if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                info["methods"][item.name] = self.extract_function_info(item)

        return info

    def extract_docstrings_from_file(self, file_path: Path) -> Dict[str, Any]:
        """
        Extract docstrings and type information from a single Python file.

        Args:
            file_path (Path): Path to the Python file

        Returns:
            Dict[str, Any]: Dictionary containing file information
        """
        file_info = {"module_docstring": None, "classes": {}, "functions": {}}

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()

            module = ast.parse(content)

            # Get module-level docstring
            if ast.get_docstring(module):
                file_info["module_docstring"] = ast.get_docstring(module)

            for node in module.body:
                if isinstance(node, ast.ClassDef):
                    file_info["classes"][node.name] = self.extract_class_info(node)
                elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    file_info["functions"][node.name] = self.extract_function_info(node)

        except Exception as e:
            self.logger.error(f"Error processing {file_path}: {str(e)}")

        return file_info

    def extract_all_docstrings(self) -> Dict[str, Dict[str, str]]:
        """
        Extract docstrings from all Python files in the directory.

        Returns:
            Dict[str, Dict[str, str]]: Dictionary mapping file paths to their docstrings
        """
        all_docstrings = {}
        python_files = self.get_python_files()

        self.logger.info(f"Found {len(python_files)} Python files to process")

        for file_path in python_files:
            self.logger.info(f"Processing {file_path}")
            relative_path = file_path.relative_to(self.directory)
            all_docstrings[str(relative_path)] = self.extract_docstrings_from_file(
                file_path
            )

        return all_docstrings

    def save_documentation(self, output_file: str = "documentation.md"):
        """
        Save extracted docstrings and type information as Markdown documentation.

        Args:
            output_file (str): Path to the output markdown file
        """
        all_docstrings = self.extract_all_docstrings()

        with open(output_file, "w", encoding="utf-8") as f:
            f.write("# Project Documentation\n\n")

            for file_path, file_info in all_docstrings.items():
                f.write(f"## {file_path}\n\n")

                if file_info["module_docstring"]:
                    f.write("### Module Documentation\n\n")
                    f.write(f"{file_info['module_docstring']}\n\n")

                # Document classes
                for class_name, class_info in file_info["classes"].items():
                    f.write(f"### Class: {class_name}\n\n")
                    if class_info["docstring"]:
                        f.write(f"{class_info['docstring']}\n\n")

                    for method_name, method_info in class_info["methods"].items():
                        f.write(f"#### {method_name}\n\n")
                        if method_info["is_async"]:
                            f.write("*Async method*\n\n")

                        # Write signature
                        args_str = ", ".join(
                            [
                                f"{arg}: {type_}"
                                for arg, type_ in method_info["args"].items()
                            ]
                        )
                        return_type = (
                            f" -> {method_info['return_type']}"
                            if method_info["return_type"]
                            else ""
                        )
                        f.write(
                            f"```python\n{method_name}({args_str}){return_type}\n```\n\n"
                        )

                        if method_info["docstring"]:
                            f.write(f"{method_info['docstring']}\n\n")

                # Document functions
                for func_name, func_info in file_info["functions"].items():
                    f.write(f"### Function: {func_name}\n\n")
                    if func_info["is_async"]:
                        f.write("*Async function*\n\n")

                    # Write signature
                    args_str = ", ".join(
                        [f"{arg}: {type_}" for arg, type_ in func_info["args"].items()]
                    )
                    return_type = (
                        f" -> {func_info['return_type']}"
                        if func_info["return_type"]
                        else ""
                    )
                    f.write(f"```python\n{func_name}({args_str}){return_type}\n```\n\n")

                    if func_info["docstring"]:
                        f.write(f"{func_info['docstring']}\n\n")

        self.logger.info(f"Documentation saved to {output_file}")


# Example usage
if __name__ == "__main__":
    extractor = DocstringExtractor("./")
    extractor.save_documentation()
