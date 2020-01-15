from main.window import all_sprites

def delete_all_sprites():
    for sprite in all_sprites:
        sprite.kill()