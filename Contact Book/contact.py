import tkinter as tk
from tkinter import messagebox, ttk
import csv
import os

FILENAME = "contacts.csv"

def load_contacts():
    contacts = []
    if os.path.exists(FILENAME):
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            contacts = list(reader)
    return contacts

def save_contacts(contacts):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(contacts)

def add_contact():
    name, phone, email, address = entry_name.get(), entry_phone.get(), entry_email.get(), entry_address.get()

    if not name or not phone:
        messagebox.showerror("Error", "Name and Phone are required!")
        return

    contacts.append([name, phone, email, address])
    save_contacts(contacts)
    update_treeview()
    clear_entries()

def update_treeview():
    tree.delete(*tree.get_children())
    for contact in contacts:
        tree.insert("", tk.END, values=contact)

def search_contact():
    query = entry_search.get().lower()
    tree.delete(*tree.get_children())
    for contact in contacts:
        if query in contact[0].lower() or query in contact[1]:
            tree.insert("", tk.END, values=contact)

def delete_contact():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "No contact selected!")
        return

    for item in selected_item:
        contacts.pop(tree.index(item))
    
    save_contacts(contacts)
    update_treeview()

def update_contact():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "No contact selected!")
        return

    index = tree.index(selected_item[0])
    contacts[index] = [entry_name.get(), entry_phone.get(), entry_email.get(), entry_address.get()]
    save_contacts(contacts)
    update_treeview()
    clear_entries()

def populate_fields(event):
    selected_item = tree.selection()
    if selected_item:
        contact = contacts[tree.index(selected_item[0])]
        entry_name.delete(0, tk.END)
        entry_name.insert(0, contact[0])
        entry_phone.delete(0, tk.END)
        entry_phone.insert(0, contact[1])
        entry_email.delete(0, tk.END)
        entry_email.insert(0, contact[2])
        entry_address.delete(0, tk.END)
        entry_address.insert(0, contact[3])

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)

contacts = load_contacts()

root = tk.Tk()
root.title("Contact Book")
root.geometry("500x400")

style = ttk.Style()
style.configure("TButton", font=("Arial", 10))
style.configure("TLabel", font=("Arial", 10))

frame_form = tk.Frame(root, padx=10, pady=10)
frame_form.pack(fill="x")

ttk.Label(frame_form, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_name = ttk.Entry(frame_form)
entry_name.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame_form, text="Phone:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_phone = ttk.Entry(frame_form)
entry_phone.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame_form, text="Email:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
entry_email = ttk.Entry(frame_form)
entry_email.grid(row=2, column=1, padx=5, pady=5)

ttk.Label(frame_form, text="Address:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
entry_address = ttk.Entry(frame_form)
entry_address.grid(row=3, column=1, padx=5, pady=5)

frame_buttons = tk.Frame(root, padx=10, pady=10)
frame_buttons.pack(fill="x")

btn_add = ttk.Button(frame_buttons, text="Add Contact", command=add_contact)
btn_add.pack(side="left", padx=5, pady=5)

btn_update = ttk.Button(frame_buttons, text="Update Contact", command=update_contact)
btn_update.pack(side="left", padx=5, pady=5)

btn_delete = ttk.Button(frame_buttons, text="Delete Contact", command=delete_contact)
btn_delete.pack(side="left", padx=5, pady=5)

frame_search = tk.Frame(root, padx=10, pady=10)
frame_search.pack(fill="x")

ttk.Label(frame_search, text="Search:").pack(side="left", padx=5)
entry_search = ttk.Entry(frame_search)
entry_search.pack(side="left", padx=5)
btn_search = ttk.Button(frame_search, text="Search", command=search_contact)
btn_search.pack(side="left", padx=5)

frame_table = tk.Frame(root, padx=10, pady=10)
frame_table.pack(fill="both", expand=True)

columns = ("Name", "Phone", "Email", "Address")
tree = ttk.Treeview(frame_table, columns=columns, show="headings")
tree.heading("Name", text="Name")
tree.heading("Phone", text="Phone")
tree.heading("Email", text="Email")
tree.heading("Address", text="Address")

tree.pack(fill="both", expand=True)
tree.bind("<<TreeviewSelect>>", populate_fields)

update_treeview()

root.mainloop()