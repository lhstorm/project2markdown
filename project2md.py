import os
from pathlib import Path

def generate_code_markdown(project_path, output_filename="codebase.md"):
    """
    Generates a Markdown file containing the code files in a project,
    excluding 'node_modules' and similar dependency directories.
    """

    print(f"Generating code Markdown for project: {project_path}")

    # 1. Define Code File Extensions
    code_extensions = {".py", ".js", ".jsx", ".ts", ".tsx"}  # Python and JavaScript extensions

    # 2. Define Directories to Exclude (Hardcoded for Simplicity)
    exclude_directories = {"node_modules", ".next", "out", ".venv", "build", "dist"} # common dependency folders

    def should_exclude(path: Path) -> bool:
        """
        Checks if a given path should be excluded based on the hardcoded list
        or if it's a hidden file/directory.
        """
        if any(part in exclude_directories for part in path.parts):
            return True
        if path.name.startswith("."):  # Exclude hidden files/directories
            return True
        return False

    # 3. Create Markdown Content
    markdown_content = "## Code Files\n\n"
    project_path_obj = Path(project_path)

    for file_path in project_path_obj.rglob("*"):
        if file_path.is_file() and file_path.suffix in code_extensions:
            if not should_exclude(file_path):
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        code_content = f.read()
                    markdown_content += f"### {file_path.name}\n\n```\n{code_content}\n```\n\n"
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

    # 4. Write to Markdown File
    output_path = Path(project_path) / output_filename  # Create the output path using pathlib
    try:
        with open(output_path, "w", encoding="utf-8") as outfile:
            outfile.write(markdown_content)
        print(f"Successfully generated {output_filename} in {project_path}")
    except Exception as e:
        print(f"Error writing to {output_path}: {e}")

    print("Code Markdown generation finished.")


if __name__ == "__main__":
    project_directory = os.getcwd()  # Use the current directory as the project path
    generate_code_markdown(project_directory)
