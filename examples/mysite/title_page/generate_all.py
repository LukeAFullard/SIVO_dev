import os
import subprocess
import sys

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    this_script = os.path.abspath(__file__)

    expected_scripts = [
        "generate_dashboard.py",
        "subpage/air/generate_dashboard.py",
        "subpage/air/issues/generate_sub_dashboard.py",
        "subpage/air/issues/generate_dashboard.py",
        "subpage/air/help/generate_dashboard.py",
        "subpage/air/science/generate_dashboard.py",
        "subpage/water/generate_dashboard.py",
        "subpage/water/issues/generate_dashboard.py",
        "subpage/water/science/generate_science_page.py",
        "subpage/water/science/fmu/manawatū/generate_fmu_page.py",
        "subpage/water/science/fmu/whanganui/generate_fmu_page.py",
        "subpage/water/science/fmu/whangaehu/generate_fmu_page.py",
        "subpage/water/science/fmu/rangitikei-turakina/generate_fmu_page.py",
        "subpage/water/science/fmu/puketoi-ki-tai/generate_fmu_page.py",
        "subpage/water/science/fmu/waiopehu/generate_fmu_page.py",
        "subpage/water/science/fmu/kai-iwi/generate_fmu_page.py",
        "subpage/water/help/generate_help_page.py",
        "subpage/land/generate_dashboard.py",
        "subpage/land/issues/generate_dashboard.py",
        "subpage/land/help/generate_dashboard.py",
        "subpage/land/science/generate_dashboard.py",
        #"build_website.py",
    ]

    expected_script_paths = set(
        os.path.abspath(os.path.join(base_dir, p)) for p in expected_scripts
    )

    found_scripts = []
    unexpected_scripts = []

    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.py'):
                script_path = os.path.abspath(os.path.join(root, file))
                if script_path != this_script:
                    found_scripts.append(script_path)
                    if script_path not in expected_script_paths:
                        unexpected_scripts.append(script_path)

    if unexpected_scripts:
        print("Warning: Found the following .py files that are not in the execution list:")
        for script in unexpected_scripts:
            print(f"  - {os.path.relpath(script, base_dir)}")
        print()

    # Run only expected scripts
    for script in expected_scripts:
        script_path = os.path.abspath(os.path.join(base_dir, script))
        if not os.path.exists(script_path):
            print(f"Error: Expected script not found: {script_path}")
            sys.exit(1)

        print(f"Running {script_path}...")

        # Add the root directory and src to PYTHONPATH so that 'src' can be imported in different ways
        env = os.environ.copy()
        root_dir = os.path.abspath(os.path.join(base_dir, '../../..'))
        src_dir = os.path.join(root_dir, 'src')
        paths = [root_dir, src_dir]

        if 'PYTHONPATH' in env:
            env['PYTHONPATH'] = f"{os.pathsep.join(paths)}{os.pathsep}{env['PYTHONPATH']}"
        else:
            env['PYTHONPATH'] = os.pathsep.join(paths)

        result = subprocess.run([sys.executable, os.path.basename(script_path)], cwd=os.path.dirname(script_path), env=env)
        if result.returncode != 0:
            print(f"Error running {script_path}. Exiting.")
            sys.exit(result.returncode)

    print("All scripts executed successfully.")

if __name__ == "__main__":
    main()
