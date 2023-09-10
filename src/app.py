import backend as be
import tk_utils as tku

timers_metadata = be.assemble_timers()
tku.start_app(timers_metadata,title="Pomodoro",geometry="800x600")
