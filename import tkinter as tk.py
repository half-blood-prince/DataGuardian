import tkinter as tk
import pandas as pd
import re
root = tk.Tk()
root.geometry("500x500")
root.title("Tkinterhub")
options_fm = tk.Frame(root)
count = 0
def filter(dic, file_path):
    print("Filtering")
    print(dic)
    print(file_path.get())
    df = pd.read_csv(file_path)
    column_list = []
    regex_list = []
    for i in dic:
        column_list.append(i)
                
        regex_list.append(dic[i])
    for i in range(len(column_list)):
        df = df[df[column_list[i]].str.contains(regex_list[i], na=False)]
    print(df)
    df.to_csv("filtered.csv", index=False)

# Switch Funtion
def switch(indicator_lb, page):

    for child in options_fm.winfo_children():
        if isinstance(child, tk.Label):
            child["bg"] = "SystemButtonFace"

    indicator_lb["bg"] = "#0097e8"

    for fm in main_fm.winfo_children():
        fm.destroy()
        root.update()
    page()


# Home Button
home_btn = tk.Button(
    options_fm,
    text="Home",
    font=("Arial", 13),
    bd=0,
    fg="#0097e8",
    activebackground="#0097e8",
    command=lambda: switch(indicator_lb=home_indicator_lb, page=home_page),
)
home_btn.place(x=0, y=0, width=125)

# Home Indicator
home_indicator_lb = tk.Label(options_fm, bg="#0097e8")
home_indicator_lb.place(x=22, y=30, width=80, height=2)

# Product Button
product_btn = tk.Button(
    options_fm,
    text="Products",
    font=("Arial", 13),
    bd=0,
    fg="#0097e8",
    activebackground="#0097e8",
    command=lambda: switch(indicator_lb=product_btn_indicator_lb, page=product_page),
)
product_btn.place(x=125, y=0, width=125)

# Product Indicator
product_btn_indicator_lb = tk.Label(options_fm)
product_btn_indicator_lb.place(x=147, y=30, width=80, height=2)

# Contact Button
contact_btn = tk.Button(
    options_fm,
    text="Contact",
    font=("Arial", 13),
    bd=0,
    fg="#0097e8",
    activebackground="#0097e8",
    command=lambda: switch(indicator_lb=contact_indicator_lb, page=contact_page),
)
contact_btn.place(x=250, y=0, width=125)

# Contact_Indicator
contact_indicator_lb = tk.Label(options_fm)
contact_indicator_lb.place(x=272, y=30, width=80, height=2)

# About Button
about_btn = tk.Button(
    options_fm,
    text="About",
    font=("Arial", 13),
    bd=0,
    fg="#0097e8",
    activebackground="#0097e8",
    command=lambda: switch(indicator_lb=about_indicator_lb, page=about_page),
)
about_btn.place(x=375, y=0, width=125)

# About Indicator
about_indicator_lb = tk.Label(options_fm)
about_indicator_lb.place(x=397, y=30, width=80, height=2)


options_fm.pack(pady=5)
options_fm.pack_propagate(False)
options_fm.configure(width=500, height=35)


# Home Page
def home_page():
    home_page_fm = tk.Frame(main_fm)

    # Page 1
    page_1 = tk.Frame(main_fm)
    # take entry from user for a file path and number of columns

    file_path = tk.StringVar()
    num_col = tk.IntVar()
    l1 = tk.Label(page_1, text="File Path: ", font=20, fg="blue")
    l1.grid(row=0, column=0, padx=3)
    e1 = tk.Entry(page_1, font=20, bg="lightyellow", textvariable=file_path)
    e1.grid(row=0, column=1, padx=10, pady=3)
    l2 = tk.Label(page_1, text="Number of Columns: ", font=20, fg="blue")
    l2.grid(row=1, column=0, padx=3)
    e2 = tk.Entry(page_1, font=20, bg="lightyellow", textvariable=num_col)
    e2.grid(row=1, column=1, padx=10, pady=3)

    page_1.pack(pady=100)

    # Page 2
    page_2 = tk.Frame(main_fm)
    dic = {}
    colName = tk.StringVar()
    regex = tk.StringVar()
    no_of_col = tk.IntVar()

    l = tk.Label(page_2, text="Entry: ", font=20, fg="blue")
    l.grid(row=0, column=0, padx=3)

    e1 = tk.Entry(page_2, font=20, bg="lightyellow", textvariable=colName)
    e1.grid(row=0, column=1, padx=10, pady=3)
    e2 = tk.Entry(page_2, font=20, bg="lightyellow", textvariable=regex)
    e2.grid(row=0, column=2, padx=10, pady=3)

    b1 = tk.Button(
        page_2, text="Submit", bg="lightgreen", command=lambda: my_check(), font=18
    )

    # label to trach number of columns
    l4 = tk.Label(page_2, text="Number of Columns: ", font=20, fg="blue")
    l4.grid(row=1, column=0, padx=3)

    l3 = tk.Label(
        page_2,
        textvariable=no_of_col,
        font=20,
        fg="blue",
    )
    l3.grid(row=1, column=1, padx=3)

    def my_check():
        dic[colName.get()] = regex.get()
        e1.delete(0, "end")
        e2.delete(0, "end")
        print(dic)
        no_of_col.set(no_of_col.get() + 1)

    b1.grid(row=2, column=0, padx=3, pady=5)

    # Page 3
    page_3 = tk.Frame(main_fm)
    page_3_lb = tk.Label(page_3, text="Third Page", font=("Bold", 20))
    page_3_lb.pack()

    # Page 4
    page_4 = tk.Frame(main_fm)
    page_4_lb = tk.Label(page_4, text="Fifth Page", font=("Bold", 20))
    page_4_lb.pack()
    bottom_frame = tk.Frame(main_fm)
    pages = [page_1, page_2, page_3, page_4]

    def move_next_page():
        global count
        if not count > len(pages) - 2:
            for p in pages:
                p.pack_forget()
            count += 1
            page = pages[count]
            page.pack(pady=100)

    def move_back_page():
        global count
        if not count == 0:
            for p in pages:
                p.pack_forget()
            count -= 1
            page = pages[count]
            page.pack(pady=100)

    back_btn = tk.Button(
        bottom_frame,
        text="Back",
        font=("Bold", 12),
        bg="#1877f2",
        fg="white",
        width=8,
        command=move_back_page,
    )
    back_btn.pack(side=tk.LEFT, padx=10)
    next_btn = tk.Button(
        bottom_frame,
        text="Next",
        font=("Bold", 12),
        bg="#1877f2",
        fg="white",
        width=8,
        command=move_next_page,
    )
    next_btn.pack(side=tk.RIGHT, padx=10)
    bottom_frame.pack(side=tk.BOTTOM, pady=10)

    home_page_fm.pack(fill=tk.BOTH, expand=True)


# Product Page
def product_page():
    product_page_fm = tk.Frame(main_fm)
    product_page_lb = tk.Label(
        product_page_fm, text="Product Page", font=("Arial", 25), fg="#0097e8"
    )
    product_page_lb.pack(pady=80)
    product_page_fm.pack(fill=tk.BOTH, expand=True)


# Contact Page
def contact_page():
    contact_page_fm = tk.Frame(main_fm)
    contact_page_lb = tk.Label(
        contact_page_fm, text="Contact Page", font=("Arial", 25), fg="#0097e8"
    )
    contact_page_lb.pack(pady=80)
    contact_page_fm.pack(fill=tk.BOTH, expand=True)


# About Page
def about_page():
    about_page_fm = tk.Frame(main_fm)
    about_page_lb = tk.Label(
        about_page_fm, text="About Page", font=("Arial", 25), fg="#0097e8"
    )
    about_page_lb.pack(pady=80)
    about_page_fm.pack(fill=tk.BOTH, expand=True)


main_fm = tk.Frame(root)
main_fm.pack(fill=tk.BOTH, expand=True)

home_page()

root.mainloop()
