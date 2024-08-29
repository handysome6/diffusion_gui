from diffusion_gui import DiffusionGUI


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication([])

    widget = DiffusionGUI()
    widget.show()

    sys.exit(app.exec_())
