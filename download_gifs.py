import re
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import requests

urls = [
    "https://cyber.dabamos.de/88x31/index.html",
    "https://cyber.dabamos.de/88x31/index2.html",
    "https://cyber.dabamos.de/88x31/index3.html",
    "https://cyber.dabamos.de/88x31/index4.html",
    "https://cyber.dabamos.de/88x31/index5.html",
]

gif_urls = []


def download_gif(save_path: Path, gif: str):
    response_gif = requests.get("https://cyber.dabamos.de/88x31/" + gif)
    save_path.write_bytes(response_gif.content)


with ThreadPoolExecutor(max_workers=4) as executor:
    for url in urls:
        response = requests.get(url)
        response.text
        gifs = re.findall(
            r'([^"]+\.gif).*height="31" width="88"', response.text, re.IGNORECASE
        )

        for gif in gifs:
            print(f"\rProcessing {gif}...", end=" ")
            save_path = Path(__file__).parent / "public" / "88x31" / gif

            if save_path.exists():
                continue

            executor.submit(download_gif, save_path, gif)
