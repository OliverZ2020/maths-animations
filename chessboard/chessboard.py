from manim import *

config.background_color = LIGHTER_GRAY
   
class FlipCounters(Scene):
    def construct(self):
        c11b = Circle(radius=0.5)
        c11b.set_fill(BLACK, opacity=1)        
        c11w = Circle(radius=0.5)
        c11w.set_fill(WHITE, opacity=1)

        c12b = Circle(radius=0.5)
        c12b.set_fill(BLACK, opacity=1)        
        c12w = Circle(radius=0.5)
        c12w.set_fill(WHITE, opacity=1)

        c21b = Circle(radius=0.5)
        c21b.set_fill(BLACK, opacity=1)        
        c21w = Circle(radius=0.5)
        c21w.set_fill(WHITE, opacity=1)

        c22b = Circle(radius=0.5)
        c22b.set_fill(BLACK, opacity=1)        
        c22w = Circle(radius=0.5)
        c22w.set_fill(WHITE, opacity=1)
        
        c12b.next_to(c11b, RIGHT, buff=0.5) 
        c21b.next_to(c11b, UP, buff=0.5) 
        c22b.next_to(c21b, RIGHT, buff=0.5) 

        c12w.next_to(c11w, RIGHT, buff=0.5) 
        c21w.next_to(c11w, UP, buff=0.5) 
        c22w.next_to(c21w, RIGHT, buff=0.5) 

        self.play(Create(c11b))
        self.play(Create(c12b))
        self.play(Create(c21b))
        self.play(Create(c22b))

        self.wait()

        self.play(Transform(c11b, c11w))
        self.play(Transform(c12b, c12w))
        self.play(Transform(c21b, c21w))
        self.play(Transform(c22b, c22w))