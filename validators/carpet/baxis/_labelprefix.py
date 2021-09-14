import _plotly_utils.basevalidators


class LabelprefixValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name="labelprefix", parent_name="carpet.baxis", **kwargs):
        super(LabelprefixValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs
        )
