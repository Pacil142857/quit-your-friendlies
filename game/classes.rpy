init python:
    class BracketSet:
        def __init__(self, *players):
            # P1 and P2 should be Character objects
            # Their names will be accessed with pX.name
            if len(players) > 0:
                self.p1 = players[0]
                self.p2 = players[1]
            else:
                self.p1 = None
                self.p2 = None
            self.winner = None
            self.loser = None
        
        def report(self, winner):
            if winner.name == p1.name:
                self.winner = p1
                self.loser = p2
            else:
                self.winner = p2
                self.loser = p1
        
        def get_p1_name(self):
            if self.p1 is None:
                return "TBD"
            return self.p1.name
        
        def get_p2_name(self):
            if self.p2 is None:
                return "TBD"
            return self.p2.name
        
        def get_p1(self):
            return self.p1
        
        def get_p2(self):
            return self.p2
        
        def get_winner_name(self):
            if self.winner is None:
                return "TBD"
            return self.winner.name

        def get_winner(self):
            return self.winner

        def get_loser_name(self):
            if self.loser is None:
                return "TBD"
            return self.loser.name
        
        def get_loser(self):
            return self.loser
        
        def set_players(self, p1, p2):
            self.p1 = p1
            self.p2 = p2
        
        def set_p1(self, p1):
            self.p1 = p1
        
        def set_p2(self, p2):
            self.p2 = p2
        
        def is_callable(self):
            return self.p1 is not None and self.p2 is not None

    def determine_winner(p1_name, p2_name, p1_score, p2_score):
        if p1_score is None or p2_score is None:
            return ""
        if p1_score > p2_score:
            return p1_name
        if p2_score > p1_score:
            return p2_name
        return ""
    
    # This class currently doesn't work, and I don't intend to fix it
    class Line(renpy.Displayable):
        def __init__(self, x1, y1, x2, y2):
            super(Line).__init__()
            self.x1 = x1
            self.y1 = y1
            self.x2 = x2
            self.y2 = y2
        
        def render(self, width, height, st, at):
            r = renpy.Render(1920, 1080)
            s = r.canvas()
            c = (255, 0, 0) # every line will be white for now
            s.aaline(c, (self.x1, self.y1), (self.x2, self.y2))
            s.line(c, (self.x1, self.y1), (self.x2, self.y2))
            r.blit(s, (0, 0))
            renpy.redraw(self, 0)
            return r
    
        def event(self, ev, x, y, st):
            renpy.redraw(self, 0)