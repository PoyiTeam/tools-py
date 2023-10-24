import av

input_container = av.open(
    'to be continued.mp4')
input_stream = input_container.streams.get(audio=0)[0]

output_container = av.open('to be continued.mp3', 'w')
output_stream = output_container.add_stream('mp3')

for frame in input_container.decode(input_stream):
    frame.pts = None
    for packet in output_stream.encode(frame):
        output_container.mux(packet)

for packet in output_stream.encode(None):
    output_container.mux(packet)

output_container.close()
