import flet as ft
from pages.home import _view_ as home_page
from pages.login import _view_ as login_page
def main(page:ft.Page):


    page.views.append(home_page(page))

ft.app(target=main)