from mpf.tests.MpfGameTestCase import MpfGameTestCase

class TestStep2(MpfGameTestCase):

    def test_attract(self):
        self.assertModeRunning("attract")