import requests
from datetime import datetime
import tkinter as tk
import webbrowser

TOKEN = "aabbccddee"
USERNAME = "tobias0ne"
GRAPH_ID = "graph01"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
BG_COLOR = "SpringGreen2"
today = datetime.now()
quantity = 1

headers = {
    "X-USER-TOKEN": TOKEN
}

# CREATE PIXELA'S USER
# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

# CREATE GRAPH
# graph_params = {
#     "id": GRAPH_ID,
#     "name": "My programming graph",
#     "unit": "commit",
#     "type": "int",
#     "color": "shibafu",
# }

# response = requests.post(url=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs", json=graph_params,headers=headers)
# print(response.text)

# CREATE PIXEL
def create_pixel():
    create_pixel_params = {
        "date": today.strftime("%Y%m%d"),
        "quantity": str(quantity)
    }

    response = requests.post(url=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}", json=create_pixel_params,headers=headers)
    print(response.text)

# UPDATE PIXEL
def update_pixel():
    global quantity
    quantity += 1
    update_pixel_params = {
        "quantity": str(quantity)
    }

    response = requests.put(url=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}", json=update_pixel_params, headers=headers)
    print(response.text)

# DELETE TODAY PIXEL
def delete_pixel():
    response = requests.delete(url=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}", headers=headers)
    print(response.text)

def view_website():
    webbrowser.open_new("https://pixe.la/v1/users/tobias0ne/graphs/graph01.html")

#UI SETUP
window = tk.Tk()
window.title("Commit Manager")
window.config(bg=BG_COLOR, padx=20, pady=20)

create_pixel_button = tk.Button(text="Add today's commit", highlightthickness=0, width=30,command=create_pixel)
create_pixel_button.grid(column=1, row=0)

update_pixel_button = tk.Button(text="Update today's commits", highlightthickness=0, width=30, command=update_pixel)
update_pixel_button.grid(column=1, row=1)

delete_pixel_button = tk.Button(text="Delete today's commits", highlightthickness=0, width=30, command=delete_pixel)
delete_pixel_button.grid(column=1, row=2)

view_website_button = tk.Button(text="View Pixela's Website", highlightthickness=0, width=30, command=view_website)
view_website_button.grid(column=1, row=3)

window.mainloop()