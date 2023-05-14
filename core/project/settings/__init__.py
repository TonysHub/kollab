from pathlib import Path

from split_settings.tools import include, optional

# BASE_DIR = Kollab
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

LOCAL_SETTINGS_PATH = str(BASE_DIR / "local/settings.dev.py")

include(
    # first load django settings
    "base.py",
    # then load our own custom settings
    "custom.py",
    # then load local settings
    optional(LOCAL_SETTINGS_PATH),
    # look for system environment variables
    # 'envvars.py',
    "docker.py",
)
