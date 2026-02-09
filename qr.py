!pip install qrcode[pil] pillow

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask
from PIL import Image

# ✅ YOUR REAL WEBSITE BASE URL
BASE_URL = "https://skp2403.github.io/for-her"

# QR FILES + TARGET PAGES
qr_pages = {
    "qr2.png": f"{BASE_URL}/page2.html",
    "qr3.png": f"{BASE_URL}/page3.html",
    "qr4.png": f"{BASE_URL}/page4.html",
}

def create_qr(filename, url):
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=14,   # high quality, print-ready
        border=4
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=RoundedModuleDrawer(),
        color_mask=RadialGradiantColorMask(
            center_color=(255, 77, 109),   # romantic pink
            edge_color=(160, 0, 60)        # deep rose
        ),
        back_color=(255, 255, 255)
    ).convert("RGBA")

    # ❤️ OPTIONAL CENTER HEART
    try:
        icon = Image.open("heart.PNG").convert("RGBA")
        size = img.size[0] // 4
        icon = icon.resize((size, size))

        pos = (
            (img.size[0] - icon.size[0]) // 2,
            (img.size[1] - icon.size[1]) // 2
        )
        img.paste(icon, pos, icon)
    except FileNotFoundError:
        print("ℹ️ heart.png not found — skipping logo")

    img.save(filename)
    print(f"✅ Created {filename}")

# Generate all QRs
for file, link in qr_pages.items():
    create_qr(file, link)




import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask
from PIL import Image, ImageDraw, ImageFont

# =============================
# CONFIG
# =============================
URL = "https://skp2403.github.io/for-her/"
QR_FILE = "qr_entry.png"
CARD_FILE = "qr_card.png"

CARD_WIDTH = 1240   # A6 @300dpi (approx)
CARD_HEIGHT = 1748

# =============================
# CREATE STYLED QR
# =============================
qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=14,
    border=4
)
qr.add_data(URL)
qr.make(fit=True)

qr_img = qr.make_image(
    image_factory=StyledPilImage,
    module_drawer=RoundedModuleDrawer(),
    color_mask=RadialGradiantColorMask(
        center_color=(255, 77, 109),
        edge_color=(160, 0, 60)
    ),
    back_color=(255, 255, 255)
).convert("RGBA")

# Optional heart logo
try:
    heart = Image.open("heart.png").convert("RGBA")
    size = qr_img.size[0] // 4
    heart = heart.resize((size, size))
    pos = (
        (qr_img.size[0] - size) // 2,
        (qr_img.size[1] - size) // 2
    )
    qr_img.paste(heart, pos, heart)
except:
    pass

qr_img.save(QR_FILE)

# =============================
# CREATE GREETING CARD
# =============================
card = Image.new("RGBA", (CARD_WIDTH, CARD_HEIGHT), "#fff0f5")
draw = ImageDraw.Draw(card)

# Fonts (fallback safe)
try:
    title_font = ImageFont.truetype("arial.ttf", 70)
    text_font = ImageFont.truetype("arial.ttf", 40)
except:
    title_font = ImageFont.load_default()
    text_font = ImageFont.load_default()

# Title
draw.text(
    (CARD_WIDTH // 2, 160),
    "For You ❤️",
    anchor="mm",
    fill="#b0003a",
    font=title_font
)

# Subtitle
draw.text(
    (CARD_WIDTH // 2, 260),
    "Scan when you're ready",
    anchor="mm",
    fill="#444",
    font=text_font
)

# Paste QR
qr_resized = qr_img.resize((700, 700))
card.paste(
    qr_resized,
    ((CARD_WIDTH - 700) // 2, 420),
    qr_resized
)

# Footer text
draw.text(
    (CARD_WIDTH // 2, 1200),
    "This is the beginning of something special ✨",
    anchor="mm",
    fill="#555",
    font=text_font
)

draw.text(
    (CARD_WIDTH // 2, 1300),
    "— from someone who loves you",
    anchor="mm",
    fill="#777",
    font=text_font
)

card.save(CARD_FILE)

print("✅ Created:")
print(" - qr_entry.png  (physical QR)")
print(" - qr_card.png   (print-ready greeting card)")
