#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Life's pathetic, have fun ♡~ Nasy.

Excited without bugs::

    O._.O
    ((=)) +1s

* author: Nasy
* date: Jul 26, 2017
* email: sy_n@me.com
* file: incremental_update.py
* license: MIT

Aim:
    Compare the files in the two folders, the B folder than the A folder more
    files, put these files into a separate folder C. If files already in C
    folder, pass it.

Why this:
    A friend of mine wants to do this.

Copyright © 2017 by Nasy. All Rights Reserved.
"""
import os
import shutil


def incremental_update(a_folder_path: str,
                       b_folder_path: str,
                       c_folder_path: str) -> None:
    """Incremental update.

    Args:
        a_folder_path (str): A folder path.
        b_folder_path (str): B folder path.
        c_folder_path (str): C folder path.

    Returns:
        None
    """
    # Compare files between 3 folders.
    c_files = (set(os.listdir(a_folder_path)) - set(os.listdir(b_folder_path))
               - set(os.listdir(c_folder_path)))

    if not os.path.isdir(c_folder_path):
        os.mkdir(c_folder_path)

    def _copy(f_path: str) -> None:
        """Copy file from B to C.

        Args:
            f_path: str. The file in B folder.
        """
        shutil.copy(
            os.path.join(b_folder_path, f_path),
            os.path.join(c_folder_path, f_path))

    for f_path in c_files:
        _copy(f_path)


if __name__ == "__main__":
    incremental_update("A", "B", "C")
