import flet as ft
from datetime import datetime
import calendar
import csv
import os

def _view_(page:ft.Page):

    len_history = 10

    def close_dlg(e):
        filter_hadir.open=False
        text_filter.value = f'{filter_bulan.value} {filter_tahun.value}'
        panel_hadir.controls = history_hadir()
        page.update()


    def year_option():
        tahun = []
        for i in range(2020,int(datetime.now().year)+51):
            tahun.append(ft.dropdown.Option(i))
        return tahun
    
    def month_option():
        option_bulan = []
        list_bulan = list(calendar.month_name)[1:]
        for i in range(12):
            option_bulan.append(ft.dropdown.Option(list_bulan[i]))
        return option_bulan

    filter_bulan=ft.Dropdown(
                    options=month_option(),
                    width=150,
                    value=calendar.month_name[datetime.now().month]
                )

    filter_tahun =ft.Dropdown(
                    options=year_option(),
                    width=150,
                    value=str(datetime.now().year)
                )

    filter_hadir = ft.AlertDialog(
        modal=True,
        title=ft.Text("Bulan dan Tahun"),
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Text("Bulan"),
                        filter_bulan
                    ],alignment="center"
                ),
                ft.Row(
                    [
                        ft.Text("Tahun"),
                        filter_tahun
                    ],alignment="center"
                ),
            ],
            spacing=10,
            width=400,
            height=150
        ),
        actions=[
            ft.TextButton("Ok", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    def open_hadir_dlg(e):
        page.dialog = filter_hadir
        filter_hadir.open = True
        page.update()

    text_filter=ft.Text(value=f'{filter_bulan.value} {filter_tahun.value}',weight=ft.FontWeight.BOLD)


    def history_hadir():
        history_items = []
        file_list = os.listdir("data")
        with open ('data/prpl_4.csv','r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                status_absent = row.get('Keterangan')
                if status_absent == 'Hadir':
                
                    # ngambil data waktu absen dari supabase sesuai index i. ini hanya contoh
                    tanggal = datetime.strptime(row.get("Tanggal"),"%d-%B-%Y")
                    waktu_absen = datetime(year=tanggal.year,month=datetime.strptime(calendar.month_name[tanggal.month],"%B").month,day=tanggal.day) # data dari supabase, ini hanya contoh
                    jam_absen = row.get("Jam")

                    if waktu_absen.month == datetime.strptime(filter_bulan.value,"%B").month and waktu_absen.year == datetime.strptime(filter_tahun.value,"%Y").year:

                        # ambil data dari supabase
                        sks = "3 SKS"
                        waktu_sks = "02:30"
                        matkul="Pengantar Rekayasa Perangkat Lunak"

                        history_items.append(
                                ft.Container(
                                    content=ft.Stack(
                                        [
                                                ft.Container(
                                                    content=ft.Row([
                                                        ft.Text(f"{waktu_absen.day} {calendar.month_name[waktu_absen.month]} {waktu_absen.year}",size=12,weight=ft.FontWeight.BOLD),
                                                        ft.Text(sks, weight = ft.FontWeight.BOLD,size=12)
                                                    ],
                                                        alignment = ft.MainAxisAlignment.SPACE_BETWEEN
                                                    ),
                                                    top= 10,
                                                    left=10,
                                                    right=5,
                                                    border=ft.border.only(bottom=ft.border.BorderSide(2,ft.colors.BLUE_300))
                                                ),
                                                ft.Container(
                                                    content=ft.Text(value=matkul, color="#00BAE9", weight=ft.FontWeight.W_500,size=15),
                                                    top=40,
                                                    left=10
                                                ),
                                                ft.Container(
                                                    content=ft.Row([
                                                        ft.Column(
                                                            [
                                                                ft.Icon(name=ft.icons.ACCOUNT_CIRCLE,color="#00BAE9",size=18),
                                                                ft.Text("Hadir",size=12), #place hoder hadir atau izin
                                                                ft.Text(f'{jam_absen}',size=12)
                                                            ],
                                                            spacing=0
                                                        ),
                                                        ft.Column(
                                                            [
                                                                ft.Icon(name=ft.icons.ACCESS_TIME_SHARP,color="#00BAE9",size=18),
                                                                ft.Text("Waktu",size=12),
                                                                ft.Text(f"{waktu_sks}",size=12)
                                                            ],
                                                            spacing=0
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
        
        if not history_items:
            history_items.append(
                ft.Container(
                    content=ft.Row(
                        [
                            ft.Text(f"No attendance was taken in {calendar.month_name[datetime.strptime(filter_bulan.value,"%B").month]} {datetime.strptime(filter_tahun.value,"%Y").year}",size=14,weight=ft.FontWeight.BOLD,color=ft.colors.RED_400)
                        ],alignment="center"
                    ),
                    width=page.width,
                    padding=5,
                    bgcolor="white",
                    height=50,
                    border_radius=20
                )
            )

        return history_items
    
    panel_hadir = ft.Column(controls=history_hadir(),spacing=5,scroll=ft.ScrollMode.ALWAYS,height=475,width=page.width)
 
    def close_izin_dlg(e):
        filter_izin.open = False
        panel_izin.controls = history_izin()
        tombol_tanggal.text = f"{filter_izin_bulan.value} {filter_izin_tahun.value}"
        page.update()
    
    def open_izin_dlg(e):
        page.dialog = filter_izin
        filter_izin.open = True
        page.update()

    filter_izin_bulan=ft.Dropdown(
                        options=month_option(),
                        width=150,
                        value=calendar.month_name[datetime.now().month]
                    )
    
    filter_izin_tahun = ft.Dropdown(
                            options=year_option(),
                            width=150,
                            value=str(datetime.now().year)
                        )

    filter_izin = ft.AlertDialog(
        modal=True,
        title=ft.Text("Bulan dan Tahun"),
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Text("Bulan"),
                        filter_izin_bulan
                    ],alignment="center"
                ),
                ft.Row(
                    [
                        ft.Text("Tahun"),
                        filter_izin_tahun
                    ],alignment="center"
                ),
            ],
            spacing=10,
            width=400,
            height=150
        ),
        actions=[
            ft.TextButton("Ok", on_click=close_izin_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    def next_month(e):
        if str(filter_izin_bulan.value) != "December":
            filter_izin_bulan.value = calendar.month_name[list(calendar.month_name).index(str(filter_izin_bulan.value))+1]
            panel_izin.controls = history_izin()
            tombol_tanggal.text = f"{filter_izin_bulan.value} {filter_izin_tahun.value}"
        else:
            filter_izin_bulan.value = calendar.month_name[1]
            filter_izin_tahun.value = str(int(filter_izin_tahun.value)+1)
            tombol_tanggal.text = f"{filter_izin_bulan.value} {filter_izin_tahun.value}"
            panel_izin.controls = history_izin()
        page.update()

    def prev_month(e):
        if str(filter_izin_bulan.value) != "January":
            filter_izin_bulan.value = calendar.month_name[list(calendar.month_name).index(str(filter_izin_bulan.value))-1]
            tombol_tanggal.text = f"{filter_izin_bulan.value} {filter_izin_tahun.value}"
            panel_izin.controls = history_izin()
        else:
            filter_izin_bulan.value = calendar.month_name[-1]
            filter_izin_tahun.value = str(int(filter_izin_tahun.value)-1)
            tombol_tanggal.text = f"{filter_izin_bulan.value} {filter_izin_tahun.value}"
            panel_izin.controls = history_izin()
        page.update()


    def history_izin():

        izin_history = []
        with open ('data/prpl_4.csv','r') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                status_absent = row.get('Keterangan')
                print(status_absent)
                if status_absent == 'Izin' or status_absent == 'Sakit' or status_absent == 'Alpa' or status_absent == 'Dispen':
                    check_color = ft.colors.GREEN_300
                    
                    if status_absent == 'Izin' or status_absent == 'Sakit' or status_absent == 'Alpa':
                        check_color = ft.colors.RED_300

                    tanggal = datetime.strptime(row.get("Tanggal"),"%d-%B-%Y")
                    waktu_absen = datetime(year=tanggal.year,month=datetime.strptime(calendar.month_name[tanggal.month],"%B").month,day=tanggal.day) # data dari supabase, ini hanya contoh
                    nama_hari = waktu_absen.strftime("%A")
                    print(waktu_absen,nama_hari)
                    if waktu_absen.month == datetime.strptime(filter_izin_bulan.value, "%B").month and waktu_absen.year == int(filter_izin_tahun.value):
                        izin_history.append(
                            ft.Container(
                                content=ft.Row(
                                    [
                                        ft.Column(
                                            [
                                                ft.Text(f"{nama_hari}, {waktu_absen.day} {calendar.month_name[waktu_absen.month]} {waktu_absen.year}",weight=ft.FontWeight.BOLD),
                                                ft.Row(
                                                    [
                                                        ft.Icon(name=ft.icons.INFO,color=ft.colors.BLUE_300,size=25),
                                                        ft.Text(status_absent.capitalize(),weight=ft.FontWeight.BOLD) # sesuai status absen
                                                    ]
                                                )
                                            ],
                                            width=250
                                        ),
                                        ft.Icon(name=ft.icons.CHECK_BOX,size=30,color=check_color)
                                    ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                ),
                                border=ft.border.only(bottom=ft.border.BorderSide(2,"#00BAE9")),
                                padding=ft.padding.only(bottom=5),
                                margin=ft.margin.only(bottom=5)
                            )
                        )

        if not izin_history:
            izin_history.append(
                ft.Container(
                    content=ft.Row(
                        [
                            ft.Text(f"No absent was taken in {calendar.month_name[datetime.strptime(filter_izin_bulan.value,"%B").month]} {datetime.strptime(filter_izin_tahun.value,"%Y").year}",size=14,weight=ft.FontWeight.BOLD,color=ft.colors.RED_400)
                        ],alignment="center"
                    ),
                    width=page.width,
                    padding=5,
                    bgcolor="white",
                    height=50,
                    border_radius=20
                )
            )

        return izin_history

    panel_izin = ft.Column(controls=history_izin(),spacing=5,scroll=ft.ScrollMode.ALWAYS,height=475,width=page.width)

    tombol_tanggal = ft.TextButton(
                text=f"{filter_izin_bulan.value} {filter_izin_tahun.value}",
                icon=ft.icons.CALENDAR_MONTH,
                icon_color="white",
                on_click=open_izin_dlg
            )

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
                                text_filter,
                                ft.ElevatedButton(
                                    content= ft.Icon(name=ft.icons.CALENDAR_MONTH,color="white"),
                                    bgcolor = ft.colors.TRANSPARENT,
                                    style=ft.ButtonStyle(
                                        padding=0
                                    ),
                                    on_click=open_hadir_dlg
                                )
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                            margin=ft.margin.only(top=20)
                        ),
                        ft.Container(
                            content = panel_hadir,
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
                                        [
                                            ft.TextButton(
                                                icon=ft.icons.ARROW_BACK_IOS_NEW_ROUNDED,
                                                icon_color="white",
                                                on_click=prev_month
                                            ),
                                            tombol_tanggal,
                                            ft.TextButton(
                                                icon=ft.icons.ARROW_FORWARD_IOS_ROUNDED,
                                                icon_color="white",
                                                on_click=next_month
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
                            content =panel_izin,
                            top=100,
                            width=page.width,
                            padding=5,
                            bgcolor="white",
                            height=400,
                            right=5,
                            left=5,
                            border_radius=20
                        ),
                        ft.Container(
                            content=ft.Row(
                                [
                                    ft.Container(
                                        content=ft.Row(
                                            [
                                                ft.Row(
                                                    [
                                                        ft.Icon(name=ft.icons.CHECK_BOX,size=30,color=ft.colors.GREEN_300),
                                                        ft.Text("Dispen",weight=ft.FontWeight.W_600,color=ft.colors.GREEN_300)
                                                    ],
                                                    alignment="center",
                                                    width=100
                                                ),
                                                ft.Row(
                                                    [
                                                        ft.Icon(name=ft.icons.CHECK_BOX,size=30,color=ft.colors.RED_300),
                                                        ft.Text("Tidak Hadir",weight=ft.FontWeight.W_600,color=ft.colors.RED_300)
                                                    ],
                                                    alignment="center",
                                                    width=100,
                                                ),
                                            ],
                                            alignment="center",
                                            spacing=35
                                        ),
                                        width=300,
                                        bgcolor="white",
                                        padding=5,
                                        border_radius=30
                                    )
                                ],
                                alignment="center",
                            ),
                            top=550,
                            left=10,
                            right=10
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
                    content=ft.Row(
                        [
                            ft.Text("Riwayat Kehadiran",color="white",size=25,text_align="center",weight=ft.FontWeight.BOLD)
                        ],alignment="center"
                    ),
                    top=50,
                    right=15,
                    left=15,
                    width=page.width
                ),
                ft.Container(
                    content=history_tab,
                    top=100,
                    bottom=30,
                    right=15,
                    left=15,
                    width=page.width
                ),
            ],
            expand=True,
            width=page.width
        )
    

    return history