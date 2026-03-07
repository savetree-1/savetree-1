from PIL import Image, ImageDraw
import os

files = ["lang.png", "frontend.png", "backend.png", "database.png", "cloud.png", "aiml.png"]
output_radius = 30 # User disliked pill shape (radius=height/2), reverting to subtle 30px

def process_image(filename):
    if not os.path.exists(filename):
        print(f"Skipping {filename}, not found.")
        return

    img = Image.open(filename).convert("RGBA")
    w, h = img.size
    
    # User said "crop up and down" and "dont crop more" -> Stick to 0.25 (Slimmer headers)
    trim_percentage = 0.25
    trim_px = int(h * trim_percentage)
    
    # Define crop box (left, top, right, bottom)
    crop_box = (0, trim_px, w, h - trim_px)
    
    # Crop
    img = img.crop(crop_box)
    
    # Now apply rounded corners to the cropped image
    w_new, h_new = img.size
    
    # Create mask for rounded corners
    mask = Image.new('L', (w_new, h_new), 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle([(0,0), (w_new, h_new)], radius=output_radius, fill=255)
    
    # Apply mask
    result = Image.new('RGBA', (w_new, h_new), (0,0,0,0))
    result.paste(img, (0,0), mask=mask)
    
    # Save back (overwrite original)
    result.save(filename)
    print(f"Processed {filename}: Cropped {trim_px}px Top/Bottom & Radius {output_radius}.")

if __name__ == "__main__":
    for f in files:
        process_image(f)
