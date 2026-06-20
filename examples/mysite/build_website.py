import os
import shutil
from pathlib import Path

# Base paths calculated relative to this script
base_dir = Path(__file__).parent
src_dir = base_dir / "title_page"
build_dir = base_dir / "build"

if build_dir.exists():
    shutil.rmtree(build_dir)
build_dir.mkdir(parents=True, exist_ok=True)

extensions_to_copy = {'.ico', '.webp', '.html', '.jpg', '.jpeg', '.png', '.svg', '.json', '.js', '.css', '.woff', '.woff2', '.ttf', '.gif'}

for root, dirs, files in os.walk(src_dir):
    for file in files:
        if Path(file).suffix.lower() in extensions_to_copy:
            src_path = Path(root) / file
            # Get path relative to src_dir
            rel_path = src_path.relative_to(src_dir)
            dest_path = build_dir / rel_path

            # Create directories if they don't exist
            dest_path.parent.mkdir(parents=True, exist_ok=True)

            # Copy file
            shutil.copy2(src_path, dest_path)

print(f"Build complete. Files packaged into {build_dir}")
