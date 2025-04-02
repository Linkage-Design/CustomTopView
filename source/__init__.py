################################################################################
#
#   __init__.py
#
################################################################################
#
#   DESCRIPTION
#       This add-on is used to align the view to a true orthographic top view
#
#   AUTHOR(S)
#       Josh Kirkpatrick
#       Jayme Wilkinson
#
#   CREATED
#       Oct 2024
#
################################################################################
#
#   Copyright (C) 2024 Linkage Design
#
#   The software and information contained herein are proprietary to, and
#   comprise valuable trade secrets of Linkage Design, whom intends
#   to preserve as trade secrets such software and information. This software
#   and information or any other copies thereof may not be provided or
#   otherwise made available to any other person or organization.
#
################################################################################
import  bpy
import  mathutils

from    . import prefs


################################################################################
#
#   class VIEW3D_OT_CustomTopView(bpy.types.Operator):
#
################################################################################
class VIEW3D_OT_CustomTopView(bpy.types.Operator):
    bl_idname       = "view3d.custom_top_view"
    bl_label        = "Align to Custom Top View"
    bl_description  = "Align the viewport to the custom top view with X axis down and Y axis right"
    bl_options      = {'REGISTER', 'UNDO'}

    def execute(self, context):
        '''
        DESCRIPTION
            This method is called by Blender to execute the operator. It will
            align the view to a custom top view with the X axis down and Y axis
            right.

            The view is set to orthographic if the force_ortho property is set to
            True.

        ARGUMENTS
            context     (in)    The current context from Blender

        RETURN
            {'FINISHED'}    The operator was executed successfully
            {'UNDO'}        The operator was not executed successfully
        '''
        for area in bpy.context.screen.areas:
            if area.type == "VIEW_3D":
                break

        for region in area.regions:
            if region.type == "WINDOW":
                break

        space = area.spaces[0]
        r3d = space.region_3d

        if context.scene.view_align_props.force_ortho:
            r3d.view_perspective = "ORTHO"

        r3d.view_rotation = mathutils.Quaternion((0.7071068, 0, 0, 0.7071068))

        return {'FINISHED'}


################################################################################
#
#   class VIEW3D_OT_CustomTopView(bpy.types.Panel):
#
################################################################################
class VIEW3D_PT_CustomTopViewPanel(bpy.types.Panel):
    bl_label        = "Linkage Custom Top View"
    bl_idname       = "VIEW3D_PT_custom_top_view"
    bl_space_type   = 'VIEW_3D'
    bl_region_type  = 'UI'
    bl_category     = 'Linkage Design'

    def draw(self, context):
        '''
        DESCRIPTION
            This method is called by Blender to draw a panel to display options
            for this tool.

        ARGUMENTS
            context     (in)    The current context from Blender

        RETURN
            {NONE}    The operator was executed successfully
        '''
        #   Get view_align_props from the scene context
        view_align_props = context.scene.view_align_props

        #   Create a layout for our panel
        parentLayt = self.layout

        #   Draw the elements of our panel in the layout
        row = parentLayt.row()
        row.prop(view_align_props, "force_ortho")
        row = parentLayt.row()
        row.operator("view3d.custom_top_view", icon='CAMERA_DATA')


################################################################################
#
#   class VIEW3D_OT_CustomTopView(bpy.types.PropertyGroup):
#
################################################################################
class CustomTopViewProperties(bpy.types.PropertyGroup):
    force_ortho: bpy.props.BoolProperty(name = "Force Orthographic View",
                                        default = True)


################################################################################
#
#    Funtions and data to register and unregister the classes of this Add-on
#
################################################################################
classes = [ VIEW3D_PT_CustomTopViewPanel,
            VIEW3D_OT_CustomTopView,
            CustomTopViewProperties,
            prefs.CustomTopViewPreferences ]

def register():
    '''
    DESCTIPTION
        This method is used by Blender to register the components of this
        Add-On.

    ARGUMENTS
        None

    RETURN
        None
    '''
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.view_align_props = bpy.props.PointerProperty(type = CustomTopViewProperties)


def unregister():
    '''
    DESCRIPTION
        This method is used by Blender to unregister the components we
        registered in this Add-On's register method.

    ARGUMENTS
        None

    RETURN
        None
    '''
    for cls in classes:
        bpy.utils.unregister_class(cls)

    if bpy.types.Scene.view_align_props:
        del bpy.types.Scene.view_align_props

###############################################################################
#
#   This is the main registration entrypoint for this Add-On
#
###############################################################################
if __name__ == "__main__":
    register()
