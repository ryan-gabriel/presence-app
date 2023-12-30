import flet as ft
from pages.home import _view_ as home_page
from pages.history import _view_ as history_page
from pages.profile import _view_ as profile_page
from pages.home import avatar_img


testing_homepage = 1


def _view_(page:ft.Page):
    
    page.padding = 0


    def changetab(e):
        my_index = e.control.selected_index
        history.visible = True if my_index == 0 else False
        homepage.visible = True if my_index == 1 else False
        profile.visible = True if my_index == 2 else False
        page.update()

    page.navigation_bar = ft.NavigationBar(
        selected_index = testing_homepage,
        on_change=changetab,
        bgcolor=ft.colors.WHITE,
        destinations=[
            ft.NavigationDestination(icon=ft.icons.LOCATION_HISTORY_ROUNDED),
            ft.NavigationDestination(icon=ft.icons.HOME_ROUNDED),
            ft.NavigationDestination(icon=ft.icons.TAG_FACES_ROUNDED),
        ],
        height=60,
        elevation=5,
        indicator_color="#00BAE9",
    )

    homepage=ft.Stack(
                        [
                        home_page(page),
                        ],
                        expand=True,
                        width=page.width
                    )
    homepage.visible = True

    history = ft.Stack(
                        [
                        history_page(page),   
                        ],
                        expand=True
                    )
    history.visible = False
    
    profile = ft.Stack(
        [
            profile_page(page),   
        ],
        expand=True,
    )
    profile.visible = False

    return ft.View(
        "/app",
        controls=[
            ft.Container(
                content= ft.Stack(
                    [
                            history,
                            homepage,
                            profile,
                            ft.Container(
                                content=page.navigation_bar,
                                width=page.width,
                                bottom=0
                            )
                    ],
                    expand=True,
                    width=page.width
                ),
                gradient=ft.LinearGradient(
                            begin=ft.alignment.top_center,
                            end=ft.alignment.bottom_center,
                            colors=['#00A7D2', "#94D3E4"],
                        ),
                width=14000,
                expand=True,
                margin=-10
            )
        ],
    )