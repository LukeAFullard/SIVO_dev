#!/bin/bash
export PYTHONPATH=$(pwd)/src

for dir in examples/basic/*/; do
  if [ -f "$dir/main.py" ]; then
    echo "Running main.py in $dir"
    (cd "$dir" && python main.py)
  fi
done
