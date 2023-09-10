import tkinter as tk
import typing

def create_widget(func_data:dict):
    button = tk.Button(
        text = func_data["text"],
        command= func_data["command"]
    )
    
    button.pack(anchor=func_data["anchor"])

# Start application function
def start_app(widget_metadata:typing.Iterable[dict],**kwargs):
    """
    Args:
    --------
        * widget_funcs: List of widget functions alongwith their display text & 
        anchor positions.
        * kwargs["title"]: App window title
        * kwargs["geometry]: App window size (e.g. "800x600")
    """


    root_window = tk.Tk()
    # Set window title & geometry
    root_window.title(kwargs["title"])
    root_window.geometry(kwargs["geometry"])

    # Create buttons with attached functionalities (i.e. widgets).
    # TODO: Generalise to accept an iterable of assembler functions, i.e. 
    # Iterable[Callable[]->dict[]] Return dict contains fields 'text', 'command', 
    # 'anchor'.
    for metadata in widget_metadata:
        create_widget(metadata)
        # Display timer status in window title.
        root_window.title(metadata["text"].split()[1:])

    # BUG: Abort timer/app if user presses close/quit. Doesn't work!
    root_window.protocol("WM_DELETE_WINDOW",root_window.destroy)

    # Create Quit button at the bottom
    quit = tk.Button(text="QUIT", fg="red",
                            command=root_window.destroy)
    quit.pack(side="bottom")

    # Display window/Start program
    root_window.mainloop()