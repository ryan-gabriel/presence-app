import flet as ft
import asyncio
from supabase import create_client, Client

url: str = "https://gkqvcndiyyrprpndgedg.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdrcXZjbmRpeXlycHJwbmRnZWRnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDIxMDM0NjYsImV4cCI6MjAxNzY3OTQ2Nn0.FDdQRXgW-_rMqIP4g5ttRwbynr-APBIlg_oFuVoOyww"
supabase: Client = create_client(url, key)

profile_link = f"testing.jpg"

profile_img = ft.Image(
    src=profile_link,
    width=150,
    height=150,
    fit=ft.ImageFit.CONTAIN,
    border_radius=150 / 2,
)


def _view_(page: ft.Page):
    profile_name = "Syahdan Alfiansyah"
    profile_nim = 2305929

    def handle_logout(e):
        res = supabase.auth.sign_out()
        page.go("/login")

    def close_logout_dlg(e):
        logout_dlg.open = False
        page.update()

    logout_dlg = ft.AlertDialog(
        modal=True,
        title=ft.Text("Log Out"),
        content=ft.Text(
            "Apakah anda yakin?", weight=ft.FontWeight.BOLD, size=30, color="black"
        ),
        actions=[
            ft.TextButton("Yes", on_click=handle_logout),
            ft.TextButton("No", on_click=close_logout_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.CENTER,
    )

    profile_menu = ft.Column(
        [
            ft.TextButton(
                content=ft.Container(
                    content=ft.Row(
                        [
                            ft.Row(
                                [
                                    ft.Icon(
                                        name=ft.icons.MANAGE_ACCOUNTS,
                                        size=25,
                                        color="#58C9E6",
                                    ),
                                    ft.Text(
                                        "Pengaturan Akun",
                                        weight=ft.FontWeight.W_300,
                                        size=15,
                                    ),
                                ]
                            ),
                            ft.Icon(
                                name=ft.icons.ARROW_FORWARD_IOS_ROUNDED, color="#58C9E6"
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    border=ft.border.only(bottom=ft.border.BorderSide(2, "#58C9E5")),
                ),
                on_click=lambda e: e.page.go("/manage_account"),
            ),
            ft.TextButton(
                content=ft.Container(
                    content=ft.Row(
                        [
                            ft.Row(
                                [
                                    ft.Icon(
                                        name=ft.icons.HELP, size=25, color="#58C9E6"
                                    ),
                                    ft.Text(
                                        "Pusat Bantuan",
                                        weight=ft.FontWeight.W_300,
                                        size=15,
                                    ),
                                ]
                            ),
                            ft.Icon(
                                name=ft.icons.ARROW_FORWARD_IOS_ROUNDED, color="#58C9E6"
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    border=ft.border.only(bottom=ft.border.BorderSide(2, "#58C9E5")),
                ),
                on_click=lambda _: page.go("/help"),
            ),
            ft.TextButton(
                content=ft.Container(
                    content=ft.Row(
                        [
                            ft.Row(
                                [
                                    ft.Icon(
                                        name=ft.icons.LOGOUT, size=25, color="#58C9E6"
                                    ),
                                    ft.Text(
                                        "Log Out", weight=ft.FontWeight.W_300, size=15
                                    ),
                                ]
                            ),
                            ft.Icon(
                                name=ft.icons.ARROW_FORWARD_IOS_ROUNDED, color="#58C9E6"
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    border=ft.border.only(bottom=ft.border.BorderSide(2, "#58C9E5")),
                ),
                on_click=handle_logout,
            ),
        ],
        spacing=12,
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
        padding=15,
    )

    profile_page = ft.Stack(
        [
            ft.Container(
                content=ft.Column(
                    [
                        ft.Row(
                            [
                                ft.Text(
                                    "Profile",
                                    size=20,
                                    color="white",
                                    weight=ft.FontWeight.BOLD,
                                )
                            ],
                            alignment="center",
                        ),
                        ft.Row([profile_img], alignment="center"),
                        ft.Column(
                            [
                                ft.Row(
                                    [
                                        ft.Text(
                                            profile_name,
                                            size=25,
                                            weight=ft.FontWeight.BOLD,
                                            color="white",
                                        )
                                    ],
                                    alignment="center",
                                ),
                                ft.Row(
                                    [ft.Text(profile_nim, size=23, color="white")],
                                    alignment="center",
                                ),
                            ],
                            spacing=5,
                        ),
                    ],
                    spacing=8,
                ),
                top=40,
                width=page.width,
            ),
            profile_menus,
        ],
        expand=True,
        width=page.width,
    )

    return profile_page
