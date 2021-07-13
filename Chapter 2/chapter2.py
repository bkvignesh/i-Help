from manim import *

class Initial(Scene):
        def construct(self):
                ihelp=ImageMobject("/home/daksh/Documents/i-Help/logo75.png", fill_opacity=0.5).scale(0.025).to_corner(RIGHT+UP)
                self.add(ihelp)
                intro = Tex("Chapter 2: Compound Interest")
                intro_1 = Tex("Class 8")        
                intro_1.next_to(intro, 1.5*DOWN)
                self.play(Write(intro))
                self.play(FadeIn(intro_1))
                self.wait(2)
                self.play(FadeOut(intro), FadeOut(intro_1))
                self.wait(1)

class SI(Scene):
        def construct(self):
                ihelp=ImageMobject("/home/daksh/Documents/i-Help/logo75.png", fill_opacity=0.5).scale(0.025).to_corner(RIGHT+UP)
                self.add(ihelp)

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

class CI(Scene):
        def construct(self):
                ihelp=ImageMobject("/home/daksh/Documents/i-Help/logo75.png", fill_opacity=0.5).scale(0.025).to_corner(RIGHT+UP)
                self.add(ihelp)

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

class Exp(Scene):
        def construct(self):
                ihelp=ImageMobject("/home/daksh/Documents/i-Help/logo75.png", fill_opacity=0.5).scale(0.025).to_corner(RIGHT+UP)
                self.add(ihelp)

                title = Tex("What just happened?").scale(1.3).set_color(color=[BLUE_A,BLUE_B])
                self.play(FadeIn(title))
                self.wait(2)
                self.clear()
                self.wait(0.2)
                defn = Tex("In year 2, the Interest was not only calculated on ", "Rs. 1000 ", "but also on the interest of year 1, that is ", "Rs. 100").scale(0.8)
                bundle1 = Circle(radius=1, color=YELLOW, fill_opacity=0.1)
                tbundle1 = Tex("Rs. 1000").set_color(BLACK).set_opacity(0.1)
                bundle2 = Circle(radius=0.5, color=RED_A, fill_opacity=0.1)
                tbundle2 = Tex("Rs. 100").set_color(BLACK).set_opacity(0.1).scale(0.6)
                gbundle1 = VGroup(bundle1, tbundle1)
                gbundle2 = VGroup(bundle2, tbundle2)
                gbundle1.move_to(2*DOWN,LEFT)
                gbundle2.move_to(2*DOWN,RIGHT)
                self.play(Write(defn).set_run_time(3))
                self.play(defn[1].animate.set_color(YELLOW_B), gbundle1.animate.set_opacity(0.9))
                self.play(defn[3].animate.set_color(RED_C), gbundle2.animate.set_opacity(0.9))
                self.wait(1)
                
                self.clear()

                title2 = Tex("Why do we use Compond Interest?").set_color(RED_C).move_to(0.5*UP)
                defn2 = Tex("To increase the profits of the lender").next_to(title2,1.5*DOWN)

                self.play(FadeIn(title2))
                self.wait(1)
                self.play(Write(defn2))
                grp1 = VGroup(title2, defn2)
                self.play(grp1.animate.scale(0.8).to_edge(UP))
                self.wait(0.5)
                exm = Tex("In our example, the lender made Rs. 10 more in profits").scale(0.8) 
                exm1 = Tex("from CI compared to SI").scale(0.8)
                exm2 = Tex("i.e. Rs 1210 - Rs. 1200 = Rs. 10").scale(0.8)

                self.play(Write(exm))
                exm1.next_to(exm, DOWN)
                self.play(Write(exm1))
                exm2.next_to(exm1, 1.5*DOWN)
                self.play(Write(exm2.set_color(BLUE_B)))
                self.wait(2)
                self.clear()

class Amount(Scene):
        def construct(self):
                ihelp=ImageMobject("/home/daksh/Documents/i-Help/logo75.png", fill_opacity=0.5).scale(0.025).to_corner(RIGHT+UP)
                self.add(ihelp)

                title3 = Tex("Amount").set_color(BLUE_B).scale(1.2).move_to(UP)
                self.wait(0.5)
                defn3 = Tex("The sum total of the principal and interest of a loan").next_to(title3, DOWN).scale(0.9)
                self.play(FadeIn(title3))
                self.play(Write(defn3))
                grp2 = VGroup(title3,defn3)
                self.play(grp2.animate.scale(0.8).to_edge(UP))
                self.wait(0.3)
                bundle1 = Circle(radius=1, color=YELLOW, fill_opacity=0.9)
                tbundle1 = Tex("Rs. 1000").set_color(BLACK)
                bundle2 = Circle(radius=0.5, color=RED_A, fill_opacity=0.9)
                tbundle2 = Tex("Rs. 100").set_color(BLACK).scale(0.6)
                gbundle1 = VGroup(bundle1, tbundle1)
                gbundle2 = VGroup(bundle2, tbundle2)
                
                bundle3 = Circle(radius=1.1, color=RED_A, fill_opacity=0.9)
                tbundle3 = Tex("Rs. 1100").set_color(BLACK)
                gbundle3 = VGroup(bundle3, tbundle3)
                gbundle1.move_to(2*RIGHT)
                gbundle2.to_edge(2*LEFT)
                self.play(gbundle1.animate.move_to(0), gbundle2.animate.move_to(0))
                self.play(gbundle2.animate.set_opacity(0), ReplacementTransform(gbundle1, gbundle3))
                self.wait(2)
                self.clear()
                title4 = Tex("How to calculate the amount for CI?").set_color(RED_B).to_edge(UP).scale(0.8)
                self.add(title4)
                self.wait(1)

                defn4 = MathTex(r'A = P({1 + \frac{r}{n}})^{nt}').move_to(1.5*UP).scale(1.2).set_color(BLUE_B)
                self.play(Write(defn4))
                self.wait(1)
                t1=Tex("Where,").move_to(DOWN,LEFT)
                t2=Tex("A is the amount (ending balance or future value);")
                t3=Tex("P is the initial principal balance (current balance or present value);").next_to(t2, 0.5*DOWN)
                t4=Tex("r is the interest rate;").next_to(t3, 0.5*DOWN)
                t5=Tex("n is the number of times interest in compounded per time period and").next_to(t4, 0.5*DOWN)
                t6=Tex("t is the number of time periods").next_to(t5, 0.5*DOWN)
                
                tgrp=VGroup(t1,t2,t3,t4,t5,t6)
                tgrp.scale(0.7)
                tgrp.arrange(0.6*DOWN, center=True, aligned_edge=RIGHT)
                tgrp.shift(2*DOWN, 2*RIGHT)
                
                
                self.play(FadeIn(tgrp))
                self.wait(5)

             

class Example(Scene):
        def construct(self):
                ihelp=ImageMobject("/home/daksh/Documents/i-Help/logo75.png", fill_opacity=0.5).scale(0.025).to_corner(RIGHT+UP)
                self.add(ihelp)

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
                self.wait(2)
                self.clear()

class VS(Scene):
        def construct(self):
                ihelp=ImageMobject("/home/daksh/Documents/i-Help/logo75.png", fill_opacity=0.5).scale(0.025).to_corner(RIGHT+UP)
                self.add(ihelp)

                title8 = Tex("SI ", "vs", " CI").to_edge(UP)
                title8[1].set_color(ORANGE)
                self.add(title8)

                bundle1 = Circle(radius=1, color=YELLOW, fill_opacity=0.9)
                tbundle1 = Tex("P").set_color(BLACK)
                tbundle11 = Tex("Principle").next_to(tbundle1, 4*DOWN).scale(0.6)
                gbundle1 = VGroup(bundle1, tbundle1, tbundle11).to_edge(LEFT)
                gbundle1.shift(1.5*UP)

                bundle2 = Circle(radius=0.5, color=RED_A, fill_opacity=0.9)
                tbundle2 = Tex("I").set_color(BLACK).scale(0.6)
                tbundle22 = Tex("Year 1").scale(0.6).next_to(tbundle2,3*DOWN)
                gbundle2 = VGroup(bundle2, tbundle2, tbundle22).next_to(gbundle1, 8.5*RIGHT)

                bundle3 = Circle(radius=0.5, color=RED_A, fill_opacity=0.9)
                tbundle3 = Tex("I").set_color(BLACK).scale(0.6)
                tbundle33 = Tex("Year 2").scale(0.6).next_to(tbundle3,3*DOWN)
                gbundle3 = VGroup(bundle3, tbundle3, tbundle33).next_to(gbundle2, 8.5*RIGHT )

                bundle4 = Circle(radius=0.5, color=RED_A, fill_opacity=0.9)
                tbundle4 = Tex("I").set_color(BLACK).scale(0.6)
                tbundle44 = Tex("Year 3").scale(0.6).next_to(tbundle4,3*DOWN)
                gbundle4 = VGroup(bundle4, tbundle4, tbundle44).next_to(gbundle3, 8.5*RIGHT)
                defn8 = Tex("SI ","- Interest is earned on the initial amount").move_to(2.5*UP).scale(0.65)
                defn8[0].set_color(BLUE_B)
                
                self.wait(0.5)
                self.play(Create(defn8))
                self.wait(1)
                self.play(GrowFromCenter(gbundle1))
                self.play(FadeIn(gbundle2))
                self.play(FadeIn(gbundle3))
                self.play(FadeIn(gbundle4))
                self.wait(2)
                
                defn9 = Tex("CI ","- Interest earned is added to the initial amount and then").scale(0.65).shift(0.5*DOWN)
                defn9[0].set_color(BLUE_B)
                defn10 = Tex("the interest on that amount is calculated for each subsequent year").scale(0.65).next_to(defn9, 0.6*DOWN)
                cbundle1 = Circle(radius=1, color=YELLOW, fill_opacity=0.9)
                ctbundle1 = Tex("P").set_color(BLACK)
                ctbundle11 = Tex("Principle").next_to(ctbundle1, 4*DOWN).scale(0.6)
                cgbundle1 = VGroup(cbundle1, ctbundle1, ctbundle11).to_edge(LEFT)
                cgbundle1.shift(2*DOWN)
                
                cbundle2 = Circle(radius=0.5, color=RED_A, fill_opacity=0.9)
                ctbundle2 = Tex("I").set_color(BLACK).scale(0.6)
                ctbundle22 = Tex("Year 1").scale(0.6).next_to(ctbundle2,3*DOWN)
                cgbundle2 = VGroup(cbundle2, ctbundle2, ctbundle22).next_to(cgbundle1, 8.5*RIGHT)

                cbundle3 = Circle(radius=0.6, color=RED_A, fill_opacity=0.9)
                ctbundle3 = Tex("I*").set_color(BLACK).scale(0.6)
                ctbundle33 = Tex("Year 2").scale(0.6).next_to(ctbundle3,3*DOWN)
                cgbundle3 = VGroup(cbundle3, ctbundle3, ctbundle33).next_to(cgbundle2, 8.2*RIGHT)

                cbundle4 = Circle(radius=0.7, color=RED_A, fill_opacity=0.9)
                ctbundle4 = Tex("I**").set_color(BLACK).scale(0.6)
                ctbundle44 = Tex("Year 3").scale(0.6).next_to(ctbundle4,3*DOWN)
                cgbundle4 = VGroup(cbundle4, ctbundle4, ctbundle44).next_to(cgbundle3, 7.8*RIGHT)

                

                self.play(Create(defn9))
                self.play(Create(defn10))
                self.wait(0.5)
                self.play(GrowFromCenter(cgbundle1))
                self.play(FadeIn(cgbundle2))
                
                self.play(FadeIn(cgbundle3))
                self.play(FadeIn(cgbundle4))
                self.wait(3)
                self.clear()

class thanks(Scene):
        def construct(self):
        
                ihelp=ImageMobject("/home/daksh/Documents/i-Help/logo75.png", fill_opacity=0.5).scale(0.025).to_corner(RIGHT+UP)

                thanks=Tex("Thank you").shift(8*DOWN)
                self.add(thanks)
                
                self.play(thanks.animate.move_to(2*UP), FadeIn(ihelp))
                self.wait(2)
                logo=ImageMobject('/home/daksh/Documents/i-Help/ihelp.png').scale(0.6).shift(0.6*DOWN)

                self.play(FadeIn(logo), run_time=1)
                self.wait(4)





