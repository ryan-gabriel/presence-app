import flet as ft
from flet import Page


def _view_(page:ft.Page):
    img = ft.Image(
        src="https://drive.google.com/uc?id=1i8CTdT1i66BOc64hfhW_AkpWKSbRfZEl",
        height=150,
        fit=ft.ImageFit.CONTAIN
    )
    head_text = ft.Text("SELAMAT DATANG", weight=ft.FontWeight.BOLD, size=30)
    body_text = ft.Text("Halo selamat datang di aplikasi presence")
    login_button = ft.ElevatedButton("Login", width=1300, on_click= lambda e: e.page.go("/login"))
    return ft.View(
        "/boarding",
        controls=[
            ft.Row(controls=[
                ft.Container(
                    content=img,
                    padding=30,
                    margin=ft.margin.only(bottom=50,top=40)
                )
            ], alignment="center"),
            ft.Row([head_text], alignment="center"),
            ft.Container(margin=ft.margin.only(bottom=5)),
            ft.Row([body_text], alignment="center"),
            ft.Container(
                ft.Stack([
                    ft.Container(
                        content=login_button,
                        border_radius=5,
                        bottom=40,
                        left=20,
                        right=20
                    )
                ]),
                width=Page.width,
                expand=True
            )
        ],
    )