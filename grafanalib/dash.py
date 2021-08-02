from grafanalib.core import *


dashboard = Dashboard(
    title="My python dashboard",
    annotations=Annotations(list=[]),
    description="",
    editable=True,
    gnetId=None,
    hideControls=False,
    id=118,
    inputs=[],
    links=[],
    panels=[
        RowPanel(
            dataSource=None,
            targets=[],
            title="Monitor Tracking",
            cacheTimeout=None,
            description=None,
            editable=True,
            error=False,
            height=None,
            gridPos={"h": 1, "w": 24, "x": 0, "y": 0},
            hideTimeOverride=False,
            id=3,
            interval=None,
            links=[],
            maxDataPoints=100,
            minSpan=None,
            repeat=Repeat(direction={}, variable=None, maxPerRow=None),
            span=None,
            timeFrom=None,
            timeShift=None,
            transparent=False,
            transformations=[],
            extraJson=None,
            panels=[],
        )
    ],
    refresh="10s",
    rows=[],
    schemaVersion=26,
    sharedCrosshair=False,
    style="dark",
    tags=[],
    templating=Templating(list=[]),
    time=Time(start="now-1h", end="now"),
    timePicker=TimePicker(
        refreshIntervals=[
            "5s",
            "10s",
            "30s",
            "1m",
            "5m",
            "15m",
            "30m",
            "1h",
            "2h",
            "1d",
        ],
        timeOptions=["5m", "15m", "1h", "6h", "12h", "24h", "2d", "7d", "30d"],
        hidden=False,
    ),
    timezone="utc",
    version=3,
    uid="DAR70jWnk",
)

dashboard = dashboard.auto_panel_ids()
import io
s = io.StringIO()
from grafanalib._gen import write_dashboard
write_dashboard(dashboard, s)
print("""{
"dashboard": %s
}
""" % s.getvalue())
