import queue
import pyaudio

from constants import RATE, CHUNK


class MicrophoneStream:

    def __init__(self: object, rate: int = RATE, chunk: int = CHUNK) -> None:
        self._rate = rate
        self._chunk = chunk

        self._buff = queue.Queue()
        self.closed = True

    def __enter__(self: object) -> object:
        self._audio_interface = pyaudio.PyAudio()
        self._audio_stream = self._audio_interface.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=self._rate,
            input=True,
            frames_per_buffer=self._chunk,
            stream_callback=self._fill_buffer,
        )

        self.closed = False

        return self

    def __exit__(
            self: object,
            type: object,
            value: object,
            traceback: object,
    ) -> None:
        """Closes the stream, regardless of whether the connection was lost or not."""
        self._audio_stream.stop_stream()
        self._audio_stream.close()
        self.closed = True
        self._buff.put(None)
        self._audio_interface.terminate()

    def _fill_buffer(
            self: object,
            in_data: object,
            frame_count: int,
            time_info: object,
            status_flags: object,
    ) -> object:
        self._buff.put(in_data)
        return None, pyaudio.paContinue

    def generator(self: object) -> object:
        while not self.closed:
            # Use a blocking get() to ensure there's at least one chunk of
            # data, and stop iteration if the chunk is None, indicating the
            # end of the audio stream.
            chunk = self._buff.get()
            if chunk is None:
                return
            data = [chunk]

            while True:
                try:
                    chunk = self._buff.get(block=False)
                    if chunk is None:
                        return
                    data.append(chunk)
                except queue.Empty:
                    break

            yield b"".join(data)
