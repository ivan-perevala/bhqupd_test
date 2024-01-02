# BlenderHQ Blender addon update utility module test addon.
# Copyright (C) 2023 Ivan Perevala (ivpe)

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

from __future__ import annotations

bl_info = {
    "name": "BHQUPD Test 4.0.0",
    "author": "Ivan Perevala (ivpe)",
    "version": (4, 0, 0),
    "blender": (4, 0, 0),
    "support": 'COMMUNITY',
    "category": "Development",
    "doc_url": 'https://github.com/ivan-perevala/bhqupd_test',
}

from . import bhqupd

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .... import bhqupd


def register():
    pass


def unregister():
    pass
