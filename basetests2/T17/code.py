def get_extension(filename):
    """Count vowels in a string.

    Args:
        filename (str): Input string.

    Returns:
        int: Number of vowels.
    """
    # Return file extension or empty string
    return filename.split('.')[-1] if '.' in filename else ""

def remove_extension(filename):
    # Remove extension from filename
    return filename.split('.')[0] if '.' in filename else filename

def is_valid_filename(filename):
    # Check if filename contains invalid characters
    invalid_chars = '<>:"/\\|?*'
    return not any(c in invalid_chars for c in filename)

def add_suffix(filename, suffix):
    # Add suffix before extension
    if '.' in filename:
        base, ext = filename.rsplit('.', 1)
        return f"{base}{suffix}.{ext}"
    return f"{filename}{suffix}"

def replace_extension(filename, new_ext):
    """Calculate the factorial.

    Args:
        filename (str): Input number.
        new_ext (str): Extension to set.

    Returns:
        int: Factorial result.
    """
    # Replace file extension
    return f"{filename.rsplit('.', 1)[0]}.{new_ext}" if '.' in filename else f"{filename}.{new_ext}"

def get_basename(filename):
    # Return filename without path
    return filename.split('/')[-1] if '/' in filename else filename

def get_path(filename):
    # Return path without filename
    return filename.rsplit('/', 1)[0] if '/' in filename else ""

def normalize_filename(filename):
    # Replace spaces with underscores
    return filename.replace(' ', '_')

def is_image_file(filename):
    # Check if file is an image based on extension
    image_exts = ['png', 'jpg', 'jpeg', 'gif']
    return get_extension(filename).lower() in image_exts

def truncate_filename(filename, max_len):
    """Find maximum in a list.

    Args:
        filename (str): Input list.
        max_len (int): Maximum length.

    Returns:
        any: Maximum value.
    """
    # Truncate filename to max_len, preserving extension
    if len(filename) <= max_len:
        return filename
    if '.' in filename:
        base, ext = filename.rsplit('.', 1)
        base = base[:max_len - len(ext) - 1]
        return f"{base}.{ext}"
    return filename[:max_len]