from manim import *

config.background_color = LIGHTER_GRAY
   
class FlipCounters(Scene):
    def construct(self):
        r = 0.5
        l = 1.5

        # Objects
        c11b = Circle(radius=r, color=BLACK, fill_opacity=1)
        c11w = Circle(radius=r, color=WHITE, fill_opacity=1)
        b11 = Square(side_length=l, color=BLACK)

        c12b = Circle(radius=r, color=BLACK, fill_opacity=1)
        c12w = Circle(radius=r, color=WHITE, fill_opacity=1)
        b12 = Square(side_length=l, color=BLACK)

        c21b = Circle(radius=0.5, color=BLACK, fill_opacity=1)
        c21w = Circle(radius=0.5, color=WHITE, fill_opacity=1)
        b21 = Square(side_length=l, color=BLACK)

        c22b = Circle(radius=0.5, color=BLACK, fill_opacity=1)
        c22w = Circle(radius=0.5, color=WHITE, fill_opacity=1)
        b22 = Square(side_length=l, color=BLACK)

                        
        # Relative Positions
        c12b.next_to(c11b, RIGHT, buff=0.5) 
        c21b.next_to(c11b, UP, buff=0.5) 
        c22b.next_to(c21b, RIGHT, buff=0.5)

        c12w.next_to(c11w, RIGHT, buff=0.5) 
        c21w.next_to(c11w, UP, buff=0.5) 
        c22w.next_to(c21w, RIGHT, buff=0.5) 

        b12.next_to(b11, RIGHT, buff=0)
        b21.next_to(b11, UP, buff=0) 
        b22.next_to(b21, RIGHT, buff=0)

        # Animations
        self.play(Create(b11))
        self.play(Create(b12))
        self.play(Create(b21))
        self.play(Create(b22))

        self.play(Create(c11b))
        self.play(Create(c12b))
        self.play(Create(c21b))
        self.play(Create(c22b))

        self.wait()

        self.play(Transform(c11b, c11w))
        self.play(Transform(c12b, c12w))
        self.play(Transform(c21b, c21w))
        self.play(Transform(c22b, c22w))

        # self.play(FadeOut(b11))