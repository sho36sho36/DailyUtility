from pathlib import Path
import importlib.util
import sys


class PluginManager:
    def __init__(self):
        self.plugins = []
        self.plugin_directory = self.get_plugin_directory()

    def get_plugin_directory(self):
        """
        Pluginフォルダの場所を取得する。

        通常のPython実行:
            プロジェクト/plugins/

        EXE実行:
            EXEと同じ場所/plugins/
        """

        if getattr(sys, "frozen", False):
            # PyInstallerでEXE化された場合
            base_dir = Path(sys.executable).resolve().parent
        else:
            # Pythonから直接実行した場合
            base_dir = Path(__file__).resolve().parent

        return base_dir / "plugins"

    def load_plugins(self):
        self.plugins.clear()

        if not self.plugin_directory.exists():
            print(
                f"[Plugin] Plugin directory not found: "
                f"{self.plugin_directory}"
            )
            return

        for plugin_file in self.plugin_directory.glob("*.py"):

            if plugin_file.name.startswith("_"):
                continue

            try:
                plugin = self.load_plugin_file(plugin_file)

                if plugin is not None:
                    self.plugins.append(plugin)

                    print(
                        f"[Plugin] Loaded: "
                        f"{plugin.name}"
                    )

            except Exception as error:
                print(
                    f"[Plugin Error] "
                    f"{plugin_file.name}: {error}"
                )

    def load_plugin_file(self, plugin_file):
        module_name = (
            f"dailyutility_plugin_"
            f"{plugin_file.stem}"
        )

        spec = importlib.util.spec_from_file_location(
            module_name,
            plugin_file
        )

        if spec is None or spec.loader is None:
            return None

        module = importlib.util.module_from_spec(spec)

        spec.loader.exec_module(module)

        plugin_class = getattr(
            module,
            "Plugin",
            None
        )

        if plugin_class is None:
            return None

        return plugin_class()

    def get_plugins(self):
        return self.plugins

    def get_plugin(self, name):
        for plugin in self.plugins:
            if plugin.name == name:
                return plugin

        return None