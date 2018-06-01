import _plotly_utils.basevalidators


class FormatsrcValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(
        self, plotly_name='formatsrc', parent_name='table.cells', **kwargs
    ):
        super(FormatsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='none',
            role='info',
            **kwargs
        )