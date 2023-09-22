import time
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk
from tkinter import ttk
import pymongo
from tkinter import messagebox
from bson import ObjectId
from bson.objectid import ObjectId
import re
from tkinter import Scrollbar
from tkinter.scrolledtext import ScrolledText

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["ZARA"]
mycol = mydb["zara_data"]

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\rosar\Desktop\BD2\pymongo\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.geometry("1080x700+200+50")
window.configure(bg="#FFFFFF")

# Creazione della scritta ZARA in alto
canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=700,
    width=1080,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    640.0,
    360.0,
    image=image_image_1
)

canvas.create_text(
    400.0,
    29.0,
    anchor="nw",
    text="ZARA",
    fill="#FFFFFF",
    font=("Italiana Regular", 128 * -1)
)

canvas.create_rectangle(
    -2.998241424560547,
    165.5,
    1280.005298614502,
    168.5,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    -2.998241424560547,
    35.5,
    1280.005298614502,
    38.5,
    fill="#FFFFFF",
    outline="")

# Creazione della scritta id e della cella in basso
canvas.create_text(
    33.0,
    195.0,
    anchor="nw",
    text="Id",
    fill="#FFFFFF",
    font=("Italiana Regular", 20 * -1)
)

cid = tk.StringVar()
custid = tk.Entry(window, textvariable=cid)
custid.place(x=33.0, y=221.0, width=219.0, height=18.0)
custid.configure(state=tk.DISABLED)

# Creazione della scritta url e della cella in basso
canvas.create_text(
    290.0,
    195.0,
    anchor="nw",
    text="Url",
    fill="#FFFFFF",
    font=("Italiana Regular", 20 * -1)
)

url = tk.StringVar()
curl = tk.Entry(window, textvariable=url)
curl.place(x=290.0, y=221.0, width=219.0, height=18.0)

# Creazione della scritta language e della cella in basso
canvas.create_text(
    547.0,
    195.0,
    anchor="nw",
    text="Language",
    fill="#FFFFFF",
    font=("Italiana Regular", 20 * -1)
)
size_options = ["en-US"]

language = tk.StringVar()
clanguage = ttk.Combobox(window, textvariable=language, values=size_options)
clanguage.place(x=547.0, y=221.0, width=219.0, height=18.0)

# Creazione della scritta name e della cella in basso
canvas.create_text(
    804.0,
    195.0,
    anchor="nw",
    text="Name",
    fill="#FFFFFF",
    font=("Italiana Regular", 20 * -1)
)
size_options = ['Dress', 'Pants', 'Shirt', 'Top', 'T-shirt', 'Jacket', 'Jeans', 'Bag', 'Sweater', 'Sweatshirt','Shorts',
                'Sneakers', 'Leggings', 'Sandals', 'Blazer', 'Shoes', 'Scarf', 'Wallet']

name = tk.StringVar()
cname = ttk.Combobox(window, textvariable=name, values=size_options)
cname.place(x=804.0, y=221.0, width=219.0, height=18.0)

# Creazione della scritta sku e della cella in basso
canvas.create_text(
    33.0,
    260.0,
    anchor="nw",
    text="Sku",
    fill="#FFFFFF",
    font=("Italiana Regular", 20 * -1)
)

sku = tk.StringVar()
csku = tk.Entry(window, textvariable=sku)
csku.place(x=33.0, y=286.0, width=219.0, height=18.0)

# Creazione della scritta brand e della cella in basso
canvas.create_text(
    290.0,
    260.0,
    anchor="nw",
    text="Brand",
    fill="#FFFFFF",
    font=("Italiana Regular", 20 * -1)
)
size_options = ["ZARA", "ZARAHOME"]

brand = tk.StringVar()
cbrand = ttk.Combobox(window, textvariable=brand, values=size_options)
cbrand.place(x=290.0, y=286.0, width=219.0, height=18.0)

# Creazione della scritta description e della cella in basso
canvas.create_text(
    547.0,
    260.0,
    anchor="nw",
    text="Description",
    fill="#FFFFFF",
    font=("Italiana Regular", 20 * -1)
)

description = tk.StringVar()
cdescription = tk.Entry(window, textvariable=description)
cdescription.place(x=547.0, y=286.0, width=219.0, height=18.0)

# Creazione della scritta price e della cella in basso
canvas.create_text(
    804.0,
    260.0,
    anchor="nw",
    text="Price",
    fill="#FFFFFF",
    font=("Italiana Regular", 20 * -1)
)

price = tk.StringVar()
cprice = tk.Entry(window, textvariable=price)
cprice.place(x=804.0, y=286.0, width=219.0, height=18.0)

# Creazione della scritta availability e della cella in basso
canvas.create_text(
    33.0,
    325.0,
    anchor="nw",
    text="Availability",
    fill="#FFFFFF",
    font=("Italiana Regular", 20 * -1)
)
size_options = ["InStock", "Notstock"]

availability = tk.StringVar()
cavailability = ttk.Combobox(window, textvariable=availability, values=size_options)
cavailability.place(x=33.0, y=351.0, width=219.0, height=18.0)

# Creazione della scritta color e della cella in basso
canvas.create_text(
    290.0,
    325.0,
    anchor="nw",
    text="Color",
    fill="#FFFFFF",
    font=("Italiana Regular", 20 * -1)
)
size_options = ["Taupe brown", "Multi-color", "Raspberry", "Gray", "Multicolored", "Anthracite grey",
                "Blue", "Peach", "Brown-Blue", "Black", "Mustard", "Black", "Ecru", "Light blue", "Sand",
                "Pink", "Fuchsia", "White", "Sea green", "Green", "Gold", "Brown", "Vanilla", "Mauve",
                "Oyster White", "Blue / Gray", "White", "Light camel", "Khaki", "Mint Green", "Anthracite grey",
                "Gray", "Black / White", "Light blue", "Multicolored", "Stone", "Dark yellow", "Navy blue",
                "Silver", "Steel", "Natural", "Oyster White", "Natural", "Brick", "Mid-pink"]

color = tk.StringVar()
ccolor = ttk.Combobox(window, textvariable=color, values=size_options)
ccolor.place(x=290.0, y=351.0, width=219.0, height=18.0)

# Creazione della scritta size_list e della cella in basso
canvas.create_text(
    547.0,
    325.0,
    anchor="nw",
    text="Size_list",
    fill="#FFFFFF",
    font=("Italiana Regular", 20 * -1)
)

# Opzioni per il menu a tendina delle taglie
size_options = ['Unavailable', "XXS", "XS", "S", "M", "L", "XL", "XXL"]

# Creazione del menu a tendina
size_list = tk.StringVar()
csize_list = ttk.Combobox(window, textvariable=size_list, values=size_options)
csize_list.place(x=547.0, y=351.0, width=219.0, height=18.0)

# Creazione della scritta scraped_at e della cella in basso
canvas.create_text(
    804.0,
    325.0,
    anchor="nw",
    text="Scraped_at",
    fill="#FFFFFF",
    font=("Italiana Regular", 20 * -1)
)

scraped_at = tk.StringVar()
cscraped_at = tk.Entry(window, textvariable=scraped_at)
cscraped_at.place(x=804.0, y=351.0, width=219.0, height=18.0)

# Creazione della griglia
tree = ttk.Treeview(window)

tree["columns"] = (
    "_id", "url", "language", "name", "sku", "brand", "description", "price",
    "availability", "color", "size_list", "scraped_at"
)

tree.heading("#0", text="Index")
tree.column("#0", width=50, anchor="center")

# Imposta gli header delle colonne
for column in tree["columns"]:
    tree.heading(column, text=column)
    tree.column(column, width=100, anchor="center")

tree.place(x=33.0, y=500.0, width=1000, height=154)

# Funzione per popolare la tabella
search_results = []
global_results = []

#Funzione che resetta i nomi delle colonne nella tabella principale
def reset_column_headers():
    for i, column in enumerate(tree["columns"]):
        tree.heading(column, text=tree["columns"][i])
        tree.column(column, width=100, anchor="center")

#Funzione che popola la tabella principale
def populate_table():
    tree.delete(*tree.get_children())
    reset_column_headers()
    data_source = search_results if search_results else mycol.find({})
    for i, text_fromDB in enumerate(data_source, start=1):
        row_data = [
            str(text_fromDB['_id']),
            str(text_fromDB['url']),
            str(text_fromDB['language']),
            str(text_fromDB['name']),
            str(text_fromDB['sku']),
            str(text_fromDB['brand']),
            str(text_fromDB['description']),
            str(text_fromDB['price']),
            str(text_fromDB['availability']),
            str(text_fromDB['color']),
            str(text_fromDB['size_list']),
            str(text_fromDB['scraped_at'])
        ]
        tree.insert(parent="", index="end", iid=i, text=i, values=row_data)

#Creazione dei due oggetti Scrollbar, uno per la scrollbar orizzontale e uno per la scrollbar verticale:
scrollbar_x = Scrollbar(window, orient="horizontal", command=tree.xview)
scrollbar_y = Scrollbar(window, orient="vertical", command=tree.yview)

#Configurazione della scrollbar orizzontale per interagire con la griglia:
tree.configure(xscrollcommand=scrollbar_x.set)

#Posizionamento delle scrollbar nel layout:
scrollbar_x.place(x=33.0, y=654.0, width=1000, height=20)
scrollbar_y.place(x=1013.0, y=500.0, width=20, height=154)

#Configurazione della scrollbar verticale per interagire con la griglia:
tree.configure(yscrollcommand=scrollbar_y.set)

# Funzione per gestire il click su una riga della tabella
def on_table_row_click(event):
    try:
        selected_item = tree.selection()[0]
        row_data = tree.item(selected_item)["values"]

        # Assegna i valori ai campi di input
        cid.set(row_data[0])
        curl.delete(0, tk.END)
        curl.insert(tk.END, row_data[1])
        clanguage.delete(0, tk.END)
        clanguage.insert(tk.END, row_data[2])
        cname.delete(0, tk.END)
        cname.insert(tk.END, row_data[3])
        csku.delete(0, tk.END)
        csku.insert(tk.END, row_data[4])
        cbrand.delete(0, tk.END)
        cbrand.insert(tk.END, row_data[5])
        cdescription.delete(0, tk.END)
        cdescription.insert(tk.END, row_data[6])
        cprice.delete(0, tk.END)
        cprice.insert(tk.END, row_data[7])
        cavailability.delete(0, tk.END)
        cavailability.insert(tk.END, row_data[8])
        ccolor.delete(0, tk.END)
        ccolor.insert(tk.END, row_data[9])
        csize_list.delete(0, tk.END)
        csize_list.insert(tk.END, row_data[10])
        cscraped_at.delete(0, tk.END)
        cscraped_at.insert(tk.END, row_data[11])
    except:
        pass

# Funzione on_table_row_click come evento del click sulla tabella
tree.bind('<ButtonRelease-1>', on_table_row_click)

# Funzione di inserimento
def insert():
    global search_results, global_results
    try:
        r = messagebox.askyesno("Insert?", "Desideri inserire un record?")
        if r:
            new_data = {
                "url": curl.get(),
                "language": clanguage.get(),
                "name": cname.get(),
                "sku": csku.get(),
                "brand": cbrand.get(),
                "description": cdescription.get(),
                "price": float(cprice.get()),
                "availability": cavailability.get(),
                "color": ccolor.get(),
                "size_list": csize_list.get(),
                "scraped_at": cscraped_at.get()
            }
            new_id = mycol.insert_one(new_data).inserted_id
            new_record = mycol.find_one({"_id": new_id})
            global_results.append(new_record)
            if search_results:
                search_results.append(new_record)
            populate_table()

    except ValueError:
        messagebox.showerror("Errore", f"non puoi inserire un articolo senza inserire il prezzo")

# Funzione di cancellazione
def delete():
    r = messagebox.askyesno("Delete?", "Desideri cancellare un record?")
    if r:
        myquery = {"_id": ObjectId(cid.get())}
        mycol.delete_one(myquery)

        for i, result in enumerate(search_results):
            if "_id" in result and result["_id"] == ObjectId(cid.get()):
                del search_results[i]
                break
        populate_table()

# Funzione di modifica
def update():
    r = messagebox.askyesno("Update?", "Desideri modificare un record?")
    if r:
        myquery = {"_id": ObjectId(custid.get())}
        newvalues = {
            "$set": {
                "url": curl.get(),
                "language": clanguage.get(),
                "name": cname.get(),
                "sku": csku.get(),
                "brand": cbrand.get(),
                "description": cdescription.get(),
                "price": float(cprice.get()),
                "availability": cavailability.get(),
                "color": ccolor.get(),
                "size_list": csize_list.get(),
                "scraped_at": cscraped_at.get()
            }
        }
        mycol.update_one(myquery, newvalues)
        for i, result in enumerate(search_results):
            if "_id" in result and result["_id"] == ObjectId(custid.get()):
                search_results[i] = mycol.find_one({"_id": ObjectId(custid.get())})
                break
        populate_table()

#Funzione di update per le combobox
def update_table_on_combobox_change(event):
    populate_table()

'''
Quando l'utente digita qualcosa nella combobox, scatta l'evento <KeyRelease>, che a sua volta chiama la funzione 
update_table_on_combobox_change, questo permette di aggiornare la tabella in tempo reale.
'''
cname.bind('<KeyRelease>', update_table_on_combobox_change)
clanguage.bind('<KeyRelease>', update_table_on_combobox_change)
cbrand.bind('<KeyRelease>', update_table_on_combobox_change)
cavailability.bind('<KeyRelease>', update_table_on_combobox_change)
ccolor.bind('<KeyRelease>', update_table_on_combobox_change)
csize_list.bind('<KeyRelease>', update_table_on_combobox_change)

#Funzione di ricerca
def find():
    global search_results
    r = messagebox.askyesno("Find?", "Desideri effettuare una ricerca?")
    if r:
        search_results.clear()
        query = {}
        url_term = curl.get().strip()
        if url_term:
            query["url"] = {"$regex": re.compile(r"\b" + re.escape(url_term) + r"\b", re.IGNORECASE)}
        language_term = clanguage.get().strip()
        if language_term:
            query["language"] = {"$regex": re.compile(r"\b" + re.escape(language_term) + r"\b", re.IGNORECASE)}
        name_term = cname.get().strip()
        if name_term:
            query["name"] = {"$regex": re.compile(r"\b" + re.escape(name_term) + r"\b", re.IGNORECASE)}
        sku_term = csku.get().strip()
        if sku_term:
            query["sku"] = {"$regex": re.compile(r"\b" + re.escape(sku_term) + r"\b", re.IGNORECASE)}
        brand_term = cbrand.get().strip()
        if brand_term:
            query["brand"] = {"$regex": re.compile(r"\b" + re.escape(brand_term) + r"\b", re.IGNORECASE)}
        description_term = cdescription.get().strip()
        if description_term:
            query["description"] = {"$regex": re.compile(r"\b" + re.escape(description_term) + r"\b", re.IGNORECASE)}
        price_input = cprice.get().strip()
        if price_input:
            query["price"] = {"$lt": float(price_input)}
        availability_term = cavailability.get().strip()
        if availability_term:
            query["availability"] = {"$regex": re.compile(r"\b" + re.escape(availability_term) + r"\b", re.IGNORECASE)}
        color_term = ccolor.get().strip()
        if color_term:
            query["color"] = {"$regex": re.compile(r"\b" + re.escape(color_term) + r"\b", re.IGNORECASE)}
        size_list_term = csize_list.get().strip()
        if size_list_term:
            query["size_list"] = {"$regex": re.compile(r"\b" + re.escape(size_list_term) + r"\b", re.IGNORECASE)}
        scraped_at_term = cscraped_at.get().strip()
        if scraped_at_term:
            query["scraped_at"] = {"$regex": re.compile(r"\b" + re.escape(scraped_at_term) + r"\b", re.IGNORECASE)}
        if not any(query.values()):  # Se tutti i valori della query sono vuoti, mostra l'intera tabella
            populate_table()
        else:
            cursor = mycol.find(query).sort("price", pymongo.ASCENDING)
            for document in cursor:
                search_results.append(document)
            if not search_results:
                messagebox.showinfo("Ricerca completata", "Mi dispiace, ma la tua ricerca non ha prodotto risultati.")
            populate_table()

#Funzione per query complesse
def find_complex():
    r = messagebox.askyesno("Stats?", "Desideri effettuare una query statistica?")
    if r:
        name_list_term = cname.get().strip()
        color_list_term = ccolor.get().strip()
        size_list_term = csize_list.get().strip()
        price_list_term = cprice.get().strip()
        brand_list_term = cbrand.get().strip()
        availability_list_term = cavailability.get().strip()

        query = {}

        if name_list_term:
            query["name"] = {"$regex": rf"\b{re.escape(name_list_term)}\b", "$options": "i"}
        if color_list_term:
            query["color"] = {"$regex": rf"\b{re.escape(color_list_term)}\b", "$options": "i"}
        if size_list_term:
            query["size_list"] = {"$regex": rf"\b{re.escape(size_list_term)}\b", "$options": "i"}
        if price_list_term:
            query["price"] = {"$lt": float(price_list_term)}
        if brand_list_term:
            query["brand"] = {"$regex": re.compile(r"\b" + re.escape(brand_list_term) + r"\b", re.IGNORECASE)}
        if availability_list_term:
            query["availability"] = {"$regex": re.compile(r"\b" + re.escape(availability_list_term) + r"\b", re.IGNORECASE)}

        aggregate_pipeline = [{"$match": query},{"$group": {"_id": None,"sum_occurrences": {"$sum": 1},
                                                            "avg_price": {"$avg": "$price"}}}]
        size_list_aggregate = list(mycol.aggregate(aggregate_pipeline))

        if not size_list_aggregate:
            messagebox.showinfo("Ricerca completata", "Mi dispiace, ma la tua ricerca non ha prodotto risultati.")
        else:
            tree.delete(*tree.get_children())
            tree.heading("#1", text="Name")
            tree.heading("#2", text="Color")
            tree.heading("#3", text="Size List")
            tree.heading("#4", text="Occurrences")
            tree.heading("#5", text="Average Price")
            for col_number in range(6, len(tree["columns"]) + 1):
                tree.heading("#{}".format(col_number), text="")
            for i, item in enumerate(size_list_aggregate, start=1):
                row_data = [
                    str(name_list_term) if name_list_term else "N/A",
                    str(color_list_term) if color_list_term else "N/A",
                    str(size_list_term) if size_list_term else "N/A",
                    str(item["sum_occurrences"]),
                    f"${round(item['avg_price'], 2)}" if "avg_price" in item else "N/A"
                ]
                tree.insert(parent="", index="end", iid=i, text=i, values=row_data)

#Funzione che ripulisce tutti i campi
def clear_fields():
    curl.delete(0, tk.END)
    clanguage.delete(0, tk.END)
    cname.delete(0, tk.END)
    csku.delete(0, tk.END)
    cbrand.delete(0, tk.END)
    cdescription.delete(0, tk.END)
    cprice.delete(0, tk.END)
    cavailability.delete(0, tk.END)
    ccolor.delete(0, tk.END)
    csize_list.delete(0, tk.END)
    cscraped_at.delete(0, tk.END)
    tree.selection_remove(tree.selection())

populate_table()

savebtn = tk.Button(text="Insert", command=insert, font=("Italiana Regular", 20 * -1), background="white",foreground="black")
savebtn.place(x=36, y=430.0, width=150.0, height=27.0)

savebtn = tk.Button(text="Delete", command=delete, font=("Italiana Regular", 20 * -1), background="white",foreground="black")
savebtn.place(x=203, y=430.0, width=150.0, height=27.0)

savebtn = tk.Button(text="Update", command=update, font=("Italiana Regular", 20 * -1), background="white",foreground="black")
savebtn.place(x=370, y=430.0, width=150.0, height=27.0)

savebtn = tk.Button(text="Find", command=find, font=("Italiana Regular", 20 * -1), background="white",foreground="black")
savebtn.place(x=537, y=430.0, width=150.0, height=27.0)

savebtn = tk.Button(text="Stats", command=find_complex, font=("Italiana Regular", 20 * -1), background="white",foreground="black")
savebtn.place(x=704, y=430.0, width=150.0, height=27.0)

clearbtn = tk.Button(text="Clear", command=clear_fields, font=("Italiana Regular", 20 * -1), background="white", foreground="black")
clearbtn.place(x=871, y=430.0, width=150.0, height=27.0)

window.resizable(False, False)
window.mainloop()