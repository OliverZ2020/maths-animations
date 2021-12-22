from manim import *

config.background_color = LIGHTER_GRAY



class FlipCounters(Scene):
    def construct(self):
        C_RADIUS = 0.5
        C_BUFF = 0.5
        
        BOX_SMALL = 1.5
        BOX_BUFF = 0

        OPACITY_SOLID = 1
        TRANSPARENT = 0
  
        RT_FAST = 0.001
        RT_FLIP_DELAY = 0.2

        FONT_SIZE = 20

        # Objects
        c00b = Circle(radius=C_RADIUS, color=BLACK, fill_opacity=OPACITY_SOLID)
        c00w = Circle(radius=C_RADIUS, color=WHITE, fill_opacity=OPACITY_SOLID)
        b00 = Square(side_length=BOX_SMALL, color=BLACK)
        
        c01b = Circle(radius=C_RADIUS, color=BLACK, fill_opacity=OPACITY_SOLID)
        c01w = Circle(radius=C_RADIUS, color=WHITE, fill_opacity=OPACITY_SOLID)
        b01 = Square(side_length=BOX_SMALL, color=BLACK)

        c02b = Circle(radius=C_RADIUS, color=BLACK, fill_opacity=OPACITY_SOLID)
        c02w = Circle(radius=C_RADIUS, color=WHITE, fill_opacity=OPACITY_SOLID)
        b02 = Square(side_length=BOX_SMALL, color=BLACK)
        
        c03b = Circle(radius=C_RADIUS, color=BLACK, fill_opacity=OPACITY_SOLID)
        c03w = Circle(radius=C_RADIUS, color=WHITE, fill_opacity=OPACITY_SOLID)
        b03 = Square(side_length=BOX_SMALL, color=BLACK)

        c10b = Circle(radius=C_RADIUS, color=BLACK, fill_opacity=OPACITY_SOLID)
        c10w = Circle(radius=C_RADIUS, color=WHITE, fill_opacity=OPACITY_SOLID)
        b10 = Square(side_length=BOX_SMALL, color=BLACK)

        # Cordinate (1, 1) is used as the position reference for others
        c11b = Circle(radius=C_RADIUS, color=BLACK, fill_opacity=OPACITY_SOLID)
        c11b.shift(LEFT*0.75).shift(DOWN*0.75)
        c11w = Circle(radius=C_RADIUS, color=WHITE, fill_opacity=OPACITY_SOLID)
        c11w.shift(LEFT*0.75).shift(DOWN*0.75)
        b11 = Square(side_length=BOX_SMALL, color=BLACK)
        b11.shift(LEFT*0.75).shift(DOWN*0.75)

        c12b = Circle(radius=C_RADIUS, color=BLACK, fill_opacity=OPACITY_SOLID)
        c12w = Circle(radius=C_RADIUS, color=WHITE, fill_opacity=OPACITY_SOLID)
        b12 = Square(side_length=BOX_SMALL, color=BLACK)

        c13b = Circle(radius=C_RADIUS, color=BLACK, fill_opacity=OPACITY_SOLID)
        c13w = Circle(radius=C_RADIUS, color=WHITE, fill_opacity=OPACITY_SOLID)
        b13 = Square(side_length=BOX_SMALL, color=BLACK)

        c20b = Circle(radius=C_RADIUS, color=BLACK, fill_opacity=OPACITY_SOLID)
        c20w = Circle(radius=C_RADIUS, color=WHITE, fill_opacity=OPACITY_SOLID)
        b20 = Square(side_length=BOX_SMALL, color=BLACK)

        c21b = Circle(radius=C_RADIUS, color=BLACK, fill_opacity=OPACITY_SOLID)
        c21w = Circle(radius=C_RADIUS, color=WHITE, fill_opacity=OPACITY_SOLID)
        b21 = Square(side_length=BOX_SMALL, color=BLACK)

        c22b = Circle(radius=C_RADIUS, color=BLACK, fill_opacity=OPACITY_SOLID)
        c22w = Circle(radius=C_RADIUS, color=WHITE, fill_opacity=OPACITY_SOLID)
        b22 = Square(side_length=BOX_SMALL, color=BLACK)
        
        c23b = Circle(radius=C_RADIUS, color=BLACK, fill_opacity=OPACITY_SOLID)
        c23w = Circle(radius=C_RADIUS, color=WHITE, fill_opacity=OPACITY_SOLID)
        b23 = Square(side_length=BOX_SMALL, color=BLACK)
        
        c30b = Circle(radius=C_RADIUS, color=BLACK, fill_opacity=OPACITY_SOLID)
        c30w = Circle(radius=C_RADIUS, color=WHITE, fill_opacity=OPACITY_SOLID)
        b30 = Square(side_length=BOX_SMALL, color=BLACK)

        c31b = Circle(radius=C_RADIUS, color=BLACK, fill_opacity=OPACITY_SOLID)
        c31w = Circle(radius=C_RADIUS, color=WHITE, fill_opacity=OPACITY_SOLID)
        b31 = Square(side_length=BOX_SMALL, color=BLACK)

        c32b = Circle(radius=C_RADIUS, color=BLACK, fill_opacity=OPACITY_SOLID)
        c32w = Circle(radius=C_RADIUS, color=WHITE, fill_opacity=OPACITY_SOLID)
        b32 = Square(side_length=BOX_SMALL, color=BLACK)

        c33b = Circle(radius=C_RADIUS, color=BLACK, fill_opacity=OPACITY_SOLID)
        c33w = Circle(radius=C_RADIUS, color=WHITE, fill_opacity=OPACITY_SOLID)
        b33 = Square(side_length=BOX_SMALL, color=BLACK)
 
        # Relative Positions
        c01b.next_to(c11b, DOWN, buff=C_BUFF)
        c00b.next_to(c01b, LEFT, buff=C_BUFF)
        c02b.next_to(c01b, RIGHT, buff=C_BUFF)
        c03b.next_to(c02b, RIGHT, buff=C_BUFF)

        c10b.next_to(c11b, LEFT, buff=C_BUFF)
        c12b.next_to(c11b, RIGHT, buff=C_BUFF)
        c13b.next_to(c12b, RIGHT,buff= C_BUFF)

        c20b.next_to(c10b, UP, buff=C_BUFF) 
        c21b.next_to(c11b, UP, buff=C_BUFF) 
        c22b.next_to(c21b, RIGHT, buff=C_BUFF)
        c23b.next_to(c13b, UP, buff=C_BUFF)

        c30b.next_to(c20b, UP, buff=C_BUFF)
        c31b.next_to(c30b, RIGHT, buff=C_BUFF)
        c32b.next_to(c31b, RIGHT, buff=C_BUFF)
        c33b.next_to(c32b, RIGHT, buff=C_BUFF)

        c01w.next_to(c11w, DOWN,  buff=C_BUFF)
        c00w.next_to(c01w, LEFT,  buff=C_BUFF)
        c02w.next_to(c01w, RIGHT, buff=C_BUFF)
        c03w.next_to(c02w, RIGHT, buff=C_BUFF)
        c10w.next_to(c11w, LEFT,  buff=C_BUFF)
        c12w.next_to(c11w, RIGHT, buff=C_BUFF) 
        c20w.next_to(c10w, UP,    buff=C_BUFF)
        c21w.next_to(c11w, UP,    buff=C_BUFF) 
        c22w.next_to(c21w, RIGHT, buff=C_BUFF) 
        c13w.next_to(c12w, RIGHT, buff=C_BUFF)
        c23w.next_to(c13w, UP,    buff=C_BUFF)
        c30w.next_to(c20w, UP,    buff=C_BUFF)
        c31w.next_to(c30w, RIGHT, buff=C_BUFF)
        c32w.next_to(c31w, RIGHT, buff=C_BUFF)
        c33w.next_to(c32w, RIGHT, buff=C_BUFF)

        b01.next_to(b11, DOWN,  buff=BOX_BUFF)
        b00.next_to(b01, LEFT,  buff=BOX_BUFF)
        b02.next_to(b01, RIGHT, buff=BOX_BUFF)
        b03.next_to(b02, RIGHT, buff=BOX_BUFF)
        b10.next_to(b11, LEFT,  buff=BOX_BUFF)
        b12.next_to(b11, RIGHT, buff=BOX_BUFF)
        b20.next_to(b10, UP,    buff=BOX_BUFF)
        b21.next_to(b11, UP,    buff=BOX_BUFF) 
        b22.next_to(b21, RIGHT, buff=BOX_BUFF)
        b23.next_to(b22, RIGHT, buff=BOX_BUFF)
        b13.next_to(b23, DOWN,  buff=BOX_BUFF)
        b30.next_to(b20, UP,    buff=BOX_BUFF)
        b31.next_to(b30, RIGHT, buff=BOX_BUFF)
        b32.next_to(b31, RIGHT, buff=BOX_BUFF)
        b33.next_to(b32, RIGHT, buff=BOX_BUFF)

        # Animations
        # Add all the small boxes
        self.add(b00, b01, b02, b03)
        self.add(b10, b11, b12, b13)
        self.add(b20, b21, b22, b23)
        self.add(b30, b31, b32, b33)
        # Create all the counters
        self.play(Create(c00b), run_time=RT_FAST)
        self.play(Create(c01b), run_time=RT_FAST)
        self.play(Create(c02b), run_time=RT_FAST)
        self.play(Create(c03b), run_time=RT_FAST)
        
        self.play(Create(c10b), run_time=RT_FAST)
        self.play(Create(c11b), run_time=RT_FAST)
        self.play(Create(c12b), run_time=RT_FAST)
        self.play(Create(c13b), run_time=RT_FAST)

        self.play(Create(c20b), run_time=RT_FAST)
        self.play(Create(c21b), run_time=RT_FAST)
        self.play(Create(c22b), run_time=RT_FAST)
        self.play(Create(c23b), run_time=RT_FAST)

        self.play(Create(c30b), run_time=RT_FAST)
        self.play(Create(c31b), run_time=RT_FAST)
        self.play(Create(c32b), run_time=RT_FAST)
        self.play(Create(c33b), run_time=RT_FAST)

        # A big box for highlighting the flip
        bbox = Square(side_length=BOX_SMALL * 2, color=PURE_RED, fill_opacity=TRANSPARENT)

        # Add a text description
        step1 = Text("Step 1", color=BLACK, font_size=FONT_SIZE).to_edge(UL, buff=2)
        self.play(Write(step1))

        bbox = bbox.shift(LEFT*1.5).shift(DOWN*1.5)
        self.play(FadeIn(bbox), run_time=RT_FLIP_DELAY)

        # Flip from (0, 0) to (1, 1)
        self.play(FadeOut(c00b), run_time=RT_FLIP_DELAY)
        self.play(FadeIn(c00w),  run_time=RT_FLIP_DELAY)
        self.play(FadeOut(c10b), run_time=RT_FLIP_DELAY)
        self.play(FadeIn(c10w),  run_time=RT_FLIP_DELAY)
        self.play(FadeOut(c11b), run_time=RT_FLIP_DELAY)
        self.play(FadeIn(c11w),  run_time=RT_FLIP_DELAY)
        self.play(FadeOut(c01b), run_time=RT_FLIP_DELAY)
        self.play(FadeIn(c01w),  run_time=RT_FLIP_DELAY)

        self.play(FadeOut(bbox), run_time=RT_FLIP_DELAY)
        bbox = bbox.shift(RIGHT*1.5)

        step2 = Text("Step 2", color=BLACK, font_size=FONT_SIZE)
        step2.next_to(step1, DOWN, buff=0.5)
        self.play(Write(step2))

        self.play(FadeIn(bbox), run_time=RT_FLIP_DELAY)

        self.wait()

        self.play(FadeOut(c11w), run_time=RT_FLIP_DELAY)
        self.play(FadeIn(c11b),  run_time=RT_FLIP_DELAY)
        self.play(FadeOut(c01w), run_time=RT_FLIP_DELAY)
        self.play(FadeIn(c01b),  run_time=RT_FLIP_DELAY)
        self.play(FadeOut(c12b), run_time=RT_FLIP_DELAY)
        self.play(FadeIn(c12w),  run_time=RT_FLIP_DELAY)
        self.play(FadeOut(c02b), run_time=RT_FLIP_DELAY)
        self.play(FadeIn(c02w),  run_time=RT_FLIP_DELAY)

        self.play(FadeOut(bbox), run_time=RT_FLIP_DELAY)
        bbox = bbox.shift(LEFT*1.5).shift(UP*1.5)

        step3 = Text("Step 3", color=BLACK, font_size=FONT_SIZE)
        step3.next_to(step2, DOWN, buff=0.5)
        self.play(Write(step3))

        self.play(FadeIn(bbox), run_time=RT_FLIP_DELAY)

        self.wait()

        self.play(FadeOut(c10w), run_time=RT_FLIP_DELAY)
        self.play(FadeIn(c10b),  run_time=RT_FLIP_DELAY)
        self.play(FadeOut(c11b), run_time=RT_FLIP_DELAY)
        self.play(FadeIn(c11w),  run_time=RT_FLIP_DELAY)
        self.play(FadeOut(c20b), run_time=RT_FLIP_DELAY)
        self.play(FadeIn(c20w),  run_time=RT_FLIP_DELAY)
        self.play(FadeOut(c21b), run_time=RT_FLIP_DELAY)
        self.play(FadeIn(c21w),  run_time=RT_FLIP_DELAY)

        self.play(FadeOut(bbox), run_time=RT_FLIP_DELAY)
        bbox = bbox.shift(RIGHT*1.5).shift(UP*1.5)

        step4 = Text("Step 4", color=BLACK, font_size=FONT_SIZE)
        step4.next_to(step3, DOWN, buff=0.5)
        self.play(Write(step4))

        self.play(FadeIn(bbox), run_time=RT_FLIP_DELAY)

        self.wait()

        self.play(FadeOut(c21w), run_time=RT_FLIP_DELAY)
        self.play(FadeIn(c21b),  run_time=RT_FLIP_DELAY)
        self.play(FadeOut(c22b), run_time=RT_FLIP_DELAY)
        self.play(FadeIn(c22w),  run_time=RT_FLIP_DELAY)
        self.play(FadeOut(c32b), run_time=RT_FLIP_DELAY)
        self.play(FadeIn(c32w),  run_time=RT_FLIP_DELAY)
        self.play(FadeOut(c31b), run_time=RT_FLIP_DELAY)
        self.play(FadeIn(c31w),  run_time=RT_FLIP_DELAY)

        self.play(FadeOut(bbox), run_time=RT_FLIP_DELAY)
        bbox = bbox.shift(RIGHT*1.5).shift(DOWN*1.5)

        step5 = Text("Step 5", color=BLACK, font_size=FONT_SIZE)
        step5.next_to(step4, DOWN, buff=0.5)
        self.play(Write(step5))

        self.play(FadeIn(bbox), run_time=RT_FLIP_DELAY)

        self.wait()

        self.play(FadeOut(c12w), run_time=RT_FLIP_DELAY)
        self.play(FadeIn(c12b),  run_time=RT_FLIP_DELAY)
        self.play(FadeOut(c13b), run_time=RT_FLIP_DELAY)
        self.play(FadeIn(c13w),  run_time=RT_FLIP_DELAY)
        self.play(FadeOut(c22w), run_time=RT_FLIP_DELAY)
        self.play(FadeIn(c22b),  run_time=RT_FLIP_DELAY)
        self.play(FadeOut(c23b), run_time=RT_FLIP_DELAY)
        self.play(FadeIn(c23w),  run_time=RT_FLIP_DELAY)

        self.play(FadeOut(bbox), run_time=RT_FLIP_DELAY)
        bbox = bbox.shift(UP*1.5)

        step6 = Text("Step 6", color=BLACK, font_size=FONT_SIZE)
        step6.next_to(step5, DOWN, buff=0.5)
        self.play(Write(step6))

        self.play(FadeIn(bbox), run_time=RT_FLIP_DELAY)

        self.wait()

        self.play(FadeOut(c32w), run_time=RT_FLIP_DELAY)
        self.play(FadeIn(c32b),  run_time=RT_FLIP_DELAY)
        self.play(FadeOut(c33b), run_time=RT_FLIP_DELAY)
        self.play(FadeIn(c33w),  run_time=RT_FLIP_DELAY)
        self.play(FadeOut(c22b), run_time=RT_FLIP_DELAY)
        self.play(FadeIn(c22w),  run_time=RT_FLIP_DELAY)
        self.play(FadeOut(c23w), run_time=RT_FLIP_DELAY)
        self.play(FadeIn(c23b),  run_time=RT_FLIP_DELAY)

        self.play(FadeOut(bbox), run_time=RT_FLIP_DELAY)

        self.wait()