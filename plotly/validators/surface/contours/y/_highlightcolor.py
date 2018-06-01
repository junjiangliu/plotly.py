import _plotly_utils.basevalidators


class HighlightcolorValidator(_plotly_utils.basevalidators.ColorValidator):

    def __init__(
        self,
        plotly_name='highlightcolor',
        parent_name='surface.contours.y',
        **kwargs
    ):
        super(HighlightcolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            role='style',
            **kwargs
        )