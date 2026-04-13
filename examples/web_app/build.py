import os

def build():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    src_dir = os.path.join(base_dir, 'src')

    with open(os.path.join(src_dir, 'index_base.html'), 'r', encoding='utf-8') as f:
        index_base = f.read()

    with open(os.path.join(src_dir, 'annotator.html'), 'r', encoding='utf-8') as f:
        annotator = f.read()

    output_html = index_base.replace('<!-- ANNOTATOR_TEMPLATE_PLACEHOLDER -->', annotator)

    with open(os.path.join(base_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(output_html)

    print("Build complete: examples/web_app/index.html has been generated.")

if __name__ == '__main__':
    build()
