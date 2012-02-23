import tw2.core as twc
import tw2.jqplugins.tagify
from nose.tools import eq_

def request_local_tst():
    global _request_local, _request_id
# if _request_id is None:
# raise KeyError('must be in a request')
    if _request_local == None:
        _request_local = {}
    try:
        return _request_local[_request_id]
    except KeyError:
        rl_data = {}
        _request_local[_request_id] = rl_data
        return rl_data

twc.core.request_local = request_local_tst
_request_local = {}
_request_id = 'whatever'

def setup():
    twc.core.request_local = request_local_tst
    twc.core.request_local()['middleware'] = twc.make_middleware()

def test_js_call():
    w = tw2.jqplugins.tagify.TagifyWidget(id='foobar', options={'key':'value'})
    w.display()

    js_calls = filter(lambda x: "JSFuncCall" in str(x), w.resources)

    assert(len(js_calls) == 1)

    for js_call in js_calls:
        print js_call.src
        eq_(js_call.src, """$('#foobar').tagify({\\"key\\": \\"value\\"})""")
