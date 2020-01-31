from main.objects.group_sprites import all_sprites


def delete_all_sprites(groups=(all_sprites,)):
    for group in groups:
        for sprite in group:
            sprite.kill()
