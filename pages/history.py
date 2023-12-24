import flet as ft
from pages.home import avatar_img


def _view_(page:ft.Page):

    len_history = 10

    def items(count):
        history_items = []
        for i in range(count):
            history_items.append(
                    ft.Container(
                        content=ft.Stack(
                            [
                                    ft.Container(
                                        content=ft.Row([
                                            ft.Text("11 Desember 2023"),
                                            # place holder buat diintergrasikan dengan back end
                                            ft.Text("3 SKS", weight = ft.FontWeight.BOLD)
                                        ],
                                            alignment = ft.MainAxisAlignment.SPACE_BETWEEN
                                        ),
                                        top= 5,
                                        left=5,
                                        right=5,
                                        border=ft.border.only(bottom=ft.border.BorderSide(2,ft.colors.BLUE_300))
                                    ),
                                    ft.Container(
                                        content=ft.Text("Rekayasa Perangkat Lunak", color="#00BAE9", weight=ft.FontWeight.W_500,size=20),
                                        top=40
                                    ),
                                    ft.Container(
                                        content=ft.Row([
                                            ft.Column(
                                                [
                                                    ft.Icon(name=ft.icons.ACCOUNT_CIRCLE,color="#00BAE9"),
                                                    ft.Text("Hadir"), #place hoder hadir atau izin
                                                    ft.Text("12:10") #place holder untuk waktu absen mahasiswa
                                                ],
                                                spacing=1
                                            ),
                                            ft.Column(
                                                [
                                                    ft.Icon(name=ft.icons.ACCESS_TIME_SHARP,color="#00BAE9"),
                                                    ft.Text("Waktu"),
                                                    ft.Text("02:30") # place holder lama jam pelajaran
                                                ],
                                                spacing=1
                                            )
                                        ],
                                            alignment=ft.MainAxisAlignment.END,
                                            spacing=20
                                        ),
                                        bottom=10,
                                        width=page.width,
                                        left=5,
                                        right=5
                                    )
                            ],
                            expand=True,
                            width=page.width
                        ),
                        width=page.width,
                        padding=5,
                        bgcolor="white",
                        height=150,
                        border_radius=20
                    )
            )
        return history_items

    history_tab = ft.Tabs(
        selected_index=0,
        animation_duration=100,
        tabs=[
            ft.Tab(
                text="Hadir",
                content=ft.Stack(
                    [
                        ft.Container(
                            content=ft.Row([
                                ft.Text("Desember 2023"), # place holder buat diintergrasikan dengan back end
                                ft.ElevatedButton(
                                    content= ft.Icon(name=ft.icons.CALENDAR_MONTH,color="white"),
                                    bgcolor = ft.colors.TRANSPARENT,
                                    style=ft.ButtonStyle(
                                        padding=0
                                    )
                                )
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                            margin=ft.margin.only(top=20)
                        ),
                        ft.Container(
                            content = ft.Column(controls=items(len_history),spacing=5,scroll=ft.ScrollMode.ALWAYS,height=475,width=page.width),
                            top=120,
                            expand=True,
                            width=page.width,
                            right=5,
                            left=5,
                        )
                    ],
                    expand=True,
                    width=page.width,
                )
            ),
            ft.Tab(
                text="Izin",
                content=ft.Stack(
                    [
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Row(
                                        [ft.Text("Riwayat Izin", color="white", weight=ft.FontWeight.BOLD)],
                                        alignment="center"
                                    ),
                                    ft.Row(
                                        [
                                            ft.TextButton(
                                                icon=ft.icons.ARROW_BACK_IOS_NEW_ROUNDED,
                                                icon_color="white"
                                            ),
                                            ft.TextButton(
                                                "Desember 2023",
                                                icon=ft.icons.CALENDAR_MONTH,
                                                icon_color="white"
                                            ),
                                            ft.TextButton(
                                                icon=ft.icons.ARROW_FORWARD_IOS_ROUNDED,
                                                icon_color="white",
                                            ),
                                        ],
                                        alignment="center"
                                    )
                                ]
                            ),
                            left=5,
                            right=5,
                            width=page.width
                        ),
                        ft.Container(
                            content=ft.Stack(
                                [
                                    ft.Container(
                                        content=ft.Row(
                                            [
                                                ft.Column(
                                                    [
                                                        ft.Text("Jumat, 8 Desember 2023"),
                                                        ft.Row(
                                                            [
                                                                ft.Icon(name=ft.icons.INFO,color=ft.colors.BLUE_300),
                                                                ft.Text("Mengikuti Lomba") # placeholder untuk keterangan izin
                                                            ]
                                                        )
                                                    ],
                                                    spacing=15
                                                ),
                                                ft.Icon(name=ft.icons.CHECK_BOX,color=ft.colors.GREEN_300,size=40)
                                            ],
                                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                        ),
                                        width = page.width,
                                        left=8,
                                        right=8,
                                        top=3
                                    ),
                                ],
                                expand=True,
                                width=page.width
                            ),
                            top=100,
                            width=page.width,
                            padding=5,
                            bgcolor="white",
                            height=90,
                            right=5,
                            left=5,
                            border_radius=20
                        )
                    ],
                        expand = True,
                        width = page.width
                    ),
            )
        ],
        scrollable=True,
        expand=True,
        width=page.width,
    )

    history = ft.Stack(
            [
                ft.Container(
                    content=ft.Row([
                        ft.Text("Riwayat Kehadiran",color="white",weight=ft.FontWeight.BOLD,size=25), 
                        ],
                        alignment=ft.MainAxisAlignment.CENTER),
                    top=50,
                    width=page.width
                ),
                ft.Container(
                    content=history_tab,
                    top=100,
                    bottom=30,
                    right=30,
                    left=30,
                    width=page.width
                )
            ],
            expand=True,
            width=page.width
        )
    

    return history