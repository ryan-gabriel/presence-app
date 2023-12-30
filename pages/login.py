import flet as ft

def _view_(page:ft.Page):
    page.horizontal_alignment = "center"
    logo_img=ft.Image(
        src=f"/login_img.svg",
        width=1000,
        height=275,
        fit = ft.ImageFit.CONTAIN
    )

    return ft.View(
        "/login",
        controls=[
            ft.Container(
            content=ft.Stack([
                ft.Container(
                    content =logo_img,
                    right = 10,
                    left = 10,
                    top = 40
                ),
                ft.Container(
                    content=ft.Row([
                        ft.Text("Log In",color=ft.colors.BLACK,weight=ft.FontWeight.BOLD,size=30),
                    ],alignment="center"),
                    top = 325,
                    width=1000,
                    right=50,
                    left=50,
                ),
                ft.Container(
                    content=ft.Row([
                        ft.Text("Absen Kehadiranmu dengan presence",color=ft.colors.BLACK,weight=ft.FontWeight.W_200,size=15),
                    ],alignment="center"),
                    top = 370,
                    width=1000,
                    right=50,
                    left=50,
                ),
                ft.Container(
                    content=ft.Column([
                        ft.TextField(label="NIM",hint_text="Masukkan NIM...",color=ft.colors.BLACK,border_color=ft.colors.BLUE,border=ft.InputBorder.UNDERLINE,suffix_icon=ft.icons.TAG_FACES,cursor_color=ft.colors.BLUE,keyboard_type=ft.KeyboardType.NUMBER),
                        ft.TextField(label="PASSWORD",password=True,can_reveal_password=True,hint_text="Masukkan Password...",color=ft.colors.BLACK,border_color=ft.colors.BLUE,border=ft.InputBorder.UNDERLINE),
                    ],alignment=ft.MainAxisAlignment.CENTER,spacing=20),
                    top = 415,
                    width=1000,
                    right=50,
                    left=50,
                ),
                ft.Container(
                    content=ft.Row([
                        ft.ElevatedButton("Log In",color=ft.colors.WHITE,bgcolor="#94D3E4",width=250,height=50,on_click = lambda e:e.page.go("/app")),
                    ],alignment="center"),
                    width=1000,
                    top = 650,
                    right=50,
                    left=50,
                ),
                ft.Container(
                    content=ft.Row([
                            ft.Text("Belum punya akun?",color=ft.colors.BLACK,weight=ft.FontWeight.W_600),
                            ft.TextButton("Register", on_click= lambda e:e.page.go("/register"))
                    ],alignment="center"),
                    width=1000,
                    top = 700,
                    right=50,
                    left=50,
                )
            ],
            expand=True,
            width=14000
            ),
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=['#00A7D2', ft.colors.WHITE],
                stops=[0.2, 0.55]
            ),
            width=14000,
            expand=True,
            )
        ],
        padding=0
    )