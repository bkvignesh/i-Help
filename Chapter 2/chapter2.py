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

# class Example(Scene):
#     def construct(self):
        example = Tex("Example")
        example.set_color(color=["#aec6cf",WHITE])
        self.play(Write(example))
        self.wait(1.5)

        example_n = example.copy().move_to(3.0*UP).scale(0.75)
        self.play(Transform(example, example_n))
        self.wait(1)

        Q = Text("Find CI on Rs.16,000 at 20% per annum for 9 months, compounded quarterly.")
        P = Text("Rs.16000")
        N = Text("9 months = 3 quarters")
        R = Text("20% p.a. = 5% per quarter")

        self.play(Write(Q.next_to(example_n, DOWN).scale(0.5)))
        self.wait(1)

        self.play(Write(P))
        P_1 = P.copy().move_to(4.0*LEFT+1*UP).scale(0.5).set_color(GOLD)
        self.wait(0.5)
        self.play(ReplacementTransform(P, P_1))
        self.wait(0.5)
        self.play(Write(N))
        N_1 = N.copy().move_to(LEFT+1*UP).scale(0.5).set_color(GOLD)
        self.wait(0.5)
        self.play(ReplacementTransform(N, N_1))
        self.wait(0.5)
        self.play(Write(R))
        R_1 = R.copy().move_to(3.5*RIGHT+1*UP).scale(0.5).set_color(GOLD)
        self.wait(0.5)
        self.play(ReplacementTransform(R, R_1))
        self.wait(0.5)

        ans1 = Tex(r"$A = P * {(1 + r/n)}^{n * t}$")
        ans11 = ans1.copy().set_color(LIGHT_PINK).scale(0.75)
        self.play(Write(ans1))
        self.wait(0.5)
        self.play(ReplacementTransform(ans1, ans11))
        self.wait(1)
        ans2 = Tex(r"$A = Rs.16000 * {(1 + {(5/100)})}^{3} = Rs.18522$")
        ans22 = ans2.copy().set_color(LIGHT_PINK).next_to(ans11, DOWN).scale(0.75)
        self.play(Write(ans2.next_to(ans1, DOWN)))
        self.wait(0.5)
        self.play(ReplacementTransform(ans2, ans22))
        self.wait(1)
        ans3 = Tex("CI = Amount - Principal")
        ans33 = ans3.copy().set_color(LIGHT_PINK).next_to(ans22, DOWN).scale(0.75)
        self.play(Write(ans3.next_to(ans2, DOWN)))
        self.wait(0.5)
        self.play(ReplacementTransform(ans3, ans33))
        self.wait(1)
        ans4 = Tex("CI = Rs.18522 - Rs.16000 = Rs.2522")
        ans44 = ans4.copy().set_color(LIGHT_PINK).next_to(ans33, DOWN).scale(0.75)
        self.play(Write(ans4.next_to(ans3, DOWN)))
        self.wait(0.5)
        self.play(ReplacementTransform(ans4, ans44))
        self.wait(1)
        