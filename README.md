# Convert-photo-to-text

Convert-photo-to-text یک ابزار گرافیکی (GUI) است که به شما امکان می‌دهد تا متن‌ها را از تصاویر استخراج کرده و آنها را در Notepad یا Microsoft Word ذخیره کنید.

## ویژگی‌ها

- انتخاب تصویر و تبدیل آن به مقیاس خاکستری
- استخراج متن از تصویر با استفاده از Tesseract OCR
- ذخیره متن استخراج شده در Notepad
- ذخیره متن استخراج شده در Microsoft Word
- کپی کردن متن استخراج شده به کلیپ‌بورد

## پیش‌نیازها

قبل از اجرای این برنامه، اطمینان حاصل کنید که پیش‌نیازهای زیر را نصب کرده‌اید:

- Python 3.x
- Tesseract-OCR
- کتابخانه‌های Python مورد نیاز:
  - tkinter
  - pillow
  - pytesseract
  - pyautogui
  - pywin32

## نصب

1. نصب Tesseract-OCR:
   - Tesseract-OCR را از [اینجا](https://github.com/tesseract-ocr/tesseract) دانلود و نصب کنید.
   - مسیر نصب Tesseract را به `pytesseract.pytesseract.tesseract_cmd` در کد تنظیم کنید.

2. نصب کتابخانه‌های Python:
   ```bash
   pip install pillow pytesseract pyautogui pywin32
اجرا
برای اجرای برنامه، کد زیر را اجرا کنید:

bash
Copy code
python convert_photo_to_text.py
استفاده
بر روی دکمه "انتخاب عکس" کلیک کنید و تصویر مورد نظر خود را انتخاب کنید.
تصویر انتخاب شده به مقیاس خاکستری تبدیل شده و متن از آن استخراج می‌شود.
متن استخراج شده در قسمت متنی نمایش داده می‌شود.
می‌توانید متن را در Notepad یا Word ذخیره کنید و یا آن را به کلیپ‌بورد کپی کنید.
ساختار پروژه
bash
Copy code
convert_photo_to_text/
│
├── convert_photo_to_text.py   # فایل اصلی برنامه
├── README.md                 # فایل توضیحات پروژه
└── requirements.txt          # فایل پیش‌نیازهای پروژه
مشارکت
پذیرای مشارکت‌های شما هستیم! لطفاً برای مشارکت در پروژه، ابتدا یک فورک ایجاد کنید، سپس تغییرات خود را اعمال و یک پول ریکوئست ارسال کنید.
