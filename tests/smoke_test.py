#!/usr/bin/env python3
"""
Basic import test - verifies package can be imported without pytest dependency.
"""

import importlib
import sys

PACKAGE_NAME = "psd_toolkit"


def main():
    try:
        # Test basic import
        mod = importlib.import_module(PACKAGE_NAME)
        print(f"✓ Successfully imported {PACKAGE_NAME}")

        # Test version attribute
        version = getattr(mod, "__version__", None)
        if version:
            print(f"✓ Version: {version}")

        # Test dir() works
        symbols = dir(mod)
        print(f"✓ Package has {len(symbols)} public symbols")

        print(f"\n✓ All smoke tests passed for {PACKAGE_NAME}")
        return 0

    except Exception as e:
        print(
            f"✗ Failed to import {PACKAGE_NAME}: {e}", file=sys.stderr
        )
        return 1


if __name__ == "__main__":
    sys.exit(main())
