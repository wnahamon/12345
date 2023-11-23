from PIL import Image
from filters import BrightFilter, DarkFilter, InverseFilter, BlurFilter, EdgeEnhance,  SharpFilter, EmbossFilter, MirrorFilter
import os



def main():

    filter_names = [
        "Add brightness",
        "Lower brightness",
        "Inversion",
        "blur",
        "edge enhance",
        "Sharp Filter",
        "emboss filter",
        "mirror filter"
    ]

    filters = [
        BrightFilter(),
        DarkFilter(),
        InverseFilter(),
        BlurFilter(),
        EdgeEnhance(),
        SharpFilter(),
        EmbossFilter(),
        MirrorFilter()
    ]

    print("welcome to console photoshop")
    is_finished = False
    while not is_finished:
        path = input("choice way to file: ")

        while not os.path.exists(path):
            path = input("file not found. input correct way to file: ")

        img = Image.open(path).convert("RGB") # черно-белый формат
        print("which filter would apply?")
        for i in range(len(filter_names)):
            print(f"{i+1}) {filter_names[i]}")
        print("0) Exit")

        choice = input("choice filter (input number): ")

        while True:
            if choice in ["0", "1", "2", "3", "4", "5", "6", "7", "8"]:
                break
            else:
                choice = input("choice from the suggested.")

        if choice == "0":
            is_finished = True
            break



        filter = filters[int(choice)-1]
        new_img = filter.apply_to_image(img)
        path = input("where save result: ")
        new_img.save(path)
        # img.save(path)                    для будущего чтобы не совершить ошибку

        answer = input("again? (yes/no): ".lower())
        while True:
            if answer in ['yes', "no"]:
                break
            else:
                answer = input("input yes or no ".lower())
        if answer == "no":
            is_finished = True


if __name__ == "__main__":
    main()