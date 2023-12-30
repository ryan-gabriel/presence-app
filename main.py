import flet as ft
from pages.boarding import _view_ as boarding_page
from pages.login import _view_ as login_page
from pages.register import _view_ as register_page
from pages.app import _view_ as app_page


def main(page:ft.Page):
    page.padding = 0
    page.theme_mode=ft.ThemeMode.LIGHT

    def route_change(route):
        page.views.clear()
        if page.route == '/boarding':
            page.views.append(boarding_page(page))
        elif page.route == '/login':
            page.views.append(login_page(page))
        elif page.route == '/register':
            page.views.append(register_page(page))
        elif page.route == '/app':
            page.views.append(app_page(page))

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


    page.views.append(boarding_page(page))
    page.update()

ft.app(target=main,assets_dir='asset')