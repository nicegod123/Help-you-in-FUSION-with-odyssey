import tkinter as tk

# Notepad++ line numbers
guides = {
    "armor pumpkin": (7, 36),
    "gatling pea turret": (40, 55),
    "giant chomper": (59, 61),
    "obsidian tall-nut": (64, 84),
    "oblivion-shroom": (88, 114),
    "doominator-shroom": (118, 144),
    "vortex melon": (149, 176),
    "laser pumpkin": (179, 207),
    "blast pumpkin": (214, 216)
}

with open("the guide.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()


def search():
    gt = srch_br.get().lower().strip()

    if gt not in guides:
        error_window = tk.Toplevel(window)
        error_window.title("Not Found")

        tk.Label(
            error_window,
            text="Plant not found!",
            font=("8bitoperator JVE", 12)
        ).pack(padx=20, pady=20)

        return

    srt, end = guides[gt]

    # Convert Notepad++ lines to Python indexes
    srt -= 1
    end -= 1

    guide_text = "".join(lines[srt:end + 1])

    guide_window = tk.Toplevel(window)
    guide_window.title(gt.title())
    guide_window.geometry("700x500")

    title_label = tk.Label(
        guide_window,
        text=gt.upper(),
        font=("8bitoperator JVE", 18)
    )
    title_label.pack(pady=10)

    text_box = tk.Text(
        guide_window,
        width=80,
        height=25,
        font=("8bitoperator JVE", 10),
        wrap="word"
    )
    text_box.pack(padx=10, pady=10, fill="both", expand=True)

    text_box.insert("1.0", guide_text)

    # Make guide read-only
    text_box.config(state="disabled")


# Main window
window = tk.Tk()
window.title("Fusion Guide")
window.geometry("600x400")

label = tk.Label(
    window,
    text="Fusion Guide",
    font=("8bitoperator JVE", 24)
)
label.pack(pady=20)

instruction = tk.Label(
    window,
    text="Enter a fusion name:",
    font=("8bitoperator JVE", 12)
)
instruction.pack()

srch_br = tk.Entry(
    window,
    width=30,
    font=("8bitoperator JVE", 12)
)
srch_br.pack(pady=10)

btn1 = tk.Button(
    window,
    text="SEARCH",
    command=search,
    font=("8bitoperator JVE", 12)
)
btn1.pack(pady=10)

window.mainloop()