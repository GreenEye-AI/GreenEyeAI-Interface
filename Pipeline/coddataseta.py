код подготовки датасета

import os

train_img_dir = "dataset/train/images"
train_lbl_dir = "dataset/train/labels"
val_img_dir = "dataset/val/images"
val_lbl_dir = "dataset/val/labels"

def count_and_check(img_dir, lbl_dir):
    imgs = sorted([f for f in os.listdir(img_dir) if f.lower().endswith(('.jpg','.jpeg','.png'))])
    lbls = sorted([f for f in os.listdir(lbl_dir) if f.lower().endswith('.txt')])

    print(f"{img_dir}: {len(imgs)} изображений")
    print(f"{lbl_dir}: {len(lbls)} файлов разметки")

    img_bases = {os.path.splitext(f)[0] for f in imgs}
    lbl_bases = {os.path.splitext(f)[0] for f in lbls}

    only_imgs = sorted(img_bases - lbl_bases)[:10]
    only_lbls = sorted(lbl_bases - img_bases)[:10]

    if only_imgs:
        print(" Изображения без разметки (примеры):", only_imgs)
    if only_lbls:
        print(" Файлы разметки без изображений (примеры):", only_lbls)
    if not only_imgs and not only_lbls:
        print(" Все изображения и файлы разметки соответствуют друг другу.\n")

print()
count_and_check(train_img_dir, train_lbl_dir)
count_and_check(val_img_dir, val_lbl_dir)
