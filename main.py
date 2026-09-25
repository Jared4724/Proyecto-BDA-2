import customtkinter as ctk
from database import conectar_db
from views import LoginViewMixin, MainViewMixin

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class AppBlog(ctk.CTk, LoginViewMixin, MainViewMixin):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Blog - Publicaciones, Categorías y Etiquetas")
        
        # Permitir redimensionar la ventana
        self.resizable(True, True)

        self.current_user_id = None
        self.current_user_name = ""
        self.current_user_role = "USER"

        self.dict_categories = {}
        self.dict_tags = {}
        self.cat_filter_dict = {"Todas las categorías": None}

        # Centrar la ventana al iniciar
        self.centrar_ventana(820, 900)

        self.pantalla_login()

    def centrar_ventana(self, ancho, alto):
        """Calcula la posición para centrar la ventana en la pantalla."""
        self.update_idletasks()
        pantalla_ancho = self.winfo_screenwidth()
        pantalla_alto = self.winfo_screenheight()

        pos_x = (pantalla_ancho // 2) - (ancho // 2)
        pos_y = (pantalla_alto // 2) - (alto // 2)

        if pos_y < 0:
            pos_y = 0

        self.geometry(f"{ancho}x{alto}+{pos_x}+{pos_y}")

    def conectar_db(self):
        return conectar_db()

    def limpiar_pantalla(self):
        for widget in self.winfo_children():
            widget.destroy()

    def cerrar_sesion(self):
        self.current_user_id = None
        self.current_user_name = ""
        self.current_user_role = "USER"
        self.pantalla_login()

if __name__ == "__main__":
    app = AppBlog()
    app.mainloop()