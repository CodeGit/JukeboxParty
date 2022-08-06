from django.test import TestCase
from django.conf import settings
from jukeboxparty.models import Genre, Tag, Musician, Alias, Album, Music, AudioFile, User, Rating
from pathlib import Path

class AudioFileTestCase(TestCase):
    def setUp(self) -> None:
        self.test_data = Path(settings.BASE_DIR, "tests", "data")
        return super().setUp()
    
    def test_AudioFile_creation(self):
        mp3_uri = Path.joinpath(self.test_data, "file_example_MP3_1MG.mp3").as_uri()
        mp4_uri = Path.joinpath(self.test_data, "file_example_MP4_480_1_5MG.mp4").as_uri()
        ogg_uri = Path.joinpath(self.test_data, "file_example_OGG_480_1_7mg.ogg").as_uri()
        svg_uri = Path.joinpath(self.test_data, "file_example_SVG_20kB.svg").as_uri()
        wav_uri = Path.joinpath(self.test_data, "file_example_WAV_1MG.wav").as_uri()
        pdf_uri = Path.joinpath(self.test_data, "file-sample_150kB.pdf").as_uri()

        mp3 = AudioFile.objects.create(path=mp3_uri)
        ogg =AudioFile.objects.create(path=ogg_uri)
        wav = AudioFile.objects.create(path=wav_uri)
        mp4 = AudioFile.objects.create(path=mp4_uri)
        svg = AudioFile.objects.create(path=svg_uri)
        pdf = AudioFile.objects.create(path=pdf_uri)


 