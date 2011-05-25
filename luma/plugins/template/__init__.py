# -*- coding: utf-8 -*-
#
# Copyright (c) 2011
#     Simen Natvig, <simen.natvig@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses/
from PyQt4.QtGui import *
from base.util.IconTheme import iconFromTheme
import os.path

lumaPlugin = True
pluginName = u"template"
pluginUserString = u"Templates"
version = u"0.2"
author = u"Simen Natvig"
description = u"Used to define the templates used by the browser-plugin."


def getIcon():
    return iconFromTheme('luma-template-plugin', ':/icons/plugins/template')


def getPluginWidget(parent, mainwin):
    from .gui.TemplateWidget import TemplateWidget
    pluginWidget = TemplateWidget()
    return pluginWidget


def getPluginSettingsWidget(parent):
    return None


def postprocess():
    return


# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
