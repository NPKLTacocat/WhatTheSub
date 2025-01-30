import tkinter as tk
from PIL import ImageTk, Image
import threading


class TranslationApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("WhatTheSub")

        self.text_display = tk.Text(self.root, wrap=tk.WORD, height=10)
        self.text_display.pack(padx=10, pady=10)

        self.running = False
        self.start_button = tk.Button(
            self.root, text="Start", command=self.toggle_capture
        )
        self.start_button.pack()

    def toggle_capture(self):
        """Start/Stop the capture process"""
        self.running = not self.running
        self.start_button.config(text="Stop" if self.running else "Start")
        if self.running:
            thread = threading.Thread(target=self.run_capture_loop)
            thread.daemon = True
            thread.start()

    def run_capture_loop(self):
        """Main processing loop (connect with other modules)"""
        # You'll need to connect this with your capture, OCR, and translation classes
        while self.running:
            # Add your processing logic here
            self.update_text("Sample translated text\n")

    def update_text(self, new_text):
        """Update the display text"""
        self.text_display.delete(1.0, tk.END)
        self.text_display.insert(tk.END, new_text)
        self.text_display.see(tk.END)

    def run(self):
        self.root.mainloop()
