from re import L
from manim import *

class Initial(Scene):
    def construct(self):
        ihelp=ImageMobject("/mnt/f/i-Help-main/logo75.png").scale(0.025).to_corner(RIGHT+UP)
        self.add(ihelp)
        intro = Tex("Chapter 4: Direct and Inverse Proportion")
        intro_1= Tex("Class 8")
        intro_1.next_to(intro, 1.5*DOWN)
        self.play(Write(intro))
        self.play(FadeIn(intro_1))
        self.wait(2)
        self.play(FadeOut(intro), FadeOut(intro_1))
        self.wait(1)
    
class Ingred(Scene):
    def construct(self):
        title = Tex("Mohan prepares tea for himself and his sister.").scale(0.75).to_edge(UP).shift(1.5*DOWN)
        title1 = Tex("He uses:").scale(0.75).next_to(title,2*DOWN)
        one = ImageMobject("/mnt/f/i-Help-main/Chapter 4/ingred").scale(1.25).shift(1.5*DOWN)
        
        title2 = Tex("How much quantity of each item will he need, if he has to make tea for ", "four", " people?").to_edge(UP).shift(2*DOWN).scale(0.75)
        title2[1].set_color(ORANGE)
        two = ImageMobject("/mnt/f/i-Help-main/Chapter 4/ingred2").scale(1.25).shift(1.5*DOWN)


        self.add(one, title, title1)
        self.wait(3)
        self.play(FadeOut(title),FadeOut(title1),FadeIn(title2))
        self.wait(0.5)
        self.play(FadeOut(one),FadeIn(two))
        self.wait(2)

class Direct(Scene):
    def construct(self):
        title3 = Tex("Direct Proportion").set_color(BLUE_B)
        
        self.add(title3)
        self.wait(0.5)
        self.play(title3.animate.to_edge(UP).scale(0.8))
        title4 = Tex("In the previous example, Mohan will need double the quantity for 4 people!").shift(UP).scale(0.75)
        three = ImageMobject("/mnt/f/i-Help-main/Chapter 4/direct").scale(1.25).shift(1.5*DOWN)
        four = ImageMobject("/mnt/f/i-Help-main/Chapter 4/direct2").scale(1.25).shift(1.6*DOWN)
        t5 = Tex("Direct Proportion means the increase or decrease of two or more quantities in the same ratio").scale(0.75).shift(UP)
        self.wait(0.5)
        self.play(FadeIn(title4))

        self.wait(2)
        self.play(ReplacementTransform(title4, t5))
        self.play(FadeIn(three))
        self.wait(1)
        self.play(FadeOut(three),FadeIn(four))
        self.wait(3)

class Examples(Scene):
    def construct(self):
        t7 = Tex("Examples of quantities in direct proportion:")
        self.add(t7)
        self.wait(1)
        

        t8 = Tex("Radius and Area of a circle")
        self.play(FadeOut(t7),FadeIn(t8))
        self.play(t8.animate.to_edge(UP).scale(0.8))

        geo = Circle(radius=2).set_color(RED_A)

        self.wait(2)
        t8 = Text("Radius ∝ Area").to_edge(DOWN).scale(0.6).set_color(BLUE_A)
        self.play(GrowFromCenter(geo), run_time=3)  
        self.play(FadeIn(t8))      
        self.wait(2)
       
class Methods(Scene):
    def construct(self):
        t9 = Tex("Methods to solve:")
        self.add(t9)
        self.wait(0.5)
        self.play(t9.animate.to_edge(UP).scale(0.8))
        
        t10 = Tex("Method 1").next_to(t9, 2*DOWN).scale(0.75)
        self.play(FadeIn(t10))
        eqn = MathTex(r"\frac{x_1}{y_1} = \frac{x_2}{y_2} = \frac{x_3}{y_3}")
        self.play(Write(eqn))
        self.wait(0.5)

        t11 = Tex("Use the equation above to find all the unknown quantities").scale(0.65).shift(2*DOWN).set_color(RED_A)
        self.play(FadeIn(t11))

        self.wait(2)

class Method2(Scene):
    def construct(self):
        
        t9 = Tex("Methods to solve:").to_edge(UP).scale(0.8)
        

        t12 = Tex("Method 2").next_to(t9, 2*DOWN).scale(0.75)
        t13 = Tex("Cross Multiplication").next_to(t12,2*DOWN).scale(0.75).set_color(BLUE_A)

        self.play(FadeIn(t12))
        self.wait(0.5)
        self.play(Write(t13))
        self.wait(0.5)

        eqn2 = MathTex(r"\frac {x}{y} = k").shift(DOWN).set_color(BLUE_A)
      
        eqn3 = MathTex(r"x = {k}\times{y}").shift(DOWN).set_color(RED_A)

        

        self.play(FadeIn(eqn2))
        self.wait(1)
        self.play(ReplacementTransform(eqn2,eqn3))
        self.wait(1.5)

        eqn4 = MathTex(r"\frac {x_1}{y_1}").shift(1.25*LEFT+DOWN)
        eqn5 = MathTex(r"\frac {x_2}{y_2}").shift(1.25*RIGHT+DOWN)
        eqn6 =VGroup(eqn4,eqn5)
        dot1 = Dot(LEFT+0.5*DOWN)
        dot2 = Dot(RIGHT+1.5*DOWN)
        line1 = Arrow(dot2, dot1, buff=0).set_color_by_gradient(BLUE,RED)

        dot3 = Dot(LEFT+1.5*DOWN)
        dot4 = Dot(RIGHT+0.5*DOWN)
        line2 = Arrow(dot3, dot4, buff=0).set_color_by_gradient(BLUE,RED)

        self.play(ReplacementTransform(eqn3,eqn6))
        self.play(Create(line1))
        self.play(Create(line2))

        eqn7 = MathTex(r"{x_1} \times {y_2} = {x_2} \times {y_1}").shift(DOWN).set_color_by_gradient(BLUE_A,RED_A)

        
        eqn8 = VGroup(eqn6,line1,line2)
        self.wait(3)
        self.play(ReplacementTransform(eqn8,eqn7))
        self.wait(2)
        

class thanks(Scene):
        def construct(self):
        
                ihelp=ImageMobject("/mnt/f/i-Help-main/logo75.png").scale(0.025).to_corner(RIGHT+UP)

                thanks=Tex("Thank you").shift(8*DOWN)
                self.add(thanks)
                
                self.play(thanks.animate.move_to(2*UP), FadeIn(ihelp))
                self.wait(2)
                logo=ImageMobject('/mnt/f/i-Help-main/ihelp.png').scale(0.6).shift(0.6*DOWN)

                self.play(FadeIn(logo), run_time=1)
                self.wait(4)






        




