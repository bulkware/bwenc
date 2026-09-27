"""bwEnc package metadata."""

from importlib.metadata import PackageNotFoundError, version


try:
    __version__ = version("bwEnc")
except PackageNotFoundError:
    # A checkout can run before an editable installation has created dist-info.
    __version__ = "development"
