import importlib
import pkgutil
import types
import pytest

"""
Basic smoke test to ensure the psd_toolkit package imports without errors.
Add lightweight, fast checks only.
"""


PACKAGE_NAME = "psd_toolkit"


def test_package_import():
    mod = importlib.import_module(PACKAGE_NAME)
    assert isinstance(mod, types.ModuleType)


@pytest.mark.parametrize(
    "finder, name, ispkg", list(pkgutil.iter_modules())
)
def test_submodule_discovery(name):
    # Only test submodules that start with the package prefix
    if not name.startswith(
        PACKAGE_NAME.split("_")[0]
    ):  # loose prefix match
        pytest.skip("Not part of psd_toolkit namespace")
    try:
        importlib.import_module(name)
    except Exception as e:
        pytest.fail(f"Failed to import submodule {name}: {e}")


def test_version_attribute():
    mod = importlib.import_module(PACKAGE_NAME)
    version = getattr(mod, "__version__", None)
    assert version is None or isinstance(version, str)


def test_help_dir_runs():
    mod = importlib.import_module(PACKAGE_NAME)
    # Ensure dir() does not raise and returns a non-empty list
    symbols = dir(mod)
    assert isinstance(symbols, list)
    assert len(symbols) > 0
