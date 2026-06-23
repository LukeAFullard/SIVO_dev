import os
import shutil
import hashlib
import sys

def get_file_hash(filepath):
    """Calculate MD5 hash of a file."""
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def build_website(subfolder=None):
    # This script is located in examples/mysite/title_page/build_website.py
    source_dir = os.path.dirname(os.path.abspath(__file__))
    # Target directory is examples/mysite/build
    target_dir = os.path.abspath(os.path.join(source_dir, "../build"))

    if subfolder:
        source_walk_dir = os.path.join(source_dir, subfolder)
        target_cleanup_dir = os.path.join(target_dir, subfolder)
        print(f"Building website subfolder '{subfolder}' from {source_walk_dir} to {target_cleanup_dir}...")
    else:
        source_walk_dir = source_dir
        target_cleanup_dir = target_dir
        print(f"Building website from {source_dir} to {target_dir}...")

    # Ensure target directory exists
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    allowed_extensions = {
        '.html', '.css', '.js', '.json', '.geojson',
        '.png', '.jpg', '.jpeg', '.gif', '.svg'
    }

    count = 0
    copied_count = 0
    valid_dest_files = set()

    if not os.path.exists(source_walk_dir):
        print(f"Source directory {source_walk_dir} does not exist.")
        return

    for root, dirs, files in os.walk(source_walk_dir):
        # Skip the target directory if it's somehow inside the source directory
        dirs[:] = [d for d in dirs if os.path.abspath(os.path.join(root, d)) != target_dir]

        # Determine relative path from source_dir
        rel_path = os.path.relpath(root, source_dir)

        for file in files:
            # Skip python files and other non-web assets
            if file.endswith('.py') or file.endswith('.md'):
                continue

            _, ext = os.path.splitext(file)
            if ext.lower() in allowed_extensions:
                src_file = os.path.join(root, file)
                dest_file = os.path.join(target_dir, rel_path, file)
                valid_dest_files.add(os.path.abspath(dest_file))

                # Check if file needs to be copied
                should_copy = True
                if os.path.exists(dest_file):
                    if get_file_hash(src_file) == get_file_hash(dest_file):
                        should_copy = False

                if should_copy:
                    # Ensure destination directory exists
                    dest_dir = os.path.dirname(dest_file)
                    if not os.path.exists(dest_dir):
                        os.makedirs(dest_dir)

                    shutil.copy2(src_file, dest_file)
                    copied_count += 1

                count += 1

    # Cleanup stale files in target directory
    removed_count = 0
    if os.path.exists(target_cleanup_dir):
        for root, dirs, files in os.walk(target_cleanup_dir, topdown=False):
            for file in files:
                dest_file = os.path.join(root, file)
                if os.path.abspath(dest_file) not in valid_dest_files:
                    os.remove(dest_file)
                    removed_count += 1

            # Remove empty directories
            for d in dirs:
                dir_path = os.path.join(root, d)
                if not os.listdir(dir_path):
                    os.rmdir(dir_path)

    print(f"Build complete. {count} files processed, {copied_count} files copied, {removed_count} stale files removed.")
    print(f"Website packaged in: {target_dir}")

subfolder_arg = None
if sys.argv and "build_website.py" in sys.argv[0] and len(sys.argv) > 1:
    subfolder_arg = sys.argv[1]

# Only execute automatically if it appears to be run directly as a script
if sys.argv and "build_website.py" in sys.argv[0]:
    build_website(subfolder_arg)
