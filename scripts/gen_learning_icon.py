from PIL import Image, ImageDraw, ImageFont

def create_learning_tile():
    # SkillIcons dimensions
    size = 100 # Generating larger then resizing to 70? Or just 70.
    # Skillicons native size is 48x48 usually per icon in the URL, but rendered at height=70? 
    # Actually skillicons "per icon" is roughly square. 
    # Let's make it 200x200 and downscale to 70 for quality.
    
    img_size = 200
    bg_color = (36, 41, 56) # #242938 (Approximation of SkillIcons Dark)
    icon_color = (255, 255, 255)
    
    img = Image.new('RGBA', (img_size, img_size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Rounded Rect
    rect_coords = [(0, 0), (img_size-1, img_size-1)]
    draw.rounded_rectangle(rect_coords, radius=40, fill=bg_color)
    
    # Draw "Hourglass" symbol (using simple polygon or text)
    # Using simple shapes for hourglass
    # Triangle down
    cx, cy = img_size//2, img_size//2
    w = 80
    h = 80
    
    # Draw an hourglass shape
    # Top triangle
    draw.polygon([(cx-w, cy-h), (cx+w, cy-h), (cx, cy)], fill=(200, 200, 200))
    # Bottom triangle
    draw.polygon([(cx, cy), (cx+w, cy+h), (cx-w, cy+h)], fill=(200, 200, 200))
    
    # Save
    img.save("learning.png")
    print("Created learning.png")

if __name__ == "__main__":
    create_learning_tile()
