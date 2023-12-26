import flet as ft
from supabase import create_client, Client

url: str = "https://gkqvcndiyyrprpndgedg.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdrcXZjbmRpeXlycHJwbmRnZWRnIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcwMjEwMzQ2NiwiZXhwIjoyMDE3Njc5NDY2fQ.xwfHGnlnCnYgj6tDESNRO1L9OeU1EdZAVZ4kzS7lBk4"
supabase: Client = create_client(url, key)


def _view_(page: ft.Page):
    page.padding = 0
    page.horizontal_alignment = "center"
    logo_img = ft.Image(
        src=f"/testing.jpg", width=1000, height=140, fit=ft.ImageFit.COVER
    )

    ref_nama = ft.Ref[ft.TextField]()
    ref_nim = ft.Ref[ft.TextField]()
    ref_kelas = ft.Ref[ft.Dropdown]()

    def create_biodata(e):
        current_user = supabase.auth.get_user()

        try:
            data, count = (
                supabase.table("Mahasiswa")
                .insert(
                    {
                        "user_id": current_user.user.id,
                        "Nama": ref_nama.current.value,
                        "Nim": ref_nim.current.value,
                        "Kelas": ref_kelas.current.value,
                    }
                )
                .execute()
            )

            if data is not None:
                page.go("/app")

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
            print(err)
            page.update()

    return ft.View(
        "/biodata",
        controls=[
            ft.Container(
                content=ft.Stack(
                    [
                        ft.Container(content=logo_img, right=40, left=40, top=40),
                        ft.Container(
                            content=ft.Row(
                                [
                                    ft.Text(
                                        "Biodata",
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
                                        "Silahkan isi biodata anda",
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
                                        ref=ref_nama,
                                        label="USERNAME",
                                        hint_text="Masukkan Username...",
                                        color=ft.colors.BLACK,
                                        border_color=ft.colors.BLUE,
                                        border=ft.InputBorder.UNDERLINE,
                                        suffix_icon=ft.icons.TAG_FACES,
                                        cursor_color=ft.colors.BLUE,
                                    ),
                                    ft.TextField(
                                        ref=ref_nim,
                                        label="NIM",
                                        hint_text="Masukkan NIM...",
                                        color=ft.colors.BLACK,
                                        border_color=ft.colors.BLUE,
                                        border=ft.InputBorder.UNDERLINE,
                                        cursor_color=ft.colors.BLUE,
                                        keyboard_type=ft.KeyboardType.NUMBER,
                                    ),
                                    ft.Dropdown(
                                        ref=ref_kelas,
                                        label="KELAS",
                                        color=ft.colors.BLACK,
                                        border_color=ft.colors.BLUE,
                                        border=ft.InputBorder.UNDERLINE,
                                        options=[
                                            ft.dropdown.Option("1-A"),
                                            ft.dropdown.Option("1-B"),
                                            ft.dropdown.Option("1-C"),
                                        ],
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=0,
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
                                        "Buat Akun",
                                        color=ft.colors.WHITE,
                                        bgcolor="#94D3E4",
                                        width=250,
                                        height=50,
                                        on_click=create_biodata,
                                        # on_click=lambda e: e.page.go("/boarding"),
                                    ),
                                ],
                                alignment="center",
                            ),
                            width=1000,
                            top=630,
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
    )
