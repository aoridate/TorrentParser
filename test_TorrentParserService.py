import unittest
from TorrentParserService import TorrentParser


class TestParseTrackerUrl(unittest.TestCase):
    def setUp(self):
    	self.parser = TorrentParser('test_data/file_1.torrent')

    def test_no_anomaly(self):

        result = self.parser.parse_tracker_url()
        expected = 'http://tracker001.clearbits.net:7070/announce'
        self.assertEqual(result, expected)