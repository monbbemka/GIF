import imageio.v3 as iio

paths = ['./assets/image2.png',
          './assets/image3.png', 
          './assets/image4.png',
          './assets/image5.png']

images = []

for path in paths:
    images.append(iio.imread(path))

iio.imwrite('chicken.gif', images, duration = 300, loop = 0)
