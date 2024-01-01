import flet as ft

profile_img = ft.Image(
    src="https://drive.google.com/uc?id=1J1OTH3KO9pEjp7hOIReT4-IF5ReXiLiQ",
    width=150,
    height=150,
    fit=ft.ImageFit.CONTAIN,
    border_radius= 150/2
)

def _view_(page:ft.Page):

    old_password = ft.Ref[ft.TextField]()
    new_password = ft.Ref[ft.TextField]()

    profile_name = "Syahdan Alfiansyah"
    profile_nim = 2305929
    
    def open_dlg(e):
        page.dialog = password_dlg
        password_dlg.open = True
        page.update()
    
    def close_dlg(e):
        password_dlg.open = False
        page.update()

    def change_password(e):
        pass
        password_dlg.open = False
        page.update()

    password_dlg = ft.AlertDialog(
                        modal=True,
                        title=ft.Text("Please confirm"),
                        content=ft.Text("Apakah anda yakin?",weight=ft.FontWeight.BOLD,size=30,color="black"),
                        actions=[
                            ft.TextButton("Yes", on_click=change_password),
                            ft.TextButton("No", on_click=close_dlg),
                        ],
                        actions_alignment=ft.MainAxisAlignment.CENTER,
                    )

    manage_password_menu = ft.Column(
        [
            ft.TextField(
                ref=old_password,
                label="Password Lama",
                hint_text="Ketikkan password lama anda...",
                label_style = ft.ButtonStyle(
                    color="black",
                ),
                password=True,
                can_reveal_password=True,
                border=ft.InputBorder.UNDERLINE,
                border_color="#58C9E6"
            ),
            ft.TextField(
                ref=new_password,
                label="Password Baru",
                hint_text="Ketikkan password baru anda...",
                label_style = ft.ButtonStyle(
                    color="black",
                ),
                password=True,
                can_reveal_password=True,
                border=ft.InputBorder.UNDERLINE,
                border_color="#58C9E6"
            ),
            ft.Row(
                [
                    ft.ElevatedButton(
                        text="Konfirmasi",
                        color="white",
                        bgcolor="#58C9E6",
                        on_click=open_dlg
                    )
                ],alignment="center"
            )
        ],
        spacing=12
    )

    change_password_menus =  ft.Container(
                            content=manage_password_menu,
                            top=330,
                            left=15,
                            right=15,
                            bottom=15,
                            width=page.width,
                            expand=True,
                            bgcolor="white",
                            border_radius=20,
                            padding=15
                        )


    def go_back(e):
        page.views.pop()
        page.update()

    change_password_page = ft.Stack(
            [
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Row(
                                [
                                    ft.Text("Profile",size=20,color="white",weight=ft.FontWeight.BOLD)
                                ],alignment="center"
                            ),
                            ft.Row(
                                [
                                    profile_img
                                ], alignment="center"
                            ),
                            ft.Column(
                                [
                                    ft.Row(
                                        [
                                            ft.Text(profile_name,size=25,weight=ft.FontWeight.BOLD,color="white")
                                        ],alignment="center"
                                    ),
                                    ft.Row(
                                        [
                                            ft.Text(profile_nim,size=23,color="white")
                                        ],alignment="center"
                                    )
                                ],
                                spacing=5
                            )
                        ],
                        spacing=8
                    ),
                    top=40,
                    width=page.width,
                ),
                ft.Container(
                    content=ft.ElevatedButton(
                            content=ft.Icon(name = ft.icons.ARROW_BACK_IOS_NEW_ROUNDED,color="white",size=30),
                            on_click= go_back,
                            bgcolor = "#58C9E6",
                            width=45,
                            height=45,
                            style = ft.ButtonStyle(
                                shape={
                                    ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=15),
                                },
                                padding=0
                            ),
                        ),
                    top=40,
                    left=15,
                ),
                change_password_menus
            ],
            expand=True,
            width=page.width,
        )
    
    return ft.View(
        '/change_password',
        controls=[
            ft.Container(
                content = change_password_page,
                expand = True,
                width= page.width,
                gradient=ft.LinearGradient(
                            begin=ft.alignment.top_center,
                            end=ft.alignment.bottom_center,
                            colors=['#00A7D2', "#94D3E4"],
                        ),
                margin=-10
                )           
        ]
    )