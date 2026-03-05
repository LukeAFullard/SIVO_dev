import sys
import os

# Add the src directory to the sys path so we can import sivo
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sivo.cli import main

if __name__ == '__main__':
    main()
