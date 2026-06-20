import os
import shutil

def build_website():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    source_dir = os.path.join(base_dir, "title_page")
    build_dir = os.path.join(base_dir, "build")

    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)

    os.makedirs(build_dir)

    copied_files = 0

    for root, dirs, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(file_path, source_dir)

            parts = os.path.normpath(rel_path).split(os.sep)

            # Copy all html files, and everything in the assets directory
            if file.endswith('.html') or parts[0] == 'assets':
                dest_path = os.path.join(build_dir, rel_path)
                dest_dir = os.path.dirname(dest_path)

                if not os.path.exists(dest_dir):
                    os.makedirs(dest_dir)

                shutil.copy2(file_path, dest_path)
                copied_files += 1

    print(f"Successfully built website in {build_dir}. Copied {copied_files} files.")

if __name__ == "__main__":
    build_website()
