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


        # Animations
        self.play(Create(b11))
        self.play(Create(b01))
        self.play(Create(b00))
        self.play(Create(b10))
        self.play(Create(b02))
        self.play(Create(b03))
        self.play(Create(b13))
        self.play(Create(b12))
        self.play(Create(b22))
        self.play(Create(b21))
        self.play(Create(b23))
        self.play(Create(b20))
    

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

        self.play(Transform(c00b, c00w))
        self.play(Transform(c10b, c10w))
        self.play(Transform(c01b, c01w))
        self.play(Transform(c11b, c11w))

        self.wait()

        self.play(Transform(c11w, c11b))
        self.play(Transform(c01w, c01b))
        self.play(Transform(c12b, c12w))
        self.play(Transform(c02b, c02w))

        self.wait()

        self.play(Transform(c10w, c10b))
        self.play(Transform(c11b, c11w))
        self.play(Transform(c20b, c20w))
        self.play(Transform(c21b, c21w))

        # self.play(FadeOut(b11))