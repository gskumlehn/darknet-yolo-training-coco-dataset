import os

train_images_dir = "images/train2017"
val_images_dir = "images/val2017"

train_txt_path = "train.txt"
val_txt_path = "val.txt"

def create_txt_file(images_dir, txt_file_path):
    image_files = [f for f in os.listdir(images_dir) if f.endswith(('.jpg', '.png'))]
    with open(txt_file_path, "w") as txt_file:
        for image_file in image_files:
            full_path = os.path.abspath(os.path.join(images_dir, image_file))
            txt_file.write(full_path + "\n")

create_txt_file(train_images_dir, train_txt_path)
create_txt_file(val_images_dir, val_txt_path)
