from tw2.core.testbase import WidgetTest
import tw2.jqplugins.tagify

class TestWidget(WidgetTest):
    # place your widget at the TestWidget attribute
    widget = tw2.jqplugins.tagify.TagifyWidget
    # Initilization args. go here
    attrs={'id':'tagifytest'}
    params={}
    expected = """<textarea id="tagifytest" name="tagifytest"></textarea>"""
