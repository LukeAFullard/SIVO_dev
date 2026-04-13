import os

def build():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    src_dir = os.path.join(base_dir, 'src')

    # Load separate files
    with open(os.path.join(src_dir, 'index_base.html'), 'r', encoding='utf-8') as f:
        index_base = f.read()

    with open(os.path.join(src_dir, 'annotator.html'), 'r', encoding='utf-8') as f:
        annotator = f.read()

    with open(os.path.join(src_dir, 'main.css'), 'r', encoding='utf-8') as f:
        main_css = f.read()

    with open(os.path.join(src_dir, 'main.js'), 'r', encoding='utf-8') as f:
        main_js = f.read()

    with open(os.path.join(src_dir, 'default_code.py'), 'r', encoding='utf-8') as f:
        default_code = f.read()

    with open(os.path.join(src_dir, 'annotator.css'), 'r', encoding='utf-8') as f:
        annotator_css = f.read()

    with open(os.path.join(src_dir, 'annotator.js'), 'r', encoding='utf-8') as f:
        annotator_js = f.read()

    # Process annotator.html
    annotator = annotator.replace('        /* ANNOTATOR_CSS_PLACEHOLDER */', annotator_css)
    annotator = annotator.replace('        // ANNOTATOR_JS_PLACEHOLDER', annotator_js)

    # Process index_base.html
    output_html = index_base.replace('        /* MAIN_CSS_PLACEHOLDER */', main_css)
    output_html = output_html.replace('DEFAULT_CODE_PLACEHOLDER', default_code)
    output_html = output_html.replace('        // MAIN_JS_PLACEHOLDER', main_js)
    output_html = output_html.replace('        <!-- ANNOTATOR_TEMPLATE_PLACEHOLDER -->', annotator)

    with open(os.path.join(base_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(output_html)

    print("Build complete: examples/web_app/index.html has been generated.")

if __name__ == '__main__':
    build()
