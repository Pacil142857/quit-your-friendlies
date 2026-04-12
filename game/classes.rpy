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

    class BracketAdvancementDataHolder:
        def __init__(self, in_winners, round_number, set_number, next_sets, losers_sets):
            self.in_winners = in_winners
            self.round_number = round_number
            self.set_number = set_number
            self.next_sets = next_sets
            self.losers_sets = losers_sets # If self.in_winners is False, then this is equivalent to self.next_sets
    
    def send_to_losers(player, advancement_data):
        """ Updates the Losers Bracket to send a player to Losers. This is only configured to work for 8-person brackets.

        player: the player (a Character object)
        winners_round: Either 1, 2, 3, or 4 for winners round 1, 2, 3, or Grand Finals
        set_number: 0 if it's the topmost set, 1 if it's below that, 2 if it's below *that*, and so on
        losers_sets: A list of sets in the relevant losers round (probably lr1, lr2, or lf)
        """
        if not advancement_data.in_winners:
            return
        winners_round = advancement_data.round_number
        set_number = advancement_data.set_number
        losers_sets = advancement_data.losers_sets

        if winners_round == 1:
            if set_number == 0:
                losers_sets[0].set_p2(player)
            elif set_number == 1:
                losers_sets[0].set_p1(player)
            elif set_number == 2:
                losers_sets[1].set_p2(player)
            elif set_number == 3:
                losers_sets[1].set_p1(player)
        elif winners_round == 2:
            if set_number == 0:
                losers_sets[1].set_p1(player)
            elif set_number == 1:
                losers_sets[0].set_p1(player)
        elif winners_round == 3:
            losers_sets[0].set_p1(player)
        elif winners_round == 4:
            losers_sets[0].set_p2(player) # Should work for True Finals
    
    def advance_in_bracket(player, advancement_data):
        """ Advances the winner of a set to their next set. This is configured for an 8-person bracket.

        player: The player who won (a Character object)
        in_winners: True if the player is in Winners bracket and False otherwise
        round_number: The round. Should be 1 for Winners/Losers Round 1, 2 for Winners/Losers Round 2, and so on.
        set_number: The number of their set. The topmost set is 0, the one below that is 1, and so on.
        next_sets: A list of sets in the round that the player is advancing to
        """
        in_winners = advancement_data.in_winners
        round_number = advancement_data.round_number
        set_number = advancement_data.set_number
        next_sets = advancement_data.next_sets

        if in_winners:
            if round_number == 1:
                if set_number == 0:
                    next_sets[0].set_p1(player)
                elif set_number == 1:
                    next_sets[0].set_p2(player)
                elif set_number == 2:
                    next_sets[1].set_p1(player)
                elif set_number == 3:
                    next_sets[1].set_p2(player)
            elif round_number == 2:
                if set_number == 0:
                    next_sets[0].set_p1(player)
                elif set_number == 1:
                    next_sets[0].set_p2(player)
            elif round_number == 3:
                next_sets[0].set_p1(player)
            elif round_number == 4:
                next_sets[0].set_p1(player) # Advances the player to True Finals
        else:
            if round_number == 1:
                next_sets[set_number].set_p2(player)
            elif round_number == 2:
                if set_number == 0:
                    next_sets[0].set_p1(player)
                elif set_number == 1:
                    next_sets[0].set_p2(player)
            elif round_number == 3:
                next_sets[0].set_p2(player)
            elif round_number == 4:
                next_sets[0].set_p2(player)

    def determine_winner(p1, p2, p1_score, p2_score):
        if p1_score is None or p2_score is None:
            return ""
        if p1_score > p2_score:
            return p1
        if p2_score > p1_score:
            return p2
        return ""
    
    def determine_loser(p1, p2, p1_score, p2_score):
        if p1_score is None or p2_score is None:
            return ""
        if p1_score < p2_score:
            return p1
        if p2_score < p1_score:
            return p2
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

    VALID_TIMER_MODES = ("countdown", "countup", "stopwatch")

    class TimerState:
        def __init__(self, duration, mode="countdown"):
            # duration is in seconds, mode can be "countdown", "countup", or "stopwatch"
            if mode not in VALID_TIMER_MODES:
                raise ValueError("TimerState mode must be one of: " + ", ".join(VALID_TIMER_MODES))
            self.duration = max(0, duration) # negative durations don't make sense
            self.mode = mode
            self.elapsed = 0.0
            self.running = False
            self.finished = False
            self.just_expired = False # set to True for one tick when the timer finishes

        def start(self):
            if not self.finished:
                self.running = True

        def pause(self):
            self.running = False

        def reset(self):
            self.elapsed = 0.0
            self.running = False
            self.finished = False
            self.just_expired = False

        def stop(self):
            # full stop, can't resume without reset.
            # does NOT trigger on_expire (that only happens when the timer runs out naturally)
            self.running = False
            self.finished = True

        def tick(self, dt):
            # Clear the expired flag each tick so it only stays True for one cycle
            self.just_expired = False
            if not self.running or self.finished:
                return
            self.elapsed += dt
            # Stopwatch has no limit, so only check for countdown/countup
            if self.mode != "stopwatch" and self.elapsed >= self.duration:
                self.elapsed = self.duration
                self.finished = True
                self.running = False
                self.just_expired = True

        def get_display_time(self):
            if self.mode == "countdown":
                t = max(0, self.duration - self.elapsed)
            else:
                t = self.elapsed
            total_secs = int(t)
            hrs = total_secs // 3600
            mins = (total_secs % 3600) // 60
            secs = total_secs % 60
            if hrs > 0:
                return "{:d}:{:02d}:{:02d}".format(hrs, mins, secs)
            return "{:02d}:{:02d}".format(mins, secs)

        def get_fraction(self):
            # Returns a value from 0.0 to 1.0 representing how much time has passed
            if self.duration <= 0:
                return 0.0
            frac = self.elapsed / self.duration
            return min(1.0, frac)