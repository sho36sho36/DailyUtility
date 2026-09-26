from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
PLUGIN_DIR = BASE_DIR / "plugins"


def get_base_dir():
    return BASE_DIR


def get_plugin_dir():
    return PLUGIN_DIR