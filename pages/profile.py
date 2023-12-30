import flet as ft
from pages.manage_account import _view_ as manage_account
from pages.help import _view_ as help


profile_link=f"/avatar.png"

profile_img = ft.Image(
        src=profile_link,
        width=150,
        height=150,
        fit=ft.ImageFit.COVER,
    )

def _view_(page:ft.Page):


    profile_name = "Syahdan Alfiansyah"
    profile_nim = 2305929

    def logout(e):
        page.dialog = logout_dlg
        logout_dlg.open = True
        page.update()

    def close_logout_dlg(e):
        logout_dlg.open = False
        page.update()

    def logout_dlg(e):
        logout_dlg.open = False
        page.update()
        e.page.go('/boarding')

    logout_dlg = ft.AlertDialog(
                    modal=True,
                    title=ft.Text("Log Out"),
                    content=ft.Text("Apakah anda yakin?",weight=ft.FontWeight.BOLD,size=20,color="black"),
                    actions=[
                        ft.TextButton("Yes", on_click=logout_dlg),
                        ft.TextButton("No", on_click=close_logout_dlg),
                    ],
                    actions_alignment=ft.MainAxisAlignment.CENTER,
                    )

    def go_manage_account(e):
        page.views.append(manage_account(page))
        page.update()

    def go_help(e):
        page.views.append(help(page))
        page.update()



    profile_menu = ft.Column(
        [
            ft.TextButton(
                content=ft.Container(
                    content=ft.Row(
                        [
                            ft.Row(
                                [
                                    ft.Icon(name=ft.icons.MANAGE_ACCOUNTS,size=25,color="#58C9E6"),
                                    ft.Text("Pengaturan Akun",weight=ft.FontWeight.W_300,size=15)
                                ]
                            ),
                            ft.Icon(name=ft.icons.ARROW_FORWARD_IOS_ROUNDED,color="#58C9E6")
                        ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    ),
                    border=ft.border.only(bottom=ft.border.BorderSide(2,"#58C9E5"))
                ),
                on_click = go_manage_account
            ),
            ft.TextButton(
                content=ft.Container(
                    content=ft.Row(
                        [
                            ft.Row(
                                [
                                    ft.Icon(name=ft.icons.HELP,size=25,color="#58C9E6"),
                                    ft.Text("Pusat Bantuan",weight=ft.FontWeight.W_300,size=15)
                                ]
                            ),
                            ft.Icon(name=ft.icons.ARROW_FORWARD_IOS_ROUNDED,color="#58C9E6")
                        ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    ),
                    border=ft.border.only(bottom=ft.border.BorderSide(2,"#58C9E5"))
                ),
                on_click= go_help
            ),
            ft.TextButton(
                content=ft.Container(
                    content=ft.Row(
                        [
                            ft.Row(
                                [
                                    ft.Icon(name=ft.icons.LOGOUT,size=25,color="#58C9E6"),
                                    ft.Text("Log Out",weight=ft.FontWeight.W_300,size=15)
                                ]
                            ),
                            ft.Icon(name=ft.icons.ARROW_FORWARD_IOS_ROUNDED,color="#58C9E6"),
                        ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    border=ft.border.only(bottom=ft.border.BorderSide(2,"#58C9E5"))
                ),
                on_click=logout
            ),
        ],
        spacing=12
    )



    profile_menus = ft.Container(
                content=profile_menu,
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

    profile_page = ft.Stack(
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
                                width=page.width
                            ),
                            profile_menus
                        ],
                        expand=True,
                        width=page.width
                    )

    return profile_page
