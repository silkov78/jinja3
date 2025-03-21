from jinja2 import Template, TemplateSyntaxError
import xml.etree.ElementTree as ET
import os

def is_valid_template(file_path: str) -> bool:
    """Check if the file is a valid Jinja2 template."""
    try:
        with open(file_path, "r") as file:
            template_content = file.read()
        Template(template_content)  # Attempt to create a Jinja2 Template object
        return True
    except TemplateSyntaxError as e:
        print(f"Template syntax error: {e}")
        return False
    except Exception as e:
        print(f"Error reading template file: {e}")
        return False
