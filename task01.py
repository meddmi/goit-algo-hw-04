"""Recursively copy files and sort them by extension."""

import shutil
import sys
from pathlib import Path

from colorized_logger import (
    print_error as log_error,
    print_info as log_info,
    print_warning as log_warning,
)

IGNORE_FILE_NAMES = {".DS_Store", "Thumbs.db"}


def get_unique_path(target: Path) -> Path:
    """Return a unique target path to avoid overwriting a file."""
    if not target.exists():
        return target

    counter = 1
    while True:
        candidate = target.with_name(f"{target.stem}_{counter}{target.suffix}")
        if not candidate.exists():
            return candidate
        counter += 1


def copy_directory_by_extension(source: Path, destination: Path) -> None:
    """Recursively copy files into directories named by extension."""
    try:
        for entry in source.iterdir():
            process_entry(entry, destination)
    except OSError as error:
        log_error(f"Cannot read directory {source}: {error}")


def process_entry(entry: Path, destination: Path) -> None:
    """Skip ignored entries, recurse into directories, or copy files."""
    try:
        if entry.name in IGNORE_FILE_NAMES:
            return

        if entry.resolve() == destination:
            return

        if entry.is_dir():
            copy_directory_by_extension(entry, destination)
            return

        if entry.is_file():
            copy_file_to_extension_directory(entry, destination)
            return

        log_warning(f"Skipping unknown entry type: {entry}")

    except OSError as error:
        log_error(f"Cannot process {entry}: {error}")


def copy_file_to_extension_directory(file_path: Path, destination_dir: Path) -> None:
    """Copy a file into an extension-based directory without overwriting."""
    extension = file_path.suffix.removeprefix(".").lower() or "no_extension"

    extension_dir = destination_dir / extension
    extension_dir.mkdir(parents=True, exist_ok=True)

    target_path = get_unique_path(extension_dir / file_path.name)
    shutil.copy2(file_path, target_path)

    log_info(
        f"  Copied {file_path.name} -> {target_path.parent.name}/{target_path.name}"
    )


def parse_arguments() -> tuple[Path, Path] | None:
    """Read the source and optional destination from sys.argv."""
    if not 2 <= len(sys.argv) <= 3:
        log_error("Usage: python task01.py <source_directory> [destination_directory]")
        return None

    source = Path(sys.argv[1]).resolve()
    destination = (
        Path(sys.argv[2]).resolve() if len(sys.argv) == 3 else Path("dist").resolve()
    )
    return source, destination


def main() -> None:
    """Validate paths and start copying files."""
    paths = parse_arguments()
    if paths is None:
        return

    source, destination = paths

    if not source.exists():
        log_error(f"Source path does not exist: {source}")
        return

    if not source.is_dir():
        log_error(f"Source path is not a directory: {source}")
        return

    if source == destination:
        log_error("Source and destination cannot be the same directory.")
        return

    try:
        destination.mkdir(parents=True, exist_ok=True)
    except OSError as error:
        log_error(f"Cannot create destination directory: {error}")
        return

    log_info(f"Copying files from {source} to {destination}...")
    copy_directory_by_extension(source, destination)


if __name__ == "__main__":
    main()
