# 학습시키기  위해서 이미지 분류모델을 늘려 놓을 려고 ! gan 모델
import matplotlib.pyplot as plt
import numpy as np
import os
from tensorflow.keras.models import *
from tensorflow.keras.layers import *
from tensorflow.keras.datasets import mnist

number_GAN_models = []
for i in range(10):
    number_GAN_models.append(load_model('./models/generator_{}.h5'.format(i)))

my_number = 22414627
imgs = []
my_number = str(my_number)
for i in str(my_number):
    print(i)
    i = int(i)
    z = np.random.normal(0,1,(1,100))
    fake_img = number_GAN_models[i].predict(z)
    fake_img = fake_img * 0.5 +0.5
    imgs.append(fake_img.reshape(28,28))

_,axs = plt.subplots(1, len(my_number),figsize=(10,40),sharex=True,sharey=True)
for i in range(len(my_number)):
    axs[i].imshow(imgs[i], cmap='gray')
    axs[i].axis('off')
plt.show()

img = imgs[0]

for i in range(1, len(my_number)):
    img = np.append(img, imgs[i], axis=1)

plt.imshow(img)
plt.axis('off')
plt.show()