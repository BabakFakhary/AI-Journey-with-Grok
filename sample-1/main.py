#                                                                 به نام خدا                                                                        
import arabic_reshaper
#-------------------------------------------------------
# install: pip install python-bidi
from bidi.algorithm import get_display
#-------------------------------------------------------
import numpy as np

# داده‌ها را دوباره تعریف می‌کنیم (برای اطمینان از شکل درست)
X = np.array([[1.0], [2.0]])   # شکل (2, 1)      ورودی (متراژ خانه)
y = np.array([[3.0], [5.0]])   # شکل (2, 1)  ← مهم: هر دو ستونی باشند خروجی واقعی (قیمت خانه)

print(" X:", X.shape)
print(" y:", y.shape)

# وزن و بایاس
w = 2.0
b = 1.0

# پیش‌بینی
y_pred = w * X + b
print(get_display(arabic_reshaper.reshape("\nپیش‌بینی:")))
print(y_pred)

# خطا
error = y_pred - y
print(get_display(arabic_reshaper.reshape("\nخطا:")))
print(error)

# میانگین مربعات خطا
mse = np.mean(error ** 2)
print("\nMSE =", mse)