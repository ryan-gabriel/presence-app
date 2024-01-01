import flet as ft
from supabase import create_client, Client

url: str = "https://gkqvcndiyyrprpndgedg.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdrcXZjbmRpeXlycHJwbmRnZWRnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDIxMDM0NjYsImV4cCI6MjAxNzY3OTQ2Nn0.FDdQRXgW-_rMqIP4g5ttRwbynr-APBIlg_oFuVoOyww"
supabase: Client = create_client(url, key)


def _view_(page: ft.Page):
    page.horizontal_alignment = "center"
    logo_img = ft.Image(
        src=f"/testing.jpg", width=1000, height=140, fit=ft.ImageFit.COVER
    )

    ref_email = ft.Ref[ft.TextField]()
    ref_password = ft.Ref[ft.TextField]()

    def handle_login(e):
        try:
            data = supabase.auth.sign_in_with_password(
                {
                    "email": ref_email.current.value,
                    "password": ref_password.current.value,
                }
            )

            user_exist = (
                supabase.table("Mahasiswa")
                .select("user_id")
                .eq("user_id", data.user.id)
                .execute()
            )

            is_first_login = user_exist.data[0] if user_exist.data else False

            if data is not None:
                ref_email.current.value, ref_password.current.value = "", ""

                if is_first_login is False:
                    page.go("/biodata")
                    return

                page.go(
                    "/app",
                )

        except Exception as err:
            page.snack_bar = ft.SnackBar(
                ft.Text(
                    str(err),
                    color=ft.colors.WHITE,
                ),
                bgcolor=ft.colors.RED,
                duration=2000,
            )
            page.snack_bar.open = True

            page.update()

    return ft.View(
        "/login",
        controls=[
            ft.Container(
                content=ft.Stack(
                    [
                        ft.Container(content=logo_img, right=40, left=40, top=40),
                        ft.Container(
                            content=ft.Row(
                                [
                                    ft.Text(
                                        "Log In",
                                        color=ft.colors.BLACK,
                                        weight=ft.FontWeight.BOLD,
                                        size=30,
                                    ),
                                ],
                                alignment="center",
                            ),
                            top=250,
                            width=1000,
                            right=50,
                            left=50,
                        ),
                        ft.Container(
                            content=ft.Row(
                                [
                                    ft.Text(
                                        "Absen Kehadiranmu dengan presence",
                                        color=ft.colors.BLACK,
                                        weight=ft.FontWeight.W_200,
                                        size=15,
                                    ),
                                ],
                                alignment="center",
                            ),
                            top=305,
                            width=1000,
                            right=50,
                            left=50,
                        ),
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.TextField(
                                        ref=ref_email,
                                        label="Email",
                                        hint_text="Masukkan Email...",
                                        color=ft.colors.BLACK,
                                        border_color=ft.colors.BLUE,
                                        border=ft.InputBorder.UNDERLINE,
                                        suffix_icon=ft.icons.TAG_FACES,
                                        cursor_color=ft.colors.BLUE,
                                        keyboard_type=ft.KeyboardType.EMAIL,
                                    ),
                                    ft.TextField(
                                        ref=ref_password,
                                        label="PASSWORD",
                                        password=True,
                                        can_reveal_password=True,
                                        hint_text="Masukkan Password...",
                                        color=ft.colors.BLACK,
                                        border_color=ft.colors.BLUE,
                                        border=ft.InputBorder.UNDERLINE,
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=20,
                            ),
                            top=340,
                            width=1000,
                            right=50,
                            left=50,
                        ),
                        ft.Container(
                            content=ft.Row(
                                [
                                    ft.ElevatedButton(
                                        "Log In",
                                        color=ft.colors.WHITE,
                                        bgcolor="#94D3E4",
                                        width=250,
                                        height=50,
                                        on_click=handle_login,
                                        # on_click=lambda e: e.page.go("/app"),
                                    ),
                                ],
                                alignment="center",
                            ),
                            width=1000,
                            top=600,
                            right=50,
                            left=50,
                        ),
                        ft.Container(
                            content=ft.Row(
                                [
                                    ft.Text(
                                        "Belum punya akun?",
                                        color=ft.colors.BLACK,
                                        weight=ft.FontWeight.W_600,
                                    ),
                                    ft.TextButton(
                                        "Register",
                                        on_click=lambda e: e.page.go("/register"),
                                    ),
                                ],
                                alignment="center",
                            ),
                            width=1000,
                            top=655,
                            right=50,
                            left=50,
                        ),
                    ],
                    expand=True,
                    width=14000,
                ),
                gradient=ft.LinearGradient(
                    begin=ft.alignment.top_center,
                    end=ft.alignment.bottom_center,
                    colors=["#00A7D2", ft.colors.WHITE],
                    stops=[0.2, 0.55],
                ),
                width=14000,
                expand=True,
            )
        ],
        padding=0,
    )
