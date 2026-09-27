"""bwEnc package metadata."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("bwEnc")
except PackageNotFoundError:
    __version__ = "development"
