import tkinter as tk

from gui.main_window import MainWindow
from plugin_manager import PluginManager


def main():
    plugin_manager = PluginManager()
    plugin_manager.load_plugins()

    root = tk.Tk()
    app = MainWindow(root, plugin_manager)
    app.run()


if __name__ == "__main__":
    main()