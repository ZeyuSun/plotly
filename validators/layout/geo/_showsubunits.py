import _plotly_utils.basevalidators


class ShowsubunitsValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name="showsubunits", parent_name="layout.geo", **kwargs):
        super(ShowsubunitsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            **kwargs
        )