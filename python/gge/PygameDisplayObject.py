
from gge.GameObject import GameObject
from gge.DisplayTypes import Resolution, Fullscreen, DisplayRep
from gge.Types import Position

import pygame

from collections import defaultdict, namedtuple

PosRep = namedtuple("PosRep", "pos rep")

class PygameDisplayObject(GameObject):
    """Assumes pygame is initialized.
    Attributes:
       Resolution"""
    def __init__(self, gge):
        super(PygameDisplayObject, self).__init__(gge)

        self.setAttribute(Resolution)
        res = self.getAttribute(Resolution)
        res.newListener(self.__handleResolution)

        self.setAttribute(Fullscreen, value=False)
        full = self.getAttribute(Fullscreen)
        full.newListener(self.__handleFullscreen)

    def update(self, dt):
        reps_bgd = defaultdict(list)
        reps_fgd = defaultdict(list)
        reps_hud = defaultdict(list)

        for game_object in self.gge.getGameObjects():
            rep = game_object.getAttributeValue(DisplayRep)
            if not rep:
                continue

            pos_rep = PosRep(game_object.getAttributeValue(Position), rep)
            if rep.layer.name == "background":
                reps_bgd[rep.layer.number].append(pos_rep)
            elif rep.layer.name == "foreground":
                reps_fgd[rep.layer.number].append(pos_rep)
            elif rep.layer.name == "hud":
                reps_hud[rep.layer.number].append(pos_rep)

        self.__display.fill((255, 255, 255))

        self.__drawLayer(reps_bgd)
        self.__drawLayer(reps_fgd)
        self.__drawLayer(reps_hud)

        pygame.display.flip()

    def getSystemFonts(self):
        return pygame.font.get_fonts()

    def __updateDisplay(self):
        res = self.getAttributeValue(Resolution)
        flags = pygame.DOUBLEBUF | pygame.HWSURFACE
        if self.getAttributeValue(Fullscreen):
            flags |= pygame.FULLSCREEN
        self.__display = pygame.display.set_mode(res, flags)

    def __handleResolution(self, value):
        self.__updateDisplay()

    def __handleFullscreen(self, value):
        self.__updateDisplay()

    def __drawLayer(self, pos_reps):
        for num in sorted(pos_reps.keys()):
            for pos_rep in pos_reps[num]:
                self.__drawRepresentation(pos_rep)

    def __drawRepresentation(self, pos_rep):
        pos = pos_rep.pos
        rep = pos_rep.rep

        # images = rep.images
        # for source, offset in images:
        #     self.__drawImage(source, offset)

        for shape in rep.shapes:
            self.__drawShape(pos, shape)

        for text in rep.text:
            self.__drawText(pos, text)

    def __drawShape(self, pos, shape):
        x = pos.x + shape.offset.x
        y = pos.y + shape.offset.y
        rect = pygame.Rect(x, y, shape.size.w, shape.size.h)
        self.__display.fill(shape.color.fill.value, rect)
        if shape.lineWidth > 0:
            pygame.draw.rect(self.__display, shape.color.line.value, rect,
                             shape.lineWidth)

    def __drawText(self, pos, text):
        x = pos.x + text.offset.x
        y = pos.y + text.offset.y
        # TODO: cache fonts? (or image)
        font = pygame.font.SysFont(text.font, text.size)
        txt = font.render(text.text, True, text.color.value)
        rect = txt.get_rect(topleft=(x, y))
        self.__display.blit(txt, rect)

    # def __drawImage(self, source, offset):
    #     print source, offset
    #     image = self.__getImage(source)

    # def __getImage(self, source):
    #     # Retrieve or load the image
    #     return None
