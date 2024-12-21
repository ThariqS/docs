import json
import re
from pathlib import Path


def convert_ipynb_to_mdx(input_path, output_path=None):
    """
    Convert a Jupyter Notebook (.ipynb) file to MDX format

    Args:
        input_path (str): Path to input .ipynb file
        output_path (str, optional): Path for output .mdx file. If None, uses same name as input

    Returns:
        str: Path to the created MDX file
    """
    # Read the notebook file
    with open(input_path, "r", encoding="utf-8") as f:
        notebook = json.load(f)

    # Initialize MDX content with frontmatter
    mdx_content = []
    mdx_content.append("---")
    mdx_content.append('title: "' + Path(input_path).stem + '"')
    mdx_content.append('date: "' + notebook.get("metadata", {}).get("date", "") + '"')
    mdx_content.append("---\n")

    # Process each cell
    for cell in notebook["cells"]:
        cell_type = cell["cell_type"]
        source = cell["source"]

        # Combine source lines and remove any ANSI escape sequences
        if isinstance(source, list):
            source = "".join(source)
        source = re.sub(r"\x1b\[[0-9;]*m", "", source)

        if cell_type == "markdown":
            # Add markdown content directly
            mdx_content.append(source.strip())
            mdx_content.append("\n")

        elif cell_type == "code":
            # Start a code group for code and output
            has_output = bool(cell.get("outputs", []))
            if has_output:
                mdx_content.append("<CodeGroup>")

            # Format code cells with proper markdown code block syntax
            mdx_content.append("```python Code\n")
            mdx_content.append(source.strip())
            mdx_content.append("```")

            # Include output if present
            outputs = cell.get("outputs", [])
            output_content = []
            for output in outputs:
                if "text" in output:
                    output_content.append("```output Output\n")
                    output_content.append("".join(output["text"]).strip())
                    output_content.append("```")
                elif "data" in output:
                    # Handle different output types
                    data = output["data"]
                    if "text/plain" in data:
                        output_content.append("```output Output\n")
                        output_content.append("".join(data["text/plain"]).strip())
                        output_content.append("```")
                    if "image/png" in data:
                        output_content.append("```output Output\n")
                        output_content.append("*[Image output]*")
                        output_content.append("```")

            if output_content:
                mdx_content.extend(output_content)

            if has_output:
                mdx_content.append("</CodeGroup>")

            mdx_content.append("\n")

    # Set output path
    if output_path is None:
        output_path = str(Path(input_path).with_suffix(".mdx"))

    # Write the MDX file
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(mdx_content))

    return output_path


# Example usage
if __name__ == "__main__":
    input_notebook = "../../python/examples/jailbreak.ipynb"
    output_path = "../notebooks/jailbreak.mdx"
    output_mdx = convert_ipynb_to_mdx(input_notebook, output_path)
    print(f"Created MDX file: {output_mdx}")
