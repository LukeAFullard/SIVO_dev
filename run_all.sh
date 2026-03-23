#!/bin/bash
export PYTHONPATH=$(pwd)/src

cd examples/basic/01_hello_world && python main.py && cd ../../..
cd examples/basic/02_url_navigation && python main.py && cd ../../..
cd examples/basic/03_json_config && python main.py && cd ../../..
cd examples/basic/04_drilldowns && python main.py && cd ../../..
cd examples/basic/05_custom_assets && python main.py && cd ../../..
cd examples/basic/06_html_overlays && python main.py && cd ../../..
cd examples/basic/07_multi_view_standalone && python main.py && cd ../../..
cd examples/basic/08_data_binding && python main.py && cd ../../..
cd examples/basic/09_animations_markers && python main.py && cd ../../..
cd examples/basic/20_api_fetch && python main.py && cd ../../..
