import customtkinter as ctk
from tkinter import messagebox
import oracledb

class LoginViewMixin:
    # -------------------------------------------------------------
    # PANTALLA: LOGIN
    # -------------------------------------------------------------
    def pantalla_login(self):
        self.limpiar_pantalla()

        frame = ctk.CTkFrame(self, width=380, height=350, corner_radius=15)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        title = ctk.CTkLabel(frame, text="Acceso al Blog", font=("Roboto", 22, "bold"))
        title.pack(pady=(35, 20))

        self.ent_email = ctk.CTkEntry(frame, placeholder_text="Correo electrónico", width=280)
        self.ent_email.pack(pady=10)

        self.ent_password = ctk.CTkEntry(frame, placeholder_text="Contraseña", show="*", width=280)
        self.ent_password.pack(pady=10)

        btn_ingresar = ctk.CTkButton(frame, text="Ingresar", width=280, command=self.procesar_login)
        btn_ingresar.pack(pady=(20, 10))

    def procesar_login(self):
        email = self.ent_email.get().strip()
        password = self.ent_password.get().strip()

        if not email or not password:
            messagebox.showwarning("Atención", "Ingresa correo y contraseña.")
            return

        try:
            conn = self.conectar_db()
            cursor = conn.cursor()
            
            user_id_out = cursor.var(oracledb.NUMBER)
            name_out = cursor.var(oracledb.STRING)
            role_out = cursor.var(oracledb.STRING)
            
            cursor.callproc("sp_login", [email, password, user_id_out, name_out, role_out])
            
            self.current_user_id = int(user_id_out.getvalue())
            self.current_user_name = str(name_out.getvalue())
            self.current_user_role = str(role_out.getvalue())
            
            cursor.close()
            conn.close()

            self.pantalla_principal()

        except oracledb.DatabaseError as e:
            error_obj, = e.args
            if "ORA-20001" in error_obj.message:
                messagebox.showerror("Acceso Denegado", "Contraseña incorrecta.")
            elif "ORA-20002" in error_obj.message:
                messagebox.showerror("Acceso Denegado", "Usuario no registrado.")
            else:
                messagebox.showerror("Error de BD", f"{error_obj.message}")
        except Exception as e:
            messagebox.showerror("Error", f"Error de conexión: {e}")
