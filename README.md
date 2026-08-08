# MMB Double-Click View Selected

A tiny Blender add-on that lets you **double-click the Middle Mouse Button (MMB)** to center the 3D View on the currently selected object.

It uses Blender's built-in keymap system, so normal MMB viewport orbiting remains unchanged.

## Features

* Double-click **MMB** to use **View Selected**.
* Normal MMB orbiting continues to work.
* No modal operators or mouse-event interception.
* No external dependencies.
* Extremely lightweight.

## Installation

1. Download `mmb_double_click_view_selected.py`.
2. Open Blender.
3. Go to **Edit → Preferences → Add-ons**.
4. Select **Install from Disk...**.
5. Choose the `.py` file.
6. Enable the add-on.

## Usage

Select an object in the 3D Viewport and **double-click the Middle Mouse Button**.

The viewport will center on the current selection, equivalent to using Blender's **View Selected** command.

## Compatibility

The add-on declares **Blender 3.0.0** as its minimum supported version.

| Blender version        | Status                      |
| ---------------------- | --------------------------- |
| Blender 3.0+           | ✅ Supported                 |
| Blender 2.9x and older | ⚠️ Not officially supported |

The add-on uses Blender's standard keymap API and the built-in `view3d.view_selected` operator. It does not rely on Blender 5.0-specific functionality, so it should remain compatible with newer Blender versions unless the relevant keymap API changes.

**Blender 5.0.x is fully supported.**

## How It Works

The add-on registers a single keymap item in Blender's **add-on key configuration**:

```text
MIDDLEMOUSE + DOUBLE_CLICK → View Selected
```

Blender's keymap system handles the double-click detection itself. The add-on therefore does not need to intercept mouse input, use a modal operator, or interfere with normal viewport navigation.

## Uninstallation

Disable or remove the add-on from:

**Edit → Preferences → Add-ons**

## License

This add-on was made entirely by AI. You are free to modify, redistribute, and repackage it as you wish.

