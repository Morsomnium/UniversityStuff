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
        self.img_list = []

    def compute(self):
        """Create the fractal by computing every pixel value."""
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                print("Computing", x, ":", y, "...")
                i = self.pixel_value((x, y))
                r = i % 4 * 64
                g = i % 8 * 32
                b = i % 16 * 16
                self.img.putpixel((x, y), b * 65536 + g * 256 + r)

    def pixel_value(self, pixel):
        """
        Return the number of iterations it took for the pixel to go out of bounds.

        Arguments:
        pixel -- the pixel coordinate (x, y)

        Returns:
        the number of iterations of computation it took to go out of bounds as integer.
        """
        if __name__ == "__main__":
            xa = self.scale[0][0]
            ya = self.scale[0][1]
            xb = self.scale[1][0]
            yb = self.scale[1][1]
            imgx = self.size[0]
            imgy = self.size[1]
            maxit = 20
            zx = pixel[0] * (xb - xa) / (imgx - 1) + xa
            zy = pixel[1] * (yb - ya) / (imgy - 1) + ya
            return self.computation((zx, zy, maxit))
        else:
            return self.computation(pixel)

    def save_image(self, filename):
        """
        Save the image to hard drive.

        Arguments:
        filename -- the file name to save the file to as a string.
        """
        self.img.save(filename)

    def gif_create(self, frames):
        img_list = []
        xa = self.scale[0][0]
        ya = self.scale[0][1]
        xb = self.scale[1][0]
        yb = self.scale[1][1]
        b = 1
        for i in range(1, frames+1):
            temp_img = Fractal((256, 256), [(xa, ya), (xb, yb)], mandelbrot_computation)
            temp_img.compute()
            img_list.append(temp_img)
            temp_img.save_image("mandelbrot" + str(i) + ".png")
            xa *= 0.9
            xb *= 0.9
            ya *= 0.9
            yb *= 0.9
        print(img_list)
        self.img_list = img_list

    def gif_save(self, filename):
        print(self.img_list)
        self.img.save(filename, save_all=True, append_images=[self.img_list])

    def image_show(self):
        """Show."""
        self.img.show()

if __name__ == "__main__":
    def mandelbrot_computation(pixel):
        """Try."""
        z = complex(0, 0)
        c = complex(pixel[0], pixel[1])
        for i in range(pixel[2]):
            if z.real ** 2 + z.imag ** 2 >= 4:
                break
            z = z * z + c
        return i
    mandelbrot = Fractal((256, 256), [(-2, -2), (2.8, 2)], mandelbrot_computation)
    mandelbrot.compute()
    #mandelbrot.image_show()
    mandelbrot.gif_create(3)
    mandelbrot.gif_save("mandelbrot.gif")
