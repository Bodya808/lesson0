import numpy as np

arr = np.array([1, 2, 3, 4])

print("Сумма элементов массива:", arr.sum())

print("Произведение элементов массива:", arr.prod())

print("Максимальное значение в массиве:", arr.max())

print("Минимальное значение в массиве:", arr.min())

print("Среднее значение элементов массива:", arr.mean())

import requests

url = 'https://genius.com/artists/Shorty-thug'
response = requests.get(url)
html_content = response.text

print(html_content)

import matplotlib.pyplot as plt

x = range(10)
y = [i ** 2 for i in x]

plt.plot(x, y)
plt.show()
