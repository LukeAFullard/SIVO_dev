import os

def build():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    src_dir = os.path.join(base_dir, 'src')

    # Load separate files
    with open(os.path.join(src_dir, 'index_template.html'), 'r', encoding='utf-8') as f:
        index_template = f.read()

    with open(os.path.join(src_dir, 'annotator_template.html'), 'r', encoding='utf-8') as f:
        annotator_template = f.read()

    with open(os.path.join(src_dir, 'builder_template.html'), 'r', encoding='utf-8') as f:
        builder_template = f.read()

    with open(os.path.join(src_dir, 'app.css'), 'r', encoding='utf-8') as f:
        app_css = f.read()

    with open(os.path.join(src_dir, 'app.js'), 'r', encoding='utf-8') as f:
        app_js = f.read()

    with open(os.path.join(src_dir, 'editor_boilerplate.py'), 'r', encoding='utf-8') as f:
        editor_boilerplate = f.read()

    with open(os.path.join(src_dir, 'annotator.css'), 'r', encoding='utf-8') as f:
        annotator_css = f.read()

    with open(os.path.join(src_dir, 'annotator.js'), 'r', encoding='utf-8') as f:
        annotator_js = f.read()

    # Process annotator_template.html
    annotator = annotator_template.replace('        /* ANNOTATOR_CSS_PLACEHOLDER */', annotator_css)
    annotator = annotator.replace('        // ANNOTATOR_JS_PLACEHOLDER', annotator_js)

    # Process index_template.html
    output_html = index_template.replace('        /* APP_CSS_PLACEHOLDER */', app_css)
    output_html = output_html.replace('EDITOR_BOILERPLATE_PLACEHOLDER', editor_boilerplate)
    output_html = output_html.replace('        // APP_JS_PLACEHOLDER', app_js)
    output_html = output_html.replace('        <!-- ANNOTATOR_TEMPLATE_PLACEHOLDER -->', annotator)
    output_html = output_html.replace('        <!-- APP_BUILDER_PLACEHOLDER -->', builder_template)

    with open(os.path.join(base_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(output_html)

    print("Build complete: examples/web_app/index.html has been generated.")

if __name__ == '__main__':
    build()
