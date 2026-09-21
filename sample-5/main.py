#                                                                  به نام خدا
# *************************************************************************************************************************************************
#                                                     می‌خواهیم یک نورون ساده را با پایتون پیاده‌سازی کنیم
# *************************************************************************************************************************************************
import numpy as np
import arabic_reshaper
#-------------------------------------------------------
# install: pip install python-bidi
from bidi.algorithm import get_display
#-------------------------------------------------------

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def tanh(z):
    return np.tanh(z)

def relu(z):
    return np.maximum(0, z)

# چند مقدار مختلف برای تست
z_values = np.array([-2.0, -1.0, 0.0, 1.0, 2.0])

print("z =", z_values)
print("Sigmoid =", sigmoid(z_values))
print("Tanh    =", tanh(z_values))
print("ReLU    =", relu(z_values))