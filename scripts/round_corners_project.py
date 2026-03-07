from PIL import Image, ImageDraw
import os

files = ["project1.png", "forestfire.png", "gitconnectx.png", "metashield.png", "image-ste.png", "lc.png", "cc.png", "cf.png", "aws.png", "cisco.png", "google.png", "nptel1.png", "nptel2.png"]
output_radius = 30

def process_image(filename):
    if not os.path.exists(filename):
        print(f"Skipping {filename}, not found.")
        return

    img = Image.open(filename).convert("RGBA")
    w, h = img.size
    
    # Create mask for rounded corners
    mask = Image.new('L', (w, h), 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle([(0,0), (w, h)], radius=output_radius, fill=255)
    
    # Apply mask
    result = Image.new('RGBA', (w, h), (0,0,0,0))
    result.paste(img, (0,0), mask=mask)
    
    # Save back
    result.save(filename)
    print(f"Processed {filename}: Applied radius {output_radius}.")

if __name__ == "__main__":
    for f in files:
        process_image(f)
