# %% find device name
import nidaqmx
import nidaqmx.system
import nidaqmx.stream_readers
import numpy as np
from datetime import datetime
from nidaqmx.constants import AcquisitionType


SAMPLE_RATE = 12800  # sampling rate
NUM_CHANNEL = 2  # number of channel
FRAME_DURATION = 500  # ms
samples = []

system = nidaqmx.system.System.local()
print(system.driver_version)
for device in system.devices:
    print(device)

# check if device is exsit
daq_chassis_name = 'cDAQ1Mod1'
device = system.devices[daq_chassis_name]
device == nidaqmx.system.Device(daq_chassis_name)


frame_size = int(SAMPLE_RATE * FRAME_DURATION * 0.001)
task = nidaqmx.Task(new_task_name='NI9234')
task.ai_channels.add_ai_accel_chan(f'{daq_chassis_name}/ai{NUM_CHANNEL}')
task.timing.cfg_samp_clk_timing(
    rate=SAMPLE_RATE, sample_mode=AcquisitionType.CONTINUOUS)


def callback(task_handle, every_n_samples_event_type,
             number_of_samples, callback_data):
    print(datetime.now().isoformat(sep=' ', timespec='milliseconds'))
    print(f'Every {number_of_samples} Samples callback invoked')
    chunk = task.in_stream.read(number_of_samples_per_channel=2000)
    samples.extend(chunk)
    return 0


task.register_every_n_samples_acquired_into_buffer_event(
    sample_interval=2000, callback_method=callback)
task.start()

input('Running task. Press Enter to stop and see number of accumulated samples.')
print(len(samples))
