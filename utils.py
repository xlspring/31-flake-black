def validate_input(text):
    """Validate that the input is not empty."""
    return text.strip() != ""


def format_name(name):
    """Format the name with proper capitalization."""
    return name.strip().title() 