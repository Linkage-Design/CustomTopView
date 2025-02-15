import bpy
from mathutils import Quaternion
from bpy.types import Operator, Panel, PropertyGroup
from bpy.props import BoolProperty, PointerProperty

bl_info = {
    "name": "Linkage Custom Top View",
    "author": "Linkage Design",
    "version": (0, 5),
    "blender": (4, 2, 0),
    "description": "Demonstrates setting a custom oriented top view",
    "category": "Object",
}

class VIEW3D_OT_CustomTopView(Operator):
    bl_idname = "view3d.custom_top_view"
    bl_label = "Align to Custom Top View"
    bl_description = "Align the viewport to the custom top view with X axis down and Y axis right"
    bl_options = {'REGISTER', 'UNDO'}    
    
    def execute(self, context):
        for area in bpy.context.screen.areas:
            if area.type == "VIEW_3D":
                break

        for region in area.regions:
            if region.type == "WINDOW":
                break

        space = area.spaces[0]
                
        r3d = space.region_3d
        if(context.scene.view_align_props.force_ortho):
            r3d.view_perspective = "ORTHO"
        #default - look down z-axis
        r3d.view_rotation = Quaternion((0.7071068, 0, 0, 0.7071068))
        return {'FINISHED'}


class VIEW3D_PT_CustomTopViewPanel(Panel):
    bl_label = "Linkage Custom Top View"
    bl_idname = "VIEW3D_PT_custom_top_view"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Linkage'

    def draw(self, context):
        view_align_props = context.scene.view_align_props
        layout = self.layout
        row = layout.row()
        row.prop(view_align_props, "force_ortho")
        row = layout.row()
        row.operator("view3d.custom_top_view", icon='CAMERA_DATA')

class TopViewProperties(PropertyGroup):
    force_ortho: BoolProperty(name="Force Orthographic View", default=True)
    
classes = [
    VIEW3D_PT_CustomTopViewPanel,
    VIEW3D_OT_CustomTopView,
    TopViewProperties,
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    
    bpy.types.Scene.view_align_props = PointerProperty(type=TopViewProperties)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    if bpy.types.Scene.view_align_props:
        del bpy.types.Scene.view_align_props

if __name__ == "__main__":
    register()