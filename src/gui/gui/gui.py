# Copyright (C) 2020 Respyrator
# This file is part of Respyrator <https://respyrator.github.io>.
#
# Respyrator is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Respyrator is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Respyrator.  If not, see <http://www.gnu.org/licenses/>.

# Built-in --------------------------------------------------------------------
# Installed -------------------------------------------------------------------
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, NoTransition
# Coded -----------------------------------------------------------------------
# Program ---------------------------------------------------------------------


class GuiManager(ScreenManager):
    pass


class GuiApp(App):

    def build(self):
        from kivy.uix.button import Button
        return Button(text='Hola mundo')


if __name__ == "__main__":
    GuiApp().run()