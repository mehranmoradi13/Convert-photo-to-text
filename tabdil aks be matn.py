import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
from PIL import Image, ImageTk
import pytesseract
import os
import time
import pyautogui
import win32com.client as win32

# تنظیم مسیر Tesseract (برای Windows)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class ImageTextExtractor:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Text Extractor")
        self.image_path = None

        self.setup_gui()

    def setup_gui(self):
        # فریم برای دکمه‌های ذخیره
        save_frame = tk.Frame(self.root)
        save_frame.pack(side=tk.TOP, pady=10)

        # دکمه برای ذخیره کردن متن در Notepad
        self.save_notepad_button = tk.Button(save_frame, text="ذخیره در Notepad", command=self.save_text_notepad, state=tk.DISABLED)
        self.save_notepad_button.pack(side=tk.LEFT, padx=10)

        # دکمه برای ذخیره کردن متن در Word
        self.save_word_button = tk.Button(save_frame, text="ذخیره در Word", command=self.save_text_word, state=tk.DISABLED)
        self.save_word_button.pack(side=tk.LEFT, padx=10)

        # دکمه برای انتخاب تصویر
        select_button = tk.Button(self.root, text="انتخاب عکس", command=self.select_image)
        select_button.pack()

        # Label برای نمایش تصویر
        self.img_label = tk.Label(self.root)
        self.img_label.pack(pady=10)

        # ScrolledText برای نمایش متن استخراج شده
        self.text_display = ScrolledText(self.root, wrap=tk.WORD, width=50, height=10, state=tk.DISABLED)
        self.text_display.pack(pady=10)

        # دکمه برای کپی کردن متن عکس
        self.copy_button = tk.Button(self.root, text="کپی کردن متن", command=self.copy_text, state=tk.DISABLED)
        self.copy_button.pack()

    def convert_to_gray_scale(self, image_path):
        try:
            img = Image.open(image_path)
            gray_img = img.convert('L')
            output_path = os.path.splitext(image_path)[0] + '_gray.png'
            gray_img.save(output_path)
            return output_path
        except Exception as e:
            messagebox.showerror("Error", f"Error converting image to gray scale: {e}")
            return None

    def extract_text_from_image(self, image_path):
        try:
            text = pytesseract.image_to_string(Image.open(image_path), lang='eng+fas', config='--psm 3 --oem 3')
            return text
        except Exception as e:
            messagebox.showerror("Error", f"Error extracting text from image: {e}")
            return ""

    def write_to_notepad_and_save(self, text):
        try:
            os.startfile("notepad.exe")
            time.sleep(2)
            pyautogui.write(text, interval=0.01)
            pyautogui.hotkey('ctrl', 's')
            time.sleep(1)
            file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                     filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
            if file_path:
                pyautogui.write(file_path)
                pyautogui.press('enter')
                messagebox.showinfo("File Saved", "Text saved successfully.")
            else:
                messagebox.showwarning("File Not Saved", "Text was not saved.")
        except Exception as e:
            messagebox.showerror("Error", f"Error writing to Notepad and saving: {e}")

    def save_text_word(self):
        text = self.text_display.get("1.0", tk.END).strip()
        if text:
            try:
                file_path = filedialog.asksaveasfilename(defaultextension=".docx",
                                                         filetypes=[("Word files", "*.docx"), ("All files", "*.*")])
                if file_path:
                    word = win32.Dispatch("Word.Application")
                    word.Visible = True
                    doc = word.Documents.Add()
                    doc.Content.Text = text
                    doc.SaveAs(file_path)
                    doc.Close()
                    word.Quit()
                    messagebox.showinfo("File Saved", "Text saved successfully.")
                else:
                    messagebox.showwarning("File Not Saved", "Text was not saved.")
            except Exception as e:
                messagebox.showerror("Error", f"Error saving text in Word: {e}")

    def copy_text(self):
        text = self.text_display.get("1.0", tk.END).strip()
        if text:
            self.root.clipboard_clear()
            self.root.clipboard_append(text)
            self.root.update()
            messagebox.showinfo("Copied", "Text copied to clipboard.")

    def select_image(self):
        messagebox.showinfo("تغییر زبان کیبورد",
                            "لطفاً زبان کیبورد سیستم خود را مطابق با زبان متن عکس مورد نظر تغییر دهید")

        self.image_path = filedialog.askopenfilename(initialdir="/", title="Select Image",
                                                     filetypes=(("All files", "*.*"), ("PNG files", "*.png"),))
        if self.image_path:
            gray_image_path = self.convert_to_gray_scale(self.image_path)
            if gray_image_path:
                self.load_image(gray_image_path)
                extracted_text = self.extract_text_from_image(gray_image_path)
                self.display_extracted_text(extracted_text)
            else:
                self.display_extracted_text("Error converting image to gray scale.")

    def load_image(self, image_path):
        img = Image.open(image_path)
        img.thumbnail((400, 400))
        img_tk = ImageTk.PhotoImage(img)
        self.img_label.config(image=img_tk)
        self.img_label.image = img_tk

    def display_extracted_text(self, text):
        self.text_display.config(state=tk.NORMAL)
        self.text_display.delete("1.0", tk.END)
        self.text_display.insert(tk.END, text)
        self.text_display.config(state=tk.DISABLED)

        if text:
            self.save_notepad_button.config(state=tk.NORMAL)
            self.save_word_button.config(state=tk.NORMAL)
            self.copy_button.config(state=tk.NORMAL)
        else:
            self.save_notepad_button.config(state=tk.DISABLED)
            self.save_word_button.config(state=tk.DISABLED)
            self.copy_button.config(state=tk.DISABLED)

    def save_text_notepad(self):
        text = self.text_display.get("1.0", tk.END).strip()
        if text:
            self.write_to_notepad_and_save(text)

# اجرای mainloop برای نمایش GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageTextExtractor(root)
    root.mainloop()
