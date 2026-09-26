import tkinter as tk
from tkinter import messagebox

from config import (
    APP_NAME,
    APP_VERSION,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
)


class MainWindow:
    def __init__(self, root, plugin_manager):
        self.root = root
        self.plugin_manager = plugin_manager

        self.root.title(
            f"{APP_NAME} v{APP_VERSION}"
        )

        self.root.geometry(
            f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}"
        )

        self.root.minsize(800, 500)

        self.create_ui()

    def create_ui(self):
        # 左側メニュー
        sidebar = tk.Frame(
            self.root,
            width=220,
            bg="#202124"
        )
        sidebar.pack(
            side="left",
            fill="y"
        )

        sidebar.pack_propagate(False)

        title = tk.Label(
            sidebar,
            text="🧰 Daily Utility",
            font=("Segoe UI", 18, "bold"),
            fg="white",
            bg="#202124"
        )
        title.pack(
            pady=(25, 30)
        )

        plugin_label = tk.Label(
            sidebar,
            text="PLUGINS",
            font=("Segoe UI", 10, "bold"),
            fg="#9aa0a6",
            bg="#202124"
        )
        plugin_label.pack(
            anchor="w",
            padx=20,
            pady=(0, 10)
        )

        for plugin in self.plugin_manager.get_plugins():
            button = tk.Button(
                sidebar,
                text=plugin.name,
                command=lambda p=plugin: self.run_plugin(p),
                anchor="w",
                font=("Segoe UI", 11),
                fg="white",
                bg="#202124",
                activebackground="#303134",
                activeforeground="white",
                relief="flat",
                bd=0,
                padx=20,
                pady=10
            )

            button.pack(
                fill="x"
            )

        # メイン部分
        main = tk.Frame(
            self.root,
            bg="#f5f5f5"
        )
        main.pack(
            side="right",
            fill="both",
            expand=True
        )

        self.content_title = tk.Label(
            main,
            text="ようこそ！",
            font=("Segoe UI", 28, "bold"),
            bg="#f5f5f5",
            fg="#202124"
        )
        self.content_title.pack(
            pady=(100, 20)
        )

        self.content_text = tk.Label(
            main,
            text=(
                "日常で使える便利機能を\n"
                "Plugin形式で追加できます。"
            ),
            font=("Segoe UI", 14),
            bg="#f5f5f5",
            fg="#5f6368",
            justify="center"
        )
        self.content_text.pack()

        version = tk.Label(
            main,
            text=f"Version {APP_VERSION}",
            font=("Segoe UI", 10),
            bg="#f5f5f5",
            fg="#80868b"
        )
        version.pack(
            pady=30
        )

        # 下部ステータス
        self.status = tk.Label(
            self.root,
            text="Ready",
            anchor="w",
            bg="#e8eaed",
            fg="#5f6368",
            padx=10
        )
        self.status.place(
            relx=0,
            rely=1,
            relwidth=1,
            anchor="sw",
            height=28
        )

    def run_plugin(self, plugin):
        self.status.config(
            text=f"実行中: {plugin.name}"
        )

        try:
            result = plugin.run()

            self.content_title.config(
                text=plugin.name
            )

            self.content_text.config(
                text=str(result)
            )

            self.status.config(
                text=f"完了: {plugin.name}"
            )

        except Exception as error:
            self.status.config(
                text=f"エラー: {plugin.name}"
            )

            messagebox.showerror(
                "Plugin Error",
                str(error)
            )

    def run(self):
        self.root.mainloop()