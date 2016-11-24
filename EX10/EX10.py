"""Drawing the fractal."""
from PIL import Image


class Fractal:
    """Fractal."""

    def __init__(self, size, scale, computation):
        """Constructor.

        Arguments:
        size -- the size of the image as a tuple (x, y)
        scale -- the scale of x and y as a list of 2-tuple
                 [(minimum_x, minimum_y), (maximum_x, maximum_y)]
        computation -- the function used for computing pixel values as a function
        """
        self.size = size
        self.scale = scale
        self.computation = computation
        self.img = Image.new("RGB", self.size, 0)
        self.pixel_dict = {}

    def compute(self):
        """Create the fractal by computing every pixel value."""
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                i = self.pixel_value((x, y))
                cur = i[(x, y)]
                self.img.putpixel((x, y), (cur % 4 * 64, cur % 8 * 32, cur % 16 * 16))
        print(self.pixel_dict)

    def pixel_value(self, pixel):
        """
        Return the number of iterations it took for the pixel to go out of bounds.

        Arguments:
        pixel -- the pixel coordinate (x, y)

        Returns:
        the number of iterations of computation it took to go out of bounds as integer.
        """
        self.pixel_dict[pixel] = self.computation(pixel)
        return self.pixel_dict

    def save_image(self, filename):
        """
        Save the image to hard drive.

        Arguments:
        filename -- the file name to save the file to as a string.
        """
        self.img.save(filename, 'PNG')

if __name__ == "__main__":
    def mandelbrot_computation(pixel):
        """Try."""
        return pixel[0] + pixel[1]
    mandelbrot = Fractal((1000, 1000), [(-2, -2), (2, 2)], mandelbrot_computation)
    mandelbrot.compute()
    #mandelbrot.save_image("mandelbrot.png")
