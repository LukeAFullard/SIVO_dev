from sivo import Sivo
from sivo.core.project import SivoProject

def test():
    svg_content = """<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect id="TX" x="10" y="10" width="80" height="80" fill="#ccc" />
        <rect id="CA" x="110" y="10" width="80" height="80" fill="#ccc" />
        <rect id="NY" x="10" y="110" width="80" height="80" fill="#ccc" />
        <rect id="WY" x="110" y="110" width="80" height="80" fill="#ccc" />
    </svg>"""
    app = Sivo.from_string(svg_content)

    data = {
        "TX": {"sales": 15000},
        "CA": {"sales": 22000},
        "NY": {"sales": 8000},
        "WY": {"sales": 500}
    }

    app.bind_data(
        data=data,
        key="sales",
        colors=["#e0f3db", "#43a2ca"],
        min_val=0,
        max_val=25000
    )

    app.to_html("test_bind_data.html")

if __name__ == "__main__":
    test()
