from ursina import *
from config import MOVE_SPEED, SPRINT_SPEED, JUMP_HEIGHT, GRAVITY

class NightmarePlayer(Entity):
    def __init__(self):
        super().__init__(
            model='cube', color=color.light_gray, scale=(0.6, 1.2, 0.6), 
            position=(0, 1, 0), collider='box'
        )
        # Setup Kamera awal
        self.camera_offset = Vec3(0, 8, -22)
        camera.position = self.position + self.camera_offset
        camera.rotation_x = 20
        
        # Lampu Senter Player (Lebih terang)
        self.light = PointLight(parent=self, y=3, color=color.white, range=20)
        
        self.velocity_y = 0
        self.is_grounded = True

    def move(self):
        if application.paused: return
        
        speed = SPRINT_SPEED if held_keys['shift'] else MOVE_SPEED
        move_dir = Vec3(held_keys['d'] - held_keys['a'], 0, held_keys['w'] - held_keys['s']).normalized()
        self.position += move_dir * speed * time.dt
        
        # Batas gerak depan-belakang
        self.z = clamp(self.z, -4, 4)

        # Gravitasi
        self.velocity_y -= GRAVITY * time.dt
        self.y += self.velocity_y * time.dt
        
        if self.y <= 1:
            self.y = 1
            self.velocity_y = 0
            self.is_grounded = True

        if held_keys['space'] and self.is_grounded:
            self.velocity_y = JUMP_HEIGHT
            self.is_grounded = False

        # Kamera Smoothing (dipercepat agar tidak tertinggal)
        camera.position = lerp(camera.position, self.position + self.camera_offset, 6 * time.dt)