import os
import subprocess
import sys

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    this_script = os.path.abspath(__file__)

    scripts_to_run = []
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.py'):
                script_path = os.path.abspath(os.path.join(root, file))
                if script_path != this_script:
                    scripts_to_run.append(script_path)

    for script in scripts_to_run:
        print(f"Running {script}...")

        # Add the root directory to PYTHONPATH so that 'src' can be imported
        env = os.environ.copy()
        root_dir = os.path.abspath(os.path.join(base_dir, '../../..'))
        if 'PYTHONPATH' in env:
            env['PYTHONPATH'] = f"{root_dir}:{env['PYTHONPATH']}"
        else:
            env['PYTHONPATH'] = root_dir

        result = subprocess.run([sys.executable, os.path.basename(script)], cwd=os.path.dirname(script), env=env)
        if result.returncode != 0:
            print(f"Error running {script}. Exiting.")
            sys.exit(result.returncode)

    print("All scripts executed successfully.")

if __name__ == "__main__":
    main()
