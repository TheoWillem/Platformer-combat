from cx_Freeze import setup, Executable

setup(
    name = "Platformer",
    version = "1.0",
    description = "Platformer",
    executables = [Executable("Main.py")],
)