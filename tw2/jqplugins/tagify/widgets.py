import tw2.core as twc
import tw2.forms as twf
import tw2.jquery
import tw2.jquery.base as tw2_jq_c_b
import tw2.jqplugins.ui.base as tw2_jq_ui


class Tagify(tw2_jq_ui.JQueryUIWidget, twf.TextArea):
    # declare static resources here
    # you can remove either or both of these, if not needed
    resources = [
        tw2.jquery.jquery_js,
        tw2_jq_ui.jquery_ui_js,
        tw2_jq_ui.jquery_ui_css,
        twc.JSLink(modname=__name__, filename='static/jquery.tagify.js'),
        twc.CSSLink(modname=__name__, filename='static/tagify.css'),
    ]

    def prepare(self):
        super(Tagify, self).prepare()
        self.add_call(twc.js_function("$('#"+self.selector+"').tagify")(twc.js_symbol(self.options)))
        # put code here to run just before the widget is displayed
