import flet as ft
from datetime import datetime
from pages.profile import profile_link

avatar_img = ft.Image(
        src=profile_link,
        width=60,
        height=60,
        fit=ft.ImageFit.CONTAIN,
        border_radius= 60/2
    )

sekarang = datetime.now()
hari = sekarang.strftime("%A")
tanggal = sekarang.day
bulan = sekarang.strftime("%B")
tahun = sekarang.year
jam = sekarang.strftime("%H")
menit = sekarang.strftime("%M")

def _view_(page:ft.Page):

    opt = ft.Ref[ft.Dropdown]() # option dropdown izin
    
    def pick_files_result(e: ft.FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else None
        )
        selected_files.update()

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()
    page.overlay.append(pick_files_dialog)

    t = ft.Text(color="black")
    konfirmasi_btn = ft.ElevatedButton("Konfirmasi")
    box_area = ft.TextField(height=100,visible=False,width=page.width,min_lines=3,max_lines=3,max_length=50)
    fileDispen = ft.Row([
        ft.ElevatedButton(
                        "Upload",
                        icon=ft.icons.UPLOAD_FILE,
                        on_click=lambda _: pick_files_dialog.pick_files(
                            allow_multiple=True
                        ),
                    ),selected_files
    ],visible=False)
    
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
                tab_content=ft.Text("Hadir",color="blue"),
                content=ft.Column([
                    ft.Row([
                        ft.Text("Absensi sekarang: ",color="#00BAE9"),
                    ],alignment="center"),
                    ft.Row([
                        ft.Text("Pengantar Rekayasa Perangkat Lunak",color="#00BAE9"),
                    ],alignment = "center"),
                    ft.Row([
                        ft.Text("Batas Absen",color="#00BAE9"),
                    ],alignment = "center"),
                    ft.Row([
                        ft.Text("12:15 ",color="#00BAE9"), #place holder
                    ],alignment = "center",),
                    ft.Row([
                        ft.ElevatedButton(
                            content= ft.Icon(name=ft.icons.FINGERPRINT,color="white",size=150),
                            bgcolor="#00BAE9",
                            style=ft.ButtonStyle(
                                padding=0
                            )
                        ),
                    ],alignment="center"),
                    ft.Row([
                        ft.Text("Absen kehadiranmu",color="#00BAE9")
                    ],alignment="center")
                ],width=1000)
            ),
            ft.Tab(
                tab_content=ft.Text("Izin",color="blue"),
                content=ft.Column([
                    ft.Text("Keterangan: ",weight=ft.FontWeight.BOLD,color="black"),
                    ft.Dropdown(
                        ref = opt,
                        width = page.width,
                        options=[
                            ft.dropdown.Option("Dispen"),
                            ft.dropdown.Option("Sakit"),
                            ft.dropdown.Option("Izin"),
                        ],
                        color="#00BAE9",
                        focused_bgcolor="94D3E4",
                        hint_text="Pilih Keterangan Anda",
                        border_radius=10,
                        on_change=dropdown_changed
                    ),
                    t,
                    box_area,
                    fileDispen,
                    ft.Stack([
                        ft.Container(
                            content= konfirmasi_btn, #belum ditambahin fungsionalitas
                            bottom=10,
                            right=10
                        )
                    ],
                    expand=True,
                    width=page.width,
                    )
                ]),
            )
        ],
        scrollable=True,
        expand=True,
        width=page.width,
    )
    

    homepage = ft.Stack(
                [
                    ft.Container(
                        content=ft.Text(f"{hari}, {tanggal} {bulan} {tahun}",text_align="center",size=12,color="white"),
                        right=50,
                        left=50,
                        top=70
                    ),
                    ft.Container(
                        content=ft.Row(
                                [
                                ft.Text(f"{jam} : {menit}",color="white",size=30,weight=ft.FontWeight.BOLD)
                                ],alignment="center"),
                        width= page.width,
                        right=50,
                        left=50,
                        top=105
                    ),
                    ft.Container(
                        content=ft.Column([
                            ft.Row([
                                ft.Text("Pilih Kehadiran",weight=ft.FontWeight.BOLD,size=20,color="black",text_align="center")
                            ],alignment="center"),
                            ft.Container(
                                content=absent_tab,
                                height=400,
                                width=page.width
                            )
                        ],),
                        width=700,
                        left=50,
                        right=50,
                        top=200,
                        bgcolor="white",
                        border_radius=25,
                        padding=10
                    )
                ],
                expand=True,
                width=page.width,
            )
    return homepage