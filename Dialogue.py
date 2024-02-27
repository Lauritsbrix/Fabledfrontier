def display_text(text):
    lines = text.split('\n')
    for i in range(0, len(lines), 4):  # Change 4 to the number of lines you want to display at once
        print('\n'.join(lines[i:i+4]))
        input("Press Enter to continue...")

intro_text = """ 
The Prophecy:
In the darkest hour, an ancient prophecy emerges,
foretelling the rise of a chosen few who would embark on a perilous quest to save Luminos.
As the Shadow Veil advances, threatening to consume everything in its path,
the destiny of the world rests on the shoulders of heroes yet to be revealed.

The Quest for Salvation:
Heroes from each race must unite, setting aside centuries-old rivalries,
to confront the malevolence that seeks to plunge their world into eternal darkness.
The journey will take them across treacherous landscapes, through forgotten ruins,
and into the heart of the Shadow Veil itself.
Armed with the relics of old, blessed by ancient deities, and guided by the wisdom of wise sages,
the heroes of Luminos must navigate political intrigue,
face mythical creatures, and ultimately confront the source of the encroaching Shadow Veil.
Only through unity, courage, and the rediscovery of forgotten lore can Luminos hope to survive.
The fate of the world rests in the hands of those willing to embark on the epic quest to save their homeland from impending doom.
The journey to salvation begins, and the heroes of Luminos must rise to the challenge or witness the end of an era.

"""
display_text(intro_text)