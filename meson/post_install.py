#!/usr/bin/env python3
import os

prefix = os.environ.get('MESON_INSTALL_PREFIX', '/usr')
datadir = os.path.join(prefix, 'share')

PROJECT_NAME = 'org.gnome.Evince'

# Packaging tools define DESTDIR and this isn't needed for them
if 'DESTDIR' not in os.environ:
    scalable_icon = os.path.join(datadir, 'icons', 'hicolor', 'scalable', 'apps', PROJECT_NAME)
    if os.path.exists(scalable_icon):
        os.remove(scalable_icon)
