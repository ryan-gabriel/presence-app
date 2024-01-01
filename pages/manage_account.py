import flet as ft
from pages.change_password import _view_ as change_passwords

profile_img = ft.Image(
    src="https://drive.google.com/uc?id=1J1OTH3KO9pEjp7hOIReT4-IF5ReXiLiQ",
    width=150,
    height=150,
    fit=ft.ImageFit.CONTAIN,
    border_radius= 150/2
)



def _view_(page:ft.Page):


    profile_name = "Syahdan Alfiansyah"
    profile_nim = 2305929


    def go_back(e):
        page.views.pop()
        page.update()

    def go_change_password(e):
        page.views.append(change_passwords(page))
        page.update()


    manage_account_menu = ft.Column(
        [
            ft.TextButton(
                content=ft.Container(
                    content=ft.Row(
                        [
                            ft.Row(
                                [
                                    ft.Icon(name=ft.icons.MANAGE_ACCOUNTS,size=25,color="#58C9E6"),
                                    ft.Text("Ubah Password",weight=ft.FontWeight.W_300,size=15)
                                ]
                            ),
                            ft.Icon(name=ft.icons.ARROW_FORWARD_IOS_ROUNDED,color="#58C9E6")
                        ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    ),
                    border=ft.border.only(bottom=ft.border.BorderSide(2,"#58C9E5"))
                ),
                on_click= go_change_password
            ),
        ],
        spacing=12
    )

    password_menus = ft.Container(
            content=manage_account_menu,
            top=340,
            left=15,
            right=15,
            bottom=15,
            width=page.width,
            expand=True,
            bgcolor="white",
            border_radius=20,
            padding=15
        )

    manage_password = ft.Stack(
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
                password_menus
            ],
            expand=True,
            width=page.width,
        )
    
    return ft.View(
        '/manage_account',
        controls=[
            ft.Container(
                content=manage_password,
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