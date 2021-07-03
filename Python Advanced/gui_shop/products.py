import json
import os

from canvas import tk
from helpers import clean_screen
from tkinter import Label, Button
from PIL import Image, ImageTk

base_folder = os.path.dirname(__file__)


def render_products():
    clean_screen()
    with open("db/products.txt", "r") as file:
        products = file.readlines()
        col = 0
        for product in products:
            current_product = json.loads(product)
            Label(text=current_product.get('name')).grid(row=0, column=col)
            image = Image.open(os.path.join(os.path.join(base_folder, 'images'), current_product.get('img_path')))
            image = image.resize((100, 100))
            photo = ImageTk.PhotoImage(image)
            img_label = Label(image=photo)
            img_label.image = photo
            img_label.grid(row=1, column=col)
            Button(tk, text=f"Buy {current_product.get('id')}").grid(row=2, column=col)
            col += 1
