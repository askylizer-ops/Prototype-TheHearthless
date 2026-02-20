from ursina import *
from config import HEART_RED, GOLD, BLACK

class GameUI(Entity):
    def __init__(self, game_manager):
        super().__init__(parent=camera.ui, z=-1)
        self.game = game_manager
        
        # 1. Interact Hint [E]
        self.interact_hint = Text(
            text='[E] INTERACT', 
            origin=(0,0), y=-0.2, scale=1.5, 
            color=GOLD, enabled=False
        )
        
        # 2. Narration Panel
        self.note_panel = Entity(parent=self, model='quad', scale=(0.8, 0.4), color=color.black90, enabled=False)
        self.note_text = Text(parent=self.note_panel, text='', origin=(0,0), scale=1.5, color=color.white)
        self.close_hint = Text(parent=self.note_panel, text='[Tekan E untuk Menutup]', y=-0.4, scale=1, color=color.gray, origin=(0,0))
        
        # 3. Pause Menu Panel
        self.pause_handler = Entity(parent=self, enabled=False)
        # Background gelap saat pause
        Entity(parent=self.pause_handler, model='quad', scale=(2, 1), color=color.black66)
        Text(parent=self.pause_handler, text='PAUSED', scale=4, origin=(0,0), y=0.15, color=GOLD)
        
        # Tombol Pause
        self.resume_btn = Button(
            parent=self.pause_handler, text='RESUME', scale=(0.25, 0.06), y=0, 
            color=color.black, highlight_color=GOLD, on_click=self.toggle_pause
        )
        self.quit_btn = Button(
            parent=self.pause_handler, text='QUIT GAME', scale=(0.25, 0.06), y=-0.08, 
            color=color.black, highlight_color=HEART_RED, on_click=application.quit
        )

    # --- FUNGSI-FUNGSI KRUSIAL ---
    def show_note(self, content):
        self.note_text.text = content
        self.note_panel.enabled = True

    def show_hint(self, state=True):
        self.interact_hint.enabled = state

    def toggle_pause(self):
        # Memastikan hanya bisa pause kalau game sudah jalan
        if not self.game.game_active: return
        
        self.pause_handler.enabled = not self.pause_handler.enabled
        application.paused = self.pause_handler.enabled
        
        # Kursor muncul saat pause
        mouse.visible = self.pause_handler.enabled
        mouse.locked = not self.pause_handler.enabled

class MainMenu(Entity):
    def __init__(self, start_call):
        super().__init__(parent=camera.ui)
        # Background Hitam Sesuai Request
        self.bg = Entity(parent=self, model='quad', scale=(2, 1), color=BLACK)
        
        self.title = Text(parent=self, text='THE HEARTLESS', scale=7, origin=(0,0), y=0.2, color=HEART_RED)
        
        self.start_btn = Button(
            parent=self, text='START JOURNEY', scale=(0.3, 0.06), y=-0.05, 
            color=color.black, highlight_color=HEART_RED, on_click=start_call
        )
        self.exit_btn = Button(
            parent=self, text='EXIT', scale=(0.3, 0.06), y=-0.13, 
            color=color.black, highlight_color=color.dark_gray, on_click=application.quit
        )