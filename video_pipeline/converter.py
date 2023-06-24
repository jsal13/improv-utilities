import glob
from datetime import datetime
from pathlib import Path, PurePath

import ffmpeg


class Converter:
    """Convert all videos in a particular directory."""

    @staticmethod
    def _get_datetime_for_recording(input_path: Path) -> str:
        """Probe metadata for creation_time."""
        # Default to using the current datetime in isoformat.
        created_dt = datetime.now()
        try:
            probe_creation_time = (
                ffmpeg.probe(input_path)
                .get("streams")[0]
                .get("tags")
                .get("creation_time")
            )
            created_dt = datetime.strptime(probe_creation_time, "%Y-%m-%dT%H:%M:%S.%fZ")
        except AttributeError:
            pass
        except TypeError:
            pass
        except ffmpeg.Error as exc:
            raise exc

        return created_dt.strftime("%Y-%m-%d_%H%M%S")

    @staticmethod
    def _create_output_name(input_path: Path) -> PurePath:
        """Create a new file with a standard output name."""
        created_dt = Converter._get_datetime_for_recording(input_path=input_path)

        # Create new output dir if it does not exist.
        output_dir = PurePath(input_path).parent
        output_path = output_dir.joinpath("converted")
        Path(output_path).mkdir(parents=True, exist_ok=True)

        # Create new filename and place it in the output path.
        file_ext = PurePath(input_path).suffix
        new_file_name = f"ACT_LOCATION_{created_dt}{file_ext}"
        new_file_path = output_path.joinpath(new_file_name)

        return new_file_path

    @staticmethod
    def convert_file(input_path: str, logging=False) -> None:
        """
        Convert video at ``input_path``.

        Notes
        -----
        - ``sn`` refers to Subtitles being ignored or not.
            - See: https://github.com/kkroening/ffmpeg-python/issues/514
        - ``scale`` in the video filter takes -2 ("keep aspect ratio")
          and 720 (for 720p).
        """
        _input_path = Path(input_path).absolute()
        print(f"* Converting: {_input_path}")

        output_path = Converter._create_output_name(input_path=_input_path)

        # The conversion
        input_stream = ffmpeg.input(_input_path, sn=None)
        vid = input_stream.video.filter("scale", -2, 720)
        aud = input_stream.audio
        output = ffmpeg.output(
            vid,
            aud,
            filename=output_path,
            format="mp4",
            preset="slower",
            vcodec="libx264",
            acodec="aac",
            r=29.93,  # Framerate
            crf=22,  # Constant Rate Factor
        ).run_async(pipe_stdout=True, pipe_stderr=True)

        if logging:
            out, err = output.communicate()
            output_dir = PurePath(_input_path).parent
            with open(
                output_dir.joinpath("output.log"), "w+", encoding="utf-8"
            ) as elog:
                elog.write(err.decode("utf-8"))
                elog.write(out.decode("utf-8"))

        print(f"* Converted file at: {output_path}")

    @staticmethod
    def convert_all(input_path: str, logging=False) -> None:
        """Call ``convert_file`` on all files in the input path."""
        _input_path = Path(input_path).absolute()

        for movie_path in glob.glob(f"{_input_path}/*.mp4"):
            Converter.convert_file(input_path=movie_path, logging=logging)


if __name__ == "__main__":
    import sys

    Converter.convert_file(input_path=sys.argv[1], logging=True)
