from PIL import Image, ImageFilter
from PIL import ImageDraw



img = Image.open('Зебра_какая-то.jpg').convert("RGB")
width = img.size[0]
height = img.size[1]



class Filter:
    """
    Базовый класс для создания фильтров.
    """

    def apply_to_colour(self, pixel: int) -> int:
        """
        Применяет фильтр к одному пикселю.
        :param pixel: цвет пикселя
        :return: новый цвет пикселя
        """
        raise NotImplementedError()
    def apply_to_pixel(self, pixel):

        r = self.apply_to_colour(pixel[0])
        g = self.apply_to_colour(pixel[1])
        b = self.apply_to_colour(pixel[2])
        return r, g, b


    def apply_to_image(self, img: Image.Image) -> Image.Image:
        """
        Применяет фильтр к изображению.
        :param img: исходное изображение
        :return: новое изображение
        """
        for i in range(img.width):
            for j in range(img.height):
                # получаем цвет
                pixel = img.getpixel((i, j))

                # как-либо меняем цвет
                new_pixel = self.apply_to_pixel(pixel)

                # сохраняем пиксель обратно
                img.putpixel((i, j), new_pixel)
        return img


class BrightFilter(Filter):
    opisanie = (
    """
    Фильтр, который делает изображение ярче.
    """
    )
    def apply_to_colour(self, pixel: int) -> int:
        new_pixel = min(pixel + 100, 255, 255, 255)
        return new_pixel


class DarkFilter(Filter):
    opisanie = (
    """
    filter which make photo dark
    """
    )
    def apply_to_colour(self, pixel: int) -> int:
        new_pixel = max(pixel - 100, 0)
        return new_pixel

class InverseFilter(Filter):
    opisanie = (
    """
    filter which maake effect inverse
    """
    )
    def apply_to_colour(self, pixel: int) -> int:
        new_pixel = 255 - pixel
        return new_pixel


class BlurFilter(Filter):
    opisanie = (
    """

    filter which applies effect blur

    """
    )
    def apply_to_image(self, img: Image.Image) -> Image.Image:
        new_img = img.filter(ImageFilter.BLUR)
        return new_img
class EdgeEnhance(Filter):
    opisanie = (
    """

    filer which edge enhance

    """
    )
    def apply_to_image(self, img: Image.Image) -> Image.Image:
        new_img = img.filter(ImageFilter.EDGE_ENHANCE)
        return new_img

class SharpFilter(Filter):
    opisanie = (
    """

    filer which make photo sharp

    """
    )
    def apply_to_image(self, img: Image.Image) -> Image.Image:
        new_img = img.filter(ImageFilter.SHARPEN)
        return new_img

class EmbossFilter(Filter):
    opisanie = (
    """

    я не придумал описание для этого фильтра, но его стоит попробовать

    """
    )
    def apply_to_image(self, img: Image.Image) -> Image.Image:
        new_img = img.filter(ImageFilter.EMBOSS)
        return new_img