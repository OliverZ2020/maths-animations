from manim import *

config.background_color = LIGHTER_GRAY
   
class FlipCounters(Scene):
    def construct(self):
        r = 0.5
        l = 1.5

        # Objects
        c00b = Circle(radius=r, color=BLACK, fill_opacity=1)
        c00w = Circle(radius=r, color=WHITE, fill_opacity=1)
        b00 = Square(side_length=l, color=BLACK)
        
        c01b = Circle(radius=r, color=BLACK, fill_opacity=1)
        c01w = Circle(radius=r, color=WHITE, fill_opacity=1)
        b01 = Square(side_length=l, color=BLACK)

        c02b = Circle(radius=r, color=BLACK, fill_opacity=1)
        c02w = Circle(radius=r, color=WHITE, fill_opacity=1)
        b02 = Square(side_length=l, color=BLACK)
        
        c03b = Circle(radius=r, color=BLACK, fill_opacity=1)
        c03w = Circle(radius=r, color=WHITE, fill_opacity=1)
        b03 = Square(side_length=l, color=BLACK)

        c10b = Circle(radius=r, color=BLACK, fill_opacity=1)
        c10w = Circle(radius=r, color=WHITE, fill_opacity=1)
        b10 = Square(side_length=l, color=BLACK)

        c11b = Circle(radius=r, color=BLACK, fill_opacity=1)
        c11w = Circle(radius=r, color=WHITE, fill_opacity=1)
        b11 = Square(side_length=l, color=BLACK)

        c12b = Circle(radius=r, color=BLACK, fill_opacity=1)
        c12w = Circle(radius=r, color=WHITE, fill_opacity=1)
        b12 = Square(side_length=l, color=BLACK)

        c13b = Circle(radius=r, color=BLACK, fill_opacity=1)
        c13w = Circle(radius=r, color=WHITE, fill_opacity=1)
        b13 = Square(side_length=l, color=BLACK)

        c20b = Circle(radius=r, color=BLACK, fill_opacity=1)
        c20w = Circle(radius=r, color=WHITE, fill_opacity=1)
        b20 = Square(side_length=l, color=BLACK)

        c21b = Circle(radius=r, color=BLACK, fill_opacity=1)
        c21w = Circle(radius=r, color=WHITE, fill_opacity=1)
        b21 = Square(side_length=l, color=BLACK)

        c22b = Circle(radius=r, color=BLACK, fill_opacity=1)
        c22w = Circle(radius=r, color=WHITE, fill_opacity=1)
        b22 = Square(side_length=l, color=BLACK)
        
        c23b = Circle(radius=r, color=BLACK, fill_opacity=1)
        c23w = Circle(radius=r, color=WHITE, fill_opacity=1)
        b23 = Square(side_length=l, color=BLACK)
        
        c30b = Circle(radius=r, color=BLACK, fill_opacity=1)
        c30w = Circle(radius=r, color=WHITE, fill_opacity=1)
        b30 = Square(side_length=l, color=BLACK)

        c31b = Circle(radius=r, color=BLACK, fill_opacity=1)
        c31w = Circle(radius=r, color=WHITE, fill_opacity=1)
        b31 = Square(side_length=l, color=BLACK)

        c32b = Circle(radius=r, color=BLACK, fill_opacity=1)
        c32w = Circle(radius=r, color=WHITE, fill_opacity=1)
        b32 = Square(side_length=l, color=BLACK)

        c33b = Circle(radius=r, color=BLACK, fill_opacity=1)
        c33w = Circle(radius=r, color=WHITE, fill_opacity=1)
        b33 = Square(side_length=l, color=BLACK)

        # Relative Positions
        c01b.next_to(c11b, DOWN, buff=0.5)
        c00b.next_to(c01b, LEFT, buff=0.5)
        c02b.next_to(c01b, RIGHT, buff=0.5)
        c03b.next_to(c02b, RIGHT, buff=0.5)
        c10b.next_to(c11b, LEFT, buff=0.5)
        c12b.next_to(c11b, RIGHT, buff=0.5)
        c20b.next_to(c10b, UP, buff=0.5) 
        c21b.next_to(c11b, UP, buff=0.5) 
        c22b.next_to(c21b, RIGHT, buff=0.5)
        c13b.next_to(c12b, RIGHT,buff= 0.5)
        c23b.next_to(c13b, UP, buff=0.5)
        c30b.next_to(c20b, UP, buff=0.5)
        c31b.next_to(c30b, RIGHT, buff=0.5)
        c32b.next_to(c31b, RIGHT, buff=0.5)
        c33b.next_to(c32b, RIGHT, buff=0.5)

        c01w.next_to(c11w, DOWN, buff=0.5)
        c00w.next_to(c01w, LEFT, buff=0.5)
        c02w.next_to(c01w, RIGHT, buff=0.5)
        c03w.next_to(c02w, RIGHT, buff=0.5)
        c10w.next_to(c11w, LEFT, buff=0.5)
        c12w.next_to(c11w, RIGHT, buff=0.5) 
        c20w.next_to(c10w, UP, buff=0.5)
        c21w.next_to(c11w, UP, buff=0.5) 
        c22w.next_to(c21w, RIGHT, buff=0.5) 
        c13w.next_to(c12w, RIGHT, buff=0.5)
        c23w.next_to(c13w, UP, buff=0.5)
        c30w.next_to(c20w, UP, buff=0.5)
        c31w.next_to(c30w, RIGHT, buff=0.5)
        c32w.next_to(c31w, RIGHT, buff=0.5)
        c33w.next_to(c32w, RIGHT, buff=0.5)

        b01.next_to(b11, DOWN, buff=0)
        b00.next_to(b01, LEFT, buff=0)
        b02.next_to(b01, RIGHT, buff=0)
        b03.next_to(b02, RIGHT, buff=0)
        b10.next_to(b11, LEFT, buff=0)
        b12.next_to(b11, RIGHT, buff=0)
        b20.next_to(b10, UP, buff=0)
        b21.next_to(b11, UP, buff=0) 
        b22.next_to(b21, RIGHT, buff=0)
        b23.next_to(b22, RIGHT, buff=0)
        b13.next_to(b23, DOWN, buff=0)
        b30.next_to(b20, UP, buff=0)
        b31.next_to(b30, RIGHT, buff=0)
        b32.next_to(b31, RIGHT, buff=0)
        b33.next_to(b32, RIGHT, buff=0)

        # Animations
        self.play(Create(b11))
        self.play(Create(b01))
        self.play(Create(b00))
        self.play(Create(b10))
        self.play(Create(b02))
        self.play(Create(b03))
        self.play(Create(b12))
        self.play(Create(b13))
        self.play(Create(b22))
        self.play(Create(b21))
        self.play(Create(b23))
        self.play(Create(b20))
        self.play(Create(b30))
        self.play(Create(b31))
        self.play(Create(b32))
        self.play(Create(b33))

        self.play(Create(c11b))
        self.play(Create(c01b))
        self.play(Create(c00b))
        self.play(Create(c02b))
        self.play(Create(c03b))
        self.play(Create(c10b))
        self.play(Create(c12b))
        self.play(Create(c13b))
        self.play(Create(c21b))
        self.play(Create(c22b))
        self.play(Create(c23b))
        self.play(Create(c20b))
        self.play(Create(c30b))
        self.play(Create(c31b))
        self.play(Create(c32b))
        self.play(Create(c33b))
        

        self.play(FadeOut(c00b), run_time = 0.2)
        self.play(FadeIn(c00w), run_time = 0.2)
        self.play(FadeOut(c10b), run_time = 0.2)
        self.play(FadeIn(c10w), run_time = 0.2)
        self.play(FadeOut(c01b), run_time = 0.2)
        self.play(FadeIn(c01w), run_time = 0.2)
        self.play(FadeOut(c11b), run_time = 0.2)
        self.play(FadeIn(c11w), run_time = 0.2)

        self.wait()

        self.play(FadeOut(c11w), run_time = 0.2)
        self.play(FadeIn(c11b), run_time = 0.2)
        self.play(FadeOut(c01w), run_time = 0.2)
        self.play(FadeIn(c01b), run_time = 0.2)
        self.play(FadeOut(c12b), run_time = 0.2)
        self.play(FadeIn(c12w), run_time = 0.2)
        self.play(FadeOut(c02b), run_time = 0.2)
        self.play(FadeIn(c02w), run_time = 0.2)

        self.wait()

        self.play(FadeOut(c10w), run_time = 0.2)
        self.play(FadeIn(c10b), run_time = 0.2)
        self.play(FadeOut(c11b), run_time = 0.2)
        self.play(FadeIn(c11w), run_time = 0.2)
        self.play(FadeOut(c20b), run_time = 0.2)
        self.play(FadeIn(c20w), run_time = 0.2)
        self.play(FadeOut(c21b), run_time = 0.2)
        self.play(FadeIn(c21w), run_time = 0.2)

        self.wait()

        self.play(FadeOut(c21w), run_time = 0.2)
        self.play(FadeIn(c21b), run_time = 0.2)
        self.play(FadeOut(c22b), run_time = 0.2)
        self.play(FadeIn(c22w), run_time = 0.2)
        self.play(FadeOut(c32b), run_time = 0.2)
        self.play(FadeIn(c32w), run_time = 0.2)
        self.play(FadeOut(c31b), run_time = 0.2)
        self.play(FadeIn(c31w), run_time = 0.2)

        self.wait()

        self.play(FadeOut(c12w), run_time = 0.2)
        self.play(FadeIn(c12b), run_time = 0.2)
        self.play(FadeOut(c13b), run_time = 0.2)
        self.play(FadeIn(c13w), run_time = 0.2)
        self.play(FadeOut(c22w), run_time = 0.2)
        self.play(FadeIn(c22b), run_time = 0.2)
        self.play(FadeOut(c23b), run_time = 0.2)
        self.play(FadeIn(c23w), run_time = 0.2)

        self.wait()

        self.play(FadeOut(c32w), run_time = 0.2)
        self.play(FadeIn(c32b), run_time = 0.2)
        self.play(FadeOut(c33b), run_time = 0.2)
        self.play(FadeIn(c33w), run_time = 0.2)
        self.play(FadeOut(c22b), run_time = 0.2)
        self.play(FadeIn(c22w), run_time = 0.2)
        self.play(FadeOut(c23w), run_time = 0.2)
        self.play(FadeIn(c23b), run_time = 0.2)

        # self.play(FadeOut(b11))