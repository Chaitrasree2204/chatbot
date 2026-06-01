import tkinter as tk
from tkinter import messagebox

# AI Expert System Knowledge Base
def skincare_advice(skin_type, concern):

    recommendations = {

        "Dry Skin": {
            "Acne": "Use a gentle hydrating cleanser, ceramide moisturizer, and consult a dermatologist for acne treatment.",
            "Dark Spots": "Use Vitamin C serum and sunscreen SPF 50 daily.",
            "Sensitivity": "Use fragrance-free products and avoid harsh exfoliants."
        },

        "Oily Skin": {
            "Acne": "Use salicylic acid cleanser, niacinamide serum, and oil-free moisturizer.",
            "Dark Spots": "Use Vitamin C serum and sunscreen daily.",
            "Sensitivity": "Use lightweight gel-based skincare products."
        },

        "Normal Skin": {
            "Acne": "Use a mild cleanser and spot treatment.",
            "Dark Spots": "Use Vitamin C serum and sunscreen.",
            "Sensitivity": "Use soothing skincare products with aloe vera."
        },

        "Acne Prone Skin": {
            "Acne": "Use salicylic acid cleanser, benzoyl peroxide treatment, and non-comedogenic moisturizer.",
            "Dark Spots": "Use niacinamide and Vitamin C serum.",
            "Sensitivity": "Use dermatologist-tested acne-safe products."
        }
    }

    return recommendations[skin_type][concern]


def generate_response():

    name = entry_name.get()

    skin_type = skin_var.get()

    concern = concern_var.get()

    if name == "":
        messagebox.showwarning(
            "Input Error",
            "Please enter your name."
        )
        return

    advice = skincare_advice(
        skin_type,
        concern
    )

    result_text.config(
        text=f"""
Hello {name}!

Skin Type: {skin_type}

Concern: {concern}

AI Recommendation:

{advice}
"""
    )


# GUI Window
root = tk.Tk()
root.title("AI Skincare Chatbot")
root.geometry("700x550")

title = tk.Label(
    root,
    text="TIRA AI Skincare Chatbot",
    font=("Arial", 18, "bold")
)

title.pack(pady=10)

# Question 1
tk.Label(
    root,
    text="What is your name?",
    font=("Arial", 12)
).pack()

entry_name = tk.Entry(root, width=40)
entry_name.pack(pady=5)

# Question 2
tk.Label(
    root,
    text="Select Your Skin Type",
    font=("Arial", 12)
).pack()

skin_var = tk.StringVar()
skin_var.set("Normal Skin")

skin_menu = tk.OptionMenu(
    root,
    skin_var,
    "Dry Skin",
    "Oily Skin",
    "Normal Skin",
    "Acne Prone Skin"
)

skin_menu.pack(pady=5)

# Question 3
tk.Label(
    root,
    text="Select Your Main Skin Concern",
    font=("Arial", 12)
).pack()

concern_var = tk.StringVar()
concern_var.set("Acne")

concern_menu = tk.OptionMenu(
    root,
    concern_var,
    "Acne",
    "Dark Spots",
    "Sensitivity"
)

concern_menu.pack(pady=5)

# Button
submit_btn = tk.Button(
    root,
    text="Get AI Recommendation",
    command=generate_response,
    bg="pink",
    font=("Arial", 12)
)

submit_btn.pack(pady=20)

# Output Area
result_text = tk.Label(
    root,
    text="",
    justify="left",
    font=("Arial", 12),
    wraplength=600
)

result_text.pack(pady=20)

root.mainloop()
