import pygame

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((200, 100))
songs = ["C:\\Users\\kazbe\\Downloads\\1.mp3", "C:\\Users\\kazbe\\Downloads\\2.mp3", "C:\\Users\\kazbe\\Downloads\\3.mp3"]
i = 0
current = songs[i]
pygame.mixer.music.load(current)
pygame.mixer.music.play()
pygame.mixer.music.pause()

running = True


def playNext():
    global current, songs, i
    next = (i + 1) % len(songs)
    current = songs[next]
    pygame.mixer.music.load(current)
    pygame.mixer.music.play()
    i = next


def playPrevious():
    global current, songs, i
    previous = (i - 1) % len(songs)
    current = songs[previous]
    pygame.mixer.music.load(current)
    pygame.mixer.music.play()
    i = previous


while running:
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_RIGHT:
                playNext()
            elif event.key == pygame.K_LEFT:
                playPrevious()