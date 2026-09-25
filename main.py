from src.menus.main_menu import main_menu
from src.models import Maneger

if __name__ == "__main__":
    Maneger.ensure_admin_account()
    main_menu()