import tkinter as tk
from tkinter import scrolledtext, messagebox
from transformers import pipeline


summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text():
    input_text = input_box.get("1.0", tk.END).strip()
    
    if not input_text:
        messagebox.showwarning("Input Required", "Please enter text to summarize.")
        return

    try:
        summary = summarizer(input_text, max_length=100, min_length=30, do_sample=False)
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, summary[0]['summary_text'])
    except Exception as e:
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, f"Error: {str(e)}")


window = tk.Tk()
window.title("Text Summarization Tool")
window.geometry("850x650")
window.configure(bg="#f9f9f9")


heading = tk.Label(window, text="Text Summarization Tool", font=("Arial", 20, "bold"), bg="#f9f9f9")
heading.pack(pady=15)


input_label = tk.Label(window, text="Enter the text to summarize:", font=("Arial", 12), bg="#f9f9f9")
input_label.pack()
input_box = scrolledtext.ScrolledText(window, width=100, height=12, wrap=tk.WORD, font=("Consolas", 11))
input_box.pack(padx=10, pady=10)


summarize_btn = tk.Button(window, text="Generate Summary", command=summarize_text,
                          font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", padx=10, pady=5)
summarize_btn.pack(pady=10)

output_label = tk.Label(window, text="Summarized Output:", font=("Arial", 12), bg="#f9f9f9")
output_label.pack()
output_box = scrolledtext.ScrolledText(window, width=100, height=8, wrap=tk.WORD, font=("Consolas", 11))
output_box.pack(padx=10, pady=10)

window.mainloop()


