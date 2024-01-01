import flet as ft
from datetime import datetime
from pages.profile import profile_link
from supabase import create_client, Client
import os
import csv

avatar_img = ft.Image(
    src=profile_link, width=60, height=60, fit=ft.ImageFit.CONTAIN, border_radius=60 / 2
)

sekarang = datetime.now()
hari = sekarang.strftime("%A")
tanggal = sekarang.day
bulan = sekarang.strftime("%B")
tahun = sekarang.year
jam = sekarang.strftime("%H")
menit = sekarang.strftime("%M")

url: str = "https://gkqvcndiyyrprpndgedg.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdrcXZjbmRpeXlycHJwbmRnZWRnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDIxMDM0NjYsImV4cCI6MjAxNzY3OTQ2Nn0.FDdQRXgW-_rMqIP4g5ttRwbynr-APBIlg_oFuVoOyww"
supabase: Client = create_client(url, key)


def get_user():
    user_id = supabase.auth.get_user().user.identities[0].user_id
    return (
        supabase.table("Mahasiswa")
        .select("*")
        .eq("user_id", user_id)
        .single()
        .execute()
        .data
    )


def get_latest_pertemuan():
    return (
        supabase.table("pertemuan")
        .select("*")
        .order("created_at", desc=True)
        .limit(1)
        .execute()
    )


def tambah_absen(nama_file, data):
    header = ["Nama", "NIM", "Keterangan", "Tanggal", "Jam"]

    # Mengecek apakah file sudah ada
    file_exist = os.path.exists(f"data/{nama_file}.csv")

    # Menulis ke file CSV
    with open(f"data/{nama_file}.csv", mode="a", newline="") as file_csv:
        writer = csv.writer(file_csv)

        # Menulis header hanya jika file baru dibuat
        if not file_exist:
            writer.writerow(header)

        # Menulis data ke dalam file CSV
        writer.writerow(data)

    return "Berhasil Absen"


def cek_sudah_absen(nama_file, nim):
    with open(f"data/{nama_file}.csv", mode="r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["NIM"] == nim:
                return True
    return False


def _view_(page: ft.Page):
    def handle_absen(e):
        try:
            user = get_user()
            pertemuan = get_latest_pertemuan()
            file_kehadiran = ""

            nama = user["Nama"]
            nim = user["Nim"]

            file_kehadiran = pertemuan.data[0]["file_kehadiran"]

            data = [nama, nim, "Hadir", f"{tanggal}-{bulan}-{tahun}", f"{jam}:{menit}"]

            if tambah_absen(file_kehadiran, data) != " ":
                page.snack_bar = ft.SnackBar(
                    ft.Text(
                        "Absen berhasil",
                        color=ft.colors.WHITE,
                    ),
                    bgcolor=ft.colors.GREEN,
                    duration=2000,
                )
                page.snack_bar.open = True

                page.update()
                return

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

    opt = ft.Ref[ft.Dropdown]()  # option dropdown izin

    def upload_files(e):
        upload_list = []
        # if file_picker.result != None and file_picker.result.files != None:
        #     for f in file_picker.result.files:
        #         upload_list.append(
        #             FilePickerUploadFile(
        #                 f.name,
        #                 upload_url=page.get_upload_url(f.name, 600),
        #             )
        #         )
        #     file_picker.upload(upload_list)

    def pick_files_result(e: ft.FilePickerResultEvent):
        print(e.files)

        # selected_files.value = (
        #     ", ".join(map(lambda f: f.name, e.files)) if e.files else None
        # )
        # selected_files.update()

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()
    page.overlay.append(pick_files_dialog)

    t = ft.Text(color="black")
    konfirmasi_btn = ft.ElevatedButton("Konfirmasi")
    box_area = ft.TextField(
        height=100,
        visible=False,
        width=page.width,
        min_lines=3,
        max_lines=3,
        max_length=50,
    )
    fileDispen = ft.Row(
        [
            ft.ElevatedButton(
                "Upload",
                icon=ft.icons.UPLOAD_FILE,
                on_click=lambda _: pick_files_dialog.pick_files(allow_multiple=True),
            ),
            selected_files,
        ],
        visible=False,
    )

    def dropdown_changed(e):
        if opt.current.value == "Izin" or opt.current.value == "Sakit":
            fileDispen.visible = False
            box_area.visible = True
            t.value = "Keterangan"
            page.update()
        elif opt.current.value == "Dispen":
            box_area.visible = False
            fileDispen.visible = True
            t.value = "File"
            page.update()

    absent_tab = ft.Tabs(
        selected_index=0,
        animation_duration=100,
        tabs=[
            ft.Tab(
                tab_content=ft.Text("Hadir", color="blue"),
                content=ft.Column(
                    [
                        ft.Row(
                            [
                                ft.Text("Absensi sekarang: ", color="#00BAE9"),
                            ],
                            alignment="center",
                        ),
                        ft.Row(
                            [
                                ft.Text(
                                    "Pengantar Rekayasa Perangkat Lunak",
                                    color="#00BAE9",
                                ),
                            ],
                            alignment="center",
                        ),
                        ft.Row(
                            [
                                ft.Text("Batas Absen", color="#00BAE9"),
                            ],
                            alignment="center",
                        ),
                        ft.Row(
                            [
                                ft.Text("12:15 ", color="#00BAE9"),  # place holder
                            ],
                            alignment="center",
                        ),
                        ft.Row(
                            [
                                ft.ElevatedButton(
                                    content=ft.Icon(
                                        name=ft.icons.FINGERPRINT,
                                        color="white",
                                        size=150,
                                    ),
                                    bgcolor="#00BAE9",
                                    style=ft.ButtonStyle(padding=0),
                                    on_click=handle_absen,
                                ),
                            ],
                            alignment="center",
                        ),
                        ft.Row(
                            [ft.Text("Absen kehadiranmu", color="#00BAE9")],
                            alignment="center",
                        ),
                    ],
                    width=1000,
                ),
            ),
            ft.Tab(
                tab_content=ft.Text("Izin", color="blue"),
                content=ft.Column(
                    [
                        ft.Text(
                            "Keterangan: ", weight=ft.FontWeight.BOLD, color="black"
                        ),
                        ft.Dropdown(
                            ref=opt,
                            width=page.width,
                            options=[
                                ft.dropdown.Option("Dispen"),
                                ft.dropdown.Option("Sakit"),
                                ft.dropdown.Option("Izin"),
                            ],
                            color="#00BAE9",
                            focused_bgcolor="94D3E4",
                            hint_text="Pilih Keterangan Anda",
                            border_radius=10,
                            on_change=dropdown_changed,
                        ),
                        t,
                        box_area,
                        fileDispen,
                        ft.Stack(
                            [
                                ft.Container(
                                    content=konfirmasi_btn,  # belum ditambahin fungsionalitas
                                    bottom=10,
                                    right=10,
                                )
                            ],
                            expand=True,
                            width=page.width,
                        ),
                    ]
                ),
            ),
        ],
        scrollable=True,
        expand=True,
        width=page.width,
    )

    homepage = ft.Stack(
        [
            ft.Container(
                content=ft.Text(
                    f"{hari}, {tanggal} {bulan} {tahun}",
                    text_align="center",
                    size=12,
                    color="white",
                ),
                right=50,
                left=50,
                top=70,
            ),
            ft.Container(
                content=ft.Row(
                    [
                        ft.Text(
                            f"{jam} : {menit}",
                            color="white",
                            size=30,
                            weight=ft.FontWeight.BOLD,
                        )
                    ],
                    alignment="center",
                ),
                width=page.width,
                right=50,
                left=50,
                top=105,
            ),
            ft.Container(
                content=ft.Column(
                    [
                        ft.Row(
                            [
                                ft.Text(
                                    "Pilih Kehadiran",
                                    weight=ft.FontWeight.BOLD,
                                    size=20,
                                    color="black",
                                    text_align="center",
                                )
                            ],
                            alignment="center",
                        ),
                        ft.Container(content=absent_tab, height=400, width=page.width),
                    ],
                ),
                width=700,
                left=50,
                right=50,
                top=200,
                bgcolor="white",
                border_radius=25,
                padding=10,
            ),
        ],
        expand=True,
        width=page.width,
    )
    return homepage
