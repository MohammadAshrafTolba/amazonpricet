from app.init_app import app
from app.tracker import TrackerThread


tracking_thread = TrackerThread()
app.run()