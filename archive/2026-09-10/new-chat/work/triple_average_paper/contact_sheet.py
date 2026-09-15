"""Create a contact sheet for visual inspection of the compiled paper."""

from pathlib import Path
from PIL import Image, ImageDraw

root = Path(__file__).resolve().parent / 'build'
paths = sorted(root.glob('page-*.png'))
width, height, columns = 260, 390, 4
sheet = Image.new('RGB', (columns * width, ((len(paths) + columns - 1) // columns) * height), '#dddddd')
draw = ImageDraw.Draw(sheet)
for i, path in enumerate(paths):
    with Image.open(path) as source:
        page = source.convert('RGB')
        page.thumbnail((width - 12, height - 26))
        x = (i % columns) * width + (width - page.width) // 2
        y = (i // columns) * height + 20
        sheet.paste(page, (x, y))
        draw.text(((i % columns) * width + 8, (i // columns) * height + 4), str(i + 1), fill='black')
sheet.save(root / 'contact_sheet.png')
print('Rendered pages:', len(paths))
