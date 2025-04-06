import random
from pathlib import Path

public_path = Path(__file__).parent / "public"

gifs_path = public_path / "88x31"

gifs = list(gifs_path.glob("*.gif"))
random.shuffle(gifs)

gifs_data = bytearray()
gif_html_elements = []


for i, gif in enumerate(gifs):
    print("\rProcessed", i, "gifs...", end="")
    gif_bytes = gif.read_bytes()
    gifs_data += gif_bytes
    gif_html_elements.append(
        f'<img src="" alt="{gif.stem}" height="31" width="88" data-length="{len(gif_bytes)}" loading="lazy" />'
    )

html_template = (public_path / "template.html").read_text()
index_html = html_template.replace("INSERT_GIF_ELEMENTS", "\n".join(gif_html_elements))

(public_path / "gif.data").write_bytes(gifs_data)
(public_path / "index.html").write_text(index_html)
