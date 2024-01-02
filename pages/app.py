import flet as ft
from pages.home import _view_ as home_page
from pages.history import _view_ as history_page
from pages.profile import _view_ as profile_page
from pages.home import avatar_img
from pages.profile import set_profile
from supabase import create_client, Client


avatar_img = ft.Image(
        src="https://drive.google.com/uc?id=1J1OTH3KO9pEjp7hOIReT4-IF5ReXiLiQ",
        width=5,
        height=5,
        fit=ft.ImageFit.COVER,
        border_radius= 60/2
    )

url: str = "https://gkqvcndiyyrprpndgedg.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdrcXZjbmRpeXlycHJwbmRnZWRnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDIxMDM0NjYsImV4cCI6MjAxNzY3OTQ2Nn0.FDdQRXgW-_rMqIP4g5ttRwbynr-APBIlg_oFuVoOyww"
supabase: Client = create_client(url, key)


def _view_(page: ft.Page):
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

    page.padding = 0

    def go_profile(e):
        history.visible = False
        homepage.visible = False
        profile.visible = True
        page.navigation_bar.selected_index = 2
        page.update()

    def changetab(e):
        my_index = e.control.selected_index
        history.visible = True if my_index == 0 else False
        homepage.visible = True if my_index == 1 else False
        profile.visible = True if my_index == 2 else False
        set_profile(get_user()["Nama"], get_user()["Nim"])
        page.update()

    page.navigation_bar = ft.NavigationBar(
        selected_index=1,
        on_change=changetab,
        bgcolor=ft.colors.WHITE,
        destinations=[
            ft.NavigationDestination(
                icon=ft.icons.LOCATION_HISTORY_OUTLINED,
                selected_icon=ft.icons.LOCATION_HISTORY_SHARP,
            ),
            ft.NavigationDestination(
                icon=ft.icons.HOME_OUTLINED,
                selected_icon=ft.icons.HOME_ROUNDED
            ),
            ft.NavigationDestination(
                icon=ft.icons.ACCOUNT_BOX_OUTLINED,
                selected_icon=ft.icons.ACCOUNT_BOX
            ),
        ],
        elevation=0,
        height=60,
        surface_tint_color="#58C9E6"
    )



    def go_home(e):
        page.navigation_bar.selected_index = 1
        homepage.visible = True
        history.visible = False
        profile.visible = False
        page.update()

    homepage = ft.Stack(
        [
            home_page(page),
            ft.Container(
                content=ft.TextButton(
                    content=avatar_img,
                    on_click=go_profile,
                    style=ft.ButtonStyle(padding=0),
                ),
                top=40,
                right=15,
            ),
        ],
        expand=True,
        width=page.width,
    )
    homepage.visible = True

    history = ft.Stack(
        [
            history_page(page),
            ft.Container(
                content=ft.TextButton(
                    content=avatar_img,
                    on_click=go_profile,
                    style=ft.ButtonStyle(padding=0),
                ),
                top=40,
                right=15,
            ),
            ft.Container(
                content=ft.ElevatedButton(
                    content=ft.Icon(
                        name=ft.icons.ARROW_BACK_IOS_NEW_ROUNDED, color="white", size=30
                    ),
                    on_click=go_home,
                    bgcolor="#58C9E6",
                    width=45,
                    height=45,
                    style=ft.ButtonStyle(
                        shape={
                            ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(
                                radius=15
                            ),
                        },
                        padding=0,
                    ),
                ),
                top=40,
                left=15,
            ),
        ],
        expand=True,
    )

    homepage=ft.Stack(
                        [
                        home_page(page),
                        ft.Container(
                            content=avatar_img,
                            top=40,
                            right=15,
                            on_click=go_profile
                            )
                        ],
                        expand=True,
                        width=page.width
                    )
    homepage.visible = True

    history = ft.Stack(
                        [
                        history_page(page),
                        ft.Container(
                            content=avatar_img,
                            top=40,
                            right=15,
                            on_click=go_profile
                            )
                        ],
                        expand=True
                    )

    history.visible = False

    profile = ft.Stack(
        [
            profile_page(page),
            ft.Container(
                content=ft.ElevatedButton(
                    content=ft.Icon(
                        name=ft.icons.ARROW_BACK_IOS_NEW_ROUNDED, color="white", size=30
                    ),
                    on_click=go_home,
                    bgcolor="#58C9E6",
                    width=45,
                    height=45,
                    style=ft.ButtonStyle(
                        shape={
                            ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(
                                radius=15
                            ),
                        },
                        padding=0,
                    ),
                ),
                top=40,
                left=15,
            ),
            profile_page(page),   
        ],
        expand=True,
    )
    profile.visible = False

    return ft.View(
        "/app",
        controls=[
            ft.Container(
                content=ft.Stack(
                    [
                        history,
                        homepage,
                        profile,
                        ft.Container(
                            content=page.navigation_bar, width=page.width, bottom=0
                        ),
                    ],
                    expand=True,
                    width=page.width,
                ),
                gradient=ft.LinearGradient(
                    begin=ft.alignment.top_center,
                    end=ft.alignment.bottom_center,
                    colors=["#00A7D2", "#94D3E4"],
                ),
                width=14000,
                expand=True,
                margin=-10,
            )
        ],
    )
