import importlib
import pkgutil
import plugins


class PluginManager:
    def __init__(self):
        self.plugins = []

    def load_plugins(self):
        self.plugins.clear()

        for module_info in pkgutil.iter_modules(plugins.__path__):
            module_name = module_info.name

            if module_name.startswith("_"):
                continue

            try:
                module = importlib.import_module(
                    f"plugins.{module_name}"
                )

                plugin_class = getattr(module, "Plugin", None)

                if plugin_class is None:
                    continue

                plugin = plugin_class()
                self.plugins.append(plugin)

            except Exception as error:
                print(
                    f"[Plugin Error] "
                    f"{module_name}: {error}"
                )

    def get_plugins(self):
        return self.plugins

    def get_plugin(self, name):
        for plugin in self.plugins:
            if plugin.name == name:
                return plugin

        return None