import os
import torch
from torchvision import transforms
from PIL import Image, ImageDraw
import math

label_dir = "temp/predict34/labels/"
image_dir = "Main_dataset/"
output_dir = "YoloV8-FT_Star_red_output/"

os.makedirs(output_dir, exist_ok=True)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def draw_star(draw, center_x, center_y, num_points=5, diameter=10, color=(102, 51, 0)):
    angle = 360 / num_points
    radius = diameter // 2
    outer_radius = radius
    inner_radius = int(radius * 0.4)
    points = []
    for i in range(num_points * 2):
        r = outer_radius if i % 2 == 0 else inner_radius
        angle_rad = (angle * i - 90) * math.pi / 180
        x = center_x + int(r * math.cos(angle_rad))
        y = center_y + int(r * math.sin(angle_rad))
        points.append((x, y))
    draw.polygon(points, fill=color)

for label_file in os.listdir(label_dir):
    if label_file.endswith(".txt"):
        label_path = os.path.join(label_dir, label_file)
        image_name = os.path.splitext(label_file)[0] + ".jpg"
        image_path = os.path.join(image_dir, image_name)
        output_path = os.path.join(output_dir, image_name)

        image = Image.open(image_path).convert("RGB")

        with open(label_path, "r") as file:
            lines = file.readlines()

        transform = transforms.ToTensor()
        image_tensor = transform(image).unsqueeze(0).to(device)

        image_draw = ImageDraw.Draw(image)

        for line in lines:
            components = line.split()
            center_x = float(components[1]) * image.width
            center_y = float(components[2]) * image.height

            draw_star(image_draw, center_x, center_y, diameter=10, color=(102, 51, 0))

        image.save(output_path)
        print(f"Annotated image saved: {output_path}")

print("Annotation process completed.")
