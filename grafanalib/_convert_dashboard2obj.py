import argparse
import json
import pprint
import textwrap

import grafanalib.core

def dashboard_code(code):
    return textwrap.dedent("""
    from grafanalib.core import *\n

    dashboard = {}
    """.format(pprint.pformat(code)))

def parse_dashboard(args):
    parser = argparse.ArgumentParser(
        description="EXPERIMENTAL dashboard parser.", prog='parse-dashboard')
    parser.add_argument(
        '--output', '-o', type=os.path.abspath,
        help='Where to write the dashboard python code'
    )
    parser.add_argument(
        'dashboard', metavar='DASHBOARD', type=os.path.abspath,
        help='Path to dashboard definition',
    )
    opts = parser.parse_args(args)

    with open(opts.dashboard) as f:
        json_data = json.load(f)

        dashboard = grafanalib.core.Dashboard.parse_json_data(json_data)

    with open(opts.output, 'w') as f:
        f.write(dashboard_code(dashboard))

def _parse_dashboard(dashboard,output):
    with open(dashboard) as f:
        json_data = json.load(f)
        dashboard = grafanalib.core.Dashboard.parse_json_data(json_data)

    with open(output, 'w') as f:
        f.write(dashboard_code(dashboard))
    return dashboard

def generate_json_from_json(dashboard):
    dashboard = dashboard.auto_panel_ids()
    import io
    s = io.StringIO()
    from grafanalib._gen import write_dashboard
    write_dashboard(dashboard, s)
    print("""{
    "dashboard": %s
    }
    """ % s.getvalue())

    
import attr
@attr.s
class TestCls(object):
    """
    # b = TestCls.converter({"a":4})
    # b.printss()
    # print(b)
    """
    a = attr.ib(default=None)
    d = attr.ib(default=None)

    def printss(self):
        print(self.a)

    @classmethod
    def converter(cls,data):
        return cls(**data)
# failed
from collections import namedtuple
class TestNamedTuple(namedtuple('TestCls',["a"])):
    """   
    tnt = TestNamedTuple()
    print(tnt.isgood())
    """
    def isgood(self):
        print("Hello World")

# one func is executed several times accourding to the numbers of args count
def foreach(func):
    def inner(args):
        return [func(arg) for arg in args]
    return inner

def printhaha(haha):
    return haha+"**"
    
if __name__ == "__main__":
    # rows_dash_originpython
    d = _parse_dashboard("./dash.json","./dash.py")
    generate_json_from_json(d)
    # cls(**data) why no exception for data with other class's property

    # b = TestCls.converter({})
    # print(b)
    # b.printss()
    
   
   