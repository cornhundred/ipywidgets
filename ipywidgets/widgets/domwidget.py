"""Contains the DOMWidget class"""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

from traitlets import Unicode, Instance, Bool, Tuple, default
from .widget import Widget, widget_serialization
from .trait_types import Color
from .widget_layout import Layout


class DOMWidget(Widget):
    """Widget that can be inserted into the DOM"""

    _model_name = Unicode('DOMWidgetModel').tag(sync=True)
    _dom_classes = Tuple(help="DOM classes applied to widget.$el.").tag(sync=True)
    layout = Instance(Layout).tag(sync=True, **widget_serialization)

    @default('layout')
    def _default_layout(self):
        return Layout()

    def add_class(self, className):
        """
        Adds a class to the top level element of the widget.

        Doesn't add the class if it already exists.
        """
        if className not in self._dom_classes:
            self._dom_classes = list(self._dom_classes) + [className]
        return self

    def remove_class(self, className):
        """
        Removes a class from the top level element of the widget.

        Doesn't remove the class if it doesn't exist.
        """
        if className in self._dom_classes:
            self._dom_classes = [c for c in self._dom_classes if c != className]
        return self
