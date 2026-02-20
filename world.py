from ursina import *
from config import GOLD, HEART_RED

class StoryNote(Entity):
    def __init__(self, position, content):
        super().__init__(
            model='sphere', position=position, scale=0.8, 
            color=GOLD, collider='sphere'
        )
        self.content = content
        # Lampu lokal pada bola kuning agar terlihat dari jauh
        self.point_light = PointLight(parent=self, color=GOLD, range=10)
        Entity(parent=self, model='sphere', scale=5, color=color.rgba(255,215,0,15))

def build_level():
    # Ambient Light: PENTING agar dunia tidak hitam total
    AmbientLight(color=color.rgba(100, 100, 100, 255)) 

    # Lantai: Kita turunkan sedikit ke y=-0.5 agar kaki player tidak tenggelam
    Entity(model='plane', scale=(200, 20), color=color.dark_gray, collider='box', y=-0.5)
    
    # Tembok Belakang
    Entity(model='cube', scale=(200, 30, 1), z=6, color=color.black, collider='box')
    
    # Pilar dekorasi (Diberi warna abu-abu agar terlihat)
    for x in range(0, 200, 20):
        Entity(model='cube', scale=(2, 15, 2), x=x, y=7, z=5, color=color.gray)

    notes = [
        StoryNote((15, 1, 0), "Dadaku terasa dingin.\nSeperti ada bagian yang tertinggal di kegelapan."),
        StoryNote((50, 1, 2), "Aku melihat seseorang berlari.\nDia tidak mencurinya, aku yang melepaskannya."),
        StoryNote((90, 1, -2), "Hati itu bukan milikku lagi.\nIa sudah menemukan rumah yang baru.")
    ]
    
    altar = Entity(model='cube', position=(140, 1.5, 0), scale=(3,6,3), color=HEART_RED, collider='box')
    altar.name = "ending_altar"
    return altar