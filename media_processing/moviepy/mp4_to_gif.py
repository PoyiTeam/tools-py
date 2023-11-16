import moviepy.editor as mp


file_name = 'video'

video_clip = mp.VideoFileClip(f'{file_name}.mp4')
video_clip.write_gif(f'{file_name}.gif', fps=10)
