import winreg


def get_installed_apps():
    apps = []

    # Check both Local Machine and Current User registries
    reg_paths = [
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
        r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
    ]

    for reg_path in reg_paths:
        try:
            reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path)
            for i in range(winreg.QueryInfoKey(reg_key)[0]):
                sub_key_name = winreg.EnumKey(reg_key, i)
                sub_key = winreg.OpenKey(reg_key, sub_key_name)
                try:
                    app_name = winreg.QueryValueEx(sub_key, "DisplayName")[0]
                    apps.append(app_name)
                except FileNotFoundError:
                    pass
                finally:
                    winreg.CloseKey(sub_key)
            winreg.CloseKey(reg_key)
        except FileNotFoundError:
            pass

    return apps


if __name__ == "__main__":
    installed_apps = get_installed_apps()
    print("Installed applications:")
    for app in installed_apps:
        print(app)
