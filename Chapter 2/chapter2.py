from manim import *

class Initial(Scene):
    def construct(self):
        intro = Tex("Chapter 2: Compound Interest")
        intro_1 = Tex("Class 8")        
        intro_1.next_to(intro, 1.5*DOWN)
        self.play(Write(intro))
        self.play(FadeIn(intro_1))
        self.wait(2)
        self.play(FadeOut(intro), FadeOut(intro_1))
        self.wait(1)

# class SI(Scene):
#     def construct(self):
        si = Tex("Simple Interest")
        si.set_color(color=["#aec6cf",WHITE])
        self.play(Write(si))
        self.wait(1.5)

        si_n = si.copy().move_to(3.0*UP).scale(0.75)
        self.play(Transform(si, si_n))
        self.wait(1)

        si_1 = Text("Principal amount = Rs.1000")
        si_2 = Text("Rate of Interest = 10% p.a.")
        si_3 = Text("Time = 2 years")

        si_4 = Text("Year 0: Rs.1000")
        si_5 = Text("Year 1: Rs.1000 + Rs.100 = Rs.1100")
        si_6 = Text("Year 2: Rs.1100 + Rs.100 = Rs.1200")

        self.play(Write(si_1))
        self.wait(1)
        si_11 = si_1.copy().move_to(1*UP).scale(0.5)
        self.play(ReplacementTransform(si_1, si_11))
        self.wait(1)

        self.play(Write(si_2.move_to(DOWN)))
        self.wait(1)
        si_22 = si_2.copy().next_to(si_1, DOWN).scale(0.5)
        self.play(ReplacementTransform(si_2, si_22))
        self.wait(1)

        self.play(Write(si_3.move_to(DOWN)))
        self.wait(1)
        si_33 = si_3.copy().next_to(si_2, DOWN).scale(0.5)
        self.play(ReplacementTransform(si_3, si_33))
        self.wait(1)

        group1 = VGroup(si_11, si_22, si_33)
        grouped1 = Text("N = 2; P = Rs.1000; R = 10%").next_to(si_n, 3*DOWN).scale(0.75)
        self.play(ReplacementTransform(group1, grouped1))

        self.play(Write(si_4.scale(0.75)))
        self.wait(1)
        self.play(Write(si_5.next_to(si_4, DOWN).scale(0.75)))
        self.wait(1)
        self.play(Write(si_6.next_to(si_5, DOWN).scale(0.75)))
        self.wait(1)
        self.clear()
        self.wait(1)

# class CI(Scene):
#     def construct(self):
        ci = Tex("Compound Interest")
        ci.set_color(color=["#aec6cf",WHITE])
        self.play(Write(ci))
        self.wait(1.5)

        ci_n = ci.copy().move_to(3.0*UP).scale(0.75)
        self.play(Transform(ci, ci_n))
        self.wait(1)

        ci_1 = Text("Principal amount = Rs.1000")
        ci_2 = Text("Rate of Interest = 10% p.a.")
        ci_3 = Text("Time = 2 years")

        ci_4 = Text("Year 0: Rs.1000")
        ci_5 = Text("Year 1: Rs.1000 + Rs.100 = Rs.1100")
        ci_6 = Text("Year 2: Rs.1100 + Rs.110 = Rs.1210")

        self.play(Write(ci_1))
        self.wait(1)
        ci_11 = ci_1.copy().move_to(1*UP).scale(0.5)
        self.play(ReplacementTransform(ci_1, ci_11))
        self.wait(1)

        self.play(Write(ci_2.move_to(DOWN)))
        self.wait(1)
        ci_22 = ci_2.copy().next_to(ci_1, DOWN).scale(0.5)
        self.play(ReplacementTransform(ci_2, ci_22))
        self.wait(1)

        self.play(Write(ci_3.move_to(DOWN)))
        self.wait(1)
        ci_33 = ci_3.copy().next_to(ci_2, DOWN).scale(0.5)
        self.play(ReplacementTransform(ci_3, ci_33))
        self.wait(1)

        group2 = VGroup(ci_11, ci_22, ci_33)
        grouped2 = Text("N = 2; P = Rs.1000; R = 10%").next_to(ci_n, 3*DOWN).scale(0.75)
        self.play(ReplacementTransform(group2, grouped2))

        self.play(Write(ci_4.scale(0.75)))
        self.wait(1)
        self.play(Write(ci_5.next_to(ci_4, DOWN).scale(0.75)))
        self.wait(1)
        self.play(Write(ci_6.next_to(ci_5, DOWN).scale(0.75)))
        self.wait(1)
        self.clear()
        self.wait(1)