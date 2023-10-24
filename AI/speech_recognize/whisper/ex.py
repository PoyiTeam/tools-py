# %%

import whisper


model = whisper.load_model("large-v2")

file_path = "PTC x DMG_Mocha with MikeDMG mori Full.mp3"

result = model.transcribe(file_path)
print(result["text"])
