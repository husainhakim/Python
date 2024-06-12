import tkinter as tk
import vlc

class VideoPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("VLC Video Player")

        self.instance = vlc.Instance('--no-xlib')
        self.player = self.instance.media_player_new()

        self.canvas = tk.Canvas(master, width=640, height=480)
        self.canvas.pack()

        self.media = self.instance.media_new("path_to_your_video.mp4")  # Replace with your video file path
        self.player.set_media(self.media)

        self.player.set_hwnd(self.canvas.winfo_id())

        self.play_button = tk.Button(master, text="Play", command=self.play)
        self.play_button.pack()

        self.pause_button = tk.Button(master, text="Pause", command=self.pause)
        self.pause_button.pack()

        self.stop_button = tk.Button(master, text="Stop", command=self.stop)
        self.stop_button.pack()

    def play(self):
        if not self.player.is_playing():
            self.player.play()

    def pause(self):
        if self.player.is_playing():
            self.player.pause()

    def stop(self):
        self.player.stop()

def main():
    root = tk.Tk()
    player = VideoPlayer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
