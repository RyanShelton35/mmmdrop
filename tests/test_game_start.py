from mpf.tests.MpfGameTestCase import MpfGameTestCase
from pathlib import Path

class TestGameStartModes(MpfGameTestCase):

    def get_machine_path(self):
        # Return the path to your machine folder
        return Path.cwd()

    def get_config_file(self):
        return 'config.yaml'

    def test_game_start_modes(self):
        # Simulate starting a game
        self.post_event('start_game')
        self.advance_time_and_run(1)
        
        # Hit a switch and verify score changes or events post
        self.hit_and_release_switch('s_start')
        self.advance_time_and_run(0.5)
        
        # Add assertions
        self.assertGameIsRunning()

        print("Checking for starting modes: combos, multiball, skill_shot, batterycharger, carousel, and base")
        self.assertModeRunning("combos")
        self.assertModeRunning("multiball")
        self.assertModeRunning("skill_shot")
        self.assertModeRunning("batterycharger")
        self.assertModeRunning("carousel")
        self.assertModeRunning("base")
