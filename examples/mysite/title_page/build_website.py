import os
import shutil

def build_website():
    # This script is located in examples/mysite/title_page/build_website.py
    source_dir = os.path.dirname(os.path.abspath(__file__))
    # Target directory is examples/mysite/build
    target_dir = os.path.abspath(os.path.join(source_dir, "../build"))

    print(f"Building website from {source_dir} to {target_dir}...")

    # Clean target directory
    if os.path.exists(target_dir):
        print(f"Cleaning existing build directory: {target_dir}")
        shutil.rmtree(target_dir)
    os.makedirs(target_dir)

    allowed_extensions = {
        '.html', '.css', '.js', '.json', '.geojson',
        '.png', '.jpg', '.jpeg', '.gif', '.svg'
    }

    count = 0
    for root, dirs, files in os.walk(source_dir):
        # Determine relative path from source_dir
        rel_path = os.path.relpath(root, source_dir)

        # Don't copy the script itself or other python files
        if rel_path == ".":
            # We are in the source_dir root
            pass

        for file in files:
            # Skip python files and other non-web assets
            if file.endswith('.py') or file.endswith('.md'):
                continue

            _, ext = os.path.splitext(file)
            if ext.lower() in allowed_extensions:
                src_file = os.path.join(root, file)
                dest_file = os.path.join(target_dir, rel_path, file)

                # Ensure destination directory exists
                dest_dir = os.path.dirname(dest_file)
                if not os.path.exists(dest_dir):
                    os.makedirs(dest_dir)

                shutil.copy2(src_file, dest_file)
                count += 1

    print(f"Build complete. Copied {count} files.")
    print(f"Website packaged in: {target_dir}")

build_website()
