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

    def compute(self):
        """Create the fractal by computing every pixel value."""
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                i = self.pixel_value((x, y))
                self.img.putpixel((x, y), (i % 4 * 64, i % 8 * 32, i % 16 * 16))

        pass

    def pixel_value(self, pixel):
        """
        Return the number of iterations it took for the pixel to go out of bounds.

        Arguments:
        pixel -- the pixel coordinate (x, y)

        Returns:
        the number of iterations of computation it took to go out of bounds as integer.
        """
        """
        i = 0
        value = self.computation(pixel)
        while value < 2:
            i += 1
        else:
            return i"""
        open(str(self.computation(pixel)))

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
        yield 'sqa'
    mandelbrot = Fractal((1000, 1000), [(-2, -2), (2, 2)], mandelbrot_computation)
    mandelbrot.compute()
    mandelbrot.save_image("mandelbrot.png")
    mandelbrot2 = Fractal((1000, 1000), [(-0.74877, 0.065053), (-0.74872, 0.065103)], mandelbrot_computation)
    mandelbrot2.compute()
    mandelbrot2.save_image("mandelbrot2.png")
