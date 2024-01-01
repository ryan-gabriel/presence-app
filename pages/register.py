import flet as ft

def _view_(page:ft.Page):
    page.padding = 0
    page.horizontal_alignment = "center"
    logo_img=ft.Image(
        src=f"https://drive.google.com/uc?id=16j6h5jRRdumjcARBB_tw7gQAjMiFUP2A",
        width=1000,
        height=275,
        fit = ft.ImageFit.COVER
    )
    return ft.View(
        "/register",
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
                            ft.Text("Buat Akun",color=ft.colors.BLACK,weight=ft.FontWeight.BOLD,size=30),
                        ],alignment="center"),
                        top = 325,
                        width=1000,
                        right=50,
                        left=50,
                    ),
                    ft.Container(
                        content=ft.Row([
                            ft.Text("Mari buat akun presence-mu",color=ft.colors.BLACK,weight=ft.FontWeight.W_200,size=15),
                        ],alignment="center"),
                        top = 380,
                        width=1000,
                        right=50,
                        left=50,
                    ),
                    ft.Container(
                        content=ft.Column([
                            ft.TextField(label="USERNAME",hint_text="Masukkan Username...",color=ft.colors.BLACK,border_color=ft.colors.BLUE,border=ft.InputBorder.UNDERLINE,suffix_icon=ft.icons.TAG_FACES,cursor_color=ft.colors.BLUE),
                            ft.TextField(label="NIM",hint_text="Masukkan NIM...",color=ft.colors.BLACK,border_color=ft.colors.BLUE,border=ft.InputBorder.UNDERLINE,cursor_color=ft.colors.BLUE,keyboard_type=ft.KeyboardType.NUMBER),
                            ft.TextField(label="EMAIL",hint_text="Masukkan Email...",color=ft.colors.BLACK,border_color=ft.colors.BLUE,border=ft.InputBorder.UNDERLINE,suffix_icon=ft.icons.EMAIL,cursor_color=ft.colors.BLUE,keyboard_type=ft.KeyboardType.EMAIL),
                            ft.TextField(label="PASSWORD",password=True,can_reveal_password=True,hint_text="Masukkan Password...",color=ft.colors.BLACK,border_color=ft.colors.BLUE,border=ft.InputBorder.UNDERLINE),
                        ],alignment=ft.MainAxisAlignment.CENTER,spacing=0),
                        top = 415,
                        width=1000,
                        right=50,
                        left=50,
                    ),
                    ft.Container(
                        content=ft.Row([
                            ft.ElevatedButton("Buat Akun",color=ft.colors.WHITE,bgcolor="#94D3E4",width=250,height=50,on_click= lambda e: e.page.go("/boarding")),
                        ],alignment="center"),
                        width=1000,
                        top = 705,
                        right=50,
                        left=50,
                    ),
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
                margin=-10
            )
        ]
    )