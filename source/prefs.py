#!/usr/bin/env python3
# -*- coding: utf-8 -*-
################################################################################
#
#   prefs.py
#
################################################################################
#
#   DESCRIPTION
#       This file contains the preferences class for this Blender Add-On.
#
#   AUTHOR
#       Jayme Wilkinson
#
#   CREATED
#       Apr 02, 2025
#
################################################################################
#
#   Copyright (C) 2025 Linkage Design
#
#   The software and information contained herein are proprietary to, and
#   comprise valuable trade secrets of Linkage Design, whom intends
#   to preserve as trade secrets such software and information. This software
#   and information or any other copies thereof may not be provided or
#   otherwise made available to any other person or organization.
#
################################################################################
import  bpy

###############################################################################
#
#   Custom Top View Addon Preferences Class
#
###############################################################################
class CustomTopViewPreferences(bpy.types.AddonPreferences):
    bl_idname       = __package__
    bl_label        = "Custom Top View"
    bl_description  = "Preferences for the Custom Top View Add-on"

    def draw(self, context):
        '''
        DESCRIPTION
            This method draws the user interface for this add-on preferenses. This
            ui lives in the add-ons section of the user's preference window

        ARGUMENTS
            context     (in)    A Blender context to get some info from.

        RETURN
            None
        '''
        #   Create a parent layout for our preference panels
        parentLayt = self.layout

        #   Create a new label for the website buttons
        parentLayt.label(text = "Custom Top View Settings")

        #  Create buttons for each url in the URL_LIST
        rowLayt = parentLayt.row()

        #   Create the button for the user to report an issue or request a feature
        op = rowLayt.operator("wm.url_open", text = "Report Issues / Request Feature", icon = "URL")
        op.url = "https://www.github.com/Linkage-Design/CustomTopView/issues"
