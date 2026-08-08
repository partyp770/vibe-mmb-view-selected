bl_info = {
    "name": "MMB Double-Click View Selected",
    "author": "ChatGPT",
    "version": (1, 0, 0),
    "blender": (3, 0, 0),
    "location": "3D View",
    "description": "Centers the 3D View on the current selection when the Middle Mouse Button is double-clicked.",
    "category": "3D View",
}

import bpy


addon_keymaps = []


def register():
    # Use the add-on keyconfig so the user's normal Blender keymap is not modified.
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon

    if kc is None:
        return

    km = kc.keymaps.new(
        name="3D View",
        space_type="VIEW_3D",
        region_type="WINDOW",
    )

    # Blender's keymap system natively supports DOUBLE_CLICK, so we do
    # not need to intercept MMB or run a modal operator. Normal MMB
    # orbiting remains intact.
    kmi = km.keymap_items.new(
        "view3d.view_selected",
        "MIDDLEMOUSE",
        "DOUBLE_CLICK",
    )

    addon_keymaps.append((km, kmi))


def unregister():
    for km, kmi in addon_keymaps:
        try:
            km.keymap_items.remove(kmi)
        except (RuntimeError, ReferenceError):
            pass

    addon_keymaps.clear()


if __name__ == "__main__":
    register()
