"""cx_Freeze entry point that preserves bwEnc's package-relative imports."""

from shiboken6 import Shiboken
from PySide6 import QtCore, QtGui, QtWidgets

from bwenc.main import main


if __name__ == "__main__":
    raise SystemExit(main())
