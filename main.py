foodSprite: Sprite = None
spriteSelector = randint(0, 9)
if spriteSelector < 5:
    foodSprite = sprites.create(img("""
            . . . . . . . . . . . 6 6 6 6 6 
                    . . . . . . . . . 6 6 7 7 7 7 8 
                    . . . . . . 8 8 8 7 7 8 8 6 8 8 
                    . . e e e e c 6 6 8 8 . 8 7 8 . 
                    . e 2 5 4 2 e c 8 . . . 6 7 8 . 
                    e 2 4 2 2 2 2 2 c . . . 6 7 8 . 
                    e 2 2 2 2 2 2 2 c . . . 8 6 8 . 
                    e 2 e e 2 2 2 2 e e e e c 6 8 . 
                    c 2 e e 2 2 2 2 e 2 5 4 2 c 8 . 
                    . c 2 e e e 2 e 2 4 2 2 2 2 c . 
                    . . c 2 2 2 e e 2 2 2 2 2 2 2 e 
                    . . . e c c e c 2 2 2 2 2 2 2 e 
                    . . . . . . . c 2 e e 2 2 e 2 c 
                    . . . . . . . c e e e e e e 2 c 
                    . . . . . . . . c e 2 2 2 2 c . 
                    . . . . . . . . . c c c c c . .
        """),
        SpriteKind.food)
    foodSprite.set_position(10, 10)
else:
    foodSprite = sprites.create(img("""
            . . . . . . . 6 . . . . . . . . 
                    . . . . . . 8 6 6 . . . 6 8 . . 
                    . . . e e e 8 8 6 6 . 6 7 8 . . 
                    . . e 2 2 2 2 e 8 6 6 7 6 . . . 
                    . e 2 2 4 4 2 7 7 7 7 7 8 6 . . 
                    . e 2 4 4 2 6 7 7 7 6 7 6 8 8 . 
                    e 2 4 5 2 2 6 7 7 6 2 7 7 6 . . 
                    e 2 4 4 2 2 6 7 6 2 2 6 7 7 6 . 
                    e 2 4 2 2 2 6 6 2 2 2 e 7 7 6 . 
                    e 2 4 2 2 4 2 2 2 4 2 2 e 7 6 . 
                    e 2 4 2 2 2 2 2 2 2 2 2 e c 6 . 
                    e 2 2 2 2 2 2 2 4 e 2 e e c . . 
                    e e 2 e 2 2 4 2 2 e e e c . . . 
                    e e e e 2 e 2 2 e e e c . . . . 
                    e e e 2 e e c e c c c . . . . . 
                    . c c c c c c c . . . . . . . .
        """),
        SpriteKind.food)
    foodSprite.set_position(150, 110)
foodSprite.say_text(":)")