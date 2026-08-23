#                                                                       به نام خدا                                                                        
# **************************************************************************************************************************************************
#                                                              محاسبه گرادیان و به‌روزرسانی وزن         
# **************************************************************************************************************************************************
import arabic_reshaper
#-------------------------------------------------------
# install: pip install python-bidi
from bidi.algorithm import get_display
#-------------------------------------------------------
import numpy as np

# داده‌ها
X = np.array([[1.0], [2.0]])
y = np.array([[3.0], [5.0]])

# وزن‌های اولیه اشتباه
w = 0.0
b = 0.0
 
# نرخ یادگیری
learning_rate = 0.1

# تعداد قدم‌ها
epochs = 20

print(get_display(arabic_reshaper.reshape("شروع آموزش...\n")))

for i in range(epochs):
    # ۱. پیش‌ بینی
    y_pred = w * X + b
    
    # ۲. محاسبه خطا
    error = y_pred - y
    
    # ۳. محاسبه گرادیان
    dw = np.mean(2 * error * X)   # گرادیان نسبت به w
    db = np.mean(2 * error)       # گرادیان نسبت به b
    
    # ۴. به‌روزرسانی وزن‌ها
    w = w - learning_rate * dw
    b = b - learning_rate * db
    
    # ۵. محاسبه MSE برای نمایش
    mse = np.mean(error ** 2)
    
    if i % 5 == 0 or i == epochs-1:
        print(f"ŋ {i:2d} | w = {w:.4f} | b = {b:.4f} | MSE = {mse:.4f}")

print(get_display(arabic_reshaper.reshape("\n نتیجه نهایی:")))
print(f"w ≈ {w:.4f}")
print(f"b ≈ {b:.4f}")