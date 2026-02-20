from ursina import *
# Import eksplisit agar tidak NameError
from config import FOG_DENSITY, BLACK
from ui_manager import GameUI, MainMenu
from player import NightmarePlayer
import world

app = Ursina()
window.color = BLACK
window.fps_counter.enabled = False

class HeartlessEngine(Entity):
    def __init__(self):
        super().__init__()
        self.ui = GameUI(self)
        self.menu = MainMenu(self.start_game)
        self.game_active = False
        self.player = None
        self.target = None

    def start_game(self):
        destroy(self.menu)
        self.game_active = True
        self.ending_altar = world.build_level()
        self.player = NightmarePlayer()
        
        # Kurangi fog jika masih terlalu gelap
        scene.fog_density = 0.02 
        scene.fog_color = color.black
        mouse.locked = True
        mouse.visible = False

    def update(self):
        if not self.game_active or not self.player: return
        self.player.move()
        
        # Cek objek terdekat untuk interaksi
        self.target = None
        self.ui.show_hint(False)
        
        for e in scene.entities:
            if hasattr(e, 'content') or e.name == "ending_altar":
                if distance(self.player.position, e.position) < 4:
                    self.target = e
                    self.ui.show_hint(True)
                    break

    def input(self, key):
        if key == 'escape':
            self.ui.toggle_pause()
        
        # Logika tombol E (Buka/Tutup Narasi)
        if key == 'e' and self.game_active:
            if self.ui.note_panel.enabled:
                self.ui.note_panel.enabled = False
            elif self.target:
                if hasattr(self.target, 'content'):
                    self.ui.show_note(self.target.content)
                elif self.target.name == "ending_altar":
                    self.ui.show_note("AKHIR CERITA:\n\nDia hidup bahagia dengan hatimu.\n\n[TAMAT]")

engine = HeartlessEngine()
app.run()