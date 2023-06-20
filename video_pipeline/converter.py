import glob
import sys
from pathlib import Path, PurePath

import ffmpeg


class DirectoryConverter:
    """Convert all videos in a particular directory."""

    def __init__(self, input_dir: str):
        """Convert input video to instagram-supported video."""
        self.input_dir = PurePath(input_dir)

    def _create_file_output_name(self, input_path: str) -> PurePath:
        """Create a new file with a standard output name."""
        try:
            created_dt = (
                ffmpeg.probe(input_path)
                .get("streams")[0]
                .get("tags")
                .get("creation_time")
            )
            created_dt = created_dt.replace(":", "")
        except:  # This is for testing.
            created_dt = "111222333"

        file_ext = input_path.suffix

        output_path = self.input_dir.joinpath("converted")
        Path(output_path).mkdir(parents=True, exist_ok=True)

        new_file_name = f"ACT_LOCATION_{created_dt}{file_ext}"
        new_file_path = output_path.joinpath(new_file_name)

        return new_file_path

    def convert_file(self, input_path: str) -> None:
        """Convert ``input_path`` to video at ``output_path``."""
        output_path = self._create_file_output_name(input_path=input_path)

        # cmd_str = f"""
        #     ffmpeg
        #     -i {self.input_path}
        #     -vf scale=-2:720
        #     -c:v libx264
        #     -profile:v main
        #     -level:v 3.0
        #     -x264-params scenecut=0:open_gop=0:min-keyint=72:keyint=72
        #     -c:a aac
        #     -preset slow
        #     -crf 23
        #     -r 29.93
        #     -sn
        #     -f mp4
        #     {self.output_path}
        # """
        # cmd = shlex.split(cmd_str)
        # subprocess.Popen(cmd, stdout=subprocess.PIPE)

        print(f"* Converted file at: {output_path}")

    def convert_all(self) -> None:
        """Call ``convert_file`` on all files in the input path."""
        for input_path in glob.glob(f"{self.input_dir}/*.txt"):
            self.convert_file(input_path=input_path)


if __name__ == "__main__":
    conv = DirectoryConverter(input_dir=sys.argv[1])
    conv.convert_all()
