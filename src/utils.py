# utils.py

import os
import datetime

def ensure_export_folder(path="exports"):
    os.makedirs(path, exist_ok=True)

def banner(title: str) -> str:
    """
    Returns a centered title banner for CLI output.

    Example:
        >>> print(banner("RC Designer"))
        ======== RC Designer ========
    """
    return f"\n{'=' * 8} {title} {'=' * 8}\n"

def timestamp() -> str:
    """
    Returns current timestamp string (YYYY-MM-DD HH:MM:SS).
    Useful for logs, report headers, or saved filenames.
    """
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def format_summary(data: dict) -> str:
    """
    Formats a key-value dict into neat CLI-style output.

    Example:
        >>> format_summary({"fck": 30, "fcd": 20})
        fck: 30
        fcd: 20
    """
    lines = [f"{key}: {value}" for key, value in data.items()]
    return "\n".join(lines)

def warn(msg: str) -> str:
    """
    Formats a warning message with emphasis.

    Example:
        >>> print(warn("Invalid input"))
        ⚠️  Warning: Invalid input
    """
    return f"⚠️  Warning: {msg}"
