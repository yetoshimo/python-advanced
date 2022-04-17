import json
import tkinter as tk
from helpers import clear_screen


def render_main_screen(screen: tk.Tk):
    tk.Button(window, text="Login", background="green", foreground="white",
              command=lambda: render_login(screen, on_success=render_products)).grid(
        row=0, column=0)
    tk.Button(window, text="Register", background="yellow", foreground="black",
              command=lambda: render_register(screen, on_success=render_main_screen)).grid(
        row=0, column=1)


def render_register(screen: tk.Tk, on_success):
    clear_screen(screen)
    inputs = [
        ("username", tk.Entry(screen)),
        ("password", tk.Entry(screen, show="*")),
        ("first_name", tk.Entry(screen)),
        ("last_name", tk.Entry(screen))
    ]
    for index, (label, input_widget) in enumerate(inputs):
        input_widget.grid(row=index, column=0)

    def on_click():
        error = register(**{user_attribute: widget.get() for (user_attribute, widget) in inputs})
        if not error:
            clear_screen(screen)
            on_success(screen)
        else:
            tk.Label(screen, text=error, background="red", foreground="white").grid(row=5, column=0)

    tk.Button(screen, text="Submit", command=lambda: on_click()).grid(row=len(inputs), column=0)


def register(**user):
    with open("user_store.txt", "a") as file:
        file.write(json.dumps(user))
        # file.write(f"{user['username']} - {user['password']}\n")


def render_login(screen: tk.Tk, on_success):
    clear_screen(screen)
    username = tk.Entry()
    username.grid(row=0, column=0)
    password = tk.Entry(screen, show="*")
    password.grid(row=1, column=0)

    def on_click():
        if login(username.get(), password.get()):
            on_success(screen)
        else:
            tk.Label(text="Invalid username or password", foreground="red").grid(row=3, column=0)

    tk.Button(screen, text="Login", command=on_click).grid(row=2, column=0)


def login(username, password):
    with open("user_store.txt") as file:
        for row in file:
            user = json.loads(row)
            if user["username"] == username and user["password"] == password:
                with open("current_user", "w") as user_file:
                    user_file.write(json.dumps(user))
                return True
    return False


ROW_SIZE = 3


def render_products(screen: tk.Tk):
    clear_screen(screen)

    with open("products.txt") as file:
        current_row = current_column = 0

        for product_index, row in enumerate(file):
            product = json.loads(row)

            if product_index % ROW_SIZE == 0:
                current_row += 3
                current_column = 0

            tk.Label(screen, text=product["name"]).grid(row=current_row, column=current_column)
            tk.Label(screen, text="image").grid(row=current_row + 1, column=current_column)
            tk.Label(screen, text=product["count"]).grid(row=current_row + 2, column=current_column)
            tk.Button(screen, text=f"Buy {product['id']}").grid(row=current_row + 3, column=current_column)
            current_column += 1


if __name__ == "__main__":
    window = tk.Tk()
    window.title('My Application')
    window.geometry("600x600")

    render_main_screen(window)

    # tk.Button(window, text="Clear Screen", command=lambda: clear_screen(window)).grid(row=1, column=1)

    window.mainloop()
