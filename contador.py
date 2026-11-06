import flet as ft

class ContadorApp:
    def __init__(self, page):
        self.page = page
        self.contador = 0
        
        self.texto_contador = ft.Text(
            value = f"contador: {self.contador}",
            size = 30
        )
        
        self.boton_incrementar = ft.Button(
            "Incrementar",
            on_click=self.incrementar
        )
        
        self.construir_interfaz()
    
    def construir_interfaz(self):
        self.page.title = "Contador interactivo"
        
        self.page.add(
            ft.Text("Contador Interactivo Infinito",
                    size=20
            ),
            self.texto_contador,
            self.boton_incrementar
        )
        
    def incrementar(self, e):
        self.contador += 1
        self.texto_contador.value = f"contador: {self.contador}"
        self.page.update()
        
def main(page: ft.Page):
    ContadorApp(page)
    
ft.run(main)