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

from    . import utils


###############################################################################
#
#   Define Default values for this module here
#
###############################################################################

#  Define the URL Locations
URL_LIST = [
    ("Report Issues", "github.com/Linkage-Design/CustomTopView/issues"),
    ("Linkage Design", "linkage-d.com"),
    ("Superhive", "superhivemarket.com/products/linkage-custom-top-view"),
    ("Gumroad", "linkagedesign.gumroad.com/l/customtopview"),
    ("YouTube", "youtube.com/LinkageDesign"),
    ("Instagram", "instagram.com/LinkageDesign")
]

#   Define a place to store and process this add-on's icon colletion.
icon_collection = utils.loadIcons()


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
        parentLayt.label(text = "Links to Websites")

        #  Create buttons for each url in the URL_LIST
        for i in range(0, len(URL_LIST), 2):
            rowLayt = parentLayt.row()
            for col in (0, 1):
                try:
                    #   Get the site and url values from URL_LIST
                    name, url = URL_LIST[i + col]
                    iconId = name.replace(' ','')

                    #   Create the button
                    op = rowLayt.operator("wm.url_open", text = name,
                             icon_value = icon_collection[iconId].icon_id)
                    op.url = f"https://{url}"

                except IndexError as e:
                    break
