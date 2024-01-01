import flet as ft
from pages.boarding import _view_ as boarding_page
from pages.login import _view_ as login_page
from pages.register import _view_ as register_page
from pages.app import _view_ as app_page
from pages.manage_account import _view_ as manage_accounts
from pages.change_password import _view_ as change_passwords
from pages.help import _view_ as help_pages
from pages.biodata import _view_ as biodata_page



def main(page: ft.Page):
    page.padding = 0
    page.theme_mode = ft.ThemeMode.LIGHT
    
    boarding = boarding_page(page)
    login = login_page(page)
    register = register_page(page)
    app = app_page(page)
    manage_account = manage_accounts(page)
    change_password = change_passwords(page)
    help = help_pages(page)
    biodata = biodata_page(page)

    def route_change(route):
        page.views.clear()
        if page.route == "/boarding":
            page.views.append(boarding)
        elif page.route == "/login":
            page.views.append(login)
        elif page.route == "/register":
            page.views.append(register)
        elif page.route == "/app":
            page.views.append(app)
        elif page.route == "/manage_account":
            page.views.append(manage_account)
        elif page.route == "/change_password":
            page.views.append(change_password)
        elif page.route == "/help":
            page.views.append(help)
        elif page.route == "/biodata":
            page.views.append(biodata)


        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

    page.views.append(boarding)
    page.update()


ft.app(target=main, assets_dir="asset")
