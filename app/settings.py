from pathlib import Path

from sdx_base.settings.app import AppSettings, get_settings

ROOT = Path(__file__).parent.parent


class Settings(AppSettings):
    project_id: str


def get_instance() -> Settings:
    return get_settings(Settings)
