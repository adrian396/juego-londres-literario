@namespace
class SpriteKind:
    Barrera = SpriteKind.create()
    Boss = SpriteKind.create()
    Barrera2 = SpriteKind.create()
    Barrera_3 = SpriteKind.create()
    Soldado1 = SpriteKind.create()
    Soldado = SpriteKind.create()
    Comida = SpriteKind.create()
    libro = SpriteKind.create()
    libro2 = SpriteKind.create()
    libro3 = SpriteKind.create()
    libro4 = SpriteKind.create()
    libro5 = SpriteKind.create()
    enemy_AVION = SpriteKind.create()
    oso = SpriteKind.create()
    jack_boss = SpriteKind.create()
    bubrbuja_ = SpriteKind.create()
    decoración = SpriteKind.create()
    ballesta = SpriteKind.create()
    flecha = SpriteKind.create()
    barrera6 = SpriteKind.create()
    jack = SpriteKind.create()
    cuchillo = SpriteKind.create()
    cuchillo_lluvia = SpriteKind.create()
    alma_ = SpriteKind.create()
    cuerpo = SpriteKind.create()
    cuerpo2 = SpriteKind.create()
    cuerpo3 = SpriteKind.create()
    cuerpo4 = SpriteKind.create()
    cuerpo5 = SpriteKind.create()
    sospechoso4 = SpriteKind.create()
    sospechoso3 = SpriteKind.create()
    sospechoso2 = SpriteKind.create()
    sospechoso1 = SpriteKind.create()
    Sherlock = SpriteKind.create()
    victima = SpriteKind.create()
    B1 = SpriteKind.create()
    B2 = SpriteKind.create()
    B3 = SpriteKind.create()
    B4 = SpriteKind.create()
    B5 = SpriteKind.create()
    B6 = SpriteKind.create()
    muro = SpriteKind.create()
    muro4 = SpriteKind.create()
    cuchillo_asesino = SpriteKind.create()
    reina = SpriteKind.create()
    reina_boss = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    sprite.destroy(effects.bubbles, 50)
    info.change_life_by(1)
sprites.on_overlap(SpriteKind.Comida, SpriteKind.player, on_on_overlap)

def on_on_overlap2(sprite, otherSprite):
    otherSprite.destroy()
    nivel6()
sprites.on_overlap(SpriteKind.player, SpriteKind.libro5, on_on_overlap2)

def on_on_overlap3(sprite, otherSprite):
    global pito_de_caballo, alma
    sprite.destroy()
    otherSprite.destroy(effects.star_field, 1)
    pito_de_caballo += 1
    alma = sprites.create(img("""
            . . c c c c c c . . . . . 
                    . c c c c c c c c . . . . 
                    b c c c c c c c b c . . . 
                    c b b c c c b b c c . . . 
                    c 2 2 b c b 2 2 c c . . . 
                    c c 2 c c c 2 c c c . . . 
                    c c c c c c c c c c . . . 
                    b b c b c b c b b c . . . 
                    c b b c b c b b c c . . . 
                    c c c c c c c c c c c . . 
                    c c c c c c c c c c c . . 
                    . c c c c c c c c c c . . 
                    . c c c c c c c c c c . . 
                    . . c c c c c c c c c c . 
                    . . . c c c c c c c c c . 
                    . . . . . c c c c c c c . 
                    . . . . . . . . . . c c c
        """),
        SpriteKind.alma_)
    alma.set_position(240, 87)
    if pito_de_caballo == 1:
        alma.follow(J1, 35)
    if pito_de_caballo == 2:
        alma.follow(J1, 45)
    if pito_de_caballo == 3:
        alma.follow(J1, 60)
    if pito_de_caballo == 4:
        alma.follow(J1, 82.5)
    if pito_de_caballo == 5:
        alma.follow(J1, 100)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.cuerpo2, on_on_overlap3)

def on_on_overlap4(sprite, otherSprite):
    global puntos
    otherSprite.destroy(effects.bubbles, 1)
    puntos += 1
sprites.on_overlap(SpriteKind.player, SpriteKind.bubrbuja_, on_on_overlap4)

def on_on_overlap5(sprite, otherSprite):
    global puntos
    otherSprite.destroy(effects.fire, 50)
    info.change_life_by(-1)
    puntos += 1
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy_AVION, on_on_overlap5)

def on_on_overlap6(sprite, otherSprite):
    oso2.x += -3
sprites.on_overlap(SpriteKind.player, SpriteKind.oso, on_on_overlap6)

def sospechoso4_mov():
    sospechoso_negro.set_velocity(150, 0)
    pause(1000)
    sospechoso_negro.set_velocity(0, 0)

def on_on_overlap7(sprite, otherSprite):
    otherSprite.destroy(effects.cool_radial, 1)
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.flecha, on_on_overlap7)

def nivel4():
    global Libros, sí, pingo, whenbut, sherlock, sospechoso_josuke, culpable, sospechoso_negro, sospechoso_fumador, victima2, b1, b2, b3, b4, b5, b6, muro1, muro2, muro3, muro42
    game.splash("NIVEL 4:", "\"Sherlock Holmes\"")
    game.show_long_text("Junto con el archiconocido Sherlock Holmes, encuentra al culpable de un asesinato en Hyde Park",
        DialogLayout.BOTTOM)
    J1.set_position(20, 80)
    info.set_score(3)
    info.change_score_by(1)
    Libros += 1
    info.set_life(5)
    sí += 10
    pingo = 0
    whenbut = 0
    tiles.set_tilemap(tilemap("""
        level_23
    """))
    scene.set_background_image(img("""
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999977999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999777999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999777779999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999997777779999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999777777777999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999997777777777799999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999977777777777779999999999999999999999999999999977999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999777777777777779999999999999999999999999977777777779999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999777777777777779999999999999999999999977777777777777999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999997777777777777779999999999999999999999977777777777777799
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999997777799999977777777777777779777799999999999999977777777777777777779
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999977777779999777777777777777777777777779999999997777777777777777777779
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999777777777777777777777777777777777777777779999977777777777777777777777
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999997777777777777777777777777777777777777777777777777777777777777777777777
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999997777777777777777777777777777777777777777777777777777777777777777777777777
                9999999999999999999999999999999999999999999999999999999999999999999999999977797779997777777777777777777777777777777777777777777777777777777777777777777777777777
                9999999999999999999999999999999999999999999999999999997799999999999999999777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                9999999999999999999999999999999999999999999999999997777777777999999999977777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                9999999999999999999999999999999999997777799999999777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                9999999999999999999999999999999999977777799999977777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                9999999999999999999999999999999999977777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                9999999999999999999999999999999999777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                9999999999999999999999999999999977777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                9999999999999999999999999999977777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                9999999999999977777777779977777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                9999999999999777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                dd99999999977777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                dd99999999777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                dd99999997777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                dd99999977777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                dd99999777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                ddd9997777779777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                ddd9779777797777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                ddd7777977797777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                ddd7777977797777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                dd77777977797777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                d777777977797777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                d777777977797777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                7777777977977777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                7777777797977777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                7777777797977777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                6666666696967777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                6666666696966666666666666666666666777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                6666666696966666666666666666666666666666666666666666677777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                6666666696966666666666666666666666666666666666666666666666666666667777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                6666666669666666666666666666666666666666666666666666666666666666666666666666677777777777777777777777777777777777777777777777777777777777777777777777777777777777
                6666666669666666666666666666666666666666666666666666666666666666666666666666777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                6666666669666666666666666666666666666666666666666666666666666666666666666666777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                6666666669666666666666666666666666666666666666666666666666666666666666666667777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                6666666669666666666666666666666666666666666666666666666666666666666666666677777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                6666666669666666666666666666666666666666666666666666666666666666666666667777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                66666666666666666666666666666666666666666666666666666666666666666666667777777777777777777777777777777777777777777777777777777777777777777777777777777777777777bb
                66666666666666666666666666666666666666666666666666666666666666666666777777777777777777777777777777777777777777777777777777777777777777777777777777777777777bbb77
                6666666666666666666666666666666666666666666666666666666666666666666677777777777777777777777777777777777777777777777777777777777777777777777777777777777bbbb77b77
                6666666666666666666666666666666666666666666666666666666666666666667777777777777777777777777777777777777777777777777777777777777777777777777777777777bbb777b77b77
                6666666666666666666666666666666666666666666666666666666666667777777777777777777777777777777777777777777777777777777777777777777777777777777777777bbb77b777b77b77
                666666666666666666666666666666666666666666666666666666666666777777777777777777777777777777777777777777777777777777777777777777777777777777bbbbbbb77b77b777b77bbb
                6666666666666666666666666666666666666666666666666666666666777777777777777777777777777777777777777777777777777777777777777777777bbbbbbbbbbb77b77b777b77b777bbbbee
                66666666666666666666666666666666666666666666666666666666777777777777777777777777777777777777777777777777777777777777bbbbbbbbbbbb777b77b77b77b77b777b77b7bbbeeeee
                666666666666666666666666666666666666666666666666666666677777777777777777777777777777777777777777777777777bbbbbbbbbbb77b77b77b77b777b77b77b77b77b777b7bbbeeeeeeee
                6666666666666666666666666666666666666666666666667777777777777777777777777777777777777777777777bbbbbbbbbbb7b77b777b7777b77b77b77b777b77b77b77b77b77bbbeeeeeeeeeee
                66666666666666666666666666666666666666666666667777777777777777777777777777777777777bbbbbbbbbbb777b777b7777b77b777b7777b77b77b77b777b77b77b77b77bbbeeeeeeeeeeeeee
                6666666666666666666666666666666666667777777777777777777777777777777777777bbbbbbbbbb77b777b77b7777b777b7777b77b777b7777b77b77b77b777b77b7bbbbbbbeeeeeeeeeeeeeeeee
                66666666666666666666667777777777777777777777777777777777777777bbbbbbbbbbb77b7777b7777b777b77b7777b777b7777b77b777b7777b77b77bbbbbbbbbbbbeeeeeeeeeeeeeeeeeeeeeeee
                666666667777777777777777777777777777777777777777777bbbbbbbbbbb77b777b77b777b7777b7777b777b77b7777b777b7777b77b77bbbbbbbbbbbbeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeee
                7777777777777777777777777777777777777777bbbbbbbbbbb77b77b7b77b77b777b77b777b7777b7777b777b77b7777b777bbbbbbbbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eee4eeeeee
                77777777777777777777777777777bbbbbbbbbbb777b777b77777b77b7b77b77b777b77b777b7777b7777b777bbbbbbbbbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4eeee4444eeeeee
                777777777777777777bbbbbbbbbbb77b777b777b777b777b77777b77b7b77b77b777b77b777b7bbbbbbbbbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee444eeee44444eee4eeeeee
                7777777bbbbbbbbbbb77b7777b77b77b777b777b777b777b77777b77b7b77b77b7bbbbbbbbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4eee44ee4eeee4444eeeeee
                bbbbbbb77b777b77b777b7777b77b77b777b777b777b777b77777bbbbbbbbbbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444444444444eee4eeeeee
                7b777b777b777b77b777b7777b77b77b777b777b77bbbbbbbbbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee444444444eeeeee4eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4e44eeee4444444444eeeeee
                7b777b777b777b77b777b7777b77b77bbbbbbbbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4eeeeeee444444444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4eee44ee4eeeeee4e4eeeeee
                7b777b777b777b77b77bbbbbbbbbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444444eeeeeeee4eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444444444eeeeee7
                7b777b7bbbbbbbbbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4eeeeeee44444444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4eeeeee4eeeeeee77
                bbbbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee444444444eeeeeee4eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4eeeeeeeeeeeeee777
                eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeee4eeeeeeeee444eee4eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4eeeeeeeeeee777777
                eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4eeee4444eeeeee4444444444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee7777777777
                eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4eeeeee4444444444eee4eeee4eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee777777777777777
                eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444444ee4eeeeeeeeee444444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee777777777777777777777777
                eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4ee44eeee4eeee4444444444ee4eeeeeeeeeeeeeeeeeeeeeeeeeeeeee77777777777777777777777777777
                eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4eeee44ee44444eeeeeee44444eeeeeeeeeeeeeeeeeeeeeeee777777777777777777777777777777777777
                eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4eeeeee4e4eeee44444444eee4eeeeeeeeeeeeeeeeeeeeee77777777777777777777777777777777777777
                eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4eeeeeeee444444eeeeeee4eee4eeeeeeeeeeeeeeeeee777777777777777777777777777777777777777777
                eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4eeeeeeee4eeeeeeeeeeeeeeee4eeeeeeeeeeee777777777777777777777777777777777777777777777777
                eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4eeeeeee4eeeeeeeeeeeeeeeeeeeeee77777777777777777777777777777777777777777777777777777777
                eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4eeeeeeeeeeeeeeeeeee77777777777777777777777777777777777777777777777777777777777
                eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4eeeeeeeeeeeeeeeee7777777777777777777777777777777777777777777777777777777777777
                eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee77777777777777777777777777777777777777777777777777777777777777777
                eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee777777777777777777777777777777777777777777777777777777777777777777777777
                eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                eeeeeeeeeeeeeeeeeeeeeeee7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                eeeeeeeeeeeeeee7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    """))
    jack_the_ripper.destroy()
    flecha2.destroy()
    sherlock = sprites.create(img("""
            . . . . . f f . . . . . . . . . 
                    . . . . f . . f . . . . . . . . 
                    . . . . . f f f f . . . . . . . 
                    . . . . f f e e e f . . . . . . 
                    . . . . f e f e e e f . . . . . 
                    . . f f f e e f e e e f . . . . 
                    . f e e f e e f e e e f . . . . 
                    . . f f f f f f f f f f . . . . 
                    . . . f d d d d d d f . . . . . 
                    . . . f d d f d f d f . . . . . 
                    . . . f d d d d d d f . . e . . 
                    . . . . f f f f f f . . e 9 e . 
                    . . . f e e 1 e e f . . e e . . 
                    . . f f e e 1 e e f f e . . . . 
                    . . . f e e f e e f . . . . . . 
                    . . . . f f . f f . . . . . . .
        """),
        SpriteKind.Sherlock)
    sherlock.set_position(140, 105)
    sospechoso_josuke = sprites.create(img("""
            . f f f f f f . . . . . f f f f 
                    f f f f f f f f . . . . f e e f 
                    f f f f f f f f f . . . f e e f 
                    f f f f f f f f f f f f f e e f 
                    . f f f f f f f f f f f f e e f 
                    . . f d d d d d d d f f f e f f 
                    . . f 9 1 d d d 1 1 d f f e f . 
                    . . f 6 1 1 d 6 1 1 d f f e f . 
                    . . f d d d d d d d d d f f f . 
                    . . . f f f f f f f f f f f . . 
                    . . f 8 f f 5 5 5 f f d d f . . 
                    . . f 8 f 8 f 5 f 8 f 8 f f . . 
                    . . f d f 8 f 8 f 8 f f f . . . 
                    . . . f f f 8 8 8 f f . . . . . 
                    . . . . f 8 8 f 8 8 f . . . . . 
                    . . . . . f f . f f . . . . . .
        """),
        SpriteKind.sospechoso1)
    sospechoso_josuke.set_position(165, 105)
    culpable = sprites.create(img("""
            . . f f f f f f f f . . 
                    . f d d d d d d d d f . 
                    . f d 7 1 d d 7 1 d f . 
                    . f d d d d d d d d f . 
                    . f d d f f f d d d f . 
                    . . f d d d d d d f . . 
                    . . f f f f f f f f . . 
                    . f f 1 5 d d 5 1 f f . 
                    f d f 1 5 1 1 5 1 f d f 
                    f d f f 1 5 5 1 f f d f 
                    f d f f 1 1 1 1 f f d f 
                    . f . f 8 8 8 8 f . f . 
                    . . . f 8 8 8 8 f . . . 
                    . . . f 8 f f 8 f . . . 
                    . . . f f . . f f . . .
        """),
        SpriteKind.sospechoso2)
    culpable.set_position(188, 105)
    sospechoso_negro = sprites.create(img("""
            . f f f f f f f f f f . 
                    f f f f f f f f f f f f 
                    f f f f f f f f f f f f 
                    f f f f f f f f f f f f 
                    f f f f f f f f f f f f 
                    f f f e e e e e e f f f 
                    f f e 1 f e e 1 f e f f 
                    . f e e e e e e e e f . 
                    . f e e e f e e e e f . 
                    . . f f f f f f f f . . 
                    . f 1 f 1 1 1 1 f 1 f . 
                    . f e f 1 1 1 1 f e f . 
                    . f e f 1 1 1 1 f e f . 
                    . . f f 6 6 6 6 f f . . 
                    . . . f 6 f f 6 f . . . 
                    . . . f f . . f f . . .
        """),
        SpriteKind.sospechoso4)
    sospechoso_negro.set_position(285, 105)
    sospechoso_fumador = sprites.create(img("""
            . . . . . . f f f f f f f f . . 
                    . . . . . f 5 5 5 5 5 5 5 f . . 
                    . . . . f 5 5 5 5 5 5 5 f b . . 
                    . . . . f d 9 1 d d 9 1 b . . . 
                    . . . . f d 1 1 d d 1 1 f b . . 
                    . . . . f d d d d d d d b b . . 
                    . . . . f d d d 1 1 4 2 f . . . 
                    . . . f f f f f f f f f f f . . 
                    . . f d e f d d e d d f e d f . 
                    . . f e d f d d e d d f d e f . 
                    . . f e d f e e e e e f d e f . 
                    . . f d e f e d e d e f e d f . 
                    . . f e d f d e e e d f d e f . 
                    . . f f f f f f f f f f f f f . 
                    . . . . . f f f . f f f . . . . 
                    . . . . . f f f . f f f . . . .
        """),
        SpriteKind.sospechoso3)
    sospechoso_fumador.set_position(235, 105)
    victima2 = sprites.create(img("""
            ......................
                    ......................
                    ......................
                    ..............ff......
                    ..f888888112e21fffff..
                    ..f88888dd11211dddff..
                    ..f88888dd11111dd1df..
                    .22222222222222222222.
                    ...222222222222222.2..
                    ..2..222....22..2...2.
                    ......................
                    ......................
                    ......................
                    ......................
        """),
        SpriteKind.victima)
    victima2.set_position(64, 114)
    b1 = sprites.create(img("""
            . . . . f f f f f f f f f . . . . 
                    . . . f 1 1 1 1 1 1 1 1 1 f . . . 
                    . . f f 1 1 1 1 1 1 1 1 1 f f . . 
                    . f f f 1 1 f f f f f f f 1 1 f . 
                    f f f f 1 1 f f f f f f f 1 1 f f 
                    f f f f 1 1 f f f f f f f 1 1 f f 
                    f f f f 1 1 f f f f f f f 1 1 f f 
                    f f f f 1 1 1 1 1 1 1 1 1 f f f f 
                    f f f f 1 1 1 1 1 1 1 1 1 f f f f 
                    f f f f 1 1 f f f f f f f 1 1 f f 
                    f f f f 1 1 f f f f f f f 1 1 f f 
                    f f f f 1 1 f f f f f f f 1 1 f f 
                    f f f f 1 1 f f f f f f f 1 1 f f 
                    . f f f 1 1 f f f f f f f 1 1 f . 
                    . . f f 1 1 1 1 1 1 1 1 1 f f . . 
                    . . . f 1 1 1 1 1 1 1 1 1 f . . . 
                    . . . . f f f f f f f f f . . . .
        """),
        SpriteKind.B1)
    b1.set_position(64, -20)
    b2 = sprites.create(img("""
            . . . . f f f f f f f f f . . . . 
                    . . . f 1 1 1 1 1 1 1 1 1 f . . . 
                    . . f f 1 1 1 1 1 1 1 1 1 f f . . 
                    . f f f 1 1 f f f f f f f 1 1 f . 
                    f f f f 1 1 f f f f f f f 1 1 f f 
                    f f f f 1 1 f f f f f f f 1 1 f f 
                    f f f f 1 1 f f f f f f f 1 1 f f 
                    f f f f 1 1 1 1 1 1 1 1 1 f f f f 
                    f f f f 1 1 1 1 1 1 1 1 1 f f f f 
                    f f f f 1 1 f f f f f f f 1 1 f f 
                    f f f f 1 1 f f f f f f f 1 1 f f 
                    f f f f 1 1 f f f f f f f 1 1 f f 
                    f f f f 1 1 f f f f f f f 1 1 f f 
                    . f f f 1 1 f f f f f f f 1 1 f . 
                    . . f f 1 1 1 1 1 1 1 1 1 f f . . 
                    . . . f 1 1 1 1 1 1 1 1 1 f . . . 
                    . . . . f f f f f f f f f . . . .
        """),
        SpriteKind.B2)
    b2.set_position(64, -20)
    b3 = sprites.create(img("""
            . . . . f f f f f f f f f . . . . 
                    . . . f 1 1 1 1 1 1 1 1 1 f . . . 
                    . . f f 1 1 1 1 1 1 1 1 1 f f . . 
                    . f f f 1 1 f f f f f f f 1 1 f . 
                    f f f f 1 1 f f f f f f f 1 1 f f 
                    f f f f 1 1 f f f f f f f 1 1 f f 
                    f f f f 1 1 f f f f f f f 1 1 f f 
                    f f f f 1 1 1 1 1 1 1 1 1 f f f f 
                    f f f f 1 1 1 1 1 1 1 1 1 f f f f 
                    f f f f 1 1 f f f f f f f 1 1 f f 
                    f f f f 1 1 f f f f f f f 1 1 f f 
                    f f f f 1 1 f f f f f f f 1 1 f f 
                    f f f f 1 1 f f f f f f f 1 1 f f 
                    . f f f 1 1 f f f f f f f 1 1 f . 
                    . . f f 1 1 1 1 1 1 1 1 1 f f . . 
                    . . . f 1 1 1 1 1 1 1 1 1 f . . . 
                    . . . . f f f f f f f f f . . . .
        """),
        SpriteKind.B3)
    b3.set_position(64, -20)
    b4 = sprites.create(img("""
            . . . . f f f f f f f f f . . . . 
                    . . . f 1 1 1 1 1 1 1 1 1 f . . . 
                    . . f f 1 1 1 1 1 1 1 1 1 f f . . 
                    . f f f 1 1 f f f f f f f 1 1 f . 
                    f f f f 1 1 f f f f f f f 1 1 f f 
                    f f f f 1 1 f f f f f f f 1 1 f f 
                    f f f f 1 1 f f f f f f f 1 1 f f 
                    f f f f 1 1 1 1 1 1 1 1 1 f f f f 
                    f f f f 1 1 1 1 1 1 1 1 1 f f f f 
                    f f f f 1 1 f f f f f f f 1 1 f f 
                    f f f f 1 1 f f f f f f f 1 1 f f 
                    f f f f 1 1 f f f f f f f 1 1 f f 
                    f f f f 1 1 f f f f f f f 1 1 f f 
                    . f f f 1 1 f f f f f f f 1 1 f . 
                    . . f f 1 1 1 1 1 1 1 1 1 f f . . 
                    . . . f 1 1 1 1 1 1 1 1 1 f . . . 
                    . . . . f f f f f f f f f . . . .
        """),
        SpriteKind.B4)
    b4.set_position(64, -20)
    b5 = sprites.create(img("""
            . . . . f f f f f f f f f . . . . 
                    . . . f 1 1 1 1 1 1 1 1 1 f . . . 
                    . . f f 1 1 1 1 1 1 1 1 1 f f . . 
                    . f f f 1 1 f f f f f f f 1 1 f . 
                    f f f f 1 1 f f f f f f f 1 1 f f 
                    f f f f 1 1 f f f f f f f 1 1 f f 
                    f f f f 1 1 f f f f f f f 1 1 f f 
                    f f f f 1 1 1 1 1 1 1 1 1 f f f f 
                    f f f f 1 1 1 1 1 1 1 1 1 f f f f 
                    f f f f 1 1 f f f f f f f 1 1 f f 
                    f f f f 1 1 f f f f f f f 1 1 f f 
                    f f f f 1 1 f f f f f f f 1 1 f f 
                    f f f f 1 1 f f f f f f f 1 1 f f 
                    . f f f 1 1 f f f f f f f 1 1 f . 
                    . . f f 1 1 1 1 1 1 1 1 1 f f . . 
                    . . . f 1 1 1 1 1 1 1 1 1 f . . . 
                    . . . . f f f f f f f f f . . . .
        """),
        SpriteKind.B5)
    b5.set_position(64, -20)
    b6 = sprites.create(img("""
            . . . . f f f f f f f f f . . . . 
                    . . . f 1 1 1 1 1 1 1 1 1 f . . . 
                    . . f f 1 1 1 1 1 1 1 1 1 f f . . 
                    . f f f 1 1 f f f f f f f 1 1 f . 
                    f f f f 1 1 f f f f f f f 1 1 f f 
                    f f f f 1 1 f f f f f f f 1 1 f f 
                    f f f f 1 1 f f f f f f f 1 1 f f 
                    f f f f 1 1 1 1 1 1 1 1 1 f f f f 
                    f f f f 1 1 1 1 1 1 1 1 1 f f f f 
                    f f f f 1 1 f f f f f f f 1 1 f f 
                    f f f f 1 1 f f f f f f f 1 1 f f 
                    f f f f 1 1 f f f f f f f 1 1 f f 
                    f f f f 1 1 f f f f f f f 1 1 f f 
                    . f f f 1 1 f f f f f f f 1 1 f . 
                    . . f f 1 1 1 1 1 1 1 1 1 f f . . 
                    . . . f 1 1 1 1 1 1 1 1 1 f . . . 
                    . . . . f f f f f f f f f . . . .
        """),
        SpriteKind.B6)
    b6.set_position(64, -20)
    muro1 = sprites.create(img("""
            ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
        """),
        SpriteKind.muro)
    muro1.set_position(128, 60)
    muro2 = sprites.create(img("""
            ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
        """),
        SpriteKind.muro)
    muro2.set_position(205, 60)
    muro3 = sprites.create(img("""
            ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
        """),
        SpriteKind.muro)
    muro3.set_position(260, 60)
    muro42 = sprites.create(img("""
            ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
                    ..2..
        """),
        SpriteKind.muro4)
    muro42.set_position(310, 60)

def on_hit_wall(sprite, location):
    sprite.destroy(effects.fire, 100)
scene.on_hit_wall(SpriteKind.enemy_AVION, on_hit_wall)

def on_b_pressed():
    global Bala, Bala_izquierda
    Bala = sprites.create_projectile_from_sprite(img("""
        b b b b 
                b b b b
    """), J1, 0, 0)
    Bala.set_velocity(150, 0)
    if controller.left.is_pressed():
        Bala_izquierda = sprites.create_projectile_from_sprite(img("""
            b b b b 
                        b b b b
        """), J1, 0, 0)
        Bala_izquierda.set_velocity(-150, 0)
        Bala.destroy()
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_on_overlap8(sprite, otherSprite):
    b1.set_position(64, 90)
    if controller.B.is_pressed():
        game.show_long_text("Este hombre de 28 años ha muerto debido a un disparo  en la espalda con una pistola. Sherlock ha reunido a los 4 sospechosos.",
            DialogLayout.BOTTOM)
        b1.destroy()
        muro1.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.victima, on_on_overlap8)

def on_on_overlap9(sprite, otherSprite):
    global pito_de_caballo, alma
    sprite.destroy()
    otherSprite.destroy(effects.star_field, 1)
    pito_de_caballo += 1
    alma = sprites.create(img("""
            . . c c c c c c . . . . . 
                    . c c c c c c c c . . . . 
                    b c c c c c c c b c . . . 
                    c b b c c c b b c c . . . 
                    c 2 2 b c b 2 2 c c . . . 
                    c c 2 c c c 2 c c c . . . 
                    c c c c c c c c c c . . . 
                    b b c b c b c b b c . . . 
                    c b b c b c b b c c . . . 
                    c c c c c c c c c c c . . 
                    c c c c c c c c c c c . . 
                    . c c c c c c c c c c . . 
                    . c c c c c c c c c c . . 
                    . . c c c c c c c c c c . 
                    . . . c c c c c c c c c . 
                    . . . . . c c c c c c c . 
                    . . . . . . . . . . c c c
        """),
        SpriteKind.alma_)
    alma.set_position(688, 87)
    if pito_de_caballo == 1:
        alma.follow(J1, 35)
    if pito_de_caballo == 2:
        alma.follow(J1, 45)
    if pito_de_caballo == 3:
        alma.follow(J1, 60)
    if pito_de_caballo == 4:
        alma.follow(J1, 82.5)
    if pito_de_caballo == 5:
        alma.follow(J1, 100)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.cuerpo5, on_on_overlap9)

def on_on_overlap10(sprite, otherSprite):
    sprite.destroy(effects.spray, 1)
    info.change_life_by(-2)
sprites.on_overlap(SpriteKind.cuchillo_lluvia,
    SpriteKind.player,
    on_on_overlap10)

def on_on_destroyed(sprite):
    global puntos, libro_3_from_hell
    puntos += 15
    libro_3_from_hell = sprites.create(img("""
            . . . . . . f f . . . . . . 
                    . . . . f f f f f . . . . . 
                    . . . f f 7 7 7 f f . . . . 
                    . . f f 7 7 7 f 7 f . . . . 
                    . f f 7 7 7 f 7 7 f f . . . 
                    f f f 7 7 f 7 7 7 7 f f . . 
                    f 1 f f 7 7 7 7 f 7 7 f f . 
                    f f 1 f f 7 7 f 7 7 7 7 f f 
                    . f f 1 f 7 7 7 7 7 f 7 6 f 
                    . . f f 1 f f 7 7 f 7 6 f f 
                    . . . f d 1 f f 6 6 6 f f . 
                    . . . f f d d f f 6 f f . . 
                    . . . . f f d d f f f . . . 
                    . . . . . . f f f . . . . .
        """),
        SpriteKind.libro3)
    libro_3_from_hell.set_position(40, 60)
sprites.on_destroyed(SpriteKind.jack, on_on_destroyed)

def nivel3():
    global Libros, sí, jack_the_ripper, fase_jack
    Barrera3_: Sprite = None
    info.set_score(2)
    info.change_score_by(1)
    Libros += 1
    info.set_life(8)
    sí += 10
    tiles.set_tilemap(tilemap("""
        level_24
    """))
    scene.set_background_image(img("""
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888588888888888888888888888888888888888888888888888888
                8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888588888888
                8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888888888888888588888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888858888888888888888888
                5888888888888885888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888888888888888888888888888888888888888888888888888888588888888888888888888888888888855555555555888888888888888888888888888888888888888888
                8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888855555555555555455888888888888888888888888888888888888888
                8888888888888888888888888888888888888d88888888888888888888888888888888888888888888888888888888888888888555444445555555455588888888888888888888888888888888888888
                8888888888888888888888888888888888888d88888888888888888888888888888888888888888888888888888888888888885444555544555555445558888888888888888888888888888888888888
                8888888888888888888888888888888888886668888888888888888888888888888888888888888888888888888888888888555455555554555555545555588888888888888888888888888888888888
                8888888888888888888888888888888888866666888888888888888888888888888888888888888888888888888888888888555555555554555555554455588888888888888888888888888888888888
                8888888888888888888888888888888888866666888888888888888888888888888888888888888888888888888888888885455555555545555555555555558888888888888888888888888888888888
                8888888888888888888888888888888888666666688888888888888888888888888888888888888888888888888888888855544555554445555555555555555888888888888888888888888888888888
                8888888888888888888888888888888886666666668888888888888888888888888888888888888888888888888888888555555444444555555555455555555588888811111111111111111111888888
                8888888888888888888888888888888886666666668888888888888888888888888888888888888888888888888888888555555555555555555554444555555588881111111111111111111111111188
                8888888888888888888888888888888866666666666888888888888888888888888888888888888888888888888888888555555555555555555544554555555588811111111111111111111111111188
                8888888888888888888888888888888dddddddddddd888888888888888888888888888888888888888888888888888885555445555555555555544444554455558111111111111111111111111111118
                8888888888888888888888888888888ddddddddddddd88888888888888888888888888888888888888888888888888885554445555555555555555445544555558111111111111111111111111111118
                888888888888888888888888888888dddddddddddddd88888888888888888588888888888888888888888888888888885545545555555444445555555545555558111111111111111111111111111118
                88888888888888888888888888888dddddddddddddddd8888888888888888888888888888888888888888888888888885545545555554555545555555545555558111111111118811111111111111118
                8888888888888888888888888888866666666666666666888888888888888888888888888888888888888888888888885545545555545555545555555554555558881111111118811111111111111888
                8888888888888888888858888886666666666666666666668888888888888888888888888888888888888888888888885545545555545555545555555554555558888888888888881111111111888888
                8888888888888888888888888866666666666666666666666888888888888888888888888888888888888888888888885545545555545555545555555555455558888888888888888111111888888888
                8888888888888888888888888866666666666666666666666888888888888888888888888888888888888888888888885555545555554555445555555555445558888888888888888888888888888888
                8888888888888888888888888866666666666666666666666888888888888888888888888888888888888888885888885554545555554445555555555555555558888888888888888888888888888888
                8888888888888888888888888666666666666666666666666888888888888888888888888888888888888888888888885555445555555555555555555555555558888888888888888888888888888888
                8888888888888888888888888dddddddddddddddddddddddd888888888888888888888888888888888888888888888885555555555555555555555555555555558888888888888888888888888888888
                8888888888888888888888888dddddddddddddddddddddddd888888888888888888888888888888888888888888888888555555555555555555555555544455588888888888888888888888888888888
                8888888888888888888888888dddddddddddddddddddddddd888888888888888888888888888888888888888888888888555555555555555555555554445455588888888888888888888888888888888
                8888888888888888888888888dddddddddddddddddddddddd888888888888888888888888888888888888888888888888555555554455555555555545555455588888888888888888888888888888888
                888588888888888888888888ddddddddd111111111dddddddd88888888888888888888888888888888888888888888888855555544445555555555455555455888888888888888888888888888888888
                888888811111888888888888ddddddd1111111111111ddddddd8888888888888888888888888888888888888888888888885555545545555555555555554558888888888888888888888888888888888
                888888811111111118888888ddeeee111111111111111eeeedd8888888888888888888888888888888888888888888888888555455445555555555555544588888888888888888888888888888888888
                888888811111111111888888ddeee11111111111111111eeedd8888888888888888888888888888888888888888888888888555455455555555555555545588888888888888888888888858888888888
                888888811111111111188888ddee1f11111111111111111eedd8888888888888888888888888888888888888888888888888885554455555555555444458888888888888888888888888888888888888
                888888811111111111111888ddee11f1111111111111111eedd8888888888888888885888888888888888888888888888888888555555555555444555588888888888888888888888888888888888888
                888888881111111111111118dde1111ff111111111111111edd8888888888888888888888888888888888888888888888888888855555555555555555888888888888888888888888888888888888888
                888888888811111111111111dde111111f11111111111111edd8888888888888888888888888888888888888888888888888888888855555555555888888888888888888888888888888888888888888
                888888888888111111111111dde1111111ff11111ff11111edd8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                888888888888888111111111dde111111111f11ff1111111edd8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                888888888888888811111111dde1111111111ff111111111edd8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                888888888888888888811118dde111111111111111111111edd8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                888888888888888888888888dde111111111111111111111edd8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                888888888888888888888888dde111111111111111111111edd8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                888888888888888888888888dde111111111111111111111edd8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                888888888888888888888888ddee1111111111111111111eedd8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                888888888888888888888888ddee1111111111111111111eedd8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                888888888888888888888888ddeee11111111111111111eeedd8888888885888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                888888888888888888888888ddeeee111111111111111eeeedd8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                888888888888888888888888ddedddd1111111111111dddeddd8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888ddeddddd111111111dddddedd88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888588888888888888ddeddddddddddddddddddeddd88888888888888888888888888888888888888888888888888888888888888888888888888888588888888888888888888888888888888
                8888888888888888888888888dddedddddddddddddddddeddd88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888dddedddddddddddddddddeddd88888888888888888888888888888888888888888588888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888ddddedddddddddddddddedddd88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888ddddedddddddddddddddedddd88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888dddddedddddddddddddeddddd88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8858888888888888888888888dddddedddddddddddddeddddd88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888ddddddedddddddddddedddddd88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888eeeeeeeeeeeeeeeeeeeeeeeee88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888858888888deddddddddddddddddddddedd88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888deddddddddddddddddddddedd88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888858888888888
                8888888888888888888888888deddddddddddddddddddddedd88888888888888888888888888888888888888888888888888888888888588888888888888888888888888888888888888888888888888
                8888888888888888888888888deddddddddddddddddddddedd88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888ddeddddddddddddddddddeddd88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888ddeddddddddddddddddddeddd88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888ddeddddddddddddddddddeddd88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888ddedddddddddddddddddedddd88888888888888888858888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888ddedddddddddddddddddedddd88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888dddeddddddddddddddddedddd88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888dddeddddddddddddddddedddd88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888588dddedddddddddddddddeddddd88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888dddedddddddddddddddeddddd88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888ddddeddddddddddddddeddddd88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888ddddedddddddddddddedddddd88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888ddddedddddddddddddedddddd88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888558888888888888
                8888888888888888888888888ddddedddddddddddddedddddd88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888558888888888888
                8888888888888888888888888dddddeddddddddddddedddddd88888888888888888888888888888888888888888888888888888888888888888888858888888888888888888888888888888888888888
                8888888888888888888888888eeeeeeeeeeeeeeeeeeeeeeeee88888888888888888888888888888888888888888858888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888deddddddddddddddddddddedd88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888deddddddddddddddddddddedd88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888deddddddddddddddddddddedd88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888deddddddddddddddddddddedd88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888ddeddddddddddddddddddeddd88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888ddeddddddddddddddddddeddd88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888ddeddddddddddddddddddeddd88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888858888888888888888888dddedddddddddddddddddeddd88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888858888
                8888888888888888888888888dddedddddddddddddddddeddd66666666888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888dddeddddddddddddddddedddd66666666666666666666666688888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888dddeddddddddddddddddedddd66666666666666666666666666666666666666688888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888ddddedddddddddddddddedddd66666666666666666666666666666666666666666666666666666688888888888888888888888888888888888888888888888888888888
                8888888888888888888888888ddddedddddddddddddddedddd66666666666666666666666666666666666666666666666666666666666666666666668888888888888888888888888888888888888888
                8888888888888888888888888ddddeddddddddddddddedddddeddddd66666666666666666666666666666666666666666666666666666666666666666666666666666668888888888888888888888888
                8888888888888888888888888dddddedddddddddddddedddddeddddddddddddddddddd666666666666666666666666666666666666666666666666666666666666666666666666666888888888888888
                8888888888888888888888888dddddedddddddddddddedddddedddddeeddddddddddddddddddddddddd66666666666666666666666666666666666666666666666666666666666666668888888888888
                8888888888888888888888888dddddedddddddddddddedddddedeeeeddeedddddddddddddeeeeeddddddddddddddddddd6666666666666666666666666666666666666666666666666d8888888888888
                8888888888888888888888888dddddeddddddddddddeddddddeeddddddddeeedddddeeeeedddddeeedddddddddddddeeeddddddddddddd66666666666666666666666666666666666ddd888888888888
                8888888888888888888888888eeeeeeeeeeeeeeeeeeeeeeeeeeddddddddddddeeeeedddddddddddddeeedddddeeeeedddeeedddddddeeeeeedddddddddd6666666666666666666666ddd888888888888
                8888888888888888888888888ddeddddddddddddddddddddededdddddddddddddeddddddddddddddddddeeeeedddddddddddeeeeeeeddddddeeeeddddddeeeedddddddddd6666666ddee888888888888
                8888888888888888888888888ddeddddddddddddddddddddededdddddddddddddeddddddddddddddddddddeddddddddddddddddedddddddddddddeeeeeeddddeeeeddddddeeeeedddedd888888888888
                8888888888888888888888888ddeddddddddddddddddddddededdddddddddddddeddddddddddddddddddddeddddddddddddddddedddddddddddddddedddddddddddeeeeeedddddeededd888888888888
                8888888888888888888885888ddeddddddddddddddddddddededdddddddddddddeddddddddddddddddddddeddddddddddddddddedddddddddddddddeddddddddddddddedddddddddeedd888888888888
                8888888888888888888888888ddeddddddddddddddddddddedeeeeeeeeeeeeeeeeedddddddddddddddddddeddddddddddddddddedddddddddddddddeddddddddddddddeddddddddddeddd88888588888
                8888888888888888888888888dddeddddddddddddddddddeddeddddddddddddddedeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeddddedddddddddddddddeddddddddddddddeddddddddddeddd88888888888
                8888888888888888888888888dddeddddddddddddddddddeddeddddddddddddddeddddddddddddddddddddeddddddddddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeddddeddddddddddeddd88888888888
                8888888888888888888888888dddeddddddddddddddddddeddeddddddddddddddeddddddddddddddddddddeddddddddddddddddedddddddddddddddeddddddddddeeeeeeeeeeeeeeeeddd88888888888
                8888888888888888888888888dddeddddddddddddddddddeddeddddddddddddddeddddddddddddddddddddeddddddddddddddddedddddddddddddddeddddddddddddddeddddddddddeddd88888888888
                8888888888888888888888888dddeddddddddddddddddddeddeddddddddddddddeddddddddddddddddddddeddddddddddddddddedddddddddddddddeddddddddddddddeddddddddddeddd88888888888
                8888888888888888888888888dddeddddddddddddddddddeddeddddddddddddddeddddddddddddddddddddeddddddddddddddddedddddddddddddddeddddddddddddddeddddddddddedddd8888888888
                8888888885888888888888888ddddeddddddddddddddddedddeddddddddddddddeddddddddddddddddddddeddddddddddddddddedddddddddddddddeddddddddddddddeddddddddddedddd8888888888
                8888888888888888888888888ddddeddddddddddddddddedddeddddddddddddddeddddddddddddddddddddeddddddddddddddddedddddddddddddddeddddddddddddddeddddddddddedddd8888888888
                8888888888888888888888888ddddeddddddddddddddddedddeeeeeeeeeeeeeeeeeeeeeeeeddddddddddddeddddddddddddddddedddddddddddddddeddddddddddddddeddddddddddedddd8888888888
                8888888888888888888888888ddddeddddddddddddddddedddeddddddddddddddeddddddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeddddddddddddeddddddddddedddd8888888888
                8888888888888888888888888ddddeddddddddddddddddedddeddddddddddddddeddddddddddddddddddddeddddddddddddddddedddddddddddddddeddeeeeeeeeeeeeeeeeeeeeeeeedddd8888888888
                8888888888888888888888888dddddeddddddddddddddeddddeddddddddddddddeddddddddddddddddddddeddddddddddddddddedddddddddddddddeddddddddddddddeddddddddddeddddd888888888
    """))
    J1.set_position(64, 64)
    jack_the_ripper = sprites.create(img("""
            .........fffffffffff........
                    ........fffffffffffff.......
                    .......fffffffffffffff......
                    .......fffffdddddfffff......
                    .......ffffffdddffffff......
                    .......ff1f1ffdff1f1ff......
                    .......fffffffdfffffff......
                    ........fddddfdfddddf.......
                    ........fdddfdddfdddf.......
                    ........fdddffdffdddf.......
                    ........ffdfffffffdff.......
                    ........fdffddd22ffdf.......
                    ........ffdddfff2ddff.......
                    ......fffffdddfd2dffff......
                    ....ffffffffffffffffffff....
                    ...ffffffffffffffffffffff...
                    ..ffffffffffffffffffffffff..
                    ..ffffffffffffffffffffffff..
                    ..ffffffffffffffffffffffff..
                    ..ffffffffffffffffffffffff..
                    ..ffffffffffffffffffffffff..
                    ..ffffffffffffffffffffffff..
                    ..ffffffffffffffffffffffff..
                    ..ffffffffffffffffffffffff..
                    ..ffffffffffffffffffffffff..
                    ..ffffffffffffffffffffffff..
                    ..ffffffffffffffffffffffff..
                    ..ffffffffffffffffffffffff..
                    ..ffffffffffffffffffffffff..
                    ..ffffffffffffffffffffffff..
                    ..ffffffffffffffffffffffff..
                    ..ffffffffffffffffffffffff..
                    ..ffffffffffffffffffffffff..
                    ..ffffffffffffffffffffffff..
                    ..ffffffffffffffffffffffff..
                    ..ffffffffffffffffffffffff..
                    .ffffffffffffffffffffffffff.
                    ffffffffffffffffffffffffffff
        """),
        SpriteKind.jack)
    jack_the_ripper.set_position(128, -10)
    jack_the_ripper.set_velocity(0, 75)
    fase_jack = 0
    game.splash("NIVEL 3:", "\"From Hell\" de Alan Moore")
    game.show_long_text("En el Tower Bridge se encuentra Jack el Destripador. Tu misión es acabar con él... si puedes.",
        DialogLayout.BOTTOM)
    Barrera2_.destroy()
    Barrera3_.destroy()
    barrera4_.destroy()
    barrera5_.destroy()
    barrera6_.destroy()
    Barrera_.destroy()
    avión.destroy()
    aquarius.destroy()
    burbuja.destroy()
    cartel.destroy()
    flecha2.destroy()
    Malo_.destroy()
    malo2.destroy()
    malo3.destroy()
    malo4.destroy()
    ballestero.destroy()
    Monster.destroy()
    burbuja.destroy()
    burbuja2.destroy()
    burbuja3.destroy()
    burbuja4.destroy()
    burbuja5.destroy()

def on_on_overlap11(sprite, otherSprite):
    sprite.set_velocity(50, 128)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.Barrera, on_on_overlap11)

def sospechoso3_mov():
    sospechoso_fumador.set_velocity(150, 0)
    pause(1000)
    sospechoso_fumador.set_velocity(0, 0)
def descubrir_al_culpable():
    global libro_4_Sherlock_Holmes
    culpable.destroy(effects.fire, 1000)
    game.show_long_text("Felicidades, has encontrado al culpable.",
        DialogLayout.BOTTOM)
    libro_4_Sherlock_Holmes = sprites.create(img("""
            . . . . . . f f . . . . . . 
                    . . . . f f f f f . . . . . 
                    . . . f f a a a f f . . . . 
                    . . f f a a a f a f . . . . 
                    . f f a a a f a a f f . . . 
                    f f f a a f a a a a f f . . 
                    f 1 f f a a a a f a a f f . 
                    f f 1 f f a a f a a a a f f 
                    . f f 1 f a a a a a f a c f 
                    . . f f 1 f f a a f a c f f 
                    . . . f d 1 f f c c c f f . 
                    . . . f f d d f f c f f . . 
                    . . . . f f d d f f f . . . 
                    . . . . . . f f f . . . . .
        """),
        SpriteKind.libro4)
    libro_4_Sherlock_Holmes.set_position(188, 80)

def on_on_overlap12(sprite, otherSprite):
    global pingo
    if controller.B.is_pressed() and whenbut == 1:
        descubrir_al_culpable()
    b3.set_position(188, 85)
    if controller.B.is_pressed() and whenbut == 0:
        game.show_long_text("El sospechoso afirma que estaba con su amigo el rubio en casa y no sabía nada.",
            DialogLayout.BOTTOM)
        b3.destroy()
        pingo += 1
    if pingo == 2:
        muro2.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.sospechoso2, on_on_overlap12)

def mover_a_jack():
    jack_the_ripper.set_position(128, 36)

def on_on_overlap13(sprite, otherSprite):
    sprite.set_velocity(-50, 128)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.Barrera2, on_on_overlap13)

def on_left_pressed():
    if sí == 0:
        animation.run_image_animation(J1,
            [img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . f f f f f f f f f f f 
                                . . . . f f c c c c c c c c f f 
                                . . . f f c c c c c c c c f . . 
                                . . . f f f f f c c c c f f . . 
                                . . . f e e e f f f f f f . . . 
                                . f . f e e e e e e e e f . f . 
                                . f f f f f f f f f f f f f f . 
                                . . f 5 5 5 5 5 5 5 5 5 f . . . 
                                . . f f 5 5 5 5 f 5 5 5 f . . . 
                                . . f 5 5 5 5 5 5 5 5 5 f . . . 
                                . . f 5 f 5 5 5 f 5 5 5 f . . . 
                                . . f 5 5 f f f 5 5 5 5 f . . . 
                                . f f 5 5 5 5 5 5 5 5 5 f f . . 
                                . f 5 5 f f f f f f f 5 5 f . . 
                                . f f f f . . . . . f f f f . .
                """),
                img("""
                    . . . . . . . f f f f f f f f f 
                                . . . . . f f f c c c c c c f f 
                                . . . . f f c c c c c c c f . . 
                                . . . f f c c c c c c c f f . . 
                                . . . f f f f f c c c c f . . . 
                                . . . f e e e f f f f f f . . . 
                                . f . f e e e e e e e e f . f . 
                                . f f f f f f f f f f f f f f . 
                                . . f 5 5 5 5 5 5 5 5 5 f . . . 
                                . . f f 5 5 5 5 f 5 5 5 f . . . 
                                . . f 5 5 5 5 5 5 5 5 5 f . . . 
                                . . f 5 f 5 5 5 f 5 5 5 f . . . 
                                . . f 5 5 f f f 5 5 5 5 f . . . 
                                . . f 5 5 5 5 5 5 5 5 5 f . . . 
                                . . f 5 5 f f f f f 5 5 f . . . 
                                . . f f f f . . . f f f f . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . f f f f f f f f f f f 
                                . . . . f f c c c c c c c c f f 
                                . . . f f c c c c c c c c f . . 
                                . . . f f f f f c c c c f f . . 
                                . . . f e e e f f f f f f . . . 
                                . f . f e e e e e e e e f . f . 
                                . f f f f f f f f f f f f f f . 
                                . . f 5 5 5 5 5 5 5 5 5 f . . . 
                                . . f f 5 5 5 5 f 5 5 5 f . . . 
                                . . f 5 5 5 5 5 5 5 5 5 f . . . 
                                . . f 5 f 5 5 5 f 5 5 5 f . . . 
                                . . f 5 5 f f f 5 5 5 5 f . . . 
                                . . f 5 5 5 5 5 5 5 5 5 f . . . 
                                . . . f 5 5 f f f 5 5 f f . . . 
                                . . . f f f f . f f f f . . . .
                """),
                img("""
                    . . . . . . . f f f f f f f f f 
                                . . . . . f f f c c c c c c f f 
                                . . . . f f c c c c c c c f . . 
                                . . . f f c c c c c c c f f . . 
                                . . . f f f f f c c c c f . . . 
                                . . . f e e e f f f f f f . . . 
                                . f . f e e e e e e e e f . f . 
                                . f f f f f f f f f f f f f f . 
                                . . f 5 5 5 5 5 5 5 5 5 f . . . 
                                . . f f 5 5 5 5 f 5 5 5 f . . . 
                                . . f 5 5 5 5 5 5 5 5 5 f . . . 
                                . . f 5 f 5 5 5 f 5 5 5 f . . . 
                                . . f 5 5 f f f 5 5 5 5 f . . . 
                                . . f 5 5 5 5 5 5 5 5 5 f . . . 
                                . . f 5 5 f f f f f 5 5 f . . . 
                                . . f f f f . . . f f f f . . .
                """)],
            250,
            True)
    if sí == 10:
        animation.run_image_animation(J1,
            [img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . f f f f f f f f f f f 
                                . . . . f f c c c c c c c c f f 
                                . . . f f c c c c c c c c f . . 
                                . . . f f f f f c c c c f f . . 
                                . . . f e e e f f f f f f . . . 
                                . f . f e e e e e e e e f . f . 
                                . f f f f f f f f f f f f f f . 
                                . . f 5 5 5 5 5 5 5 5 5 f . . . 
                                . . f f 5 5 5 5 f 5 5 5 f . . . 
                                f f f 5 5 5 5 5 5 5 5 5 f . . . 
                                8 8 f 5 f 5 5 f 5 5 5 5 f . . . 
                                f 8 f 5 5 f f 5 5 5 5 5 f . . . 
                                . f f 5 5 5 5 5 5 5 5 5 f f . . 
                                . f 5 5 f f f f f f f 5 5 f . . 
                                . f f f f . . . . . f f f f . .
                """),
                img("""
                    . . . . . . . f f f f f f f f f 
                                . . . . . f f f c c c c c c f f 
                                . . . . f f c c c c c c c f . . 
                                . . . f f c c c c c c c f f . . 
                                . . . f f f f f c c c c f . . . 
                                . . . f e e e f f f f f f . . . 
                                . f . f e e e e e e e e f . f . 
                                . f f f f f f f f f f f f f f . 
                                . . f 5 5 5 5 5 5 5 5 5 f . . . 
                                . . f f 5 5 5 5 f 5 5 5 f . . . 
                                f f f 5 5 5 5 5 5 5 5 5 f . . . 
                                8 8 f 5 f 5 5 f 5 5 5 5 f . . . 
                                f 8 f 5 5 f f 5 5 5 5 5 f . . . 
                                . f f 5 5 5 5 5 5 5 5 5 f . . . 
                                . . f 5 5 f f f f f 5 5 f . . . 
                                . . f f f f . . . f f f f . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . f f f f f f f f f f f 
                                . . . . f f c c c c c c c c f f 
                                . . . f f c c c c c c c c f . . 
                                . . . f f f f f c c c c f f . . 
                                . . . f e e e f f f f f f . . . 
                                . f . f e e e e e e e e f . f . 
                                . f f f f f f f f f f f f f f . 
                                . . f 5 5 5 5 5 5 5 5 5 f . . . 
                                . . f f 5 5 5 5 f 5 5 5 f . . . 
                                f f f 5 5 5 5 5 5 5 5 5 f . . . 
                                8 8 f 5 f 5 5 f 5 5 5 5 f . . . 
                                f 8 f 5 5 f f 5 5 5 5 5 f . . . 
                                . f f 5 5 5 5 5 5 5 5 5 f . . . 
                                . . . f 5 5 f f f 5 5 f f . . . 
                                . . . f f f f . f f f f . . . .
                """),
                img("""
                    . . . . . . . f f f f f f f f f 
                                . . . . . f f f c c c c c c f f 
                                . . . . f f c c c c c c c f . . 
                                . . . f f c c c c c c c f f . . 
                                . . . f f f f f c c c c f . . . 
                                . . . f e e e f f f f f f . . . 
                                . f . f e e e e e e e e f . f . 
                                . f f f f f f f f f f f f f f . 
                                . . f 5 5 5 5 5 5 5 5 5 f . . . 
                                . . f f 5 5 5 5 f 5 5 5 f . . . 
                                f f f 5 5 5 5 5 5 5 5 5 f . . . 
                                8 8 f 5 f 5 5 f 5 5 5 5 f . . . 
                                f 8 f 5 5 f f 5 5 5 5 5 f . . . 
                                . f f 5 5 5 5 5 5 5 5 5 f . . . 
                                . . f 5 5 f f f f f 5 5 f . . . 
                                . . f f f f . . . f f f f . . .
                """)],
            250,
            True)
    if sí == 20:
        animation.run_image_animation(J1,
            [img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . f f f f f f f f f f f 
                                f f . . f f c c c c c c c c f f 
                                2 2 f f f c c c c c c c c f . . 
                                f f . f f f f f c c c c f f . . 
                                . . . f e e e f f f f f f . . . 
                                . f . f e e e e e e e e f . f . 
                                . f f f f f f f f f f f f f f . 
                                . . f 5 5 5 5 5 5 5 5 5 f . . . 
                                . . f f 5 5 5 5 f 5 5 5 f . . . 
                                f f f 5 5 5 5 5 5 5 5 5 f . . . 
                                8 8 f 5 f 5 f 5 5 5 5 5 f . . . 
                                f 8 f 5 5 f 5 5 5 5 5 5 f . . . 
                                . f f 5 5 5 5 5 5 5 5 5 f f . . 
                                . f 5 5 f f f f f f f 5 5 f . . 
                                . f f f f . . . . . f f f f . .
                """),
                img("""
                    . . . . . . . f f f f f f f f f 
                                . . . . . f f f c c c c c c f f 
                                f f . . f f c c c c c c c f . . 
                                2 2 f f f c c c c c c c f f . . 
                                f f . f f f f f c c c c f . . . 
                                . . . f e e e f f f f f f . . . 
                                . f . f e e e e e e e e f . f . 
                                . f f f f f f f f f f f f f f . 
                                . . f 5 5 5 5 5 5 5 5 5 f . . . 
                                . . f f 5 5 5 5 f 5 5 5 f . . . 
                                f f f 5 5 5 5 5 5 5 5 5 f . . . 
                                8 8 f 5 f 5 f 5 5 5 5 5 f . . . 
                                f 8 f 5 5 f 5 5 5 5 5 5 f . . . 
                                . f f 5 5 5 5 5 5 5 5 5 f . . . 
                                . . f 5 5 f f f f f 5 5 f . . . 
                                . . f f f f . . . f f f f . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . f f f f f f f f f f f 
                                f f . . f f c c c c c c c c f f 
                                2 2 f f f c c c c c c c c f . . 
                                f f . f f f f f c c c c f f . . 
                                . . . f e e e f f f f f f . . . 
                                . f . f e e e e e e e e f . f . 
                                . f f f f f f f f f f f f f f . 
                                . . f 5 5 5 5 5 5 5 5 5 f . . . 
                                . . f f 5 5 5 5 f 5 5 5 f . . . 
                                f f f 5 5 5 5 5 5 5 5 5 f . . . 
                                8 8 f 5 f 5 f 5 5 5 5 5 f . . . 
                                f 8 f 5 5 f 5 5 5 5 5 5 f . . . 
                                . f f 5 5 5 5 5 5 5 5 5 f . . . 
                                . . . f 5 5 f f f 5 5 f f . . . 
                                . . . f f f f . f f f f . . . .
                """),
                img("""
                    . . . . . . . f f f f f f f f f 
                                . . . . . f f f c c c c c c f f 
                                f f . . f f c c c c c c c f . . 
                                2 2 f f f c c c c c c c f f . . 
                                f f . f f f f f c c c c f . . . 
                                . . . f e e e f f f f f f . . . 
                                . f . f e e e e e e e e f . f . 
                                . f f f f f f f f f f f f f f . 
                                . . f 5 5 5 5 5 5 5 5 5 f . . . 
                                . . f f 5 5 5 5 f 5 5 5 f . . . 
                                f f f 5 5 5 5 5 5 5 5 5 f . . . 
                                8 8 f 5 f 5 f 5 5 5 5 5 f . . . 
                                f 8 f 5 5 f 5 5 5 5 5 5 f . . . 
                                . f f 5 5 5 5 5 5 5 5 5 f . . . 
                                . . f 5 5 f f f f f 5 5 f . . . 
                                . . f f f f . . . f f f f . . .
                """)],
            250,
            True)
    if sí == 30:
        animation.run_image_animation(J1,
            [img("""
                    . . . . . . . . . . . . f f . . 
                                . . . . . f f f f f f f 7 7 f f 
                                f f . . f f c c c c c c f 7 7 f 
                                2 2 f f f c c c c c c c c f f . 
                                f f . f f f f f c c c c f f . . 
                                . . . f e e e f f f f f f . . . 
                                . f . f e e e e e e e e f . f . 
                                . f f f f f f f f f f f f f f . 
                                . . f 5 5 5 5 5 5 5 5 5 f . . . 
                                . . f f 5 5 5 5 f 5 5 5 f . . . 
                                f f f 5 5 5 5 5 5 5 5 5 f . . . 
                                8 8 f 5 f f f 5 5 5 5 5 f . . . 
                                f 8 f 5 5 5 5 5 5 5 5 5 f . . . 
                                . f f 5 5 5 5 5 5 5 5 5 f f . . 
                                . f 5 5 f f f f f f f 5 5 f . . 
                                . f f f f . . . . . f f f f . .
                """),
                img("""
                    . . . . . . . f f f f f f f f f 
                                . . . . . f f f c c c f 7 7 f f 
                                f f . . f f c c c c c c f 7 7 f 
                                2 2 f f f c c c c c c c c f f . 
                                f f . f f f f f c c c c f f . . 
                                . . . f e e e f f f f f f . . . 
                                . f . f e e e e e e e e f . f . 
                                . f f f f f f f f f f f f f f . 
                                . . f 5 5 5 5 5 5 5 5 5 f . . . 
                                . . f f 5 5 5 5 f 5 5 5 f . . . 
                                f f f 5 5 5 5 5 5 5 5 5 f . . . 
                                8 8 f 5 f f f 5 5 5 5 5 f . . . 
                                f 8 f 5 5 5 5 5 5 5 5 5 f . . . 
                                . f f 5 5 5 5 5 5 5 5 5 f . . . 
                                . . f 5 5 f f f f f 5 5 f . . . 
                                . . f f f f . . . f f f f . . .
                """),
                img("""
                    . . . . . . . . . . . . f f . . 
                                . . . . . f f f f f f f 7 7 f f 
                                f f . . f f c c c c c c f 7 7 f 
                                2 2 f f f c c c c c c c c f f . 
                                f f . f f f f f c c c c f f . . 
                                . . . f e e e f f f f f f . . . 
                                . f . f e e e e e e e e f . f . 
                                . f f f f f f f f f f f f f f . 
                                . . f 5 5 5 5 5 5 5 5 5 f . . . 
                                . . f f 5 5 5 5 f 5 5 5 f . . . 
                                f f f 5 5 5 5 5 5 5 5 5 f . . . 
                                8 8 f 5 f f f 5 5 5 5 5 f . . . 
                                f 8 f 5 5 5 5 5 5 5 5 5 f . . . 
                                . f f 5 5 5 5 5 5 5 5 5 f . . . 
                                . . . f 5 5 f f f 5 5 f f . . . 
                                . . . f f f f . f f f f . . . .
                """),
                img("""
                    . . . . . . . f f f f f f f f f 
                                . . . . . f f f c c c f 7 7 f f 
                                f f . . f f c c c c c c f 7 7 f 
                                2 2 f f f c c c c c c c c f f . 
                                f f . f f f f f c c c c f f . . 
                                . . . f e e e f f f f f f . . . 
                                . f . f e e e e e e e e f . f . 
                                . f f f f f f f f f f f f f f . 
                                . . f 5 5 5 5 5 5 5 5 5 f . . . 
                                . . f f 5 5 5 5 f 5 5 5 f . . . 
                                f f f 5 5 5 5 5 5 5 5 5 f . . . 
                                8 8 f 5 f f f 5 5 5 5 5 f . . . 
                                f 8 f 5 5 5 5 5 5 5 5 5 f . . . 
                                . f f 5 5 5 5 5 5 5 5 5 f . . . 
                                . . f 5 5 f f f f f 5 5 f . . . 
                                . . f f f f . . . f f f f . . .
                """)],
            250,
            True)
    if sí == 40:
        animation.run_image_animation(J1,
            [img("""
                    . . . . . . . . . . . . f f . . 
                                . . . . . f f f f f f f 7 7 f f 
                                f f . . f f c c c c c c f 7 7 f 
                                2 2 f f f c c c c c c c c f f . 
                                f f . f f f f f c c c c f f . . 
                                . . . f e e e f f f f f f . . . 
                                . f . f e e e e e e e e f . f . 
                                . f f f f f f f f f f f f f f . 
                                . . f 5 5 5 5 5 5 5 5 5 f . . . 
                                . . f f 5 5 5 5 f 5 5 5 f . f f 
                                f f f 4 5 5 5 5 5 5 5 5 f f a a 
                                8 8 f 4 f f f 5 5 5 5 5 f f a f 
                                f 8 f 4 4 5 5 5 5 5 5 5 f . f . 
                                . f f 4 4 4 4 4 4 4 4 5 f f . . 
                                . f 4 4 f f f f f f f 4 5 f . . 
                                . f f f f . . . . . f f f f . .
                """),
                img("""
                    . . . . . . . f f f f f f f f . 
                                . . . . . f f f c c c f 7 7 f f 
                                f f . . f f c c c c c c f 7 7 f 
                                2 2 f f f c c c c c c c c f f . 
                                f f . f f f f f c c c c f f . . 
                                . . . f e e e f f f f f f . . . 
                                . f . f e e e e e e e e f . f . 
                                . f f f f f f f f f f f f f f . 
                                . . f 5 5 5 5 5 5 5 5 5 f . . . 
                                . . f f 5 5 5 5 f 5 5 5 f . f f 
                                f f f 4 5 5 5 5 5 5 5 5 f f a a 
                                8 8 f 4 f f f 5 5 5 5 5 f f a f 
                                f 8 f 4 4 5 5 5 5 5 5 5 f . f . 
                                . f f 4 4 4 4 4 4 4 4 5 f . . . 
                                . . f 4 4 f f f f f 4 4 f . . . 
                                . . f f f f . . . f f f f . . .
                """),
                img("""
                    . . . . . . . . . . . . f f . . 
                                . . . . . f f f f f f f 7 7 f f 
                                f f . . f f c c c c c c f 7 7 f 
                                2 2 f f f c c c c c c c c f f . 
                                f f . f f f f f c c c c f f . . 
                                . . . f e e e f f f f f f . . . 
                                . f . f e e e e e e e e f . f . 
                                . f f f f f f f f f f f f f f . 
                                . . f 5 5 5 5 5 5 5 5 5 f . . . 
                                . . f f 5 5 5 5 f 5 5 5 f . f f 
                                f f f 4 5 5 5 5 5 5 5 5 f f a a 
                                8 8 f 4 f f f 5 5 5 5 5 f f a f 
                                f 8 f 4 4 5 5 5 5 5 5 5 f . f . 
                                . f f 4 4 4 4 4 4 4 4 5 f . . . 
                                . . . f 4 4 f f f 4 4 f f . . . 
                                . . . f f f f . f f f f . . . .
                """),
                img("""
                    . . . . . . . f f f f f f f f . 
                                . . . . . f f f c c c f 7 7 f f 
                                f f . . f f c c c c c c f 7 7 f 
                                2 2 f f f c c c c c c c c f f . 
                                f f . f f f f f c c c c f f . . 
                                . . . f e e e f f f f f f . . . 
                                . f . f e e e e e e e e f . f . 
                                . f f f f f f f f f f f f f f . 
                                . . f 5 5 5 5 5 5 5 5 5 f . . . 
                                . . f f 5 5 5 5 f 5 5 5 f . f f 
                                f f f 4 5 5 5 5 5 5 5 5 f f a a 
                                8 8 f 4 f f f 5 5 5 5 5 f f a f 
                                f 8 f 4 4 5 5 5 5 5 5 5 f . f . 
                                . f f 4 4 4 4 4 4 4 4 5 f . . . 
                                . . f 4 4 f f f f f 4 4 f . . . 
                                . . f f f f . . . f f f f . . .
                """)],
            250,
            True)
    if sí == 50:
        animation.run_image_animation(J1,
            [img("""
                    ............ffffffff..........
                                .ff........fcccccccf.....ff...
                                f22f......fcccccccf.....f77f..
                                ff22f....fffffffff......ff77f.
                                .fff...f.feeeeeeef..f....fff..
                                .......ffffffffffffff.........
                                ........f425555255f...........
                                ...ff...f255555525f...........
                                ..f44f..fff5555ff5f...........
                                ..ff44f.ffff55fff5f...........
                                ...fff..f245555525f.......ff..
                                ........f244455525ff.....faaf.
                                ........f44ffff555f5f....ffaaf
                                .ff...fff4ff222f55f55f....fff.
                                f88f..f4fff2222ffff555f.......
                                ff88fff5554222255555555f......
                                .fff.f55544222555555555f......
                                ....ff555422555555555ffff.....
                                ....ff45555555555555555ff.....
                                ...f4f45555555555555555ff.....
                                ..f44f445525555555f55555f.....
                                ..f44f444425555555f55555f.....
                                .f444f444222555555f55555f.....
                                .f444f4444244455554f5555f.....
                                .f444f4444444444455f555ff.....
                                ..f44f44444444444454fffff.....
                                ..fffff44444444444444444f.....
                                .....ff4444444444444444ff.....
                                ......fffffffffffffffff.......
                                ..........ff.......ff.........
                """),
                img("""
                    ............ffffffff..........
                                .ff........fcccccccf.....ff...
                                f22f......fcccccccf.....f77f..
                                ff22f....fffffffff......ff77f.
                                .fff...f.feeeeeeef..f....fff..
                                .......ffffffffffffff.........
                                ........f425555255f...........
                                ...ff...f255555525f...........
                                ..f44f..fff5555ff5f...........
                                ..ff44f.ffff55fff5f...........
                                ...fff..f245555525f.......ff..
                                ........f244455525ff.....faaf.
                                ........f44ffff555f5f....ffaaf
                                .ff...fff4ff222f55f55f....fff.
                                f88f..f4fff2222ffff555f.......
                                ff88fff5554222255555555f......
                                .fff.f55544222555555555f......
                                ....ff555422555555555ffff.....
                                ....ff45555555555555555ff.....
                                ...f4f45555555555555555ff.....
                                ..f44f445525555555f55555f.....
                                ..f44f444425555555f55555f.....
                                .f444f444222555555f55555f.....
                                .f444f4444244455554f5555f.....
                                .f444f4444444444455f555ff.....
                                ..f44f44444444444454fffff.....
                                ..fffff44444444444444444f.....
                                .....ff4444444444444444ff.....
                                ......fffffffffffffffff.......
                                .........ff.........ff........
                """),
                img("""
                    ............ffffffff..........
                                .ff........fcccccccf.....ff...
                                f22f......fcccccccf.....f77f..
                                ff22f....fffffffff......ff77f.
                                .fff...f.feeeeeeef..f....fff..
                                .......ffffffffffffff.........
                                ........f425555255f...........
                                ...ff...f255555525f...........
                                ..f44f..fff5555ff5f...........
                                ..ff44f.ffff55fff5f...........
                                ...fff..f245555525f.......ff..
                                ........f244455525ff.....faaf.
                                ........f44ffff555f5f....ffaaf
                                .ff...fff4ff222f55f55f....fff.
                                f88f..f4fff2222ffff555f.......
                                ff88fff5554222255555555f......
                                .fff.f55544222555555555f......
                                ....ff555422555555555ffff.....
                                ....ff45555555555555555ff.....
                                ...f4f45555555555555555ff.....
                                ..f44f445525555555f55555f.....
                                ..f44f444425555555f55555f.....
                                .f444f444222555555f55555f.....
                                .f444f4444244455554f5555f.....
                                .f444f4444444444455f555ff.....
                                ..f44f44444444444454fffff.....
                                ..fffff44444444444444444f.....
                                .....ff4444444444444444ff.....
                                ......fffffffffffffffff.......
                                ........ff...........ff.......
                """),
                img("""
                    ............ffffffff..........
                                .ff........fcccccccf.....ff...
                                f22f......fcccccccf.....f77f..
                                ff22f....fffffffff......ff77f.
                                .fff...f.feeeeeeef..f....fff..
                                .......ffffffffffffff.........
                                ........f425555255f...........
                                ...ff...f255555525f...........
                                ..f44f..fff5555ff5f...........
                                ..ff44f.ffff55fff5f...........
                                ...fff..f245555525f.......ff..
                                ........f244455525ff.....faaf.
                                ........f44ffff555f5f....ffaaf
                                .ff...fff4ff222f55f55f....fff.
                                f88f..f4fff2222ffff555f.......
                                ff88fff5554222255555555f......
                                .fff.f55544222555555555f......
                                ....ff555422555555555ffff.....
                                ....ff45555555555555555ff.....
                                ...f4f45555555555555555ff.....
                                ..f44f445525555555f55555f.....
                                ..f44f444425555555f55555f.....
                                .f444f444222555555f55555f.....
                                .f444f4444244455554f5555f.....
                                .f444f4444444444455f555ff.....
                                ..f44f44444444444454fffff.....
                                ..fffff44444444444444444f.....
                                .....ff4444444444444444ff.....
                                ......fffffffffffffffff.......
                                .........ff.........ff........
                """),
                img("""
                    ............ffffffff..........
                                .ff........fcccccccf.....ff...
                                f22f......fcccccccf.....f77f..
                                ff22f....fffffffff......ff77f.
                                .fff...f.feeeeeeef..f....fff..
                                .......ffffffffffffff.........
                                ........f425555255f...........
                                ...ff...f255555525f...........
                                ..f44f..fff5555ff5f...........
                                ..ff44f.ffff55fff5f...........
                                ...fff..f245555525f.......ff..
                                ........f244455525ff.....faaf.
                                ........f44ffff555f5f....ffaaf
                                .ff...fff4ff222f55f55f....fff.
                                f88f..f4fff2222ffff555f.......
                                ff88fff5554222255555555f......
                                .fff.f55544222555555555f......
                                ....ff555422555555555ffff.....
                                ....ff45555555555555555ff.....
                                ...f4f45555555555555555ff.....
                                ..f44f445525555555f55555f.....
                                ..f44f444425555555f55555f.....
                                .f444f444222555555f55555f.....
                                .f444f4444244455554f5555f.....
                                .f444f4444444444455f555ff.....
                                ..f44f44444444444454fffff.....
                                ..fffff44444444444444444f.....
                                .....ff4444444444444444ff.....
                                ......fffffffffffffffff.......
                                ..........ff.......ff.........
                """),
                img("""
                    ............ffffffff..........
                                .ff........fcccccccf.....ff...
                                f22f......fcccccccf.....f77f..
                                ff22f....fffffffff......ff77f.
                                .fff...f.feeeeeeef..f....fff..
                                .......ffffffffffffff.........
                                ........f425555255f...........
                                ...ff...f255555525f...........
                                ..f44f..fff5555ff5f...........
                                ..ff44f.ffff55fff5f...........
                                ...fff..f245555525f.......ff..
                                ........f244455525ff.....faaf.
                                ........f44ffff555f5f....ffaaf
                                .ff...fff4ff222f55f55f....fff.
                                f88f..f4fff2222ffff555f.......
                                ff88fff5554222255555555f......
                                .fff.f55544222555555555f......
                                ....ff555422555555555ffff.....
                                ....ff45555555555555555ff.....
                                ...f4f45555555555555555ff.....
                                ..f44f445525555555f55555f.....
                                ..f44f444425555555f55555f.....
                                .f444f444222555555f55555f.....
                                .f444f4444244455554f5555f.....
                                .f444f4444444444455f555ff.....
                                ..f44f44444444444454fffff.....
                                ..fffff44444444444444444f.....
                                .....ff4444444444444444ff.....
                                ......fffffffffffffffff.......
                                ...........ff.....ff..........
                """),
                img("""
                    ............ffffffff..........
                                .ff........fcccccccf.....ff...
                                f22f......fcccccccf.....f77f..
                                ff22f....fffffffff......ff77f.
                                .fff...f.feeeeeeef..f....fff..
                                .......ffffffffffffff.........
                                ........f425555255f...........
                                ...ff...f255555525f...........
                                ..f44f..fff5555ff5f...........
                                ..ff44f.ffff55fff5f...........
                                ...fff..f245555525f.......ff..
                                ........f244455525ff.....faaf.
                                ........f44ffff555f5f....ffaaf
                                .ff...fff4ff222f55f55f....fff.
                                f88f..f4fff2222ffff555f.......
                                ff88fff5554222255555555f......
                                .fff.f55544222555555555f......
                                ....ff555422555555555ffff.....
                                ....ff45555555555555555ff.....
                                ...f4f45555555555555555ff.....
                                ..f44f445525555555f55555f.....
                                ..f44f444425555555f55555f.....
                                .f444f444222555555f55555f.....
                                .f444f4444244455554f5555f.....
                                .f444f4444444444455f555ff.....
                                ..f44f44444444444454fffff.....
                                ..fffff44444444444444444f.....
                                .....ff4444444444444444ff.....
                                ......fffffffffffffffff.......
                                ............ff...ff...........
                """),
                img("""
                    ............ffffffff..........
                                .ff........fcccccccf.....ff...
                                f22f......fcccccccf.....f77f..
                                ff22f....fffffffff......ff77f.
                                .fff...f.feeeeeeef..f....fff..
                                .......ffffffffffffff.........
                                ........f425555255f...........
                                ...ff...f255555525f...........
                                ..f44f..fff5555ff5f...........
                                ..ff44f.ffff55fff5f...........
                                ...fff..f245555525f.......ff..
                                ........f244455525ff.....faaf.
                                ........f44ffff555f5f....ffaaf
                                .ff...fff4ff222f55f55f....fff.
                                f88f..f4fff2222ffff555f.......
                                ff88fff5554222255555555f......
                                .fff.f55544222555555555f......
                                ....ff555422555555555ffff.....
                                ....ff45555555555555555ff.....
                                ...f4f45555555555555555ff.....
                                ..f44f445525555555f55555f.....
                                ..f44f444425555555f55555f.....
                                .f444f444222555555f55555f.....
                                .f444f4444244455554f5555f.....
                                .f444f4444444444455f555ff.....
                                ..f44f44444444444454fffff.....
                                ..fffff44444444444444444f.....
                                .....ff4444444444444444ff.....
                                ......fffffffffffffffff.......
                                ...........ff.....ff..........
                """)],
            75,
            True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def nivel6():
    global Libros, Z_vida_reina_Z, vida_boss, sí, reina2, Soldado_, Soldado1_
    info.set_score(4)
    info.change_score_by(1)
    Libros += 1
    info.set_life(5)
    Z_vida_reina_Z = 0
    vida_boss = 0
    sí += 10
    J1.set_position(8, 81)
    tiles.set_tilemap(tilemap("""
        level_25
    """))
    scene.set_background_image(img("""
        ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
    """))
    reina2 = sprites.create(img("""
            . . . 1 1 1 1 1 1 . . 
                    . . 1 1 1 1 1 1 1 . . 
                    . . 1 d d d d 1 1 1 . 
                    . . 1 f d f d d 1 1 . 
                    . . 1 d d d d d 1 1 . 
                    . . 1 f f f f d 1 1 . 
                    . . . d d d d d . . . 
                    . . . 3 3 3 3 3 . . . 
                    . d 3 3 b b 3 3 3 d . 
                    d d 3 b b 3 3 b b d d 
                    d d 3 3 3 3 3 b 3 d d 
                    d d 3 3 3 3 b b 3 d d 
                    d d 3 3 b b b 3 3 d d 
                    . . 3 3 3 3 3 3 3 . . 
                    . . . d d . . d d . . 
                    . . f f f . f f f . .
        """),
        SpriteKind.reina)
    tiles.place_on_tile(reina2, tiles.get_tile_location(5, 6))
    Soldado_ = sprites.create(img("""
            . . . f f f f f . 
                    . . f f f f f f f 
                    . . f f f f f f f 
                    . . f f f f f f f 
                    . . f f f f f f f 
                    . . f f f f f f f 
                    . . f f f f f f f 
                    . . f f f f f f f 
                    . . f f f f f f f 
                    f f f f f f f f f 
                    . . f f d f d d f 
                    . . f d d d d d f 
                    . . f f f f f f f 
                    . . f 2 5 2 2 2 f 
                    . . f 8 8 f 8 8 f 
                    . . . f f . f f .
        """),
        SpriteKind.Soldado)
    tiles.place_on_tile(Soldado_, tiles.get_tile_location(2, 6))
    Soldado1_ = sprites.create(img("""
            . . . f f f f f . 
                    . . f f f f f f f 
                    . . f f f f f f f 
                    . . f f f f f f f 
                    . . f f f f f f f 
                    . . f f f f f f f 
                    . . f f f f f f f 
                    . . f f f f f f f 
                    . . f f f f f f f 
                    f f f f f f f f f 
                    . . f f d f d d f 
                    . . f d d d d d f 
                    . . f f f f f f f 
                    . . f 2 5 2 2 2 f 
                    . . f 8 8 f 8 8 f 
                    . . . f f . f f .
        """),
        SpriteKind.Soldado)
    tiles.place_on_tile(Soldado1_, tiles.get_tile_location(3, 6))

def on_on_overlap14(sprite, otherSprite):
    sprite.destroy()
sprites.on_overlap(SpriteKind.flecha, SpriteKind.barrera6, on_on_overlap14)

def on_right_released():
    if sí == 0:
        animation.run_image_animation(J1,
            [img("""
                . . . . . . . f f f . . . . . . 
                            . . . . . f f c c c f f . . . . 
                            . . . . f c c c c c c c f . . . 
                            . . . f c c c c c c c c c f . . 
                            . . . f c c c f f f c c c f . . 
                            . . . f f f f e e e f f f f . . 
                            . f . f e e e e e e e e e f . f 
                            . f f f f f f f f f f f f f f f 
                            . . . f 5 5 5 5 5 5 5 5 5 f . . 
                            . . . f 5 5 f 5 5 5 f 5 5 f . . 
                            . . . f 5 5 5 5 5 5 5 5 5 f . . 
                            . . . f 5 5 f 5 5 5 f 5 5 f . . 
                            . . . f 5 5 5 f f f 5 5 5 f . . 
                            . . . f 5 5 5 5 5 5 5 5 5 f . . 
                            . . . f 5 5 f f f f f 5 5 f . . 
                            . . . f f f f . . . f f f f . .
            """)],
            250,
            True)
    if sí == 10:
        animation.run_image_animation(J1,
            [img("""
                . . . . . . . f f f . . . . . . 
                            . . . . . f f c c c f f . . . . 
                            . . . . f c c c c c c c f . . . 
                            . . . f c c c c c c c c c f . . 
                            . . . f c c c f f f c c c f . . 
                            . . . f f f f e e e f f f f . . 
                            . f . f e e e e e e e e e f . f 
                            . f f f f f f f f f f f f f f f 
                            . . . f 5 5 5 5 5 5 5 5 5 f . . 
                            . . . f 5 5 f 5 5 5 f 5 5 f . . 
                            f f . f 5 5 5 5 5 5 5 5 5 f . . 
                            8 8 f f 5 5 5 f 5 5 f 5 5 f . . 
                            f 8 f f 5 5 5 5 f f 5 5 5 f . . 
                            . f . f 5 5 5 5 5 5 5 5 5 f . . 
                            . . . f 5 5 f f f f f 5 5 f . . 
                            . . . f f f f . . . f f f f . .
            """)],
            250,
            True)
    if sí == 20:
        animation.run_image_animation(J1,
            [img("""
                . . . . . . . f f f . . . . . . 
                            . . . . . f f c c c f f . . . . 
                            f f . . f c c c c c c c f . . . 
                            2 2 f f c c c c c c c c c f . . 
                            f f . f c c c f f f c c c f . . 
                            . . . f f f f e e e f f f f . . 
                            . f . f e e e e e e e e e f . f 
                            . f f f f f f f f f f f f f f f 
                            . . . f 5 5 5 5 5 5 5 5 5 f . . 
                            . . . f 5 5 f 5 5 5 f 5 5 f . . 
                            f f . f 5 5 5 5 5 5 5 5 5 f . . 
                            8 8 f f 5 5 5 f 5 f 5 5 5 f . . 
                            f 8 f f 5 5 5 5 f 5 5 5 5 f . . 
                            . f . f 5 5 5 5 5 5 5 5 5 f . . 
                            . . . f 5 5 f f f f f 5 5 f . . 
                            . . . f f f f . . . f f f f . .
            """)],
            250,
            True)
    if sí == 30:
        animation.run_image_animation(J1,
            [img("""
                . . . . . . . f f f . . f f . . 
                            . . . . . f f c c c f f 7 7 f . 
                            f f . . f c c c c c c c f 7 7 f 
                            2 2 f f c c c c c c c c c f f . 
                            f f . f c c c f f f c c c f . . 
                            . . . f f f f e e e f f f f . . 
                            . f . f e e e e e e e e e f . f 
                            . f f f f f f f f f f f f f f f 
                            . . . f 5 5 5 5 5 5 5 5 5 f . . 
                            . . . f 5 5 f 5 5 5 f 5 5 f . . 
                            f f . f 5 5 5 5 5 5 5 5 5 f . . 
                            8 8 f f 5 5 5 f f f 5 5 5 f . . 
                            f 8 f f 5 5 5 5 5 5 5 5 5 f . . 
                            . f . f 5 5 5 5 5 5 5 5 5 f . . 
                            . . . f 5 5 f f f f f 5 5 f . . 
                            . . . f f f f . . . f f f f . .
            """)],
            250,
            True)
    if sí == 40:
        animation.run_image_animation(J1,
            [img("""
                . . . . . . . f f f . . f f . . 
                            . . . . . f f c c c f f 7 7 f . 
                            f f . . f c c c c c c c f 7 7 f 
                            2 2 f f c c c c c c c c c f f . 
                            f f . f c c c f f f c c c f . . 
                            . . . f f f f e e e f f f f . . 
                            . f . f e e e e e e e e e f . f 
                            . f f f f f f f f f f f f f f f 
                            . . . f 5 5 5 5 5 5 5 5 5 f . . 
                            . . . f 5 5 f 5 5 5 f 5 5 f f f 
                            f f . f 4 5 5 5 5 5 5 5 5 f a a 
                            8 8 f f 4 5 5 f f f 5 5 5 f a f 
                            f 8 f f 4 4 5 5 5 5 5 5 5 f f . 
                            . f . f 4 4 4 4 4 4 4 5 5 f . . 
                            . . . f 4 4 f f f f f 4 4 f . . 
                            . . . f f f f . . . f f f f . .
            """)],
            250,
            True)
    if sí == 50:
        animation.run_image_animation(J1,
            [img("""
                    .........ffffffff.............
                                .ff......fccccccff.......ff...
                                f22f......fccccccff.....f77f..
                                ff22f......fffffffff....ff77f.
                                .fff....f..feeeeeeef.f...fff..
                                ........ffffffffffffff........
                                ..........f455252555f.........
                                ...ff.....f452555255f.........
                                ..f44f....f4ff555ff5f.........
                                ..ff44f...f4fff5fff5f.........
                                ...fff....f442555255f.....ff..
                                ..........f442445255f....faaf.
                                ..........f44fffff55f....ffaaf
                                .ff.......f4f2222ff5f.....fff.
                                f88f.....fffff2222ffff........
                                ff88f...f4444422224455f.......
                                .fff...f455544222555555f......
                                ......f45555422555555555f.....
                                ......f45555555555555555f.....
                                .....ff45555555555555555ff....
                                .....ff55555552555555555ff....
                                ....f5f55555552555555555f5f...
                                ....f5f45555522255555555f5f...
                                ...f55f44444552555555555f55f..
                                ..f455f44444444555555555f455f.
                                ..f445f44444444455555555f445f.
                                ...f44f44444444444444455f44f..
                                ....ffff444444444444444ffff...
                                .......fffffffffffffffff......
                                .......ff.......ff............
                """),
                img("""
                    .........ffffffff.............
                                .ff......fccccccff.......ff...
                                f22f......fccccccff.....f77f..
                                ff22f......fffffffff....ff77f.
                                .fff....f..feeeeeeef.f...fff..
                                ........ffffffffffffff........
                                ..........f455252555f.........
                                ...ff.....f452555255f.........
                                ..f44f....f4ff555ff5f.........
                                ..ff44f...f4fff5fff5f.........
                                ...fff....f442555255f.....ff..
                                ..........f442445255f....faaf.
                                ..........f44fffff55f....ffaaf
                                .ff.......f4f2222ff5f.....fff.
                                f88f.....fffff2222ffff........
                                ff88f...f4444422224455f.......
                                .fff...f455544222555555f......
                                ......f45555422555555555f.....
                                .....ff45555555555555555ff....
                                .....ff45555555555555555ff....
                                ....f5f55555552555555555f5f...
                                ....f5f55555552555555555f5f...
                                ...f55f45555522255555555f55f..
                                ..f455f44444552555555555f455f.
                                ..f445f44444444555555555f445f.
                                ...f44f44444444455555555f44f..
                                ....fff44444444444444455fff...
                                ......ff444444444444444ff.....
                                .......fffffffffffffffff......
                                .......ff.......ff............
                """)],
            550,
            True)
controller.right.on_event(ControllerButtonEvent.RELEASED, on_right_released)

def on_on_destroyed2(sprite):
    muro42.destroy()
sprites.on_destroyed(SpriteKind.B5, on_on_destroyed2)

def on_left_released():
    if sí == 0:
        animation.run_image_animation(J1,
            [img("""
                . . . . . . . f f f . . . . . . 
                            . . . . . f f c c c f f . . . . 
                            . . . . f c c c c c c c f . . . 
                            . . . f c c c c c c c c c f . . 
                            . . . f c c c f f f c c c f . . 
                            . . . f f f f e e e f f f f . . 
                            . f . f e e e e e e e e e f . f 
                            . f f f f f f f f f f f f f f f 
                            . . . f 5 5 5 5 5 5 5 5 5 f . . 
                            . . . f 5 5 f 5 5 5 f 5 5 f . . 
                            . . . f 5 5 5 5 5 5 5 5 5 f . . 
                            . . . f 5 5 f 5 5 5 f 5 5 f . . 
                            . . . f 5 5 5 f f f 5 5 5 f . . 
                            . . . f 5 5 5 5 5 5 5 5 5 f . . 
                            . . . f 5 5 f f f f f 5 5 f . . 
                            . . . f f f f . . . f f f f . .
            """)],
            250,
            True)
    if sí == 10:
        animation.run_image_animation(J1,
            [img("""
                . . . . . . . f f f . . . . . . 
                            . . . . . f f c c c f f . . . . 
                            . . . . f c c c c c c c f . . . 
                            . . . f c c c c c c c c c f . . 
                            . . . f c c c f f f c c c f . . 
                            . . . f f f f e e e f f f f . . 
                            . f . f e e e e e e e e e f . f 
                            . f f f f f f f f f f f f f f f 
                            . . . f 5 5 5 5 5 5 5 5 5 f . . 
                            . . . f 5 5 f 5 5 5 f 5 5 f . . 
                            f f . f 5 5 5 5 5 5 5 5 5 f . . 
                            8 8 f f 5 5 5 f 5 5 f 5 5 f . . 
                            f 8 f f 5 5 5 5 f f 5 5 5 f . . 
                            . f . f 5 5 5 5 5 5 5 5 5 f . . 
                            . . . f 5 5 f f f f f 5 5 f . . 
                            . . . f f f f . . . f f f f . .
            """)],
            250,
            True)
    if sí == 20:
        animation.run_image_animation(J1,
            [img("""
                . . . . . . . f f f . . . . . . 
                            . . . . . f f c c c f f . . . . 
                            f f . . f c c c c c c c f . . . 
                            2 2 f f c c c c c c c c c f . . 
                            f f . f c c c f f f c c c f . . 
                            . . . f f f f e e e f f f f . . 
                            . f . f e e e e e e e e e f . f 
                            . f f f f f f f f f f f f f f f 
                            . . . f 5 5 5 5 5 5 5 5 5 f . . 
                            . . . f 5 5 f 5 5 5 f 5 5 f . . 
                            f f . f 5 5 5 5 5 5 5 5 5 f . . 
                            8 8 f f 5 5 5 f 5 f 5 5 5 f . . 
                            f 8 f f 5 5 5 5 f 5 5 5 5 f . . 
                            . f . f 5 5 5 5 5 5 5 5 5 f . . 
                            . . . f 5 5 f f f f f 5 5 f . . 
                            . . . f f f f . . . f f f f . .
            """)],
            250,
            True)
    if sí == 30:
        animation.run_image_animation(J1,
            [img("""
                . . . . . . . f f f . . f f . . 
                            . . . . . f f c c c f f 7 7 f . 
                            f f . . f c c c c c c c f 7 7 f 
                            2 2 f f c c c c c c c c c f f . 
                            f f . f c c c f f f c c c f . . 
                            . . . f f f f e e e f f f f . . 
                            . f . f e e e e e e e e e f . f 
                            . f f f f f f f f f f f f f f f 
                            . . . f 5 5 5 5 5 5 5 5 5 f . . 
                            . . . f 5 5 f 5 5 5 f 5 5 f . . 
                            f f . f 5 5 5 5 5 5 5 5 5 f . . 
                            8 8 f f 5 5 5 f f f 5 5 5 f . . 
                            f 8 f f 5 5 5 5 5 5 5 5 5 f . . 
                            . f . f 5 5 5 5 5 5 5 5 5 f . . 
                            . . . f 5 5 f f f f f 5 5 f . . 
                            . . . f f f f . . . f f f f . .
            """)],
            250,
            True)
    if sí == 40:
        animation.run_image_animation(J1,
            [img("""
                . . . . . . . f f f . . f f . . 
                            . . . . . f f c c c f f 7 7 f . 
                            f f . . f c c c c c c c f 7 7 f 
                            2 2 f f c c c c c c c c c f f . 
                            f f . f c c c f f f c c c f . . 
                            . . . f f f f e e e f f f f . . 
                            . f . f e e e e e e e e e f . f 
                            . f f f f f f f f f f f f f f f 
                            . . . f 5 5 5 5 5 5 5 5 5 f . . 
                            . . . f 5 5 f 5 5 5 f 5 5 f f f 
                            f f . f 4 5 5 5 5 5 5 5 5 f a a 
                            8 8 f f 4 5 5 f f f 5 5 5 f a f 
                            f 8 f f 4 4 5 5 5 5 5 5 5 f f . 
                            . f . f 4 4 4 4 4 4 4 5 5 f . . 
                            . . . f 4 4 f f f f f 4 4 f . . 
                            . . . f f f f . . . f f f f . .
            """)],
            250,
            True)
    if sí == 50:
        animation.run_image_animation(J1,
            [img("""
                    .........ffffffff.............
                                .ff......fccccccff.......ff...
                                f22f......fccccccff.....f77f..
                                ff22f......fffffffff....ff77f.
                                .fff....f..feeeeeeef.f...fff..
                                ........ffffffffffffff........
                                ..........f455252555f.........
                                ...ff.....f452555255f.........
                                ..f44f....f4ff555ff5f.........
                                ..ff44f...f4fff5fff5f.........
                                ...fff....f442555255f.....ff..
                                ..........f442445255f....faaf.
                                ..........f44fffff55f....ffaaf
                                .ff.......f4f2222ff5f.....fff.
                                f88f.....fffff2222ffff........
                                ff88f...f4444422224455f.......
                                .fff...f455544222555555f......
                                ......f45555422555555555f.....
                                ......f45555555555555555f.....
                                .....ff45555555555555555ff....
                                .....ff55555552555555555ff....
                                ....f5f55555552555555555f5f...
                                ....f5f45555522255555555f5f...
                                ...f55f44444552555555555f55f..
                                ..f455f44444444555555555f455f.
                                ..f445f44444444455555555f445f.
                                ...f44f44444444444444455f44f..
                                ....ffff444444444444444ffff...
                                .......fffffffffffffffff......
                                .......ff.......ff............
                """),
                img("""
                    .........ffffffff.............
                                .ff......fccccccff.......ff...
                                f22f......fccccccff.....f77f..
                                ff22f......fffffffff....ff77f.
                                .fff....f..feeeeeeef.f...fff..
                                ........ffffffffffffff........
                                ..........f455252555f.........
                                ...ff.....f452555255f.........
                                ..f44f....f4ff555ff5f.........
                                ..ff44f...f4fff5fff5f.........
                                ...fff....f442555255f.....ff..
                                ..........f442445255f....faaf.
                                ..........f44fffff55f....ffaaf
                                .ff.......f4f2222ff5f.....fff.
                                f88f.....fffff2222ffff........
                                ff88f...f4444422224455f.......
                                .fff...f455544222555555f......
                                ......f45555422555555555f.....
                                .....ff45555555555555555ff....
                                .....ff45555555555555555ff....
                                ....f5f55555552555555555f5f...
                                ....f5f55555552555555555f5f...
                                ...f55f45555522255555555f55f..
                                ..f455f44444552555555555f455f.
                                ..f445f44444444555555555f445f.
                                ...f44f44444444455555555f44f..
                                ....fff44444444444444455fff...
                                ......ff444444444444444ff.....
                                .......fffffffffffffffff......
                                .......ff.......ff............
                """)],
            550,
            True)
controller.left.on_event(ControllerButtonEvent.RELEASED, on_left_released)

def nivel2():
    global Libros, sí, eoaiu, burbuja, burbuja2, burbuja3, burbuja4, burbuja5, cartel, Malo_, malo2, malo3, malo4, ballestero, Barrera_, Barrera2_, barrera__3, barrera4_, barrera5_, barrera6_, Monster, libro_2_londrés
    info.set_score(1)
    info.change_score_by(1)
    J1.set_position(20, 79)
    Libros += 1
    info.set_life(5)
    sí += 10
    tiles.set_tilemap(tilemap("""
        level_26
    """))
    scene.set_background_image(img("""
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111991199999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111111119999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999111111111111199999999999999999999999999
                9999999999999999999999999999999999999999999999999991111111111999999999999999999bbbbb9999999999999999999999999999999999999999999991111111111111999999999999999999
                999999999999999999999999999999999999999999999999111111111111119bbbbbb9999999999bbbbb999999999999bbbbb99999999999999999999999999999999991111111119999999999999999
                999999999999999999999999999999999999999999999991111111111111119bbbbbb99ddddddddbbbbbdddddddddd99bbbbb99999999999999999999999999999999999999999999999999999999999
                999999999999999999999999999999999999999999999991111111111111111bbbbbbdddddddddddddddddddddddddddbbbbb99999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999911111111111111111dddddddd111111111111111111111dddddddd91111111999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999911111111111111dddddd1111199999999999999999999911111dddddd11111999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999911111111111dddddd11111111199999999999999999999999f9111dddddd111bbbb9999999999999999999999999999999999999999999999
                111119999999999999999999999999999999999999999991bbbbb111ddddd1111111111111999999999999999999999f99999111ddddd9bbbbb999999999999999999999999999999999999999999999
                111111999999999999999999999999999999999999999999bbbbb1ddddd111111111111111199999999999999999999f9999999911ddddbbbbb999999999999999999999999999999999999999999999
                111111199999999999999999999999999999999999999999bbbbbddd111999911111111111199999999999999999999f9999999999111ddbbbb999999999999999999999999999999999999999999999
                111111111119999999999999999999999999999999999999bbbbbd11191111999111111111199999999999999999999f999999999999111ddd9999999999999999999999999999999999999999999999
                1111111111111999999999999999999999999999999999999dddd11999911119999111111199999999999999999999f99999999999999911dddd99999999999999999999999999999999999999999999
                111111111111199999999999999999999999999999999999ddd11f9999999111999991111199999999999999999999f9999999999999999911ddd9999999999999999999999999999999999999999999
                111111111111119999999999999999999999999bbb9999ddd11999f999999999999999999999999999999999999999f999999999999999999911ddd99999999999999999999999999999999999999999
                111111111111119999999999999999999999999bbbbb9ddd119999f999999999999999999999999999999999999999f9999999999999999999911ddd9999999999999999999999999999999999999999
                999111111111199999999999999999999999999bbbbbdd119999999f9999999999999999999999999999999999999f9999999999999999999999911dd999999999999999999999999999999999999999
                999999991111199999999999999999999999999bbbbbd11999999999f999999999999999999999999999999999999f99999999999999999999999911ddd9999999999999999999999999999999999999
                999999999999999999999999999999999999999bbbdd119999999999f999999999999999999999999999999999999f999999999999999999999999911ddd9bbbb9999999999999999999999999999999
                9999999999999999999999999999999999999999ddd19999999999999f99999999999999999999999999999999999f9999999999999999999999999991dddbbbb9999999999999999999999999999999
                999999999999999999999999999999999999999ddd199999999999999f99999999999999999999999999999999999f99999999999999999999999999991ddbbbb9999999999999999999999999999999
                99999999999999999999999999999999999999ddd19999999999999999f999999999999999999999999999999999f9999999999999999999999999999991ddbbb9999999999999999999999999999999
                9999999999999999999999999999999999999ddd1999999999999999999f99999999999999999999999999999999f99999999999999999999999999999991ddd99999999999999999999999999999999
                999999999999999999999999999999999999ddd19999999999999999999f99999999999999999999999999999999f999999999999999999999999999999991ddd9999999999999999999999999999999
                999999999999999999999999999999999999dd1999999999999999999999f9999999999999999999999999999999f9999999999999999999999999999999991dd9999999999999999999999999999999
                99999999999999999999999999999bbbb99dd19999999999999999999999f999999999999999999999999999999f999999999999999999999999999999999991dd999999999999999999999999999999
                99999999999999999999999999999bbbbbdd1199999999999999999999999f99999999999999999999999999999f9999999999999999999999999999999999911dd99999999999999999999999999999
                99999999999999999999999999999bbbbbd11999999999999999999999999f99999999999999999999999999999f99999999999999999999999999999999999911dd9999999999999999999999999999
                99999999999999999999999999999bbbbbd199999999999999999999999999f9999999999999999999999999999f99999999999999999999999999999999999991dd9999999999999999999999999999
                99999999999999999999999999999bbbbb19999999999999999999999999999f99999999999999999999999999f9999999999999999999999999999999999999991dd999999999999999999999999999
                9999999999999999999999999999999dd119999999999999999999999999999f99999999999999999999999999f99999999999999999999999999999999999999911ddbbb99999999999999999999999
                9999999999999999999999999999999dd19f9999999999999999999999999999f9999999999999999999999999f999999999999999999999999999999999999999f1ddbbbb9999999999999999999999
                999999999999999999999999999999dd1999ff99999999999999999999999999f9999999999999999999999999f9999999999999999999999999999999999999ff991dbbbb9999999999999999999999
                99999999999999999999999999999ddd199999f99999999999999999999999999f99999999999999999999999f9999999999999999999999999999999999999f99991dbbbb9999999999999999999999
                99999999999999999999999999999dd19999999f99999999999999999999999999f9999999999999999999999f99999999999999999999999999999999999ff9999991dbbb9999999999999999999999
                9999999999999999999999999999dd1199999999ff999999999999999999999999f9999999999999999999999f9999999999999999999999999999999999f9999999911dd99999999999999999999999
                9999999999999999999999999999dd199999999999f999999999999999999999999f999999999999999999999f99999999999999999999999999999999ff99999999991dd99999999999999999999999
                999999999999999999999999999dd11999999999999ff9999999999999999999999f999999999999999999999f9999999999999999999999999999999f99999999999911dd9999999999999999999999
                999999999999999999999999999dd1999999999999999f9999999999999999999999f9999999999999999999f999999999999999999999999999999ff999999999999991dd9999999999999999999999
                99999999999999999999999999ddd19999999999999999f9999999999999999999999f999999999999999999f99999999999999999999999999999f99999999999999991ddd999999999999999999999
                99999999999999999999999bbbbd1999999999999999999ff99999999999999999999f999999999999999999f999999999999999999999999999ff9999999999999999991dd999999999999999999999
                99999999999999999999999bbbbd199999999999999999999f99999999999999999999f99999999999999999f99999999999999999999999999f999999999999999999991dd999999999999999999999
                99999999999999999999999bbbb19999999999999999999999ff999999999999999999f9999999999999999f9999999999999999999999999ff99999999999999999999991dd99999999999999999999
                99999999999999999999999bbbd1999999999999999999999999f999999999999999999f999999999999999f999999999999999999999999f9999999999999999999999991ddbbb99999999999999999
                99999999999999999999999bbbd19999999999999999999999999f999999999999999999f99999999999999f9999999999999999999999ff99999999999999999999999991ddbbb99999999999999999
                999999999999999999999999dd1999999999999999999999999999ff9999999999999999f99999999999999f999999999999999999999f99999999999999999999999999991dbbbb9999999999999999
                999999999999999999999999dd199999999999999999999999999999f9999999999999999f999999999999f99999999999999999999ff999999999999999999999999999991dbbbb9999999999999999
                999999999999999999999999dd1999999999999999999999999999999f999999999999999f999999999999f9999999999999999999f99999999999999999999999999999991dbbbb9999999999999999
                99999999999999999999999dd199999999999999999999999999999999ff99999999999999f99999999999f999999999999999999f9999999999999999999999999999999991dbbb9999999999999999
                99999999999999999999999dd19999999999999999999999999999999999f99999999999999f9999999999f9999999999999999ff99999999999999999999999999999999991dd999999999999999999
                99999999999999999999999dd199999999999999999999999999999999999ff999999999999f999999999f9999999999999999f9999999999999999999999999999999999991dd999999999999999999
                99999999999999999999999dd19999999999999999999999999999999999999f999999999999f99999999f99999999999999ff99999999999999999999999999999999999991dd999999999999999999
                9999999999999999999999ddd199999999999999999999999999999999999999f99999999999f99999999f9999999999999f9999999999999999999999999999999999999991ddd99999999999999999
                9999999999999999999999dd19999999999999999999999999999999999999999ff9999999999f9999999f99999999999ff999999999999999999999999999999999999999991dd99999999999999999
                9999999999999999999999dd1999999999999999999999999999999999999999999f999999999f9999999f9999999999f99999999999999999999999999999999999999999991dd99999999999999999
                99999999999999999999bbbd19999999999999999999999999999999999999999999ff99999999f99999f999999999ff999999999999999999999999999999999999999999991dd99999999999999999
                9999999999999999999bbbbd1999999999999999999999999999999999999999999999f99999999f9999f99999999f99999999999999999999999999999999999999999999991dd99999999999999999
                9999999999999999999bbbbd19999999999999999999999999999999999999999999999f9999999f9999f999999ff999999999999999999999999999999999999999999999991dd99999999999999999
                9999999999999999999bbbbd199999999999999999999999999999999999999999999999ff999999f999f99999f99999999999999999999999999999999999999999999999991dd99999999999999999
                9999999999999999999999dd19999999999999999999999999999999999999999999999999f99999f99f9999ff999999999999999999999999999999999999999999999999991dd99999999999999999
                9999999999999999999999dd199999999999999999999999999999999999999999999999999ff9999f9f999f99999999999999999999999999999999999999999999999999991dbbb999999999999999
                9999999999999999999999dd19999999999999999999999999999999999999999999999999999f9999ff9ff999999999999999999999999999999999999999999999999999991dbbb999999999999999
                9999999999999999999999dd199999999999999999999999999999999999999999999999999999f999fff99999999999999999999999999999999999999999999999999999991dbbb999999999999999
                9999999999999999999999dd1999999999999999999999999999999999999999999999999999999ff9ffff9999999999999999999999999999999999999999999999999999991dbbb999999999999999
                9999999999999999999999dd19999999999999999999999999999999999999999999999999999999111111fff9999999999999999999999999999999999999999999999999991dbbb999999999999999
                9999999999999999999999dd1999999999999999999999999999999999999999999999999fffffff111111999fff9999999999999999999999999999999999999999999999991dd99999999999999999
                9999999999999999999999dd19999999999999999999999999999999999ffffffffffffff9999999111111999999fff9999999999999999999999999999999999999999999991dd99999999999999999
                9999999999999999999999dd1999999999999999999999fffffffffffff99999999999999999999f111111999999999fff9999999999999999999999999999999999999999991dd99999999999999999
                9999999999999999999999dd19999999ffffffffffffff99999999999999999999999999999999f1111111199999999999ff99999999999999999999999999999999999999991dd99999999999999999
                9999999999999999999999dd1fffffff999999999999999999999999999999999999999999999f9111111119999999999999fff99999999999999999999999999999999999991dd99999999999999999
                99999999999999999999bbbd1999999999999999999999999999999999999999999999999999f991119f111f999999999999999fff99999999999999999999999999999999991dd99999999999999999
                99999999999999999999bbbd199999999999999999999999999999999999999999999999999f9991119f1119f99999999999999999fff99999999999999999999999999999991dd99999999999999999
                99999999999999999999bbbd19999999999999999999999999999999999999999999999999f99991119f11119f9999999999999999999fff99999999999999999999999999991dd99999999999999999
                99999999999999999999bbbd1999999999999999999999999999999999999999999999999f999911119f111199f999999999999999999999fff99999999999999999999999991dd99999999999999999
                99999999999999999999bbbdd199999999999999999999999999999999999999999999999f999911119f911199f999999999999999999999999fff9999999999999999999991ddd99999999999999999
                99999999999999999999999dd19999999999999999999999999999999999999999999999f9999911199f9111999f99999999999999999999999999fff9999999999999999991dd999999999999999999
                99999999999999999999999dd1999999999999999999999999999999999999999999999f99999911199f91111999f9999999999999999999999999999fff9999999999999991dd999999999999999999
                99999999999999999999999dd199999999999999999999999999999999999999999999f999999111199f911119999f999999999999999999999999999999ff99999999999991dd999999999999999999
                99999999999999999999999dd19999999999999999999999999999999999999999999f9999999111199f9911199999f9999999999999999999999999999999fff99999999991dd999999999999999999
                999999999999999999999999dd199999999999999999999999999999999999999999f99999999111999f99111999999f999999999999999999999999999999999fff9999991dbbbb9999999999999999
                999999999999999999999999dd19999999999999999999999999999999999999999f999999999111999f991111999999f99999999999999999999999999999999999fff9991dbbbb9999999999999999
                999999999999999999999999dd1999999999999999999999999999999999999999f9999999991111999f991111999999f99999999999999999999999999999999999999ff91dbbbb9999999999999999
                9999999999999999999999999dd19999999999999999999999999999999999999f99999999991111999f9991119999999f9999999999999999999999999999999999999991ddbbb99999999999999999
                9999999999999999999999999dd1999999999999999999999999999999999999f999999999991119999f99911199999999f999999999999999999999999999999999999991ddbbb99999999999999999
                9999999999999999999999999dd199999999999999999999999999999999999f9999999999991119999f999111199999999f99999999999999999999999999999999999991ddbbb99999999999999999
                99999999999999999999999999dd1999999999999999999999999999999999f99999999999911119999f9991111999999999f999999999999999999999999999999999991dd999999999999999999999
                99999999999999999999999999dd199999999999999999999999999999999f999999999999911119999f99991119999999999f99999999999999999999999999999999991dd999999999999999999999
                999999999999999999999999bbbdd19999999999999999999999999999999f999999999999911199999f999911199999999999f999999999999999999999999999999991ddd999999999999999999999
                999999999999999999999999bbbbd1999999999999999999999999999999f9999999999999911199999f999911119999999999f999999999999999999999999999999991dd9999999999999999999999
                999999999999999999999999bbbbd119999999999999999999999999999f99999999999999911199999f9999111199999999999f99999999999999999999999999999911dd9999999999999999999999
                9999999999999999999999999bbbdd1999999999999999999999999999f999999999999999111199999f99999111999999999999f999999999999999999999999999991dd99999999999999999999999
                9999999999999999999999999bbbdd119999999999999999999999999f9999999999999999111199999f999991111999999999999f99999999999999999999999999911bbbb999999999999999999999
                99999999999999999999999999999dd1999999999999999999999999f99999999999999999111999999f9999911119999999999999f999999999999999999999999991dbbbb999999999999999999999
                99999999999999999999999999999ddd19999999999999999999999f999999999999999999111999999f99999911199999999999999f9999999999999999999999991ddbbbb999999999999999999999
                999999999999999999999999999999dd1999999999999999999999f9999999999999999991111999999f999999111999999999999999f999999999999999999999991ddbbb9999999999999999999999
                9999999999999999999999999999999dd19999999999999999999f99999999999999999991111999999f9999991111999999999999999f9999999999999999999991dd99999999999999999999999999
                9999999999999999999999999999999dd1199999999999999999f999999999999999999991119999999f9999991111999999999999999f9999999999999999999911dd99999999999999999999999999
                99999999999999999999999999999999dd19999999999999999f9999999999999999999991119999999f99999991119999999999999999f99999999999999999991dd999999999999999999999999999
                999999999999999999999999999999bbbbd199999999999999f99999999999999999999911119999999f999999911199999999999999999f999999999999999991dd9999999999999999999999999999
                999999999999999999999999999999bbbbd11999999999999f999999999999999999999911119999999f9999999111199999999999999999f99999999999999911dd9999999999999999999999999999
                999999999999999999999999999999bbbbdd1199999999999f999999999999999999999911199999999f99999991111999999999999999999f999999999999911dd99999999999999999999999999999
                9999999999999999999999999999999bbb9dd19999999999f9999999999999999999999911199999999f999999991119999999999999999999f9999999999991dd999999999999999999999999999999
                999999999999999999999999999999999999dd199999999f99999999999999999999999111199999999f9999999911199999999999999999999f99999999991dbbb99999999999999999999999999999
                999999999999999999999999999999999999ddd1999999f999999999999999999999999111199999999f9999999911119999999999999999999f9999999991dbbbb99999999999999999999999999999
                9999999999999999999999999999999999999ddd19999f9999999999999999999999999111999999999f99999999111199999999999999999999f99999991ddbbbb99999999999999999999999999999
                99999999999999999999999999999999999999ddd199f99999999999999999999999999111999999999f999999999111999999999999999999999f999991dddbbbb99999999999999999999999999999
                9999999999999999999999999999999999999bbbdd1f999999999999999999999999999111999999999f9999999991119999999999999999999999f9991ddd9bbb999999999999999999999999999999
                9999999999999999999999999999999999999bbbbdd1999999999999999999999999991111999999999f99999999911119999999999999999999999f91ddd99999999999999999999999999999999999
                9999999999999999999999999999999999999bbbbbdd119999999999999999999999991111999999999f9999999991111f99999999999999999999911ddd999999999999999999999999999999999999
                9999999999999999999999999999999999999bbbbbddd11999999999999999999999991119999999999f9999999999111f9999999999999999999911ddd9999999999999999999999999999999999999
                99999999999999999999999999999999999999bbbb99dd1199999999999999999999991119999999999f99999999991119f99999999999999999911dd999999999999999999999999999999999999999
                999999999999999999999999999999999999999999999ddd11999999999999999999911119999999999f99999999991111f999999999999999911ddbbb99999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999ddd1199999999999999999911119999999999f999999999911119f9999999999999911ddbbbb99999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999bbbdd11999999999999999911199999999999f999999999991119f99999999999911ddbbbbbb99999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999bbbbbdd119999999999999911199999999999f9999999999911199f99999999911ddddbbbbbb99999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999bbbbbddd11199999999999111199999999999f9999999999911119f9999999111ddd99bbbb9999999999999999999999999999999999999999
                99999999999999999999999999999999999999999999999bbbb9dddd111999999999111199999999999f99999999999111199f9999111dddd99999999999999999999999999999999999999999999999
    """))
    aquarius.destroy()
    oso2.destroy()
    avión.destroy()
    avión.destroy()
    avión.destroy()
    avión.destroy()
    avión.destroy()
    avión.destroy()
    avión.destroy()
    avión.destroy()
    avión.destroy()
    avión.destroy()
    avión.destroy()
    eoaiu = 0
    burbuja = sprites.create(img("""
            . . . . 6 6 6 6 6 6 6 . . . . 
                    . . 6 6 6 6 6 6 6 6 6 6 6 . . 
                    . 6 6 6 6 6 6 6 9 6 6 6 6 6 . 
                    . 6 6 6 6 6 6 6 6 6 9 6 6 6 . 
                    6 6 6 6 6 6 6 6 6 6 6 9 6 6 6 
                    6 6 6 6 6 6 6 6 6 6 6 6 9 6 6 
                    6 6 6 6 6 6 6 6 6 6 6 6 9 6 6 
                    6 6 6 6 6 6 6 6 6 6 6 6 9 6 6 
                    6 8 6 6 6 6 6 6 6 6 6 6 9 6 6 
                    6 8 8 6 6 6 6 6 6 6 6 6 6 6 6 
                    6 8 8 8 6 6 6 6 6 6 6 6 6 6 6 
                    . 6 8 8 6 6 6 6 6 6 6 6 6 6 . 
                    . 6 8 8 8 8 6 6 6 6 6 6 6 6 . 
                    . . 6 6 8 8 8 6 6 6 6 6 6 . . 
                    . . . . 6 6 6 6 6 6 6 . . . .
        """),
        SpriteKind.bubrbuja_)
    burbuja.set_position(50, 104)
    burbuja2 = sprites.create(img("""
            . . . . 6 6 6 6 6 6 6 . . . . 
                    . . 6 6 6 6 6 6 6 6 6 6 6 . . 
                    . 6 6 6 6 6 6 6 9 6 6 6 6 6 . 
                    . 6 6 6 6 6 6 6 6 6 9 6 6 6 . 
                    6 6 6 6 6 6 6 6 6 6 6 9 6 6 6 
                    6 6 6 6 6 6 6 6 6 6 6 6 9 6 6 
                    6 6 6 6 6 6 6 6 6 6 6 6 9 6 6 
                    6 6 6 6 6 6 6 6 6 6 6 6 9 6 6 
                    6 8 6 6 6 6 6 6 6 6 6 6 9 6 6 
                    6 8 8 6 6 6 6 6 6 6 6 6 6 6 6 
                    6 8 8 8 6 6 6 6 6 6 6 6 6 6 6 
                    . 6 8 8 6 6 6 6 6 6 6 6 6 6 . 
                    . 6 8 8 8 8 6 6 6 6 6 6 6 6 . 
                    . . 6 6 8 8 8 6 6 6 6 6 6 . . 
                    . . . . 6 6 6 6 6 6 6 . . . .
        """),
        SpriteKind.bubrbuja_)
    burbuja2.set_position(86, 104)
    burbuja3 = sprites.create(img("""
            . . . . 6 6 6 6 6 6 6 . . . . 
                    . . 6 6 6 6 6 6 6 6 6 6 6 . . 
                    . 6 6 6 6 6 6 6 9 6 6 6 6 6 . 
                    . 6 6 6 6 6 6 6 6 6 9 6 6 6 . 
                    6 6 6 6 6 6 6 6 6 6 6 9 6 6 6 
                    6 6 6 6 6 6 6 6 6 6 6 6 9 6 6 
                    6 6 6 6 6 6 6 6 6 6 6 6 9 6 6 
                    6 6 6 6 6 6 6 6 6 6 6 6 9 6 6 
                    6 8 6 6 6 6 6 6 6 6 6 6 9 6 6 
                    6 8 8 6 6 6 6 6 6 6 6 6 6 6 6 
                    6 8 8 8 6 6 6 6 6 6 6 6 6 6 6 
                    . 6 8 8 6 6 6 6 6 6 6 6 6 6 . 
                    . 6 8 8 8 8 6 6 6 6 6 6 6 6 . 
                    . . 6 6 8 8 8 6 6 6 6 6 6 . . 
                    . . . . 6 6 6 6 6 6 6 . . . .
        """),
        SpriteKind.bubrbuja_)
    burbuja3.set_position(104, 104)
    burbuja4 = sprites.create(img("""
            . . . . 6 6 6 6 6 6 6 . . . . 
                    . . 6 6 6 6 6 6 6 6 6 6 6 . . 
                    . 6 6 6 6 6 6 6 9 6 6 6 6 6 . 
                    . 6 6 6 6 6 6 6 6 6 9 6 6 6 . 
                    6 6 6 6 6 6 6 6 6 6 6 9 6 6 6 
                    6 6 6 6 6 6 6 6 6 6 6 6 9 6 6 
                    6 6 6 6 6 6 6 6 6 6 6 6 9 6 6 
                    6 6 6 6 6 6 6 6 6 6 6 6 9 6 6 
                    6 8 6 6 6 6 6 6 6 6 6 6 9 6 6 
                    6 8 8 6 6 6 6 6 6 6 6 6 6 6 6 
                    6 8 8 8 6 6 6 6 6 6 6 6 6 6 6 
                    . 6 8 8 6 6 6 6 6 6 6 6 6 6 . 
                    . 6 8 8 8 8 6 6 6 6 6 6 6 6 . 
                    . . 6 6 8 8 8 6 6 6 6 6 6 . . 
                    . . . . 6 6 6 6 6 6 6 . . . .
        """),
        SpriteKind.bubrbuja_)
    burbuja4.set_position(220, 104)
    burbuja5 = sprites.create(img("""
            . . . . 6 6 6 6 6 6 6 . . . . 
                    . . 6 6 6 6 6 6 6 6 6 6 6 . . 
                    . 6 6 6 6 6 6 6 9 6 6 6 6 6 . 
                    . 6 6 6 6 6 6 6 6 6 9 6 6 6 . 
                    6 6 6 6 6 6 6 6 6 6 6 9 6 6 6 
                    6 6 6 6 6 6 6 6 6 6 6 6 9 6 6 
                    6 6 6 6 6 6 6 6 6 6 6 6 9 6 6 
                    6 6 6 6 6 6 6 6 6 6 6 6 9 6 6 
                    6 8 6 6 6 6 6 6 6 6 6 6 9 6 6 
                    6 8 8 6 6 6 6 6 6 6 6 6 6 6 6 
                    6 8 8 8 6 6 6 6 6 6 6 6 6 6 6 
                    . 6 8 8 6 6 6 6 6 6 6 6 6 6 . 
                    . 6 8 8 8 8 6 6 6 6 6 6 6 6 . 
                    . . 6 6 8 8 8 6 6 6 6 6 6 . . 
                    . . . . 6 6 6 6 6 6 6 . . . .
        """),
        SpriteKind.bubrbuja_)
    burbuja5.set_position(68, 104)
    cartel = sprites.create(img("""
            e e e e e e e e e e e e e e e e e e 
                    e e e f e e e e e f e e e e f f e e 
                    e e f f f e e e e f e e e f e e f e 
                    e f f f f f e f f f f f e f f f f e 
                    e f f f f f e e e f e e e f e e f e 
                    e f f f f f e e e f e e e f e e f e 
                    e e e e e e e e e e e e e e e e e e
        """),
        SpriteKind.decoración)
    cartel.set_position(200, 88)
    Malo_ = sprites.create(img("""
            . . . . . . . . f f f . . . . . 
                    . . . . . . . f 2 2 2 f . . . . 
                    . . . . . . f 2 2 f f . . . . . 
                    . . . . . f f f f f f . . . . . 
                    . . . . f 1 1 1 1 1 d f . . . . 
                    . . . . f 1 1 1 1 1 d f . . . . 
                    . . . . f 1 f 1 f 1 d f . . . . 
                    f f . . f 1 1 1 1 d d f . . f . 
                    f 9 f f . f 1 1 d f f . . f 1 f 
                    f 9 9 b f 1 f f f 1 d f . f 1 f 
                    . f b f f 1 1 2 1 1 d f . f 2 f 
                    . . f 1 f 1 2 2 2 1 d f f f 2 f 
                    . . f d f 1 1 2 1 1 d f 1 f d f 
                    . . . f f 1 1 2 1 d d f 1 f d f 
                    . . . . f 1 1 f 1 d d f f . f . 
                    . . . . f f f . f f f . . . . .
        """),
        SpriteKind.enemy)
    Malo_.set_position(235, 95)
    Malo_.set_velocity(50, 120)
    malo2 = sprites.create(img("""
            . . . . . . . . f f f . . . . . 
                    . . . . . . . f 8 8 8 f . . . . 
                    . . . . . . f 8 8 f f . . . . . 
                    . . . . . f f f f f f . . . . . 
                    . . . . f 1 1 1 1 1 d f . . . . 
                    . . . . f 1 1 1 1 1 d f . . . . 
                    . . . . f 1 f 1 f 1 d f . . . . 
                    f f . . f 1 1 1 1 d d f . . f . 
                    f 9 f f . f 1 1 d f f . . f 1 f 
                    f 9 9 b f 1 f f f 1 d f . f 1 f 
                    . f b f f 1 1 8 1 1 d f . f 8 f 
                    . . f 1 f 1 8 8 8 1 d f f f 8 f 
                    . . f d f 1 1 8 1 1 d f 1 f d f 
                    . . . f f 1 1 8 1 d d f 1 f d f 
                    . . . . f 1 1 f 1 d d f f . f . 
                    . . . . f f f . f f f . . . . .
        """),
        SpriteKind.enemy)
    malo2.set_position(290, 98)
    malo2.set_velocity(65, 120)
    malo3 = sprites.create(img("""
            . . . . . . . . f f f . . . . . 
                    . . . . . . . f 4 4 4 f . . . . 
                    . . . . . . f 4 4 f f . . . . . 
                    . . . . . f f f f f f . . . . . 
                    . . . . f 1 1 1 1 1 d f . . . . 
                    . . . . f 1 1 1 1 1 d f . . . . 
                    . . . . f 1 f 1 f 1 d f . . . . 
                    f f . . f 1 1 1 1 d d f . . f . 
                    f 9 f f . f 1 1 d f f . . f 1 f 
                    f 9 9 b f 1 f f f 1 d f . f 1 f 
                    . f b f f 1 1 4 1 1 d f . f 4 f 
                    . . f 1 f 1 4 4 4 1 d f f f 4 f 
                    . . f d f 1 1 4 1 1 d f 1 f d f 
                    . . . f f 1 1 4 1 d d f 1 f d f 
                    . . . . f 1 1 f 1 d d f f . f . 
                    . . . . f f f . f f f . . . . .
        """),
        SpriteKind.enemy)
    malo3.set_position(280, 98)
    malo3.set_velocity(55, 120)
    malo4 = sprites.create(img("""
            . . . . . . . . f f f . . . . . 
                    . . . . . . . f 5 5 5 f . . . . 
                    . . . . . . f 5 5 f f . . . . . 
                    . . . . . f f f f f f . . . . . 
                    . . . . f 1 1 1 1 1 d f . . . . 
                    . . . . f 1 1 1 1 1 d f . . . . 
                    . . . . f 1 f 1 f 1 d f . . . . 
                    f f . . f 1 1 1 1 d d f . . f . 
                    f 9 f f . f 1 1 d f f . . f 1 f 
                    f 9 9 b f 1 f f f 1 d f . f 1 f 
                    . f b f f 1 1 5 1 1 d f . f 5 f 
                    . . f 1 f 1 5 5 5 1 d f f f 5 f 
                    . . f d f 1 1 5 1 1 d f 1 f d f 
                    . . . f f 1 1 5 1 d d f 1 f d f 
                    . . . . f 1 1 f 1 d d f f . f . 
                    . . . . f f f . f f f . . . . .
        """),
        SpriteKind.enemy)
    malo4.set_position(280, 98)
    malo4.set_velocity(-60, 120)
    ballestero = sprites.create(img("""
            .............fffff.
                    ............fffff..
                    ...........fffff...
                    ..........ffffff...
                    .........ffffffdf..
                    .....f...f11111df..
                    ....fef..f1f1f1df..
                    ...feef..f1111ddf..
                    ..feeffffff11dff...
                    .fefeeed1f1fff1df..
                    feff444d4efff11df..
                    .fefeeed1eeeff1dff.
                    ..feeffffeeef11df1f
                    ...feef.ffeeefddf1f
                    ....feffffeeefffff.
                    .....ffeeeeeeeeeeef
                    ......feeeeeeeeeeef
                    ......fffffffffffff
        """),
        SpriteKind.ballesta)
    ballestero.set_position(510, 104)
    Barrera_ = sprites.create(img("""
            d 1 1 1 1 1 1 b d 1 1 1 1 1 1 b 
                    1 d d d d d d b 1 d d d d d b b 
                    1 d d d d d d b 1 d d d d b d b 
                    1 d d d d d d b 1 d d d 1 1 d b 
                    1 d d d d d d b 1 d d b d d d b 
                    1 d d d d d d b 1 d b b d d d b 
                    1 d d d d d d d 1 d b b d d d d 
                    b b b b b b d e b b b b b b d e 
                    d 1 1 1 1 1 1 b d 1 1 1 1 1 1 b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d b b b 1 d d d d d d b 
                    1 d d d b b b b 1 d d d d d d b 
                    1 d d d b b d d 1 d d d d d d d 
                    b b b b b b b e b b b b b b b e
        """),
        SpriteKind.Barrera)
    Barrera_.set_position(200, 104)
    Barrera2_ = sprites.create(img("""
            d 1 1 1 1 1 1 b d 1 1 1 1 1 1 b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d d 1 d d d d d d d 
                    b b b b b b d e b b b b b b d e 
                    d 1 1 1 1 1 1 b d 1 1 1 1 1 1 b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d d 1 d d d d d d d 
                    b b b b b b d e b b b b b b b e
        """),
        SpriteKind.Barrera2)
    Barrera2_.set_position(263, 104)
    barrera__3 = sprites.create(img("""
            d 1 1 1 1 1 1 b d 1 1 1 1 1 1 b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d d 1 d d d d d d d 
                    b b b b b b d e b b b b b b d e 
                    d 1 1 1 1 1 1 b d 1 1 1 1 1 1 b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d d 1 d d d d d d d 
                    b b b b b b d e b b b b b b b e
        """),
        SpriteKind.Barrera_3)
    barrera__3.set_position(169, 104)
    barrera4_ = sprites.create(img("""
            b 
                    b 
                    b 
                    b 
                    b 
                    b 
                    d 
                    e 
                    b 
                    b 
                    b 
                    b 
                    b 
                    b 
                    d 
                    e
        """),
        SpriteKind.Barrera_3)
    barrera4_.set_position(272, 104)
    barrera5_ = sprites.create(img("""
            d 1 1 1 1 1 1 b d 1 1 1 1 1 1 b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d d 1 d d d d d d d 
                    b b b b b b d e b b b b b b d e 
                    d 1 1 1 1 1 1 b d 1 1 1 1 1 1 b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d d 1 d d d d d d d 
                    b b b b b b d e b b b b b b b e
        """),
        SpriteKind.Barrera2)
    barrera5_.set_position(423, 104)
    barrera6_ = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . d 
                    . . . . . . . . . . . . . . . d 
                    . . . . . . . . . . . . . . . d 
                    . . . . . . . . . . . . . . . d 
                    . . . . . . . . . . . . . . . d 
                    . . . . . . . . . . . . . . . d 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.barrera6)
    barrera6_.set_position(424, 104)
    Monster = sprites.create(img("""
            . f f 1 1 1 f f . 
                    f f c f 1 1 f f f 
                    f c f f f f f f f 
                    f c 7 f f f 7 f f 
                    f f 7 7 f 7 7 f f 
                    f c 7 f 7 f 7 f f 
                    f f 7 f 7 f 7 f f 
                    f f 7 f 7 f 7 f f 
                    f f 7 f f f 7 f f 
                    f f f f f f f f f 
                    f f f f f f f f f 
                    f f f f f f f f f 
                    . f f f f f f f . 
                    . . f f f f f . .
        """),
        SpriteKind.Comida)
    Monster.set_position(184, 105)
    game.splash("NIVEL 2:", "\"Londres\" de Edward Rutherfurd")
    game.show_long_text("Pasa frente al London Eye en la época del medievo, combatiendo templarios.",
        DialogLayout.BOTTOM)
    libro_2_londrés = sprites.create(img("""
            . . . . . . f f . . . . . . 
                    . . . . f f f f f . . . . . 
                    . . . f f 2 2 2 f f . . . . 
                    . . f f 2 2 2 f 2 f . . . . 
                    . f f 2 2 2 f 2 2 f f . . . 
                    f f f 2 2 f 2 2 2 2 f f . . 
                    f 1 f f 2 2 2 2 f 2 2 f f . 
                    f f 1 f f 2 2 f 2 2 2 2 f f 
                    . f f 1 f 2 2 2 2 2 f 2 e f 
                    . . f f 1 f f 2 2 f 2 e f f 
                    . . . f d 1 f f e e e f f . 
                    . . . f f d d f f e f f . . 
                    . . . . f f d d f f f . . . 
                    . . . . . . f f f . . . . .
        """),
        SpriteKind.libro2)
    libro_2_londrés.set_position(745, 65)

def on_on_overlap15(sprite, otherSprite):
    J1.x += -24
    game.show_long_text("Deberías inspeccionar primero las pruebas de esta zona.",
        DialogLayout.BOTTOM)
sprites.on_overlap(SpriteKind.player, SpriteKind.muro4, on_on_overlap15)

def nivel5():
    global Libros, sí, pito_de_caballo, torturado, torturado2, torturado3, torturado4, torturado5, libro_5_londres_bajo_tierra
    game.splash("NIVEL 5:", "\"Londres bajo tierra\"")
    game.show_long_text("Experimenta las horribles torturas que se daban en un pasado en las profundidades de Londres",
        DialogLayout.BOTTOM)
    info.set_score(4)
    info.change_score_by(1)
    Libros += 1
    J1.set_position(20, 80)
    info.set_life(5)
    sí += 10
    pito_de_caballo = 0
    tiles.set_tilemap(tilemap("""
        level_27
    """))
    scene.set_background_image(img("""
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeeeeeeeeeefffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeeeeeeeeeeeeeeeeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeeeeeeeeeeeeeeeeeeeeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                bbbbbbbbfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeeeeeeeeeeeeeeeeeeeeeeeeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                bbbbbbbbbbbbbbbbcbbbbbbbffffffffffffffffffffffffffffffffffffffffffffffffeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                bbbbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbfffffffffffffffffffffffffffffffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                bbbbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbffffffffffffffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                bbbbbbbbbbbbbbbccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeeeeeeefffffffffffeeeeeeeeeeeeffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                bbbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeeeeeeebbbbbbbbfffffffeeeeeeeeeefffffffffffffffffffffffffffffffffffffffffffffffffffffff
                bbbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeeeeeeeeebbbbbbbbbbbbbbbeeeeeeeeeeffffffffffffffffffffffffffffffffffffffffffffffffffffff
                bbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeeeebbeeeebbbbbbbbbbbbbbbbbeeeeeeeeebbbbbbbbbbbbbffffffffffffffffffffffffffffffffffffffff
                bbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeeebbbbeeeebbbbbbbbbbbbbbbbbeeeeeeeebbbbbbbbbbbbbbbbbbbbbbbbbbbbb999fffffffffffffffffffff
                bbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeeebbbbbeeeeebbbbbbbbbbbbbbbbeeeeeeeeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb99bbbbbbbbbbbffffffff
                bbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeeebbbbbbeeeebbbbbbbbbbbbbbeeeeeeeeeeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb9bbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeeebbbbbbbbeeeebbbbbbbbbbbbeeeeeeeeeeeeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb9bbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeebbbbbbbbbeeeebbbbbbbbbbbeeeeeebeeeeeeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb9bbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeebbbbbbbbbbeeeebbbbbbbbeeeeeebbbeeeeeeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb9bbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeeebbbbbbbbbbeeeebbbbbbbeeeeeebbbbeeeeeeeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbb9bbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeebbbbbbbbbbbbeeeebbbbbeeeeeebbbbbbeeeeeeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbb9bbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeebbbbbbbbbbbbeeeeebbeeeeeebbbbbbbbeeeeeeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbb9bbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeebbbbbbbbbbbbbeeeeeeeeeeebbbbbbbbbeeeeeeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbb9bbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeebbbbbbbbbbbbbbeeeeeeeeebbbbbbbbbbeeeeeeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbb9bbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeebbbbbbbbbbbbbeefffeeebbbbbbbbbbbbeeeeeeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbb9bbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeebbbbbbbbbeeeeeefffeebbbbbbbbbbbbbeeeeeeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbb9bbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeebbbbbeeeeeeeeeefffebbbbbbbbbbbbbbeeeeeeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbb99bbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeebeeeeeeeeeeeeeeeeeeebbbbbbbbbbbbbeeeeeeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb9bbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeeeeeeeeeeeeebbbeeeeeeebbbbbbbbbbbbeeeeeeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb9bbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeeeeeeeeebbbbbbeeeeeeeeebbbbbbbbbbbeeeeeeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb9bbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeeeeebbbbbbbbbbeeeebeeeeebbbbbbbbbbeeeeeeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb9bbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeeebbbbbbbbbbbbeeebbbeeeeebbbbbbbbeeeeeeeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb9bbbbbbbbbbbbbbbbb
                ffffffffbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeebbbbbbbbbbbeeeebbbbeeeebbbbbbbbeeeeeeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb9bbbbbbbbbbbbbbbbb
                ffffffffffffffffffffffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeebbbbbbbbbbbeeeebbbbbeeeebbbbbbbeeeeeeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb9bbbbbbbbbbbbbbbbb
                fffffffffffffffffffffffffffffffffffffbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeeebbbbbbbbbbeeebbbbbbeeeeebbbbbeeeeeeeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb9bbbbbbbbbbbbbbbbb
                ffffffffffffffffffffffffffffffffffffffffffffffffff9bbbbbbbbbbbbbbeeeeeeeebbbbbbbbbeeebbbbbbbeeeeebbbeeeeeeeebbbbbbbbbbbbbbb9bbbbbbbbbbbbbbbbb99bbbbbbbbbbbbbbbbb
                fffffffffffffffffffffffffffffffffffffffffffffffff99ffffffffffffffeeeeeeeebbbbbbbbeeeebbbbbbbbeeeeebbeeeeeeeebbbbbbbbbbbbbbb9bbbbbbbbbbbbbbbbb9bbbbbbbbbbbbbbbbbb
                fffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffeeeeeeeeffffffbeeeebbbbbbbbbeeeeeeeeeeeeebbbbbbbbbbbbbbbb99bbbbbbbbbbbbbbbb9bbbbbbbbbbbbbbbbbb
                fffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffeeeeeeeeeffffffeeeffffffffffbeeeeeeeeeeeebbbbbbbbbbbbbbbbb9bbbbbbbbbbbbbbbb9bbbbbbbbbbbbbbbbbb
                ffffffffffffffffffffffffffffffffffffffffffffffff99fffffffffffffffffeeeeeeeeeefffeeeeffffffffffffeeeeeeeeeefffbbbbbbbbbbbbbbb9bbbbbbbbbbbbbbb99bbbbbbbbbbbbbbbbbb
                ffffffffffffffffffffffffffffffffffffffffffffffff99ffffffffffffffffffeeeeeeeeeeffeeeefffffffffffeeeeeeeeeeffffffffffffffffffb9bbbbbbbbbbbbbbb9bbbbbbbbbbbbbbbbbbb
                ffffffffffffffffffffffffffffffffffffffffffffffff99fffffffffffffffffffeeeeeeeeeeeeeefffffffffeeeeeeeeeeeeffffffffffffffffffff9fffffffffffffb99bbbbbbbbbbbbbbbbbbb
                ffffffffffffffffffffffffffffffffffffffffffffffff99ffffffffffffffffffffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffffffff9ffffffffffffff9ffffffffffffbbbbbbbb
                ffffffffffffffffffffffffffffffffffffffffffffffff99fffffffffffffffffffffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffffffffffffffffffff9ffffffffffffff9ffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffff99ffffffffffffffffffffffeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffffffffff9ffffffffffffff9ffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffeeeeeeeeeeeeeeeeeeeeeeeeeeeffffffffffffffffffffffff9ffffffffffffff9ffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffff99ffffffffffffffffffffffffffeeeeeeeeeeeeeeeeeeeeeeeffffffffffffffffffffffffff9ffffffffffffff9ffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffff99ffffffffffffffffffffffffffffeeeeeeeeeeeeeeeeeeeffffffffffffffffffffffffffff9ffffffffffffff9ffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffffffffffffffffffeeeeeeeeeeeeefffffffffffffffffffffffffffffff9ffffffffffffff9ffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffff9ffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffff99fffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffff9fffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffff9fffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffff9fffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffff9fffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffff99fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffff9fffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffff99ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff99fffffffffffffff9fffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff99fffffffffffffff9fffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffff9fffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffff9fffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffff99fffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffff9ffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffff9ffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffff9ffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffff9ffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffff9ffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffff9ffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffff9ffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffff9ffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffff9ffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffff9fffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffff9fffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffff9fffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffff9ffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffff9ffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffff99ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffff99ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffff9fffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffff99fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffff9ffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffff99fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff99ffffffffffffffff9ffffffffffffffffff
    """))
    sherlock.destroy()
    sherlock.destroy()
    culpable.destroy()
    sospechoso_fumador.destroy()
    sospechoso_josuke.destroy()
    sospechoso_negro.destroy()
    victima2.destroy()
    torturado = sprites.create(img("""
            11................11
                    1111............1111
                    11..1d..5555..d1..11
                    11..2de.fddf.ed2..11
                    11...eeeddddee2...11
                    11....eedffdee....11
                    11....eeee2eee....11
                    11....eeeeeeee....11
                    11.....eeeeee.....11
                    11.....ee2eee.....11
                    11.....ee2eee.....11
                    11.....ee2eee.....11
                    11.....ee2eee.....11
                    11.....eeeeee.....11
                    11.....eeeeee.....11
                    11.....dd..dd.....11
                    11.....dd..dd.....11
        """),
        SpriteKind.cuerpo)
    torturado.set_position(152, 87)
    torturado2 = sprites.create(img("""
            11................11
                    1111............1111
                    11..1e..ffff..e1..11
                    11..2e1.2ee2.1e2..11
                    11...211eeee111...11
                    11....11effe11....11
                    11....11111111....11
                    11....11111111....11
                    11.....111111.....11
                    11.......22.......11
                    11.......22.......11
                    11................11
                    11................11
                    11................11
                    11...1111111111...11
                    11..ee11111111ee..11
                    11..eee111111eee..11
        """),
        SpriteKind.cuerpo2)
    torturado2.set_position(240, 87)
    torturado3 = sprites.create(img("""
            1 1 . . . . . . . . . . 
                    1 1 1 1 1 1 . . . . f . 
                    1 1 . . . 1 . . . . f f 
                    1 1 . . . 2 . d . . f f 
                    1 1 . d 1 2 1 d 2 d f f 
                    1 1 . d d d d d 2 d f f 
                    1 d . . d d d f 1 1 f . 
                    1 d d . f f f . 9 1 . . 
                    1 1 d d f f f d . . . . 
                    1 1 . d f f f d . . . . 
                    1 1 . . f f f d . . . . 
                    1 1 . . f f f d . . . . 
                    1 1 . . f f f . . . . . 
                    1 1 . . f f f . . . . . 
                    1 1 . . d . d . . . . . 
                    1 1 . d d . d d . . . . 
                    1 1 . . . . . . . . . .
        """),
        SpriteKind.cuerpo3)
    torturado3.set_position(288, 87)
    torturado4 = sprites.create(img("""
            11................11
                    1111............1111
                    11..1d........d1..11
                    11..2de......ed2..11
                    11...eee....ee2...11
                    11....eee22eee....11
                    11....eeeeeeee....11
                    11....eeeeeeee....11
                    11.....eeeeee.....11
                    11.....ee2eee.....11
                    11.....ee2eee.....11
                    11.....ee2eee.....11
                    11.....ee2eee.....11
                    11.....eeeeee.....11
                    11.....eeeeee.dd1e11
                    11.....dd..dd.fdde11
                    11.....dd..dd.dd1e11
        """),
        SpriteKind.cuerpo4)
    torturado4.set_position(416, 87)
    torturado5 = sprites.create(img("""
            11................11
                    11................11
                    11112211222211221111
                    11..22e.f22f.e22..11
                    11...eee2222eee...11
                    11....ee2ff2ee....11
                    11....eeeeeeee....11
                    11....eeeeeeee....11
                    11.....eeeeee.....11
                    11.....2eeee2.....11
                    11111112eeee21111111
                    11.....2eeee2.....11
                    11.....eeeeee.....11
                    11.....eeeeee.....11
                    11.....eeeeee.....11
                    11.....22..22.....11
                    11.....22..22.....11
        """),
        SpriteKind.cuerpo5)
    torturado5.set_position(688, 87)
    libro_5_londres_bajo_tierra = sprites.create(img("""
            . . . . . . f f . . . . . . 
                    . . . . f f f f f . . . . . 
                    . . . f f 4 4 4 f f . . . . 
                    . . f f 4 4 4 f 4 f . . . . 
                    . f f 4 4 4 f 4 4 f f . . . 
                    f f f 4 4 f 4 4 4 4 f f . . 
                    f 1 f f 4 4 4 4 f 4 4 f f . 
                    f f 1 f f 4 4 f 4 4 4 4 f f 
                    . f f 1 f 4 4 4 4 4 f 4 e f 
                    . . f f 1 f f 4 4 f 4 e f f 
                    . . . f d 1 f f e e e f f . 
                    . . . f f d d f f e f f . . 
                    . . . . f f d d f f f . . . 
                    . . . . . . f f f . . . . .
        """),
        SpriteKind.libro5)
    libro_5_londres_bajo_tierra.set_position(768, 87)

def on_overlap_tile(sprite, location):
    info.change_life_by(-1)
    J1.y += -30
    J1.x += -64
    pause(50)
scene.on_overlap_tile(SpriteKind.player, myTiles.tile9, on_overlap_tile)

def on_on_overlap16(sprite, otherSprite):
    global pito_de_caballo, alma
    sprite.destroy()
    otherSprite.destroy(effects.star_field, 1)
    pito_de_caballo += 1
    alma = sprites.create(img("""
            . . c c c c c c . . . . . 
                    . c c c c c c c c . . . . 
                    b c c c c c c c b c . . . 
                    c b b c c c b b c c . . . 
                    c 2 2 b c b 2 2 c c . . . 
                    c c 2 c c c 2 c c c . . . 
                    c c c c c c c c c c . . . 
                    b b c b c b c b b c . . . 
                    c b b c b c b b c c . . . 
                    c c c c c c c c c c c . . 
                    c c c c c c c c c c c . . 
                    . c c c c c c c c c c . . 
                    . c c c c c c c c c c . . 
                    . . c c c c c c c c c c . 
                    . . . c c c c c c c c c . 
                    . . . . . c c c c c c c . 
                    . . . . . . . . . . c c c
        """),
        SpriteKind.alma_)
    alma.set_position(416, 87)
    if pito_de_caballo == 1:
        alma.follow(J1, 35)
    if pito_de_caballo == 2:
        alma.follow(J1, 45)
    if pito_de_caballo == 3:
        alma.follow(J1, 60)
    if pito_de_caballo == 4:
        alma.follow(J1, 82.5)
    if pito_de_caballo == 5:
        alma.follow(J1, 100)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.cuerpo4, on_on_overlap16)

def on_right_pressed():
    if sí == 0:
        animation.run_image_animation(J1,
            [img("""
                    . . . . . . . . . . . . . . . . 
                                f f f f f f f f f f f . . . . . 
                                f f c c c c c c c c f f . . . . 
                                . . f c c c c c c c c f f . . . 
                                . . f f c c c c f f f f f . . . 
                                . . . f f f f f f e e e f . . . 
                                . f . f e e e e e e e e f . f . 
                                . f f f f f f f f f f f f f f . 
                                . . . f 5 5 5 5 5 5 5 5 5 f . . 
                                . . . f 5 5 5 f 5 5 5 5 f f . . 
                                . . . f 5 5 5 5 5 5 5 5 5 f . . 
                                . . . f 5 5 5 f 5 5 5 f 5 f . . 
                                . . . f 5 5 5 5 f f f 5 5 f . . 
                                . . f f 5 5 5 5 5 5 5 5 5 f f . 
                                . . f 5 5 5 f f f f f 5 5 5 f . 
                                . . f f f f . . . . . f f f f .
                """),
                img("""
                    f f f f f f f f f . . . . . . . 
                                f f c c c c c c f f f . . . . . 
                                . . f c c c c c c c f f . . . . 
                                . . f f c c c c c c c f f . . . 
                                . . . f c c c c f f f f f . . . 
                                . . . f f f f f f e e e f . . . 
                                . f . f e e e e e e e e f . f . 
                                . f f f f f f f f f f f f f f . 
                                . . . f 5 5 5 5 5 5 5 5 5 f . . 
                                . . . f 5 5 5 f 5 5 5 5 f f . . 
                                . . . f 5 5 5 5 5 5 5 5 5 f . . 
                                . . . f 5 5 5 f 5 5 5 f 5 f . . 
                                . . . f 5 5 5 5 f f f 5 5 f . . 
                                . . . f 5 5 5 5 5 5 5 5 5 f . . 
                                . . . f 5 5 f f f f f 5 5 f . . 
                                . . . f f f f . . . f f f f . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                f f f f f f f f f f f . . . . . 
                                f f c c c c c c c c f f . . . . 
                                . . f c c c c c c c c f f . . . 
                                . . f f c c c c f f f f f . . . 
                                . . . f f f f f f e e e f . . . 
                                . f . f e e e e e e e e f . f . 
                                . f f f f f f f f f f f f f f . 
                                . . . f 5 5 5 5 5 5 5 5 5 f . . 
                                . . . f 5 5 5 f 5 5 5 5 f f . . 
                                . . . f 5 5 5 5 5 5 5 5 5 f . . 
                                . . . f 5 5 5 f 5 5 5 f 5 f . . 
                                . . . f 5 5 5 5 f f f 5 5 f . . 
                                . . . . f 5 5 5 5 5 5 5 f . . . 
                                . . . . f 5 5 f f f 5 5 f . . . 
                                . . . . f f f f . f f f f . . .
                """),
                img("""
                    f f f f f f f f f . . . . . . . 
                                f f c c c c c c f f f . . . . . 
                                . . f c c c c c c c f f . . . . 
                                . . f f c c c c c c c f f . . . 
                                . . . f c c c c f f f f f . . . 
                                . . . f f f f f f e e e f . . . 
                                . f . f e e e e e e e e f . f . 
                                . f f f f f f f f f f f f f f . 
                                . . . f 5 5 5 5 5 5 5 5 5 f . . 
                                . . . f 5 5 5 f 5 5 5 5 f f . . 
                                . . . f 5 5 5 5 5 5 5 5 5 f . . 
                                . . . f 5 5 5 f 5 5 5 f 5 f . . 
                                . . . f 5 5 5 5 f f f 5 5 f . . 
                                . . . f 5 5 5 5 5 5 5 5 5 f . . 
                                . . . f 5 5 f f f f f 5 5 f . . 
                                . . . f f f f . . . f f f f . .
                """)],
            250,
            True)
    if sí == 10:
        animation.run_image_animation(J1,
            [img("""
                    . . . . . . . . . . . . . . . . 
                                f f f f f f f f f f f . . . . . 
                                f f c c c c c c c c f f . . . . 
                                . . f c c c c c c c c f f . . . 
                                . . f f c c c c f f f f f . . . 
                                . . . f f f f f f e e e f . . . 
                                . f . f e e e e e e e e f . f . 
                                . f f f f f f f f f f f f f f . 
                                . . . f 5 5 5 5 5 5 5 5 5 f . . 
                                . . . f 5 5 5 f 5 5 5 5 f f . . 
                                f f . f 5 5 5 5 5 5 5 5 5 f . . 
                                8 8 f f 5 5 5 5 f 5 5 f 5 f . . 
                                f 8 f f 5 5 5 5 5 f f 5 5 f . . 
                                . f f f 5 5 5 5 5 5 5 5 5 f f . 
                                . . f 5 5 5 f f f f f 5 5 5 f . 
                                . . f f f f . . . . . f f f f .
                """),
                img("""
                    f f f f f f f f f . . . . . . . 
                                f f c c c c c c f f f . . . . . 
                                . . f c c c c c c c f f . . . . 
                                . . f f c c c c c c c f f . . . 
                                . . . f c c c c f f f f f . . . 
                                . . . f f f f f f e e e f . . . 
                                . f . f e e e e e e e e f . f . 
                                . f f f f f f f f f f f f f f . 
                                . . . f 5 5 5 5 5 5 5 5 5 f . . 
                                . . . f 5 5 5 f 5 5 5 5 f f . . 
                                f f . f 5 5 5 5 5 5 5 5 5 f . . 
                                8 8 f f 5 5 5 5 f 5 5 f 5 f . . 
                                f 8 f f 5 5 5 5 5 f f 5 5 f . . 
                                . f . f 5 5 5 5 5 5 5 5 5 f . . 
                                . . . f 5 5 f f f f f 5 5 f . . 
                                . . . f f f f . . . f f f f . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                f f f f f f f f f f f . . . . . 
                                f f c c c c c c c c f f . . . . 
                                . . f c c c c c c c c f f . . . 
                                . . f f c c c c f f f f f . . . 
                                . . . f f f f f f e e e f . . . 
                                . f . f e e e e e e e e f . f . 
                                . f f f f f f f f f f f f f f . 
                                . . . f 5 5 5 5 5 5 5 5 5 f . . 
                                . . . f 5 5 5 f 5 5 5 5 f f . . 
                                f f . f 5 5 5 5 5 5 5 5 5 f . . 
                                8 8 f f 5 5 5 5 f 5 5 f 5 f . . 
                                f 8 f f 5 5 5 5 5 f f 5 5 f . . 
                                . f . . f 5 5 5 5 5 5 5 f . . . 
                                . . . . f 5 5 f f f 5 5 f . . . 
                                . . . . f f f f . f f f f . . .
                """),
                img("""
                    f f f f f f f f f . . . . . . . 
                                f f c c c c c c f f f . . . . . 
                                . . f c c c c c c c f f . . . . 
                                . . f f c c c c c c c f f . . . 
                                . . . f c c c c f f f f f . . . 
                                . . . f f f f f f e e e f . . . 
                                . f . f e e e e e e e e f . f . 
                                . f f f f f f f f f f f f f f . 
                                . . . f 5 5 5 5 5 5 5 5 5 f . . 
                                . . . f 5 5 5 f 5 5 5 5 f f . . 
                                f f . f 5 5 5 5 5 5 5 5 5 f . . 
                                8 8 f f 5 5 5 5 f 5 5 f 5 f . . 
                                f 8 f f 5 5 5 5 5 f f 5 5 f . . 
                                . f . f 5 5 5 5 5 5 5 5 5 f . . 
                                . . . f 5 5 f f f f f 5 5 f . . 
                                . . . f f f f . . . f f f f . .
                """)],
            250,
            True)
    if sí == 20:
        animation.run_image_animation(J1,
            [img("""
                    . . . . . . . . . . . . . . . . 
                                f f f f f f f f f f f . . . . . 
                                f f c c c c c c c c f f . . . . 
                                2 2 f c c c c c c c c f f . . . 
                                f f f f c c c c f f f f f . . . 
                                . . . f f f f f f e e e f . . . 
                                . f . f e e e e e e e e f . f . 
                                . f f f f f f f f f f f f f f . 
                                . . . f 5 5 5 5 5 5 5 5 5 f . . 
                                . . . f 5 5 5 f 5 5 5 5 f f . . 
                                f f . f 5 5 5 5 5 5 5 5 5 f . . 
                                8 8 f f 5 5 5 5 5 f 5 f 5 f . . 
                                f 8 f f 5 5 5 5 5 5 f 5 5 f . . 
                                . f f f 5 5 5 5 5 5 5 5 5 f f . 
                                . . f 5 5 5 f f f f f 5 5 5 f . 
                                . . f f f f . . . . . f f f f .
                """),
                img("""
                    f f f f f f f f f . . . . . . . 
                                f f c c c c c c f f f . . . . . 
                                f f f c c c c c c c f f . . . . 
                                2 2 f f c c c c c c c f f . . . 
                                f f . f c c c c f f f f f . . . 
                                . . . f f f f f f e e e f . . . 
                                . f . f e e e e e e e e f . f . 
                                . f f f f f f f f f f f f f f . 
                                . . . f 5 5 5 5 5 5 5 5 5 f . . 
                                . . . f 5 5 5 f 5 5 5 5 f f . . 
                                f f . f 5 5 5 5 5 5 5 5 5 f . . 
                                8 8 f f 5 5 5 5 5 f 5 f 5 f . . 
                                f 8 f f 5 5 5 5 5 5 f 5 5 f . . 
                                . f . f 5 5 5 5 5 5 5 5 5 f . . 
                                . . . f 5 5 f f f f f 5 5 f . . 
                                . . . f f f f . . . f f f f . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                f f f f f f f f f f f . . . . . 
                                f f c c c c c c c c f f . . . . 
                                2 2 f c c c c c c c c f f . . . 
                                f f f f c c c c f f f f f . . . 
                                . . . f f f f f f e e e f . . . 
                                . f . f e e e e e e e e f . f . 
                                . f f f f f f f f f f f f f f . 
                                . . . f 5 5 5 5 5 5 5 5 5 f . . 
                                . . . f 5 5 5 f 5 5 5 5 f f . . 
                                f f . f 5 5 5 5 5 5 5 5 5 f . . 
                                8 8 f f 5 5 5 5 5 f 5 f 5 f . . 
                                f 8 f f 5 5 5 5 5 5 f 5 5 f . . 
                                . f . . f 5 5 5 5 5 5 5 f . . . 
                                . . . . f 5 5 f f f 5 5 f . . . 
                                . . . . f f f f . f f f f . . .
                """),
                img("""
                    f f f f f f f f f . . . . . . . 
                                f f c c c c c c f f f . . . . . 
                                f f f c c c c c c c f f . . . . 
                                2 2 f f c c c c c c c f f . . . 
                                f f . f c c c c f f f f f . . . 
                                . . . f f f f f f e e e f . . . 
                                . f . f e e e e e e e e f . f . 
                                . f f f f f f f f f f f f f f . 
                                . . . f 5 5 5 5 5 5 5 5 5 f . . 
                                . . . f 5 5 5 f 5 5 5 5 f f . . 
                                f f . f 5 5 5 5 5 5 5 5 5 f . . 
                                8 8 f f 5 5 5 5 5 f 5 f 5 f . . 
                                f 8 f f 5 5 5 5 5 5 f 5 5 f . . 
                                . f . f 5 5 5 5 5 5 5 5 5 f . . 
                                . . . f 5 5 f f f f f 5 5 f . . 
                                . . . f f f f . . . f f f f . .
                """)],
            250,
            True)
    if sí == 30:
        animation.run_image_animation(J1,
            [img("""
                    . . . . . . . . . . . . f f . . 
                                f f f f f f f f f f f f 7 7 f . 
                                f f c c c c c c c c f f f 7 7 f 
                                2 2 f c c c c c c c c f f f f . 
                                f f f f c c c c f f f f f . . . 
                                . . . f f f f f f e e e f . . . 
                                . f . f e e e e e e e e f . f . 
                                . f f f f f f f f f f f f f f . 
                                . . . f 5 5 5 5 5 5 5 5 5 f . . 
                                . . . f 5 5 5 f 5 5 5 5 f f . . 
                                f f . f 5 5 5 5 5 5 5 5 5 f . . 
                                8 8 f f 5 5 5 5 5 f f f 5 f . . 
                                f 8 f f 5 5 5 5 5 5 5 5 5 f . . 
                                . f f f 5 5 5 5 5 5 5 5 5 f f . 
                                . . f 5 5 5 f f f f f 5 5 5 f . 
                                . . f f f f . . . . . f f f f .
                """),
                img("""
                    f f f f f f f f f . . . f f . . 
                                f f c c c c c c f f f f 7 7 f . 
                                f f f c c c c c c c f f f 7 7 f 
                                2 2 f f c c c c c c c f f f f . 
                                f f . f c c c c f f f f f . . . 
                                . . . f f f f f f e e e f . . . 
                                . f . f e e e e e e e e f . f . 
                                . f f f f f f f f f f f f f f . 
                                . . . f 5 5 5 5 5 5 5 5 5 f . . 
                                . . . f 5 5 5 f 5 5 5 5 f f . . 
                                f f . f 5 5 5 5 5 5 5 5 5 f . . 
                                8 8 f f 5 5 5 5 5 f f f 5 f . . 
                                f 8 f f 5 5 5 5 5 5 5 5 5 f . . 
                                . f . f 5 5 5 5 5 5 5 5 5 f . . 
                                . . . f 5 5 f f f f f 5 5 f . . 
                                . . . f f f f . . . f f f f . .
                """),
                img("""
                    . . . . . . . . . . . . f f . . 
                                f f f f f f f f f f f f 7 7 f . 
                                f f c c c c c c c c f f f 7 7 f 
                                2 2 f c c c c c c c c f f f f . 
                                f f f f c c c c f f f f f . . . 
                                . . . f f f f f f e e e f . . . 
                                . f . f e e e e e e e e f . f . 
                                . f f f f f f f f f f f f f f . 
                                . . . f 5 5 5 5 5 5 5 5 5 f . . 
                                . . . f 5 5 5 f 5 5 5 5 f f . . 
                                f f . f 5 5 5 5 5 5 5 5 5 f . . 
                                8 8 f f 5 5 5 5 5 f f f 5 f . . 
                                f 8 f f 5 5 5 5 5 5 5 5 5 f . . 
                                . f . . f 5 5 5 5 5 5 5 f . . . 
                                . . . . f 5 5 f f f 5 5 f . . . 
                                . . . . f f f f . f f f f . . .
                """),
                img("""
                    f f f f f f f f f . . . f f . . 
                                f f c c c c c c f f f f 7 7 f . 
                                f f f c c c c c c c f f f 7 7 f 
                                2 2 f f c c c c c c c f f f f . 
                                f f . f c c c c f f f f f . . . 
                                . . . f f f f f f e e e f . . . 
                                . f . f e e e e e e e e f . f . 
                                . f f f f f f f f f f f f f f . 
                                . . . f 5 5 5 5 5 5 5 5 5 f . . 
                                . . . f 5 5 5 f 5 5 5 5 f f . . 
                                f f . f 5 5 5 5 5 5 5 5 5 f . . 
                                8 8 f f 5 5 5 5 5 f f f 5 f . . 
                                f 8 f f 5 5 5 5 5 5 5 5 5 f . . 
                                . f . f 5 5 5 5 5 5 5 5 5 f . . 
                                . . . f 5 5 f f f f f 5 5 f . . 
                                . . . f f f f . . . f f f f . .
                """)],
            250,
            True)
    if sí == 40:
        animation.run_image_animation(J1,
            [img("""
                    . . . . . . . . . . . . f f . . 
                                f f f f f f f f f f f f 7 7 f . 
                                f f c c c c c c c c f f f 7 7 f 
                                2 2 f c c c c c c c c f f f f . 
                                f f f f c c c c f f f f f . . . 
                                . . . f f f f f f e e e f . . . 
                                . f . f e e e e e e e e f . f . 
                                . f f f f f f f f f f f f f f . 
                                . . . f 5 5 5 5 5 5 5 5 5 f . . 
                                . . . f 5 5 5 f 5 5 5 5 f f f f 
                                f f . f 4 5 5 5 5 5 5 5 5 f a a 
                                8 8 f f 4 5 5 5 5 f f f 5 f a f 
                                f 8 f f 4 4 5 5 5 5 5 5 5 f f . 
                                . f f f 4 4 4 4 4 4 4 5 5 f f . 
                                . . f 4 4 4 f f f f f 4 4 5 f . 
                                . . f f f f . . . . . f f f f .
                """),
                img("""
                    f f f f f f f f f . . . f f . . 
                                f f c c c c c c f f f f 7 7 f . 
                                f f f c c c c c c c f f f 7 7 f 
                                2 2 f f c c c c c c c f f f f . 
                                f f . f c c c c f f f f f . . . 
                                . . . f f f f f f e e e f . . . 
                                . f . f e e e e e e e e f . f . 
                                . f f f f f f f f f f f f f f . 
                                . . . f 5 5 5 5 5 5 5 5 5 f . . 
                                . . . f 5 5 5 f 5 5 5 5 f f f f 
                                f f . f 4 5 5 5 5 5 5 5 5 f a a 
                                8 8 f f 4 5 5 5 5 f f f 5 f a f 
                                f 8 f f 4 4 5 5 5 5 5 5 5 f f . 
                                . f . f 4 4 4 4 4 4 4 5 5 f . . 
                                . . . f 4 4 f f f f f 4 4 f . . 
                                . . . f f f f . . . f f f f . .
                """),
                img("""
                    . . . . . . . . . . . . f f . . 
                                f f f f f f f f f f f f 7 7 f . 
                                f f c c c c c c c c f f f 7 7 f 
                                2 2 f c c c c c c c c f f f f . 
                                f f f f c c c c f f f f f . . . 
                                . . . f f f f f f e e e f . . . 
                                . f . f e e e e e e e e f . f . 
                                . f f f f f f f f f f f f f f . 
                                . . . f 5 5 5 5 5 5 5 5 5 f . . 
                                . . . f 5 5 5 f 5 5 5 5 f f f f 
                                f f . f 4 5 5 5 5 5 5 5 5 f a a 
                                8 8 f f 4 5 5 5 5 f f f 5 f a f 
                                f 8 f f 4 4 5 5 5 5 5 5 5 f f . 
                                . f . . f 4 4 4 4 4 4 5 f . . . 
                                . . . . f 4 4 f f f 4 4 f . . . 
                                . . . . f f f f . f f f f . . .
                """),
                img("""
                    f f f f f f f f f . . . f f . . 
                                f f c c c c c c f f f f 7 7 f . 
                                f f f c c c c c c c f f f 7 7 f 
                                2 2 f f c c c c c c c f f f f . 
                                f f . f c c c c f f f f f . . . 
                                . . . f f f f f f e e e f . . . 
                                . f . f e e e e e e e e f . f . 
                                . f f f f f f f f f f f f f f . 
                                . . . f 5 5 5 5 5 5 5 5 5 f . . 
                                . . . f 5 5 5 f 5 5 5 5 f f f f 
                                f f . f 4 5 5 5 5 5 5 5 5 f a a 
                                8 8 f f 4 5 5 5 5 f f f 5 f a f 
                                f 8 f f 4 4 5 5 5 5 5 5 5 f f . 
                                . f . f 4 4 4 4 4 4 4 5 5 f . . 
                                . . . f 4 4 f f f f f 4 4 f . . 
                                . . . f f f f . . . f f f f . .
                """)],
            250,
            True)
    if sí == 50:
        animation.run_image_animation(J1,
            [img("""
                    ..........ffffffff............
                                .ff.......fccccccff......ff...
                                f22f.......fccccccff....f77f..
                                ff22f.......fffffffff...ff77f.
                                .fff.....f..feeeeeeef.f..fff..
                                .........ffffffffffffff.......
                                ...........f452555525f........
                                ...ff......f425555552f........
                                ..f44f.....f4ff5555fff........
                                ..ff44f....f4fff55ffff........
                                ...fff.....f425555552f....ff..
                                ..........ff424445552f...faaf.
                                .........f4f444ffff55f...ffaaf
                                .ff.....f44f44ff222f5fff..fff.
                                f88f...f444ffff2222fff5f......
                                ff88f.f44444444222244555f.....
                                .fff..f44555544222555555f.....
                                .....ffff555542255555555ff....
                                .....ff55555555555555555ff....
                                .....ff55555555555555555f5f...
                                .....f55555f555555525555f55f..
                                .....f55555f555555525555f55f..
                                .....f55555f555555222555f555f.
                                .....f5555f4445555525555f555f.
                                .....ff555f4444445555555f555f.
                                .....fffff44444444555555f55f..
                                .....f44444444444444444fffff..
                                .....ff4444444444444444ff.....
                                .......fffffffffffffffff......
                                .........ff.......ff..........
                """),
                img("""
                    ..........ffffffff............
                                .ff.......fccccccff......ff...
                                f22f.......fccccccff....f77f..
                                ff22f.......fffffffff...ff77f.
                                .fff.....f..feeeeeeef.f..fff..
                                .........ffffffffffffff.......
                                ...........f452555525f........
                                ...ff......f425555552f........
                                ..f44f.....f4ff5555fff........
                                ..ff44f....f4fff55ffff........
                                ...fff.....f425555552f....ff..
                                ..........ff424445552f...faaf.
                                .........f4f444ffff55f...ffaaf
                                .ff.....f44f44ff222f5fff..fff.
                                f88f...f444ffff2222fff5f......
                                ff88f.f44444444222244555f.....
                                .fff..f44555544222555555f.....
                                .....ffff555542255555555ff....
                                .....ff55555555555555555ff....
                                .....ff55555555555555555f5f...
                                .....f55555f555555525555f55f..
                                .....f55555f555555525555f55f..
                                .....f55555f555555222555f555f.
                                .....f5555f4445555525555f555f.
                                .....ff555f4444445555555f555f.
                                .....fffff44444444555555f55f..
                                .....f44444444444444444fffff..
                                .....ff4444444444444444ff.....
                                .......fffffffffffffffff......
                                ........ff.........ff.........
                """),
                img("""
                    ..........ffffffff............
                                .ff.......fccccccff......ff...
                                f22f.......fccccccff....f77f..
                                ff22f.......fffffffff...ff77f.
                                .fff.....f..feeeeeeef.f..fff..
                                .........ffffffffffffff.......
                                ...........f452555525f........
                                ...ff......f425555552f........
                                ..f44f.....f4ff5555fff........
                                ..ff44f....f4fff55ffff........
                                ...fff.....f425555552f....ff..
                                ..........ff424445552f...faaf.
                                .........f4f444ffff55f...ffaaf
                                .ff.....f44f44ff222f5fff..fff.
                                f88f...f444ffff2222fff5f......
                                ff88f.f44444444222244555f.....
                                .fff..f44555544222555555f.....
                                .....ffff555542255555555ff....
                                .....ff55555555555555555ff....
                                .....ff55555555555555555f5f...
                                .....f55555f555555525555f55f..
                                .....f55555f555555525555f55f..
                                .....f55555f555555222555f555f.
                                .....f5555f4445555525555f555f.
                                .....ff555f4444445555555f555f.
                                .....fffff44444444555555f55f..
                                .....f44444444444444444fffff..
                                .....ff4444444444444444ff.....
                                .......fffffffffffffffff......
                                .......ff...........ff........
                """),
                img("""
                    ..........ffffffff............
                                .ff.......fccccccff......ff...
                                f22f.......fccccccff....f77f..
                                ff22f.......fffffffff...ff77f.
                                .fff.....f..feeeeeeef.f..fff..
                                .........ffffffffffffff.......
                                ...........f452555525f........
                                ...ff......f425555552f........
                                ..f44f.....f4ff5555fff........
                                ..ff44f....f4fff55ffff........
                                ...fff.....f425555552f....ff..
                                ..........ff424445552f...faaf.
                                .........f4f444ffff55f...ffaaf
                                .ff.....f44f44ff222f5fff..fff.
                                f88f...f444ffff2222fff5f......
                                ff88f.f44444444222244555f.....
                                .fff..f44555544222555555f.....
                                .....ffff555542255555555ff....
                                .....ff55555555555555555ff....
                                .....ff55555555555555555f5f...
                                .....f55555f555555525555f55f..
                                .....f55555f555555525555f55f..
                                .....f55555f555555222555f555f.
                                .....f5555f4445555525555f555f.
                                .....ff555f4444445555555f555f.
                                .....fffff44444444555555f55f..
                                .....f44444444444444444fffff..
                                .....ff4444444444444444ff.....
                                .......fffffffffffffffff......
                                ........ff.........ff.........
                """),
                img("""
                    ..........ffffffff............
                                .ff.......fccccccff......ff...
                                f22f.......fccccccff....f77f..
                                ff22f.......fffffffff...ff77f.
                                .fff.....f..feeeeeeef.f..fff..
                                .........ffffffffffffff.......
                                ...........f452555525f........
                                ...ff......f425555552f........
                                ..f44f.....f4ff5555fff........
                                ..ff44f....f4fff55ffff........
                                ...fff.....f425555552f....ff..
                                ..........ff424445552f...faaf.
                                .........f4f444ffff55f...ffaaf
                                .ff.....f44f44ff222f5fff..fff.
                                f88f...f444ffff2222fff5f......
                                ff88f.f44444444222244555f.....
                                .fff..f44555544222555555f.....
                                .....ffff555542255555555ff....
                                .....ff55555555555555555ff....
                                .....ff55555555555555555f5f...
                                .....f55555f555555525555f55f..
                                .....f55555f555555525555f55f..
                                .....f55555f555555222555f555f.
                                .....f5555f4445555525555f555f.
                                .....ff555f4444445555555f555f.
                                .....fffff44444444555555f55f..
                                .....f44444444444444444fffff..
                                .....ff4444444444444444ff.....
                                .......fffffffffffffffff......
                                .........ff.......ff..........
                """),
                img("""
                    ..........ffffffff............
                                .ff.......fccccccff......ff...
                                f22f.......fccccccff....f77f..
                                ff22f.......fffffffff...ff77f.
                                .fff.....f..feeeeeeef.f..fff..
                                .........ffffffffffffff.......
                                ...........f452555525f........
                                ...ff......f425555552f........
                                ..f44f.....f4ff5555fff........
                                ..ff44f....f4fff55ffff........
                                ...fff.....f425555552f....ff..
                                ..........ff424445552f...faaf.
                                .........f4f444ffff55f...ffaaf
                                .ff.....f44f44ff222f5fff..fff.
                                f88f...f444ffff2222fff5f......
                                ff88f.f44444444222244555f.....
                                .fff..f44555544222555555f.....
                                .....ffff555542255555555ff....
                                .....ff55555555555555555ff....
                                .....ff55555555555555555f5f...
                                .....f55555f555555525555f55f..
                                .....f55555f555555525555f55f..
                                .....f55555f555555222555f555f.
                                .....f5555f4445555525555f555f.
                                .....ff555f4444445555555f555f.
                                .....fffff44444444555555f55f..
                                .....f44444444444444444fffff..
                                .....ff4444444444444444ff.....
                                .......fffffffffffffffff......
                                ..........ff.....ff...........
                """),
                img("""
                    ..........ffffffff............
                                .ff.......fccccccff......ff...
                                f22f.......fccccccff....f77f..
                                ff22f.......fffffffff...ff77f.
                                .fff.....f..feeeeeeef.f..fff..
                                .........ffffffffffffff.......
                                ...........f452555525f........
                                ...ff......f425555552f........
                                ..f44f.....f4ff5555fff........
                                ..ff44f....f4fff55ffff........
                                ...fff.....f425555552f....ff..
                                ..........ff424445552f...faaf.
                                .........f4f444ffff55f...ffaaf
                                .ff.....f44f44ff222f5fff..fff.
                                f88f...f444ffff2222fff5f......
                                ff88f.f44444444222244555f.....
                                .fff..f44555544222555555f.....
                                .....ffff555542255555555ff....
                                .....ff55555555555555555ff....
                                .....ff55555555555555555f5f...
                                .....f55555f555555525555f55f..
                                .....f55555f555555525555f55f..
                                .....f55555f555555222555f555f.
                                .....f5555f4445555525555f555f.
                                .....ff555f4444445555555f555f.
                                .....fffff44444444555555f55f..
                                .....f44444444444444444fffff..
                                .....ff4444444444444444ff.....
                                .......fffffffffffffffff......
                                ...........ff...ff............
                """),
                img("""
                    ..........ffffffff............
                                .ff.......fccccccff......ff...
                                f22f.......fccccccff....f77f..
                                ff22f.......fffffffff...ff77f.
                                .fff.....f..feeeeeeef.f..fff..
                                .........ffffffffffffff.......
                                ...........f452555525f........
                                ...ff......f425555552f........
                                ..f44f.....f4ff5555fff........
                                ..ff44f....f4fff55ffff........
                                ...fff.....f425555552f....ff..
                                ..........ff424445552f...faaf.
                                .........f4f444ffff55f...ffaaf
                                .ff.....f44f44ff222f5fff..fff.
                                f88f...f444ffff2222fff5f......
                                ff88f.f44444444222244555f.....
                                .fff..f44555544222555555f.....
                                .....ffff555542255555555ff....
                                .....ff55555555555555555ff....
                                .....ff55555555555555555f5f...
                                .....f55555f555555525555f55f..
                                .....f55555f555555525555f55f..
                                .....f55555f555555222555f555f.
                                .....f5555f4445555525555f555f.
                                .....ff555f4444445555555f555f.
                                .....fffff44444444555555f55f..
                                .....f44444444444444444fffff..
                                .....ff4444444444444444ff.....
                                .......fffffffffffffffff......
                                ..........ff.....ff...........
                """)],
            75,
            True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_on_overlap17(sprite, otherSprite):
    global pito_de_caballo, alma
    sprite.destroy()
    otherSprite.destroy(effects.star_field, 1)
    pito_de_caballo += 1
    alma = sprites.create(img("""
            . . c c c c c c . . . . . 
                    . c c c c c c c c . . . . 
                    b c c c c c c c b c . . . 
                    c b b c c c b b c c . . . 
                    c 2 2 b c b 2 2 c c . . . 
                    c c 2 c c c 2 c c c . . . 
                    c c c c c c c c c c . . . 
                    b b c b c b c b b c . . . 
                    c b b c b c b b c c . . . 
                    c c c c c c c c c c c . . 
                    c c c c c c c c c c c . . 
                    . c c c c c c c c c c . . 
                    . c c c c c c c c c c . . 
                    . . c c c c c c c c c c . 
                    . . . c c c c c c c c c . 
                    . . . . . c c c c c c c . 
                    . . . . . . . . . . c c c
        """),
        SpriteKind.alma_)
    alma.set_position(288, 87)
    if pito_de_caballo == 1:
        alma.follow(J1, 35)
    if pito_de_caballo == 2:
        alma.follow(J1, 45)
    if pito_de_caballo == 3:
        alma.follow(J1, 60)
    if pito_de_caballo == 4:
        alma.follow(J1, 82.5)
    if pito_de_caballo == 5:
        alma.follow(J1, 100)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.cuerpo3, on_on_overlap17)

def on_on_overlap18(sprite, otherSprite):
    otherSprite.destroy()
    nivel3()
sprites.on_overlap(SpriteKind.player, SpriteKind.libro2, on_on_overlap18)

def on_on_overlap19(sprite, otherSprite):
    sprite.set_velocity(50, 128)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.Barrera_3, on_on_overlap19)

def on_on_overlap20(sprite, otherSprite):
    otherSprite.destroy(effects.halo, 1)
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.alma_, on_on_overlap20)

def on_on_overlap21(sprite, otherSprite):
    J1.x += -24
    game.show_long_text("Deberías inspeccionar primero las pruebas de esta zona.",
        DialogLayout.BOTTOM)
sprites.on_overlap(SpriteKind.player, SpriteKind.muro, on_on_overlap21)

def on_on_overlap22(sprite, otherSprite):
    global cuchillo_asesino2, pingo
    if controller.B.is_pressed() and whenbut == 1:
        J1.set_velocity(0, 0)
        cuchillo_asesino2 = sprites.create(img("""
                . . . . . . . . . . . . . . e e 
                            . . . . . . . . . . . . . e e e 
                            . . . . . . . . . . . . e e e . 
                            . . . . . . . . . . . e e e . . 
                            . . . . . . . . . . 1 e e . . . 
                            . . . . . . . . . 1 1 1 1 1 2 . 
                            . . . . . . . . 1 1 1 1 1 2 2 . 
                            . . . . . . . 1 1 1 1 1 2 2 . . 
                            . . . . . . 1 1 1 1 1 2 2 . . . 
                            . . . . . 1 1 1 1 1 2 2 . . . . 
                            . . . . 1 1 1 1 1 2 2 . . . . . 
                            . . . 1 1 1 1 1 2 2 . . . . . . 
                            . . 1 1 1 1 2 2 2 . . . . . . . 
                            . 1 1 1 2 2 2 . . . . . . . . . 
                            1 1 2 2 2 . . . . . . . . . . . 
                            2 2 2 . . . . . . . . . . . . .
            """),
            SpriteKind.cuchillo_asesino)
        cuchillo_asesino2.set_position(450, -5)
        cuchillo_asesino2.follow(J1, 250)
    b2.set_position(165, 85)
    if controller.B.is_pressed() and whenbut == 0:
        game.show_long_text("Este señor confiesa que efectivamente estaba aquí en la hora de la muerte paseando al perro pero no vio nada, pues no pasó cerca del cuerpo.",
            DialogLayout.BOTTOM)
        b2.destroy()
        pingo += 1
    if pingo == 2:
        muro2.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.sospechoso1, on_on_overlap22)

def on_on_overlap23(sprite, otherSprite):
    global reina_boss2, Z_vida_reina_Z
    if Z_vida_reina_Z == 4:
        otherSprite.destroy(effects.rings, 500)
        reina_boss2 = sprites.create(img("""
                ............111111111............
                            ...........11111111111...........
                            ...........11111111111...........
                            ..........1111111111111..........
                            ..........1177777777711..........
                            .........111717777717111.........
                            .........111771777177111.........
                            .........711719171917117.........
                            .........771719171917177.........
                            .777.....177777777777771.....777.
                            76677....11177fffff77111....77667
                            776677...111776777677111...776677
                            776767...11117777777111....767677
                            .7676777..111b33333311...7776767.
                            .76776677...3b3333333...77667767.
                            .77776767777b3333333b77776767777.
                            ..77767766773333333337766776777..
                            ..7776776766333bb33336676776777..
                            ...77677677633bb33bb3677677677...
                            ...777776777333333b33777677777...
                            ...77777677733333bb33777677777...
                            ....77777777333bbb33377777777....
                            ......7.7.7.333333333.7.7.7......
                            ............b33333b33............
                            ............3bb3bb333............
                            ............33bb33333............
                            ............7777.7777............
                            ............f777.777f............
                            ............fff7.7fff............
                            ............ffff.ffff............
                            ............ffff.ffff............
                            ............ffff.ffff............
                            ............f..f.f..f............
            """),
            SpriteKind.reina_boss)
        reina_boss2.set_position(80, 65)
    Z_vida_reina_Z += 1
    sprite.destroy()
sprites.on_overlap(SpriteKind.projectile, SpriteKind.reina, on_on_overlap23)

def on_on_overlap24(sprite, otherSprite):
    global puntos
    otherSprite.destroy(effects.fire, 50)
    sprite.destroy()
    puntos += 1
sprites.on_overlap(SpriteKind.projectile,
    SpriteKind.enemy_AVION,
    on_on_overlap24)

def on_on_overlap25(sprite, otherSprite):
    sprite.destroy()
    otherSprite.destroy()
sprites.on_overlap(SpriteKind.projectile, SpriteKind.Barrera, on_on_overlap25)

def on_on_overlap26(sprite, otherSprite):
    sprite.destroy(effects.spray, 1)
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.cuchillo, SpriteKind.player, on_on_overlap26)

def on_on_overlap27(sprite, otherSprite):
    global vida_jack
    if vida_jack == 26:
        jack_the_ripper.destroy(effects.blizzard, 2500)
    vida_jack += 1
    sprite.destroy()
sprites.on_overlap(SpriteKind.projectile, SpriteKind.jack, on_on_overlap27)

def on_on_overlap28(sprite, otherSprite):
    global pito_de_caballo, alma
    sprite.destroy()
    otherSprite.destroy(effects.star_field, 1)
    pito_de_caballo += 1
    alma = sprites.create(img("""
            . . c c c c c c . . . . . 
                    . c c c c c c c c . . . . 
                    b c c c c c c c b c . . . 
                    c b b c c c b b c c . . . 
                    c 2 2 b c b 2 2 c c . . . 
                    c c 2 c c c 2 c c c . . . 
                    c c c c c c c c c c . . . 
                    b b c b c b c b b c . . . 
                    c b b c b c b b c c . . . 
                    c c c c c c c c c c c . . 
                    c c c c c c c c c c c . . 
                    . c c c c c c c c c c . . 
                    . c c c c c c c c c c . . 
                    . . c c c c c c c c c c . 
                    . . . c c c c c c c c c . 
                    . . . . . c c c c c c c . 
                    . . . . . . . . . . c c c
        """),
        SpriteKind.alma_)
    alma.set_position(152, 87)
    if pito_de_caballo == 1:
        alma.follow(J1, 35)
    if pito_de_caballo == 2:
        alma.follow(J1, 45)
    if pito_de_caballo == 3:
        alma.follow(J1, 60)
    if pito_de_caballo == 4:
        alma.follow(J1, 82.5)
    if pito_de_caballo == 5:
        alma.follow(J1, 100)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.cuerpo, on_on_overlap28)

def on_on_overlap29(sprite, otherSprite):
    global eoaiu
    otherSprite.destroy()
    sprite.destroy(effects.disintegrate, 1)
    eoaiu += 1
sprites.on_overlap(SpriteKind.ballesta, SpriteKind.projectile, on_on_overlap29)

def on_on_destroyed3(sprite):
    muro3.destroy()
sprites.on_destroyed(SpriteKind.B4, on_on_destroyed3)

def on_on_overlap30(sprite, otherSprite):
    otherSprite.destroy()
    nivel4()
sprites.on_overlap(SpriteKind.player, SpriteKind.libro3, on_on_overlap30)

def on_on_overlap31(sprite, otherSprite):
    otherSprite.destroy()
    nivel2()
sprites.on_overlap(SpriteKind.player, SpriteKind.libro, on_on_overlap31)

def on_on_overlap32(sprite, otherSprite):
    sherlock.follow(J1, 30)
    sherlock.x += -3
    pause(100)
sprites.on_overlap(SpriteKind.player, SpriteKind.Sherlock, on_on_overlap32)

def on_on_overlap33(sprite, otherSprite):
    otherSprite.destroy()
    nivel5()
sprites.on_overlap(SpriteKind.player, SpriteKind.libro4, on_on_overlap33)

def on_on_overlap34(sprite, otherSprite):
    otherSprite.destroy(effects.rings, 1)
    sprite.destroy()
sprites.on_overlap(SpriteKind.projectile, SpriteKind.Soldado, on_on_overlap34)

def on_on_destroyed4(sprite):
    global whenbut
    sospechoso1_mov()
    sospechoso4_mov()
    sospechoso3_mov()
    culpable.set_velocity(150, 0)
    pause(1050)
    culpable.set_velocity(0, 0)
    game.show_long_text("Sherlock: ¿Crees saber quién es el asesino? Si es así, pulsa B sobre él.",
        DialogLayout.BOTTOM)
    whenbut = 1
sprites.on_destroyed(SpriteKind.muro4, on_on_destroyed4)

def nivel1():
    global Libros, oso2, aquarius, libro_1_paddington
    game.splash("NIVEL 1:", "\"Paddington\"")
    game.show_long_text("El primer libro que tendrás que conseguir es `Paddington´, y para ello deberás evitar los aviones mientras cruzas frente al Big Ben",
        DialogLayout.BOTTOM)
    J1.set_position(72, 73)
    Libros = 0
    info.set_life(5)
    tiles.set_tilemap(tilemap("""
        level
    """))
    scene.set_background_image(img("""
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                888888888888888888888888888888888888888f888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                88888888888888888888888888888888888888fdf88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                8888888888888888888888888888888888888fdddf888888888888888888888888888888888888888888888888888888888888888888888f88f8888888888f8888888888888888888888888888888888
                8888888888888888888888888888888888888fdddf88888888888888888888888888888888888888888888888888888888888888888888fdf8ff88f88888ff8888888888888888888888888888888888
                888888888888888888888888888888888888fdddddf8888888888888888888888888888888888888888888888888888888888888888888fdf8ff8fdf8f88ff8888888888888888888888888888888888
                888888888888888888888888888888888888fdd6ddf8888888888888888888888888888888888888888888888888888888888888888888fdf8fffdddff88ff8888888888888888888888888888888888
                88888888888888888888888888888888888fddd6ddf8888888888888888888888888888888888888888888888888888888888888888888fdf8ffdd6dff88ff8888888888888888888888888888888888
                88888888888888888888888888888888888fdd666ddf88888888888888888888888888888888888888888888888888888888888888888fddf8ffdd6dff8fdf8888888888888888888888888888888888
                88888888888888888888888888888888888fd66666df88888888888888888888888888888888888888888888888888888888888888888fddf8fdd66fdfffddf888888888888888888888888888888888
                8888888888888888888888888888888888fdd66666ddf8888888888888888888888888888888888888888888888888888888888888888fddfffdd66fdfdfddf888888888888888888888888888888888
                8888888888888888888888888888888888fdd66666ddf888888888888888888888888888888888888888888888888888888888888888fdddfddd666fdfdfddf888888888888888888888888888888888
                888888888888888888888888888888888fddd66666ddf888888888888888888888888888888888888888888888888888888888888888fddddfffff6fdfdfddf888888888888888888888888888888888
                888888888888888888888888888888888fdeeeeeeeeedf88888888888888888888888888888888888888888888888888888888888888fdddddddddfffffdddf888888888888888888888888888888888
                88888888888888888888888888888888fddddddddddddf88888888888888888888888888888888888888888888888888888888888888fdddddddddddddfdddf888888888888888888888888888888888
                88888888888888888888888888888888fddddddddddddf88888888888888888888888888888888888888888888888888888888888888fdddddddddddddfdddf888888888888888888888888888888888
                88888888888888888888888888888888fddddddddddddf88888888888888888888888888888888888888888888888888888888888888fdddddddddddddfdddf888888888888888888888888888888888
                88888888888888888888888888888888fddddddddddddf88888888888888888888888888888888888888888888888888888888888888fdddddddddddddfdddf888888888888888888888888888888888
                88888888888888888888888888888888feeeeeeeeeeeef88888888888888888888888888888888888888888888888888888888888888feedddddddddddfdddf888888888888888888888888888888888
                88888888888888888888888888888888fddddeddeddddf88888888888888888888888888888888888888888888888888888888888888fddeeeedddddddfdddf888888888888888888888888888888888
                88888888888888888888888888888888fddddeddeddddf88888888888888888888888888888888888888888888888888888888888888fddddedeeeddddfdeef888888888888888888888888888888888
                88888888888888888888888888888888fddddeeeeddddfffffffffffffffffffffffffffffffff888888888888888888888888888888fddddeddedeeeefeddf888888888888888888888888888888888
                88888888888888888888888888888888fddddddddddddfdeddddddddddddddddddddddddddddddfffffffffffffffffffffffffffffffddddeddedddddfdddf888888888888888888888888888888888
                88888888888888888888888888888888fddddddddddddfddedddddddddddddddddddddddddddddddddddddddddddddddddddddddddedfddddeededddddfdddf888888888888888888888888888888888
                88888888888888888888888888888888fddddddddddddfdddeeeeeeeeeeeeeedddddddddddddddddddddddddddddddddddddddddddedfddddddeedddddfdddf888888888888888888888888888888888
                88888888888888888888888888888888fddddddddddddfdddddddddddddddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeddddddddddddddeddfdddddddddddddfdddf888888888888888888888888888888888
                8888888888888888888888888888888ffddddddddddddfdddddddddddddddddddddddddddddddddddddddddddddeeeeeeeeeeeeeedddfdddddddddddddfdddf888888888888888888888888888888888
                8888888888888888888888888888888ffddddddddddddf666666666666666dddddddddddddddddddddddddddddddddddddddddddddddfeedddddddddddffddff88888888888888888888888888888888
                8888888888888888888888888888888ffeeeeeeddddddffffffffffffffff6666666666666666666666666666666ddddddddddddddddfddeeeedddddddffddff88888888888888888888888888888888
                888888888888888888888888888888fffddddddeeeeeef888888888888888fffffffffffffffffffffffffffffff6666666666666666fddddddeeeedddfdfef8f8888888888888888888888888888888
                888888888888888888888888888888f8fddddddddddddf8888888888888888888888888888888888888888888888fffffffffffffffffddddddddddeeefefdf8ff888888888888888888888888888888
                88888888888888888888888888888ff8fddddddddddddf88888888888888888888888888888888888888888888888888888888888888fdddddddddddddfddff88f888888888888888888888888888888
                8888888888888888888888888888ff88fddddddddddddf88888888888888888888888888888888888888888888888888888888888888fdddddddddddddfddff888f88888888888888888888888888888
                8888888888888888888888888888f888fddddddddddddf88888888888888888888888888888888888888888888888888888888888888fdddddddddddddfdddf888f88888888888888888888888888888
                88888888888888888888888888ff8888fddddddddddddf88888888888888888888888888888888888888888888888888888888888888fdddddddddddddfdddff888f8888888888888888888888888888
                8888888888888888888888888ff8888ffddddddddddddf88888888888888888888888888888888888888888888888888888888888888fdddddddddddddfdddfff88f8888888888888888888888888888
                888888888888888888888888ff88888ffddddddddddddf88888888888888888888888888888888888888888888888888888888888888fdddddddddddddfdddf8f888ff88888888888888888888888888
                8888888888888888888888ff888888f8fddddddddddddf88888888888888888888888888888888888888888888888888888888888888fdddddddddddddfdddf8f8888ff8888888888888888888888888
                888888888888888888888ff8888888f8fddddddddddddf88888888888888888888888888888888888888888888888888888888888888fdddddddddddddfdddf88f8888ff888888888888888888888888
                8888888888888888888fff8888888f88fddddddddddddf88888888888888888888888888888888888888888888888888888888888888fdddddddddddddfdddf88f88888ff88888888888888888888888
                88888888888888888fff888888888f88fddddddddddddf88888888888888888888888888888888888888888888888888888888888888fdddddddddddddfdddf888f88888ff8888888888888888888888
                8888888888888888ff8888888888f888fddddddddddddf88888888888888888888888888888888888888888888888888888888888888fdddddddddddddfdddf8888f888888f888888888888888888888
                888888888888888ff8888888888f8888feeeeeeddddddf88888888888888888888888888888888888888888888888888888888888888feeeddddddddddfdddf8888ff888888f88888888888888888888
                8888888888888fff8888888888f88888fddddddeeeeeef88888888888888888888888888888888888888888888888888888888888888fdddeeeeddddddfdddf88888f8888888f8888888888888888888
                88888888888ff88888888888ff888888fddddddddddddf88888888888888888888888888888888888888888888888888888888888888fdddddddeeeeddfdeef888888f8888888ff88888888888888888
                888888888ff88888888888ff88888888fddddddddddddf88888888888888888888888888888888888888888888888888888888888888fdddddddddddeefeddf888888ff88888888f8888888888888888
                8888888ff888888888888f8888888888fddddddddddddf88888888888888888888888888888888888888888888888888888888888888fdddddddddddddfdddf8888888ff88888888fff8888888888888
                88888ff888888888888ff88888888888fddddddddddddf88888888888888888888888888888888888888888888888888888888888888fdddddddddddddfdddf88888888ff888888888fff88888888888
                88fff88888888888fff8888888888888fddddddddddddf88888888888888888888888888888888888888888888888888888888888888fdddddddddddddfdddf888888888ff88888888888fff88888888
                ffffffff8888ffff8888888888888888fddddddddddddf88888888888888888888888888888888888888888888888888888888888888fdddddddddddddfdddf8888888888f8888888888888ff8888888
                eeeeeeeeffffffffffffffff88888888fddddddddddddf88888888888888888888888888888888888888888888888888888888888888fdddddddddddddfdddf88888888888ff8888888888888fff8888
                eeeeeeeeeeeeeeeeeeeeeeeefffffffffddddddddddddffffffff8888888888888888888888888888888888888888888888888888888fdddddddddddddfdddf888888888888fff88888888888888ff88
                eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddddddddddddfeeeeeeeffffffffffff8888888888888888888888888888888888888888888fdddddddddddddfdddf88888888888888ff888888888888888ff
                eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddddddddddddfeeeeeeeeeeeeeeeeeeeffffffffffff8888888888888888888888888888888fdddddddddddddfdddf8888888888888888ff888888888888888
                ffffffffeeeeeeeeeeeeeeeeeeeeeeeefeeedddddddddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffffffffff8888888888888888888fdddddddddddddfdfff888888888888888888fff888888888888
                88888888ffffffffffffffffeeeeeeeefdddeeeedddddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffffffffff8888888fdddddddddddddfffff888888888888888888888ffff88888888
                888888888888888888888888fffffffffdddddddeeeddffffffffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffffffdddddddddddddffccf8888888888888888888888888ffff8888
                88888888888888888888888888888888fddddddddddeef8888888ffffffffffffffffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefdddddddddddddffccff8888888888888888888888888888fff8
                88888888888888888888888888888888fddddddddddddf88888888888888888888888fffffffffffffffeeeeeeeeeeeeeeeeeeeeeeeefeedddddddddddffccffffffffff8888888888888888888888ff
                88888888888888888888888888888888fddddddddddddf88888888888888888888888888888888888888ffffffffffffffffeeeeeeeefddeeeddddddddffcceeeeeeeeeeffffffffffffffff88888888
                88888888888888888888888888888888fddddddddddddf888888888888888888888888888888888888888888888888888888fffffffffdddddeeddddddffeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffffff
                88888888888888888888888888888888fddddddddddddf88888888888888888888888888888888888888888888888888888888888888fdddddddeeedddfffffffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                88888888888888888888888888888888fddddddddddddf88888888888888888888888888888888888888888888888888888888888888fddddddddddeeefeddf8fffffffffffeeeeeeeeeeeeeeeeeeeee
                88888888888888888888888888888888fddddddddddddf88888888888888888888888888888888888888888888888888888888888888fdddddddddddddfdddf8888888888ffffffffffeeeeeeeeeeeee
                88888888888888888888888888888888fddddddddddddf88888888888888888888888888888888888888888888888888888888888888fdddddddddddddfdddf8888888888888888888ffffffffffeeee
                88888888888888888888888888888888fddddddddddddf88888888888888888888888888888888888888888888888888888888888888fdddddddddddddfdddf8888888888888888888888888888fffff
                88888888888888888888888888888888fddddddddddddf88888888888888888888888888888888888888888888888888888888888888fdddddddddddddfdddf888888888888888888888888888888888
                8888888888888888888888888888888ffffffffddddddf8888888888888888888888888888888888888888888888888888888888888ffdddddddddddddfdddfff8888888888888888888888888888888
                888888888888888888888888888888fddddddddfffffffff8888888888888888888888888888888888888888888888888888888888ffffffffffddddddfdddfddf888888888888888888888888888888
                888888888888888888888888888888fdddddddddddddddddf88888888888888888888888888888888888888888888888888888888fddddddddddffffffffffdddf888888888888888888888888888888
                888888888888888888888888888888fdddddddddddddddddf88888888888888888888888888888888888888888888888888888888fddddddddddddddddddfddddf888888888888888888888888888888
                888888888888888888888888888888fdddddddddddddddddf88888888888888888888888888888888888888888888888888888888fddddddddddddddddddfddddf888888888888888888888888888888
                888888888888888888888888888888fdddddddddddddddddf88888888888888888888888888888888888888888888888888888888fddddddddddddddddddfddddf888888888888888888888888888888
                888888888888888888888888888888fdddddddddddddddddf88888888888888888888888888888888888888888888888888888888fddddddddddddddddddfddddf888888888888888888888888888888
                88888888888888888888888888888fddddddddddddddddddf8888888888888888888888888888888888888888888888888888888fddddddddddddddddddddfdddf888888888888888888888888888888
                88888888888888888888888888888fddddddddddddddddddf8888888888888888888888888888888888888888888888888888888fddddddddddddddddddddfdddf888888888888888888888888888888
                88888888888888888888888888888fddddddddddddddddddf8888888888888888888888888888888888888888888888888888888fddddddddddddddddddddfdddf888888888888888888888888888888
                88888886666666666888888888888fddddddddddddd66666f8888888888888888888888888888888888888888888888888888888fddddddddddddddddddddfdddf888888888888888888888888888888
                8666666666666666666668888888fddddddddd666666666666666666688888888888888888888888888888666666666666688888fdddddddddddddddddddddfddf888888888888888888888888888888
                66666666666666666666666666666666666666666666666666666666666668888888888888888888666666666666666666666668fddddddddddddddddddddd6666666666688888888866666666666668
                6666666666666666666666666666666666666666666666666666666666666666666666888666666666666666666666666666666666666666666666666666666666666666666666666666666999996666
                6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666999999999999666666666666666666666666666666666666666666669999666669966
                6669999999999999666666666666666666666666666666666666666666666666666666666666666666666666999666666666666999966666666666666666666666666666666666666666666666666699
                6666666666666666999966666669666666666666666666666666666666666666666666666666666666666666666666666666666666699999999999666666666666666666666666666666666666666666
                6666666666666666666699999996666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
    """))
    oso2 = sprites.create(img("""
            . . f f . f f f f f f . f f . . 
                    . f e e f 2 2 2 2 2 2 f e e f . 
                    f f f f 2 2 2 2 2 2 2 2 f f f f 
                    f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 
                    . f f f f f f f f f f f f f f . 
                    . . f e e e e 1 f e 1 f e f . . 
                    . . f e e e e 1 f e 1 f e f . . 
                    . . f e e e e e e e e e e f . . 
                    . f e e e e e e f f f e e e f . 
                    . . f e e e e e e f e e e f . . 
                    . f e e e e e e f 2 f e e e f . 
                    . . f f f f f f f f f f f f . . 
                    . . . f 8 8 8 8 8 8 8 8 f . . . 
                    . . f e 8 8 8 8 8 8 8 8 e f . . 
                    . . . f f e e f f e e f f . . . 
                    . . . . f f f . . f f f . . . .
        """),
        SpriteKind.oso)
    oso2.follow(J1, 95)
    aquarius = sprites.create(img("""
            . 6 6 1 1 1 6 6 . 
                    6 6 6 6 1 1 9 6 6 
                    6 6 6 6 6 6 6 9 6 
                    6 6 8 6 6 6 6 6 9 
                    6 8 6 8 6 6 6 6 9 
                    6 8 6 8 6 6 6 6 6 
                    6 8 8 8 6 6 6 6 6 
                    6 8 6 8 6 6 6 6 6 
                    6 8 6 8 6 6 6 6 6 
                    6 6 6 8 6 6 6 6 6 
                    6 6 6 8 6 6 6 6 6 
                    6 6 6 6 6 6 6 6 6 
                    . 6 6 6 6 6 6 6 . 
                    . . 6 6 6 6 6 . .
        """),
        SpriteKind.Comida)
    aquarius.set_position(538, 41)
    libro_1_paddington = sprites.create(img("""
            . . . . . . f f . . . . . . 
                    . . . . f f f f f . . . . . 
                    . . . f f 8 8 8 f f . . . . 
                    . . f f 8 8 8 f 8 f . . . . 
                    . f f 8 8 8 f 8 8 f f . . . 
                    f f f 8 8 f 8 8 8 8 f f . . 
                    f 1 f f 8 8 8 8 f 8 8 f f . 
                    f f 1 f f 8 8 f 8 8 8 8 f f 
                    . f f 1 f 8 8 8 8 8 f 8 c f 
                    . . f f 1 f f 8 8 f 8 c f f 
                    . . . f d 1 f f c c c f f . 
                    . . . f f d d f f c f f . . 
                    . . . . f f d d f f f . . . 
                    . . . . . . f f f . . . . .
        """),
        SpriteKind.libro)
    libro_1_paddington.set_position(768, 105)

def on_hit_wall2(sprite, location):
    sprite.destroy(effects.spray, 1)
scene.on_hit_wall(SpriteKind.cuchillo_lluvia, on_hit_wall2)

def on_on_overlap35(sprite, otherSprite):
    global cuchillo_asesino2
    if controller.B.is_pressed() and whenbut == 1:
        J1.set_velocity(0, 0)
        cuchillo_asesino2 = sprites.create(img("""
                . . . . . . . . . . . . . . e e 
                            . . . . . . . . . . . . . e e e 
                            . . . . . . . . . . . . e e e . 
                            . . . . . . . . . . . e e e . . 
                            . . . . . . . . . . 1 e e . . . 
                            . . . . . . . . . 1 1 1 1 1 2 . 
                            . . . . . . . . 1 1 1 1 1 2 2 . 
                            . . . . . . . 1 1 1 1 1 2 2 . . 
                            . . . . . . 1 1 1 1 1 2 2 . . . 
                            . . . . . 1 1 1 1 1 2 2 . . . . 
                            . . . . 1 1 1 1 1 2 2 . . . . . 
                            . . . 1 1 1 1 1 2 2 . . . . . . 
                            . . 1 1 1 1 2 2 2 . . . . . . . 
                            . 1 1 1 2 2 2 . . . . . . . . . 
                            1 1 2 2 2 . . . . . . . . . . . 
                            2 2 2 . . . . . . . . . . . . .
            """),
            SpriteKind.cuchillo_asesino)
        cuchillo_asesino2.set_position(450, -5)
        cuchillo_asesino2.follow(J1, 250)
    b5.set_position(285, 85)
    if controller.B.is_pressed() and whenbut == 0:
        game.show_long_text("El hombre cuenta que estaba vigilando el parque y observó a un hombre con bate paseando al perro, un señor rubio acostado en el banco y al señor calvo en un arbusto, e intuye que \"hacía sus necesidades\".",
            DialogLayout.BOTTOM)
        b5.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.sospechoso4, on_on_overlap35)

def on_on_overlap36(sprite, otherSprite):
    info.change_life_by(-777)
sprites.on_overlap(SpriteKind.player,
    SpriteKind.cuchillo_asesino,
    on_on_overlap36)

def on_on_overlap37(sprite, otherSprite):
    global puntos
    otherSprite.destroy(effects.disintegrate, 1)
    sprite.destroy()
    puntos += 1
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap37)

def sospechoso1_mov():
    sospechoso_josuke.set_velocity(150, 0)
    pause(1000)
    sospechoso_josuke.set_velocity(0, 0)

def on_on_overlap38(sprite, otherSprite):
    global cuchillo_asesino2
    if controller.B.is_pressed() and whenbut == 1:
        J1.set_velocity(0, 0)
        cuchillo_asesino2 = sprites.create(img("""
                . . . . . . . . . . . . . . e e 
                            . . . . . . . . . . . . . e e e 
                            . . . . . . . . . . . . e e e . 
                            . . . . . . . . . . . e e e . . 
                            . . . . . . . . . . 1 e e . . . 
                            . . . . . . . . . 1 1 1 1 1 2 . 
                            . . . . . . . . 1 1 1 1 1 2 2 . 
                            . . . . . . . 1 1 1 1 1 2 2 . . 
                            . . . . . . 1 1 1 1 1 2 2 . . . 
                            . . . . . 1 1 1 1 1 2 2 . . . . 
                            . . . . 1 1 1 1 1 2 2 . . . . . 
                            . . . 1 1 1 1 1 2 2 . . . . . . 
                            . . 1 1 1 1 2 2 2 . . . . . . . 
                            . 1 1 1 2 2 2 . . . . . . . . . 
                            1 1 2 2 2 . . . . . . . . . . . 
                            2 2 2 . . . . . . . . . . . . .
            """),
            SpriteKind.cuchillo_asesino)
        cuchillo_asesino2.set_position(450, -5)
        cuchillo_asesino2.follow(J1, 250)
    b4.set_position(235, 85)
    if controller.B.is_pressed() and whenbut == 0:
        game.show_long_text("Este hombre rubio cuenta que estuvo aquí durmiendo en el banco y no oyó ni vio nada.",
            DialogLayout.BOTTOM)
        b4.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.sospechoso3, on_on_overlap38)

def on_on_overlap39(sprite, otherSprite):
    global puntos
    otherSprite.destroy(effects.disintegrate, 1)
    info.change_life_by(-1)
    puntos += 1
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap39)

cuchillo13: Sprite = None
cuchillo12: Sprite = None
cuchillo11: Sprite = None
cuchillo10: Sprite = None
cuchillo9: Sprite = None
cuchillo8: Sprite = None
cuchillo7: Sprite = None
cuchillo6: Sprite = None
cuchillo5: Sprite = None
cuchillo4: Sprite = None
cuchillo3: Sprite = None
cuchillo2: Sprite = None
cuchillo14: Sprite = None
libro_1_paddington: Sprite = None
vida_jack = 0
reina_boss2: Sprite = None
cuchillo_asesino2: Sprite = None
libro_5_londres_bajo_tierra: Sprite = None
torturado5: Sprite = None
torturado4: Sprite = None
torturado3: Sprite = None
torturado2: Sprite = None
torturado: Sprite = None
libro_2_londrés: Sprite = None
barrera__3: Sprite = None
eoaiu = 0
Soldado1_: Sprite = None
Soldado_: Sprite = None
reina2: Sprite = None
vida_boss = 0
Z_vida_reina_Z = 0
libro_4_Sherlock_Holmes: Sprite = None
burbuja5: Sprite = None
burbuja4: Sprite = None
burbuja3: Sprite = None
burbuja2: Sprite = None
Monster: Sprite = None
ballestero: Sprite = None
malo4: Sprite = None
malo3: Sprite = None
malo2: Sprite = None
Malo_: Sprite = None
cartel: Sprite = None
burbuja: Sprite = None
aquarius: Sprite = None
avión: Sprite = None
Barrera_: Sprite = None
barrera6_: Sprite = None
barrera5_: Sprite = None
barrera4_: Sprite = None
Barrera2_: Sprite = None
fase_jack = 0
libro_3_from_hell: Sprite = None
Bala_izquierda: Sprite = None
Bala: Sprite = None
muro42: Sprite = None
muro3: Sprite = None
muro2: Sprite = None
muro1: Sprite = None
b6: Sprite = None
b5: Sprite = None
b4: Sprite = None
b3: Sprite = None
b2: Sprite = None
b1: Sprite = None
victima2: Sprite = None
sospechoso_fumador: Sprite = None
culpable: Sprite = None
sospechoso_josuke: Sprite = None
sherlock: Sprite = None
flecha2: Sprite = None
jack_the_ripper: Sprite = None
whenbut = 0
pingo = 0
Libros = 0
sospechoso_negro: Sprite = None
oso2: Sprite = None
puntos = 0
alma: Sprite = None
pito_de_caballo = 0
J1: Sprite = None
sí = 0
sí = 0
J1 = sprites.create(img("""
        f f f f f f f f f . . . . . . . 
            f f c c c c c c f f f . . . . . 
            . . f c c c c c c c f f . . . . 
            . . f f c c c c c c c f f . . . 
            . . . f c c c c f f f f f . . . 
            . . . f f f f f f e e e f . . . 
            . f . f e e e e e e e e f . f . 
            . f f f f f f f f f f f f f f . 
            . . . f 5 5 5 5 5 5 5 5 5 f . . 
            . . . f 5 5 5 f 5 5 5 5 f f . . 
            . . . f 5 5 5 5 5 5 5 5 5 f . . 
            . . . f 5 5 5 f 5 5 5 f 5 f . . 
            . . . f 5 5 5 5 f f f 5 5 f . . 
            . . . f 5 5 5 5 5 5 5 5 5 f . . 
            . . . f 5 5 f f f f f 5 5 f . . 
            . . . f f f f . . . f f f f . .
    """),
    SpriteKind.player)
controller.move_sprite(J1, 100, 0)
scene.camera_follow_sprite(J1)
game.splash("¡VIAJE POR LONDRES!", "Recorreremos algunos de")
game.splash("los lugares más caracte-", "-rísticos de la ciudad")
game.splash("para recolectar 5 libros.", "¡VAMOS ALLÁ!")
info.change_score_by(1)
nivel1()

def on_update_interval():
    global flecha2
    if Libros == 1 and eoaiu < 1:
        flecha2 = sprites.create(img("""
                . . . f . . . . . . . . . . 
                            . f f f . . . . . . . . 1 1 
                            f f f f e e e e e e e e e e 
                            . f f f . . . . . . . . 1 1 
                            . . . f . . . . . . . . . .
            """),
            SpriteKind.flecha)
        flecha2.set_velocity(-150, 0)
        flecha2.set_position(510, 104)
game.on_update_interval(250, on_update_interval)

def on_update_interval2():
    global avión
    if Libros == 0:
        avión = sprites.create(img("""
                . . . . . . . f f f . . . . . . . . 
                            . . . . . . f c c f . . . . . . . . 
                            . . . . . f c c c f . . . . . . f f 
                            . . . . . f c c c f . . . . . f c f 
                            . . . f f f f f f f f f f f f c c f 
                            . f f f f c c c c c c c c c c c c f 
                            f 2 2 2 f c c c c c c c c c c c c f 
                            f f f f f c c c c c c c c c c c c f 
                            f c c c c c c c c c f c c c c c c f 
                            f f f f f f c c c c f f f f f f f . 
                            . . . . . f c c c c f . . . . . . . 
                            . . . . . . f c c c f . . . . . . . 
                            . . . . . . . f f c f . . . . . . . 
                            . . . . . . . . f f f . . . . . . .
            """),
            SpriteKind.enemy_AVION)
        avión.set_position(800, randint(75, 125))
        avión.set_velocity(-100, 0)
game.on_update_interval(1000, on_update_interval2)

def on_forever():
    J1.set_velocity(0, 120)
    if controller.A.is_pressed() and J1.is_hitting_tile(CollisionDirection.BOTTOM):
        if controller.up.is_pressed():
            J1.set_velocity(0, -100)
            pause(350)
        else:
            J1.set_velocity(0, -100)
        pause(350)
forever(on_forever)

def on_forever2():
    if vida_jack >= 1 and 0 <= 10:
        jack_the_ripper.set_image(img("""
            ............fffffffffff............
                        ...........fffffffffffff...........
                        ..........fffffffffffffff..........
                        ..........fffff11111fffff..........
                        ..........ffffff111ffffff..........
                        ..........ff1f1ff1ff1f1ff..........
                        ..........fffffff1fffffff..........
                        ...........fddd1f1f1dddf...........
                        ...........fd11fd1df11df...........
                        ...........fd11ffdff11df...........
                        ...........ff1fffffff1ff...........
                        ...........fdff11111ffdf...........
                        ..........ffddd12221dddff..........
                        ........ffffddd22222dddffff........
                        ......fffffffdd12221ddfffffff......
                        .....ffffcffffd21112dffffcffff.....
                        ..fffffccffffff2dfd2ffffffccfffff..
                        .ffffccfffffffffffffffffffffccffff.
                        fffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffff
                        .fffffffffffffffffffffffffffffffff.
                        ..fffffffffffffffffffffffffffffff..
                        ..fffffffffffffffffffffffffffffff..
                        ..fffffffffffffffffffffffffffffff..
                        ..fffffffffffffffffffffffffffffff..
                        ..fffffffffffffffffffffffffffffff..
                        ..fffffffffffffffffffffffffffffff..
                        ..fffffffffffffffffffffffffffffff..
                        ..fffffffffffffffffffffffffffffff..
                        ..fffffffffffffffffffffffffffffff..
                        ..fffffffffffffffffffffffffffffff..
                        ..fffffffffffffffffffffffffffffff..
                        ..fffffffffffffffffffffffffffffff..
                        ..fffffffffffffffffffffffffffffff..
                        ..fffffffffffffffffffffffffffffff..
                        ..fffffffffffffffffffffffffffffff..
                        ..fffffffffffffffffffffffffffffff..
                        ..fffffffffffffffffffffffffffffff..
                        ..fffffffffffffffffffffffffffffff..
                        ..fffffffffffffffffffffffffffffff..
                        ..fffffffffffffffffffffffffffffff..
                        ..fffffffffffffffffffffffffffffff..
                        ..fffffffffffffffffffffffffffffff..
                        ..fffffffffffffffffffffffffffffff..
                        .fffffffffffffffffffffffffffffffff.
                        ff..fff...fff...fff...fff...fff..ff
        """))
    if vida_jack >= 11 and 0 <= 24:
        jack_the_ripper.set_image(img("""
            ..................fffffffffff....................
                        .................fffffffffffff...................
                        ................fffffffffffffff..................
                        ................fffff11111fffff..................
                        ................ffffff111ffffff..................
                        ................ff121ff1ff121ff..................
                        ................fffffff1fffffff..................
                        .................f1111f1f1111f...................
                        .................f111f111f111f...................
                        .................f111ff1ff111f...................
                        .................ff1fffffff1ff...................
                        .................f1ff21212ff1f...................
                        ................fff112222211fff..................
                        ..............ffffff1122211ffffff................
                        ............fffffffbf11111fbfffffff..............
                        ..........fffffccffbbfffffbbfffccffff............
                        ........fffffccfffffbeeeeebffffffccffff..........
                        .......ffffccffffffffbebebfffffffffccfff.........
                        .......ffccffffffffffffffffffffffffffccf.........
                        .......fffffffffffffffffffffffffffffffff.........
                        .......ffffffffffffffffffffffffffffffffff........
                        ......fffffffffffffffffffffffffffffffffff........
                        ......fffffffffffffffffffffffffffffffffff........
                        ......ffffffffffffffffffffffffffffffffffff.......
                        ......ffffffffffffffffffffffffffffffffffff.......
                        .....fffffffffffffffffffffffffffffffffffff.......
                        .....ffffffffffffffffffffffffffffffffffffff......
                        .....ffffffffffffffffffffffffffffffffffffff......
                        .....ffffffffffffffffffffffffffffffffffffff......
                        ....ffffffffffffffffffffffffffffffffffffffff.....
                        ....ffffffffffffffffffffffffffffffffffffffff.....
                        ....ffffffffffffffffffffffffffffffffffffffff.....
                        ....ffffffffffffffffffffffffffffffffffffffff.....
                        ....fffffffffffffffffffffffffffffffffffffffff....
                        ...ffffffffffffffffffffffffffffffffffffffffff....
                        ...ffffffffffffffffffffffffffffffffffffffffff....
                        ...fffffffffffffffffffffffffffffffffffffffffff...
                        ...fffffffffffffffffffffffffffffffffffffffffff...
                        ..ffffffffffffffffffffffffffffffffffffffffffff...
                        ..fffffffffffffffffffffffffffffffffffffffffffff..
                        ..fffffffffffffffffffffffffffffffffffffffffffff..
                        ..fffffffffffffffffffffffffffffffffffffffffffff..
                        .fffffffffffffffffffffffffffffffffffffffffffffff.
                        .fffffffffffffffffffffffffffffffffffffffffffffff.
                        .ffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffff.....
                        ......fffffffffffffffffffffffffffffffffff........
                        ...........fffffffffffffffffffffffff.............
        """))
    if Z_vida_reina_Z >= 1:
        reina2.set_image(img("""
            . . . 1 1 1 1 1 1 . . 
                        . . 1 1 1 1 1 1 1 . . 
                        . . 1 d d d d 1 1 1 . 
                        . . 1 f d f d d 1 1 . 
                        . . 1 d d d d d 1 1 . 
                        . . 1 f f f d d 1 1 . 
                        . . . d d d f d . . . 
                        . . . 3 3 3 3 3 . . . 
                        . d 3 3 b b 3 3 3 d . 
                        d d 3 b b 3 3 b b d d 
                        d d 3 2 2 3 3 b 3 d d 
                        d d 3 2 e 3 b b 3 d d 
                        d d 3 3 b b b 3 3 d d 
                        . . 3 3 3 3 3 3 3 . . 
                        . . . d d . . d d . . 
                        . . f f f . f f f . .
        """))
    if Z_vida_reina_Z >= 2:
        reina2.set_image(img("""
            . . . 1 1 1 1 1 1 . . 
                        . . 1 1 1 1 1 1 1 . . 
                        . . 1 d d d d 1 1 1 . 
                        . . 1 f d f d d 1 1 . 
                        . . 1 d d d d d 1 1 . 
                        . . 1 2 2 2 2 d 1 1 . 
                        . . . 2 1 1 1 d . . . 
                        . . . 3 3 3 3 3 . . . 
                        . d 3 3 b b 3 3 3 d . 
                        d d 3 b b 3 3 b b d d 
                        d d 3 2 2 3 3 b 3 d d 
                        d d 3 2 e 3 b b 3 d d 
                        d d 3 3 b b b 2 2 d d 
                        . . 3 3 3 3 3 2 e . . 
                        . . . d d . . d d . . 
                        . . f f f . f f f . .
        """))
    if Z_vida_reina_Z >= 3:
        reina2.set_image(img("""
            . . . 1 1 1 1 1 1 . . 
                        . . 1 1 1 1 1 1 1 . . 
                        . . 1 d d d d 1 1 1 . 
                        . . 1 f d f d d 1 1 . 
                        . . 1 9 d 9 d d 1 1 . 
                        . . 1 f f 9 d d 1 1 . 
                        . . . d d f d d . . . 
                        . . . 3 3 2 2 3 . . . 
                        . d 3 3 b 2 e 3 3 d . 
                        d d 3 b b 3 3 b b d d 
                        d d 3 2 2 3 3 b 3 d d 
                        d d 3 2 e 3 b b 3 d d 
                        d d 3 3 b b b 2 2 d d 
                        . . 3 3 3 3 3 2 e . . 
                        . . . d d . . d d . . 
                        . . f f f . f f f . .
        """))
    if Z_vida_reina_Z >= 4:
        reina2.set_image(img("""
            . . . 1 1 1 1 1 1 . . 
                        . . 1 1 1 1 1 1 1 . . 
                        . . 1 2 e 2 d 1 1 1 . 
                        . . 1 f 2 f d d 1 1 . 
                        . . 1 9 d 9 d d 1 1 . 
                        . . 1 2 2 2 d d 1 1 . 
                        . . . 2 1 1 d d . . . 
                        . . . 3 3 2 2 3 . . . 
                        . d 3 3 b 2 e 3 3 d . 
                        d d 3 b b 3 3 b b d d 
                        d d 3 2 2 3 3 b 3 d d 
                        d d 3 2 e 3 b b 3 d d 
                        d d 3 3 b b b 2 2 d d 
                        . . 3 3 3 3 3 2 e . . 
                        . . . d d . . d d . . 
                        . . f f f . f f f . .
        """))
    if vida_boss >= 1 or vida_boss <= 3:
        animation.run_image_animation(reina_boss2,
            [img("""
                    ...........111111111.............
                                ...........11111111111...........
                                ...........11111111111...........
                                ..........1111111111111..........
                                .........11177777777711..........
                                .........111717777717111.........
                                .........111771777177111.........
                                .........711719171917117.........
                                .........771719171917177.........
                                .777.....177777777777771.....777.
                                76677....11177fffff77111....77667
                                776677...111776777677111...776677
                                776767....11177777771111...767677
                                .7676777..111b333333111..7776767.
                                .76776677...3b3333333...77667767.
                                .77776767777b3333333b77776767777.
                                ..77767766773333333337766776777..
                                ..7776776766333bb33336676776777..
                                ...77677677633bb33bb3677677677...
                                ...777776777333333b33777677777...
                                ...77777677733333bb33777677777...
                                ....77777777333bbb33377777777....
                                ......7.7.7.333333333.7.7.7......
                                ............b33333b33............
                                ............3bb3bb333............
                                ............33bb33333............
                                ............7777.7777............
                                ............f777.777f............
                                ............fff7.7fff............
                                ............ffff.ffff............
                                ............ffff.ffff............
                                ............ffff.ffff............
                                ............f..f.f..f............
                """),
                img("""
                    ............111111111............
                                ...........11111111111...........
                                ...........11111111111...........
                                ..........1111111111111..........
                                ..........1177777777711..........
                                .........111717777717111.........
                                .........111771777177111.........
                                .........711719171917117.........
                                .........771719171917177.........
                                .........177777777777771.........
                                .........11177fffff77111.........
                                .........111776777677111.........
                                77777....111177777771111....77777
                                766777....111b333333111....777667
                                77666777....3b3333333....77766677
                                .7676667777.b3333333b.7777666767.
                                .7677676667733333333377666767767.
                                .76776776767333bb333376767767767.
                                .7777677677633bb33bb367767767777.
                                ..7776776776333333b336776776777..
                                ..777777677733333bb337776777777..
                                ...777777777333bbb333777777777...
                                ....7777777733333333377777777....
                                ......7.7.7.b33333b33.7.7.7......
                                ............3bb3bb333............
                                ............33bb33333............
                                ............7777.7777............
                                ............f777.777f............
                                ............fff7.7fff............
                                ............ffff.ffff............
                                ............ffff.ffff............
                                ............ffff.ffff............
                                ............f..f.f..f............
                """),
                img("""
                    .............111111111...........
                                ...........11111111111...........
                                ...........11111111111...........
                                ..........1111111111111..........
                                ..........11777777777111.........
                                .........111717777717111.........
                                .........111771777177111.........
                                .........711719171917117.........
                                .........771719171917177.........
                                .........177777777777771.........
                                .........11177fffff77111.........
                                .........111776777677111.........
                                .........11117777777111..........
                                ..........111b333333111..........
                                ............3b3333333............
                                777.........b3333333b.........777
                                766777777777333333333777777777667
                                776666666777333bb3333777666666677
                                77677677666633bb33bb3666677677677
                                776776776776333333b33677677677677
                                .7777677677733333bb3377767767777.
                                ..7776776777333bbb3337776776777..
                                ....7777777733333333377777777....
                                .....7777777b33333b337777777.....
                                ......7.7.7.3bb3bb333.7.7.7......
                                ............33bb33333............
                                ............7777.7777............
                                ............f777.777f............
                                ............fff7.7fff............
                                ............ffff.ffff............
                                ............ffff.ffff............
                                ............ffff.ffff............
                                ............f..f.f..f............
                """),
                img("""
                    ............111111111............
                                ...........11111111111...........
                                ...........11111111111...........
                                ..........1111111111111..........
                                ..........1177777777711..........
                                .........111717777717111.........
                                .........111771777177111.........
                                .........711719171917117.........
                                .........771719171917177.........
                                .........177777777777771.........
                                .........11177fffff77111.........
                                .........111776777677111.........
                                77777....111177777771111....77777
                                766777....111b333333111....777667
                                77666777....3b3333333....77766677
                                .7676667777.b3333333b.7777666767.
                                .7677676667733333333377666767767.
                                .76776776767333bb333376767767767.
                                .7777677677633bb33bb367767767777.
                                ..7776776776333333b336776776777..
                                ..777777677733333bb337776777777..
                                ...777777777333bbb333777777777...
                                ....7777777733333333377777777....
                                ......7.7.7.b33333b33.7.7.7......
                                ............3bb3bb333............
                                ............33bb33333............
                                ............7777.7777............
                                ............f777.777f............
                                ............fff7.7fff............
                                ............ffff.ffff............
                                ............ffff.ffff............
                                ............ffff.ffff............
                                ............f..f.f..f............
                """)],
            120,
            True)
    if vida_boss >= 4 or vida_boss <= 6:
        animation.run_image_animation(reina_boss2,
            [img("""
                    ...................11......11.1...................
                                ................11.1111.1111111...................
                                ................111111111111111.................77
                                7...............111111111111111................777
                                77..............111111111111111...............7777
                                67..............111111111111111...............7767
                                677..............1177777777711...............77667
                                7667.............1177777777711.............7777677
                                7667.............1171117111711............7777667.
                                76667...........711169171691117...........7776677.
                                .66767..........771186171861177..........77766677.
                                .76767...........7777777777777...........77766677.
                                .7676777..........177fffff771..........7777666667.
                                .76776667..........7fffffff7..........77776677667.
                                .667766767777..777..7777777..777..777777766777667.
                                .6677667677777777773b333333b777777777776666777667.
                                .6676677766667766667b33333b7666677776666666777667.
                                .7776677776666666776333333b6777666666777766777667.
                                ..77667777667776677733333337777667776777766777767.
                                ..77667777667776677733bb3337777667776777766777777.
                                ...767777766777667.33bb33bb377766777677776677.777.
                                ...777.777667.7667.333333b33..766777667776677..7..
                                ...77...77677..67..33333bb33..766777667776677.....
                                ...77....767...7..7333bbb3333.7767.7667.77677.....
                                .........777.....73b33333333b..777.7677.77677.....
                                .........77.....773bb333333b37..7..777...7777.....
                                ..........7.....7673bb33333b777.....7.....77......
                                ...............7677773333377777...................
                                ...............6777773333376776...................
                                ..............767777673333767776..................
                                ..............77777767..3.7677767.................
                                ..............7767767.....7767767.................
                                .............7766677......7777777.................
                                .............7766677......77776667................
                                .............7776677......77776667................
                                .............777777........77776777...............
                                .............767777........77677777...............
                                ............7767767........76777767...............
                                ............7677776........76777767...............
                                ............7777776.........6777776...............
                                ............6777777.........7777777...............
                                ............6777776.........7777776...............
                                ..............676.6.........6777776...............
                                ..............6.6...........6.676.................
                                ..............................6.6.................
                """),
                img("""
                    ....................1.....1..1....................
                                .................11.11.1.11111....................
                                ................111111111111111.................77
                                7...............111111111111111................777
                                77..............111111111111111...............7777
                                67..............11111111111111................7767
                                677.............11177777777711...............77667
                                7667.............1177777777711.............7777677
                                7667.............1171117111711............7777667.
                                76667...........711169171691117...........7776677.
                                .66767..........771186171861177..........77766677.
                                .76767...........7777777777777...........77766677.
                                .7676777..........177fffff771..........7777666667.
                                .76776667..........7fffffff7..........77776677667.
                                .667766767777..777..7777777..777..777777766777667.
                                .6677667677777777773b333333b777777777776666777667.
                                .6676677766667766667b33333b7666677776666666777667.
                                .7776677776666666776333333b6777666666777766777667.
                                ..77667777667776677733333337777667776777766777767.
                                ..77667777667776677733bb3337777667776777766777777.
                                ...767777766777667.33bb33bb377766777677776677.777.
                                ...777.777667.7667.333333b33..766777667776677..7..
                                ...77...77677..67..33333bb33..766777667776677.....
                                ...77....767...7..7333bbb3333.7767.7667.77677.....
                                .........777.....73b33333333b..777.7677.77677.....
                                .........77.....773bb333333b37..7..777...7777.....
                                ..........7.....7673bb33333b777.....7.....77......
                                ...............7677773333377777...................
                                ...............6777773333376776...................
                                ..............767777673333767776..................
                                ..............77777767..3.7677767.................
                                ..............7767767.....7767767.................
                                .............7766677......7777777.................
                                .............7766677......77776667................
                                .............7776677......77776667................
                                .............777777........77776777...............
                                .............767777........77677777...............
                                ............7767767........76777767...............
                                ............7677776........76777767...............
                                ............7777776.........6777776...............
                                ............6777777.........7777777...............
                                ............6777776.........7777776...............
                                ..............676.6.........6777776...............
                                ..............6.6...........6.676.................
                                ..............................6.6.................
                """),
                img("""
                    ................1..1.11.1..1..1...................
                                ................1111.11.1.11.11...................
                                .................1111111111111..................77
                                7................11111111111111................777
                                77..............111111111111111...............7777
                                67..............11111111111111................7767
                                677.............11177777777711...............77667
                                7667............111777777777111............7777677
                                7667.............11711171117111...........7777667.
                                76667...........711169171691117...........7776677.
                                .66767..........771186171861177..........77766677.
                                .76767...........7777777777777...........77766677.
                                .7676777..........177fffff771..........7777666667.
                                .76776667..........7fffffff7..........77776677667.
                                .667766767777..777..7777777..777..777777766777667.
                                .6677667677777777773b333333b777777777776666777667.
                                .6676677766667766667b33333b7666677776666666777667.
                                .7776677776666666776333333b6777666666777766777667.
                                ..77667777667776677733333337777667776777766777767.
                                ..77667777667776677733bb3337777667776777766777777.
                                ...767777766777667.33bb33bb377766777677776677.777.
                                ...777.777667.7667.333333b33..766777667776677..7..
                                ...77...77677..67..33333bb33..766777667776677.....
                                ...77....767...7..7333bbb3333.7767.7667.77677.....
                                .........777.....73b33333333b..777.7677.77677.....
                                .........77.....773bb333333b37..7..777...7777.....
                                ..........7.....7673bb33333b777.....7.....77......
                                ...............7677773333377777...................
                                ...............6777773333376776...................
                                ..............767777673333767776..................
                                ..............77777767..3.7677767.................
                                ..............7767767.....7767767.................
                                .............7766677......7777777.................
                                .............7766677......77776667................
                                .............7776677......77776667................
                                .............777777........77776777...............
                                .............767777........77677777...............
                                ............7767767........76777767...............
                                ............7677776........76777767...............
                                ............7777776.........6777776...............
                                ............6777777.........7777777...............
                                ............6777776.........7777776...............
                                ..............676.6.........6777776...............
                                ..............6.6...........6.676.................
                                ..............................6.6.................
                """)],
            120,
            True)
    if vida_boss >= 7 or vida_boss <= 9:
        animation.run_image_animation(reina_boss2,
            [img("""
                    ..........................1.........1............................
                                .........................11.........11...........................
                                .........................11.........11...........................
                                ........................111.........111..........................
                                77......................111.........111.......................777
                                777.....................111.........111......................7776
                                767.....................111.........111.....................77766
                                7667....................11111.....11111....................777667
                                76767...................111111111111111...................7766677
                                .67767..................111111111111111..................77677677
                                .677677.................111111111111111.................777767677
                                .7677677................111111111111111................777776767.
                                .76777677...............111111111111111...............7777776667.
                                .76777767................1111111111111...............7777666677..
                                .7667777677..............1111186911111..............77766777677..
                                ..7766676777.............111116f611111.............777776777677..
                                ..77777666777...........711111869111117..........77777776666677..
                                ..777767776677..........771111111111177.........77766666677777...
                                ..7777677767777..........7777777777777.........777677777767777...
                                ..77767777677777..........17711111771........77777767777767777...
                                ...76777766667777..........722222227.......777777776666776777....
                                ...7766666777677777........711111117.....77777777766777666777....
                                ....77777677767777777777...677777776.....7777777776767777777.....
                                ....7777767776777777777677776666666777.677777777767767777777.....
                                ....7777767776777777666777666667666667776777777776776777777......
                                .....777677776777666777667777776777776667666777776777677777......
                                .....77767766666676777777666666766666777776766666777767777.......
                                ......776667776776777777777777767777777777767777666676777........
                                .......7777777677677777777776676766777777777677677776677.........
                                ........777777676777777777777776777777777777677677777777.........
                                ........777777663bb33337777777767777777777bb36767777777..........
                                .........7777776b333333333b3377677777733333b336777777............
                                ..........7777763333333333b3333333333333333b336777777............
                                ...........7777633333b333bb333333333333333bb33677777.............
                                ............77763bbbb333bb33bb3333333b3333333367777..............
                                .............7763bbb3333333b33333333b33333333367.................
                                ................33333333333b33333333b3333333b3...................
                                ..................33333333b377677333bb333333b....................
                                ........................7677776777773b333........................
                                ......................117767776777767711.........................
                                ....................1111767666666667711111.......................
                                .................1111111767777677776711111111....................
                                ...............11111111117677767776771111111111..................
                                .................1111111177666666677711111111....................
                                ....................11111333bb33333b311111.......................
                                ......................1333333333333bb311.........................
                                .....................33333b33333333bb33..........................
                                .....................3333bb3333b333b3333.........................
                                .....................33bbb33333b33333333.........................
                                .....................33bbb33333bb333b333.........................
                                .....................3bb3333333bb33bbbb3.........................
                                .....................3b333333333b33333337........................
                                ....................63b333333333b33333367........................
                                ....................67b333333333333377767........................
                                ....................677767.......776777677.......................
                                ...................7767767........77667677.......................
                                ...................776767.........77776677.......................
                                ...................776767..........7777667.......................
                                ...................776767..........7777676.......................
                                ...................777677..........7776767.......................
                                ...................777677..........7776767.......................
                                ...................776677...........776676.......................
                                ...................77676ff..........ff6767.......................
                                ....................6776ff..........fff6ff.......................
                                ....................ff7ffff.........fffff........................
                                ....................fffffff........ffffff........................
                                ....................fffffff........ffffff........................
                                ....................fffffff........fffff.........................
                                .....................ffffff........fffff.........................
                                ......................fffff........ffff..........................
                """),
                img("""
                    ..........................1.........1............................
                                .........................11.........11...........................
                                .........................11.........11...........................
                                ........................111.........111..........................
                                77......................111.........111.......................777
                                777.....................111.........111......................7776
                                767.....................111.........111.....................77766
                                7667....................11111.....11111....................777667
                                76767...................111111111111111...................7766677
                                .67767..................111111111111111..................77677677
                                .677677.................111111111111111.................777767677
                                .7677677................111111111111111................777776767.
                                .76777677...............111111111111111...............7777776667.
                                .76777767................1111111111111...............7777666677..
                                .7667777677..............1111169611111..............77766777677..
                                ..7766676777.............111118f911111.............777776777677..
                                ..77777666777...........711111686111117..........77777776666677..
                                ..777767776677..........771111111111177.........77766666677777...
                                ..7777677767777..........7777777777777.........777677777767777...
                                ..77767777677777..........17711111771........77777767777767777...
                                ...76777766667777..........722222227.......777777776666776777....
                                ...7766666777677777........711111117.....77777777766777666777....
                                ....77777677767777777777...677777776.....7777777776767777777.....
                                ....7777767776777777777677776666666777.677777777767767777777.....
                                ....7777767776777777666777666667666667776777777776776777777......
                                .....777677776777666777667777776777776667666777776777677777......
                                .....77767766666676777777666666766666777776766666777767777.......
                                ......776667776776777777777777767777777777767777666676777........
                                .......7777777677677777777776676766777777777677677776677.........
                                ........777777676777777777777776777777777777677677777777.........
                                ........777777663bb33337777777767777777777bb36767777777..........
                                .........7777776b333333333b3377677777733333b336777777............
                                ..........7777763333333333b3333333333333333b336777777............
                                ...........7777633333b333bb333333333333333bb33677777.............
                                ............77763bbbb333bb33bb3333333b3333333367777..............
                                .............7763bbb3333333b33333333b33333333367.................
                                ................33333333333b33333333b3333333b3...................
                                ..................33333333b377677333bb333333b....................
                                ........................7677776777773b333........................
                                ......................117767776777767711.........................
                                ....................1111767666666667711111.......................
                                .................1111111767777677776711111111....................
                                ...............11111111117677767776771111111111..................
                                .................1111111177666666677711111111....................
                                ....................11111333bb33333b311111.......................
                                ......................1333333333333bb311.........................
                                .....................33333b33333333bb33..........................
                                .....................3333bb3333b333b3333.........................
                                .....................33bbb33333b33333333.........................
                                .....................33bbb33333bb333b333.........................
                                .....................3bb3333333bb33bbbb3.........................
                                .....................3b333333333b33333337........................
                                ....................63b333333333b33333367........................
                                ....................67b333333333333377767........................
                                ....................677767.......776777677.......................
                                ...................7767767........77667677.......................
                                ...................776767.........77776677.......................
                                ...................776767..........7777667.......................
                                ...................776767..........7777676.......................
                                ...................777677..........7776767.......................
                                ...................777677..........7776767.......................
                                ...................776677...........776676.......................
                                ...................77676ff..........ff6767.......................
                                ....................6776ff..........fff6ff.......................
                                ....................ff7ffff.........fffff........................
                                ....................fffffff........ffffff........................
                                ....................fffffff........ffffff........................
                                ....................fffffff........fffff.........................
                                .....................ffffff........fffff.........................
                                ......................fffff........ffff..........................
                """),
                img("""
                    ..........................1.........1............................
                                .........................11.........11...........................
                                .........................11.........11...........................
                                ........................111.........111..........................
                                77......................111.........111.......................777
                                777.....................111.........111......................7776
                                767.....................111.........111.....................77766
                                7667....................11111.....11111....................777667
                                76767...................111111111111111...................7766677
                                .67767..................111111111111111..................77677677
                                .677677.................111111111111111.................777767677
                                .7677677................111111111111111................777776767.
                                .76777677...............111111111111111...............7777776667.
                                .76777767................1111111111111...............7777666677..
                                .7667777677..............1111186911111..............77766777677..
                                ..7766676777.............111116f611111.............777776777677..
                                ..77777666777...........711111869111117..........77777776666677..
                                ..777767776677..........771111111111177.........77766666677777...
                                ..7777677767777..........7777777777777.........777677777767777...
                                ..77767777677777..........17711111771........77777767777767777...
                                ...76777766667777..........722222227.......777777776666776777....
                                ...7766666777677777........711111117.....77777777766777666777....
                                ....77777677767777777777...677777776.....7777777776767777777.....
                                ....7777767776777777777677776666666777.677777777767767777777.....
                                ....7777767776777777666777666667666667776777777776776777777......
                                .....777677776777666777667777776777776667666777776777677777......
                                .....77767766666676777777666666766666777776766666777767777.......
                                ......776667776776777777777777767777777777767777666676777........
                                .......7777777677677777777776676766777777777677677776677.........
                                ........777777676777777777777776777777777777677677777777.........
                                ........777777663bb33337777777767777777777bb36767777777..........
                                .........7777776b333333333b3377677777733333b336777777............
                                ..........7777763333333333b3333333333333333b336777777............
                                ...........7777633333b333bb333333333333333bb33677777.............
                                ............77763bbbb333bb33bb3333333b3333333367777..............
                                .............7763bbb3333333b33333333b33333333367.................
                                ................33333333333b33333333b3333333b3...................
                                ..................33333333b377677333bb333333b....................
                                ........................7677776777773b333........................
                                ......................117767776777767711.........................
                                ....................1111767666666667711111.......................
                                .................1111111767777677776711111111....................
                                ...............11111111117677767776771111111111..................
                                .................1111111177666666677711111111....................
                                ....................11111333bb33333b311111.......................
                                ......................1333333333333bb311.........................
                                .....................33333b33333333bb33..........................
                                .....................3333bb3333b333b3333.........................
                                .....................33bbb33333b33333333.........................
                                .....................33bbb33333bb333b333.........................
                                .....................3bb3333333bb33bbbb3.........................
                                .....................3b333333333b33333337........................
                                ....................63b333333333b33333367........................
                                ....................67b333333333333377767........................
                                ....................677767.......776777677.......................
                                ...................7767767........77667677.......................
                                ...................776767.........77776677.......................
                                ...................776767..........7777667.......................
                                ...................776767..........7777676.......................
                                ...................777677..........7776767.......................
                                ...................777677..........7776767.......................
                                ...................776677...........776676.......................
                                ...................77676ff..........ff6767.......................
                                ....................6776ff..........fff6ff.......................
                                ....................ff7ffff.........fffff........................
                                ....................fffffff........ffffff........................
                                ....................fffffff........ffffff........................
                                ....................fffffff........fffff.........................
                                .....................ffffff........fffff.........................
                                ......................fffff........ffff..........................
                """),
                img("""
                    ..........................1.........1............................
                                .........................11.........11...........................
                                .........................11.........11...........................
                                ........................111.........111..........................
                                77......................111.........111.......................777
                                777.....................111.........111......................7776
                                767.....................111.........111.....................77766
                                7667....................11111.....11111....................777667
                                76767...................111111111111111...................7766677
                                .67767..................111111111111111..................77677677
                                .677677.................111111111111111.................777767677
                                .7677677................111111111111111................777776767.
                                .76777677...............111111111111111...............7777776667.
                                .76777767................1111111111111...............7777666677..
                                .7667777677..............1111169611111..............77766777677..
                                ..7766676777.............111118f911111.............777776777677..
                                ..77777666777...........711111686111117..........77777776666677..
                                ..777767776677..........771111111111177.........77766666677777...
                                ..7777677767777..........7777777777777.........777677777767777...
                                ..77767777677777..........17711111771........77777767777767777...
                                ...76777766667777..........722222227.......777777776666776777....
                                ...7766666777677777........711111117.....77777777766777666777....
                                ....77777677767777777777...677777776.....7777777776767777777.....
                                ....7777767776777777777677776666666777.677777777767767777777.....
                                ....7777767776777777666777666667666667776777777776776777777......
                                .....777677776777666777667777776777776667666777776777677777......
                                .....77767766666676777777666666766666777776766666777767777.......
                                ......776667776776777777777777767777777777767777666676777........
                                .......7777777677677777777776676766777777777677677776677.........
                                ........777777676777777777777776777777777777677677777777.........
                                ........777777663bb33337777777767777777777bb36767777777..........
                                .........7777776b333333333b3377677777733333b336777777............
                                ..........7777763333333333b3333333333333333b336777777............
                                ...........7777633333b333bb333333333333333bb33677777.............
                                ............77763bbbb333bb33bb3333333b3333333367777..............
                                .............7763bbb3333333b33333333b33333333367.................
                                ................33333333333b33333333b3333333b3...................
                                ..................33333333b377677333bb333333b....................
                                ........................7677776777773b333........................
                                ......................117767776777767711.........................
                                ....................1111767666666667711111.......................
                                .................1111111767777677776711111111....................
                                ...............11111111117677767776771111111111..................
                                .................1111111177666666677711111111....................
                                ....................11111333bb33333b311111.......................
                                ......................1333333333333bb311.........................
                                .....................33333b33333333bb33..........................
                                .....................3333bb3333b333b3333.........................
                                .....................33bbb33333b33333333.........................
                                .....................33bbb33333bb333b333.........................
                                .....................3bb3333333bb33bbbb3.........................
                                .....................3b333333333b33333337........................
                                ....................63b333333333b33333367........................
                                ....................67b333333333333377767........................
                                ....................677767.......776777677.......................
                                ...................7767767........77667677.......................
                                ...................776767.........77776677.......................
                                ...................776767..........7777667.......................
                                ...................776767..........7777676.......................
                                ...................777677..........7776767.......................
                                ...................777677..........7776767.......................
                                ...................776677...........776676.......................
                                ...................77676ff..........ff6767.......................
                                ....................6776ff..........fff6ff.......................
                                ....................ff7ffff.........fffff........................
                                ....................fffffff........ffffff........................
                                ....................fffffff........ffffff........................
                                ....................fffffff........fffff.........................
                                .....................ffffff........fffff.........................
                                ......................fffff........ffff..........................
                """),
                img("""
                    ..........................1.........1............................
                                .........................11.........11...........................
                                .........................11.........11...........................
                                ........................111.........111..........................
                                77......................111.........111.......................777
                                777.....................111.........111......................7776
                                767.....................111.........111.....................77766
                                7667....................11111.....11111....................777667
                                76767...................111111111111111...................7766677
                                .67767..................111111111111111..................77677677
                                .677677.................111111111111111.................777767677
                                .7677677................111111111111111................777776767.
                                .76777677...............111111111111111...............7777776667.
                                .76777767................1111869691111...............7777666677..
                                .7667777677..............1111686961111..............77766777677..
                                ..7766676777.............111186f691111.............777776777677..
                                ..77777666777...........711116869611117..........77777776666677..
                                ..777767776677..........771111111111177.........77766666677777...
                                ..7777677767777..........7777777777777.........777677777767777...
                                ..77767777677777..........17711111771........77777767777767777...
                                ...76777766667777..........722222227.......777777776666776777....
                                ...7766666777677777........711111117.....77777777766777666777....
                                ....77777677767777777777...677777776.....7777777776767777777.....
                                ....7777767776777777777677776666666777.677777777767767777777.....
                                ....7777767776777777666777666667666667776777777776776777777......
                                .....777677776777666777667777776777776667666777776777677777......
                                .....77767766666676777777666666766666777776766666777767777.......
                                ......776667776776777777777777767777777777767777666676777........
                                .......7777777677677777777776676766777777777677677776677.........
                                ........777777676777777777777776777777777777677677777777.........
                                ........777777663bb33337777777767777777777bb36767777777..........
                                .........7777776b333333333b3377677777733333b336777777............
                                ..........7777763333333333b3333333333333333b336777777............
                                ...........7777633333b333bb333333333333333bb33677777.............
                                ............77763bbbb333bb33bb3333333b3333333367777..............
                                .............7763bbb3333333b33333333b33333333367.................
                                ................33333333333b33333333b3333333b3...................
                                ..................33333333b377677333bb333333b....................
                                ........................7677776777773b333........................
                                ......................117767776777767711.........................
                                ....................1111767666666667711111.......................
                                .................1111111767777677776711111111....................
                                ...............11111111117677767776771111111111..................
                                .................1111111177666666677711111111....................
                                ....................11111333bb33333b311111.......................
                                ......................1333333333333bb311.........................
                                .....................33333b33333333bb33..........................
                                .....................3333bb3333b333b3333.........................
                                .....................33bbb33333b33333333.........................
                                .....................33bbb33333bb333b333.........................
                                .....................3bb3333333bb33bbbb3.........................
                                .....................3b333333333b33333337........................
                                ....................63b333333333b33333367........................
                                ....................67b333333333333377767........................
                                ....................677767.......776777677.......................
                                ...................7767767........77667677.......................
                                ...................776767.........77776677.......................
                                ...................776767..........7777667.......................
                                ...................776767..........7777676.......................
                                ...................777677..........7776767.......................
                                ...................777677..........7776767.......................
                                ...................776677...........776676.......................
                                ...................77676ff..........ff6767.......................
                                ....................6776ff..........fff6ff.......................
                                ....................ff7ffff.........fffff........................
                                ....................fffffff........ffffff........................
                                ....................fffffff........ffffff........................
                                ....................fffffff........fffff.........................
                                .....................ffffff........fffff.........................
                                ......................fffff........ffff..........................
                """),
                img("""
                    ..........................1.........1............................
                                .........................11.........11...........................
                                .........................11.........11...........................
                                ........................111.........111..........................
                                77......................111.........111.......................777
                                777.....................111.........111......................7776
                                767.....................111.........111.....................77766
                                7667....................11111.....11111....................777667
                                76767...................111111111111111...................7766677
                                .67767..................111111111111111..................77677677
                                .677677.................111111111111111.................777767677
                                .7677677................111111111111111................777776767.
                                .76777677...............111111111111111...............7777776667.
                                .76777767................1111686961111...............7777666677..
                                .7667777677..............1111868691111..............77766777677..
                                ..7766676777.............111168f961111.............777776777677..
                                ..77777666777...........711118686911117..........77777776666677..
                                ..777767776677..........771111111111177.........77766666677777...
                                ..7777677767777..........7777777777777.........777677777767777...
                                ..77767777677777..........17711111771........77777767777767777...
                                ...76777766667777..........722222227.......777777776666776777....
                                ...7766666777677777........711111117.....77777777766777666777....
                                ....77777677767777777777...677777776.....7777777776767777777.....
                                ....7777767776777777777677776666666777.677777777767767777777.....
                                ....7777767776777777666777666667666667776777777776776777777......
                                .....777677776777666777667777776777776667666777776777677777......
                                .....77767766666676777777666666766666777776766666777767777.......
                                ......776667776776777777777777767777777777767777666676777........
                                .......7777777677677777777776676766777777777677677776677.........
                                ........777777676777777777777776777777777777677677777777.........
                                ........777777663bb33337777777767777777777bb36767777777..........
                                .........7777776b333333333b3377677777733333b336777777............
                                ..........7777763333333333b3333333333333333b336777777............
                                ...........7777633333b333bb333333333333333bb33677777.............
                                ............77763bbbb333bb33bb3333333b3333333367777..............
                                .............7763bbb3333333b33333333b33333333367.................
                                ................33333333333b33333333b3333333b3...................
                                ..................33333333b377677333bb333333b....................
                                ........................7677776777773b333........................
                                ......................117767776777767711.........................
                                ....................1111767666666667711111.......................
                                .................1111111767777677776711111111....................
                                ...............11111111117677767776771111111111..................
                                .................1111111177666666677711111111....................
                                ....................11111333bb33333b311111.......................
                                ......................1333333333333bb311.........................
                                .....................33333b33333333bb33..........................
                                .....................3333bb3333b333b3333.........................
                                .....................33bbb33333b33333333.........................
                                .....................33bbb33333bb333b333.........................
                                .....................3bb3333333bb33bbbb3.........................
                                .....................3b333333333b33333337........................
                                ....................63b333333333b33333367........................
                                ....................67b333333333333377767........................
                                ....................677767.......776777677.......................
                                ...................7767767........77667677.......................
                                ...................776767.........77776677.......................
                                ...................776767..........7777667.......................
                                ...................776767..........7777676.......................
                                ...................777677..........7776767.......................
                                ...................777677..........7776767.......................
                                ...................776677...........776676.......................
                                ...................77676ff..........ff6767.......................
                                ....................6776ff..........fff6ff.......................
                                ....................ff7ffff.........fffff........................
                                ....................fffffff........ffffff........................
                                ....................fffffff........ffffff........................
                                ....................fffffff........fffff.........................
                                .....................ffffff........fffff.........................
                                ......................fffff........ffff..........................
                """)],
            150,
            True)
forever(on_forever2)

def on_forever3():
    global cuchillo14, cuchillo2, cuchillo3, cuchillo4, cuchillo5, cuchillo6, cuchillo7, cuchillo8, cuchillo9, cuchillo10, cuchillo11, cuchillo12, cuchillo13
    if vida_jack == 2:
        jack_the_ripper.start_effect(effects.disintegrate, 1)
        jack_the_ripper.set_position(215, -10)
        jack_the_ripper.set_velocity(0, 120)
        pause(350)
        cuchillo14 = sprites.create(img("""
                . . . . . . . . f . . . 
                            1 1 1 1 1 1 1 1 f e e e 
                            1 1 1 1 1 1 1 1 f e e e 
                            . . . . . . . . f . . .
            """),
            SpriteKind.cuchillo)
        cuchillo14.set_position(239, 65)
        cuchillo14.follow(J1, 110)
        pause(900)
        cuchillo14.destroy(effects.spray, 1)
        pause(900)
    if vida_jack >= 3 and vida_jack <= 8:
        jack_the_ripper.start_effect(effects.disintegrate, 1)
        jack_the_ripper.set_position(120, 104)
        cuchillo14 = sprites.create(img("""
                . . . . . . . . f . . . 
                            1 1 1 1 1 1 1 1 f e e e 
                            1 1 1 1 1 1 1 1 f e e e 
                            . . . . . . . . f . . .
            """),
            SpriteKind.cuchillo)
        cuchillo14.follow(J1, 110)
        cuchillo14.set_position(229, 65)
        cuchillo2 = sprites.create(img("""
                . . . f . . . . . . . . 
                            e e e f 1 1 1 1 1 1 1 1 
                            e e e f 1 1 1 1 1 1 1 1 
                            . . . f . . . . . . . .
            """),
            SpriteKind.cuchillo)
        cuchillo2.set_position(27, 65)
        cuchillo2.follow(J1, 110)
        pause(800)
        cuchillo14.destroy(effects.spray, 1)
        cuchillo2.destroy(effects.spray, 1)
        pause(1100)
    if vida_jack >= 9 and vida_jack <= 10:
        jack_the_ripper.start_effect(effects.disintegrate, 1)
        jack_the_ripper.set_position(120, 104)
        cuchillo14 = sprites.create(img("""
                . . . . . . . . f . . . 
                            1 1 1 1 1 1 1 1 f e e e 
                            1 1 1 1 1 1 1 1 f e e e 
                            . . . . . . . . f . . .
            """),
            SpriteKind.cuchillo)
        cuchillo14.follow(J1, 110)
        cuchillo14.set_position(229, 35)
        cuchillo2 = sprites.create(img("""
                . . . f . . . . . . . . 
                            e e e f 1 1 1 1 1 1 1 1 
                            e e e f 1 1 1 1 1 1 1 1 
                            . . . f . . . . . . . .
            """),
            SpriteKind.cuchillo)
        cuchillo2.set_position(27, 35)
        cuchillo2.follow(J1, 110)
        cuchillo3 = sprites.create(img("""
                . . . f . . . . . . . . 
                            e e e f 1 1 1 1 1 1 1 1 
                            e e e f 1 1 1 1 1 1 1 1 
                            . . . f . . . . . . . .
            """),
            SpriteKind.cuchillo)
        cuchillo3.set_position(27, 80)
        cuchillo3.follow(J1, 110)
        cuchillo4 = sprites.create(img("""
                . . . . . . . . f . . . 
                            1 1 1 1 1 1 1 1 f e e e 
                            1 1 1 1 1 1 1 1 f e e e 
                            . . . . . . . . f . . .
            """),
            SpriteKind.cuchillo)
        cuchillo4.follow(J1, 110)
        cuchillo4.set_position(229, 80)
        pause(750)
        cuchillo14.destroy(effects.spray, 1)
        cuchillo2.destroy(effects.spray, 1)
        cuchillo3.destroy(effects.spray, 1)
        cuchillo4.destroy(effects.spray, 1)
        pause(1650)
    if vida_jack >= 11 and vida_jack <= 18:
        tiles.set_tilemap(tilemap("""
            level_28
        """))
        cuchillo14 = sprites.create(img("""
                . e e . 
                            . e e . 
                            . e e . 
                            f f f f 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 .
            """),
            SpriteKind.cuchillo_lluvia)
        cuchillo14.set_position(0, 5)
        cuchillo14.set_velocity(0, 100)
        pause(50)
        cuchillo2 = sprites.create(img("""
                . e e . 
                            . e e . 
                            . e e . 
                            f f f f 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 .
            """),
            SpriteKind.cuchillo_lluvia)
        cuchillo2.set_position(21, 5)
        cuchillo2.set_velocity(0, 100)
        pause(50)
        cuchillo3 = sprites.create(img("""
                . e e . 
                            . e e . 
                            . e e . 
                            f f f f 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 .
            """),
            SpriteKind.cuchillo_lluvia)
        cuchillo3.set_position(42, 5)
        cuchillo3.set_velocity(0, 100)
        pause(50)
        cuchillo4 = sprites.create(img("""
                . e e . 
                            . e e . 
                            . e e . 
                            f f f f 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 .
            """),
            SpriteKind.cuchillo_lluvia)
        cuchillo4.set_position(63, 5)
        cuchillo4.set_velocity(0, 100)
        pause(50)
        cuchillo5 = sprites.create(img("""
                . e e . 
                            . e e . 
                            . e e . 
                            f f f f 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 .
            """),
            SpriteKind.cuchillo_lluvia)
        cuchillo5.set_position(84, 5)
        cuchillo5.set_velocity(0, 100)
        pause(50)
        cuchillo6 = sprites.create(img("""
                . e e . 
                            . e e . 
                            . e e . 
                            f f f f 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 .
            """),
            SpriteKind.cuchillo_lluvia)
        cuchillo6.set_position(105, 5)
        cuchillo6.set_velocity(0, 100)
        pause(50)
        cuchillo7 = sprites.create(img("""
                . e e . 
                            . e e . 
                            . e e . 
                            f f f f 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 .
            """),
            SpriteKind.cuchillo_lluvia)
        cuchillo7.set_position(126, 5)
        cuchillo7.set_velocity(0, 100)
        pause(50)
        cuchillo8 = sprites.create(img("""
                . e e . 
                            . e e . 
                            . e e . 
                            f f f f 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 .
            """),
            SpriteKind.cuchillo_lluvia)
        cuchillo8.set_position(147, 5)
        cuchillo8.set_velocity(0, 100)
        pause(50)
        cuchillo9 = sprites.create(img("""
                . e e . 
                            . e e . 
                            . e e . 
                            f f f f 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 .
            """),
            SpriteKind.cuchillo_lluvia)
        cuchillo9.set_position(168, 5)
        cuchillo9.set_velocity(0, 100)
        pause(50)
        cuchillo10 = sprites.create(img("""
                . e e . 
                            . e e . 
                            . e e . 
                            f f f f 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 .
            """),
            SpriteKind.cuchillo_lluvia)
        cuchillo10.set_position(189, 5)
        cuchillo10.set_velocity(0, 100)
        pause(50)
        cuchillo11 = sprites.create(img("""
                . e e . 
                            . e e . 
                            . e e . 
                            f f f f 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 .
            """),
            SpriteKind.cuchillo_lluvia)
        cuchillo11.set_position(210, 5)
        cuchillo11.set_velocity(0, 100)
        pause(50)
        cuchillo12 = sprites.create(img("""
                . e e . 
                            . e e . 
                            . e e . 
                            f f f f 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 .
            """),
            SpriteKind.cuchillo_lluvia)
        cuchillo12.set_position(231, 5)
        cuchillo12.set_velocity(0, 100)
        pause(50)
        cuchillo13 = sprites.create(img("""
                . e e . 
                            . e e . 
                            . e e . 
                            f f f f 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 .
            """),
            SpriteKind.cuchillo_lluvia)
        cuchillo13.set_position(252, 5)
        cuchillo13.set_velocity(0, 100)
        pause(350)
    if vida_jack >= 19 and vida_jack <= 24:
        cuchillo13 = sprites.create(img("""
                . e e . 
                            . e e . 
                            . e e . 
                            f f f f 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 .
            """),
            SpriteKind.cuchillo_lluvia)
        cuchillo13.set_position(252, 5)
        cuchillo13.set_velocity(0, 100)
        pause(50)
        cuchillo12 = sprites.create(img("""
                . e e . 
                            . e e . 
                            . e e . 
                            f f f f 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 .
            """),
            SpriteKind.cuchillo_lluvia)
        cuchillo12.set_position(231, 5)
        cuchillo12.set_velocity(0, 100)
        pause(50)
        cuchillo11 = sprites.create(img("""
                . e e . 
                            . e e . 
                            . e e . 
                            f f f f 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 .
            """),
            SpriteKind.cuchillo_lluvia)
        cuchillo11.set_position(210, 5)
        cuchillo11.set_velocity(0, 100)
        pause(50)
        cuchillo10 = sprites.create(img("""
                . e e . 
                            . e e . 
                            . e e . 
                            f f f f 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 .
            """),
            SpriteKind.cuchillo_lluvia)
        cuchillo10.set_position(189, 5)
        cuchillo10.set_velocity(0, 100)
        pause(50)
        cuchillo9 = sprites.create(img("""
                . e e . 
                            . e e . 
                            . e e . 
                            f f f f 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 .
            """),
            SpriteKind.cuchillo_lluvia)
        cuchillo9.set_position(168, 5)
        cuchillo9.set_velocity(0, 100)
        pause(50)
        cuchillo8 = sprites.create(img("""
                . e e . 
                            . e e . 
                            . e e . 
                            f f f f 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 .
            """),
            SpriteKind.cuchillo_lluvia)
        cuchillo8.set_position(147, 5)
        cuchillo8.set_velocity(0, 100)
        pause(50)
        cuchillo7 = sprites.create(img("""
                . e e . 
                            . e e . 
                            . e e . 
                            f f f f 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 .
            """),
            SpriteKind.cuchillo_lluvia)
        cuchillo7.set_position(126, 5)
        cuchillo7.set_velocity(0, 100)
        pause(50)
        cuchillo6 = sprites.create(img("""
                . e e . 
                            . e e . 
                            . e e . 
                            f f f f 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 .
            """),
            SpriteKind.cuchillo_lluvia)
        cuchillo6.set_position(105, 5)
        cuchillo6.set_velocity(0, 100)
        pause(50)
        cuchillo5 = sprites.create(img("""
                . e e . 
                            . e e . 
                            . e e . 
                            f f f f 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 .
            """),
            SpriteKind.cuchillo_lluvia)
        cuchillo5.set_position(84, 5)
        cuchillo5.set_velocity(0, 100)
        pause(50)
        cuchillo4 = sprites.create(img("""
                . e e . 
                            . e e . 
                            . e e . 
                            f f f f 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 .
            """),
            SpriteKind.cuchillo_lluvia)
        cuchillo4.set_position(63, 5)
        cuchillo4.set_velocity(0, 100)
        pause(50)
        cuchillo3 = sprites.create(img("""
                . e e . 
                            . e e . 
                            . e e . 
                            f f f f 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 .
            """),
            SpriteKind.cuchillo_lluvia)
        cuchillo3.set_position(42, 5)
        cuchillo3.set_velocity(0, 100)
        pause(50)
        cuchillo2 = sprites.create(img("""
                . e e . 
                            . e e . 
                            . e e . 
                            f f f f 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 .
            """),
            SpriteKind.cuchillo_lluvia)
        cuchillo2.set_position(21, 5)
        cuchillo2.set_velocity(0, 100)
        pause(50)
        cuchillo14 = sprites.create(img("""
                . e e . 
                            . e e . 
                            . e e . 
                            f f f f 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 . 
                            . 1 1 .
            """),
            SpriteKind.cuchillo_lluvia)
        cuchillo14.set_position(0, 5)
        cuchillo14.set_velocity(0, 100)
        pause(50)
    if vida_jack == 25:
        mover_a_jack()
forever(on_forever3)

def on_forever4():
    global cuchillo14
    if vida_jack == 1:
        jack_the_ripper.start_effect(effects.disintegrate, 1)
        jack_the_ripper.set_position(40, -10)
        jack_the_ripper.set_velocity(0, 120)
        pause(350)
        cuchillo14 = sprites.create(img("""
                . . . f . . . . . . . . 
                            e e e f 1 1 1 1 1 1 1 1 
                            e e e f 1 1 1 1 1 1 1 1 
                            . . . f . . . . . . . .
            """),
            SpriteKind.cuchillo)
        cuchillo14.set_position(17, 65)
        cuchillo14.follow(J1, 110)
        pause(900)
        cuchillo14.destroy(effects.spray, 1)
        pause(900)
forever(on_forever4)
