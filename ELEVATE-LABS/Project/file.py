import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import stepic

# Dark theme colors
DARK_BG = "#2e2e2e"
DARK_FG = "#ffffff"
BTN_BG = "#444"
BTN_FG = "#fff"

def open_hide_window():
    root.iconify()
    win = tk.Toplevel(root)
    win.title("Hide Data in Image")
    win.attributes('-fullscreen', True)
    win.configure(bg=DARK_BG)

    def close_and_return():
        win.destroy()
        root.deiconify()

    def load_image():
        file = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.bmp")])
        if file:
            img = Image.open(file)
            img.thumbnail((300, 300))
            imgTk = ImageTk.PhotoImage(img)
            image_label.config(image=imgTk)
            image_label.image = imgTk
            image_label.path = file

    def hide_text():
        if not hasattr(image_label, 'path'):
            messagebox.showwarning("Warning", "Please select an image.")
            return
        message = message_entry.get("1.0", tk.END).strip()
        if not message:
            messagebox.showwarning("Warning", "Please enter a message.")
            return
        try:
            img = Image.open(image_label.path).convert('RGB')
            encoded_img = stepic.encode(img, message.encode())
            save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png")])
            if save_path:
                encoded_img.save(save_path)
                messagebox.showinfo("Success", "Message hidden successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to hide message: {e}")

    ttk.Label(win, text="Select Image:", background=DARK_BG, foreground=DARK_FG).pack(pady=5)
    image_label = ttk.Label(win, background=DARK_BG)
    image_label.pack()

    ttk.Button(win, text="Browse Image", command=load_image).pack(pady=5)

    ttk.Label(win, text="Enter Message to Hide:", background=DARK_BG, foreground=DARK_FG).pack(pady=5)
    message_entry = tk.Text(win, height=5, width=60, bg="#1e1e1e", fg=DARK_FG)
    message_entry.pack()

    ttk.Button(win, text="Hide Message", command=hide_text).pack(pady=10)
    ttk.Button(win, text="Close & Return to Menu", command=close_and_return).pack(pady=20)

def open_extract_window():
    root.iconify()
    win = tk.Toplevel(root)
    win.title("Extract Data from Image")
    win.attributes('-fullscreen', True)
    win.configure(bg=DARK_BG)

    def close_and_return():
        win.destroy()
        root.deiconify()

    def load_and_extract():
        file = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.bmp")])
        if file:
            try:
                img = Image.open(file)
                hidden_data = stepic.decode(img)
                extracted_message.delete("1.0", tk.END)
                extracted_message.insert(tk.END, hidden_data)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to extract message: {e}")

    ttk.Label(win, text="Extract Message from Image", background=DARK_BG, foreground=DARK_FG).pack(pady=10)
    ttk.Button(win, text="Select Stego Image", command=load_and_extract).pack(pady=5)

    extracted_message = tk.Text(win, height=10, width=60, bg="#1e1e1e", fg=DARK_FG)
    extracted_message.pack(pady=10)

    ttk.Button(win, text="Close & Return to Menu", command=close_and_return).pack(pady=20)

# Main Window
root = tk.Tk()
root.title("Steganography Tool")
root.attributes('-fullscreen', True)
root.configure(bg=DARK_BG)

def exit_fullscreen(event):
    root.attributes('-fullscreen', False)

root.bind("<Escape>", exit_fullscreen)

# Style
style = ttk.Style(root)
style.theme_use("clam")
style.configure("TButton", background=BTN_BG, foreground=BTN_FG, padding=6)
style.configure("TLabel", background=DARK_BG, foreground=DARK_FG)

# GUI Elements
ttk.Label(root, text="Steganography Tool", font=("Helvetica", 20), background=DARK_BG, foreground=DARK_FG).pack(pady=40)
ttk.Button(root, text="Hide Data in Image", command=open_hide_window).pack(pady=20)
ttk.Button(root, text="Extract Data from Image", command=open_extract_window).pack(pady=20)
ttk.Button(root, text="Close Application", command=root.destroy).pack(pady=20)  # <--- New Close Button


root.mainloop()
