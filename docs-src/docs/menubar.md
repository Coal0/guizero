# MenuBar

(Contains a `tkinter.Menu` object)

`__init__.py(self, master, toplevel, options)`

### What is it?
The `MenuBar` object displays a menu at the top of the screen, with each menu option leading to a submenu.

![MenuBar on Windows](images/menubar_windows.png)

### How do I make one?

Create a `MenuBar` object like this:

```python
from guizero import App, MenuBar
def file_function():
    print("File option")

def edit_function():
    print("Edit option")

app = App()
menubar = MenuBar(app,
                  toplevel=["File", "Edit"],
                  options=[
                      [ ["File option 1", file_function], ["File option 2", file_function] ],
                      [ ["Edit option 1", edit_function], ["Edit option 2", edit_function] ]
                  ])
app.display()
```


### Starting parameters

When you create a `MenuBar` object you **must** specify all of the parameters.

| Parameter | Takes | Default | Compulsory | Description                         |
| --------- | --------- | ------- | ---------- | -------------------------|
| master    | App   | - | Yes       | The container to which this widget belongs
| toplevel   | list    | -  | Yes         | A list of top level menu items |
| options | 3D list | - | Yes   | A list of submenus, with each submenu being a list of options and each option being a text/command pair. See notes above for more details. |

The `toplevel` parameter should be a list of options you wish to display on the menu. In the example, the `toplevel` options are File and Edit:

![Top level menu on Windows](images/toplevel_windows.png)

The options parameter should be a 3D List containing lists of submenu items, which are themselves lists. The elements in the list correspond to the elements in the `toplevel` list, so the first list of submenu items provided in `options` will be the submenu for the first menu heading provided in `toplevel` and so on.

The menu item sub-sublists within `options` should contain pairs consisting of the text to display on the menu and the function to call when that option is selected. In this example, the text "File option 1" is displayed and the function `file_function` is called if this option is clicked on.

```python
["File option 1", file_function]
```

The MenuBar is never displayed on a grid so there are no grid or alignment parameters.

### Methods

There are no methods for the `MenuBar` object

### Properties

There are no properties for the `MenuBar` object