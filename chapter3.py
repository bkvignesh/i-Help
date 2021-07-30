from manim import *

class Initial(Scene):
    def construct(self):
        ihelp=ImageMobject("/mnt/f/i-Help-main/logo75.png").scale(0.025).to_corner(RIGHT+UP)
        self.add(ihelp)
        intro = Tex("Chapter 3: Graphs and Charts")
        intro_1 = Tex("Class 8")        
        intro_1.next_to(intro, 1.5*DOWN)
        self.play(Write(intro))
        self.play(FadeIn(intro_1))
        self.wait(2)
        self.play(FadeOut(intro), FadeOut(intro_1))
        self.wait(1)

class gc(Scene):
    def construct(self):
        title1 = Tex("Yash went to buy some fruits from the shop")
        title2 = Tex("He bought: Apple, Banana, Orange, Apple, Banana, Watermelon,")
        title3 = Tex("Orange, Orange, Watermelon, Apple, Orange, Watermelon")
        title1.move_to(3*UP)
        title2.set_color(RED_A)
        title3.next_to(title2, DOWN)
        title3.set_color(RED_A)

        self.play(FadeIn(title1))
        self.wait(0.5)
        self.play(Write(title2))
        self.play(Write(title3))

        self.wait(2)

class gc1(Scene):
    def construct(self):
        title4 = Tex("Isn’t this confusing if Yash wants to know his full shopping list?").scale(0.9)
        title4.move_to(3*UP)
        title5 = Tex("Here is a better way for Yash to know:").move_to(3*LEFT).scale(0.8).set_color(BLUE_A)
        self.play(FadeIn(title4))
        self.wait(2)
        self.play(Write(title5))
        

        chart = ImageMobject("/mnt/f/i-Help-main/Chapter 3/ch3f.png").scale(1.5).move_to(4*RIGHT).set_opacity(0.9)
        self.play(GrowFromCenter(chart))

        self.wait(4)

class bar(Scene):
    def construct(self):
        title6 = Tex("Bar Graph")
        self.play(title6.animate.to_edge(UP).scale(0.9))
        title7 = Tex("This is a Bar Graph:").scale(0.75).move_to(4*LEFT).set_color(GREEN_A)
        bar = ImageMobject("/mnt/f/i-Help-main/Chapter 3/bar.png").scale(0.8).move_to(DOWN, 2*LEFT)
        

        self.play(FadeIn(bar))
        self.play(Write(title7))
        self.wait(2)
        title8 = Tex("Now we know that he bought 3 apples, 2 bananas").scale(0.7).next_to(title7, DOWN)
        title81 = Tex("4 oranges, and 3 watermelons").scale(0.7).next_to(title8, DOWN)
        self.play(Write(title8))
        self.play(Write(title81))
    
        self.wait(3)

class hist(Scene):
    def construct(self):

        title9 = Tex("Histogram")
        self.play(title9.animate.to_edge(UP).scale(0.9))
        hist = ImageMobject("/mnt/f/i-Help-main/Chapter 3/hist.png").scale(0.8).move_to(DOWN, 2*LEFT)
        title10 = Tex("The same bar graph can be made in this way too").scale(0.65).move_to(3.5*LEFT).set_color(GREEN_A)
        title11 = Tex("and then it is called a histogram!").scale(0.65).next_to(title10, DOWN).set_color(GREEN_A)

        self.play(FadeIn(hist))
        self.wait(1)
        self.play(Write(title10))
        self.play(Write(title11))

        self.wait(3)

class line(Scene):
    def construct(self):

        title12 = Tex("Line Graph")
        self.play(title12.animate.to_edge(UP).scale(0.9))

        line = ImageMobject("/mnt/f/i-Help-main/Chapter 3/line.png").scale(0.8).move_to(DOWN, 2*LEFT)

        title13 = Tex("The same data can be expressed").scale(0.65).move_to(3.5*LEFT).set_color(GREEN_A)
        title131 = Tex("through a line graph like this:").scale(0.65).next_to(title13, DOWN).set_color(GREEN_A)

        self.play(FadeIn(line))
        self.wait(1)
        self.play(Write(title13))
        self.play(Write(title131))
        self.wait(3)

class pie(Scene):
    def construct(self):

        title14 = Tex("Pie Chart")
        self.play(title14.animate.to_edge(UP).scale(0.9))
        pie = ImageMobject("/mnt/f/i-Help-main/Chapter 3/pie.png").scale(0.8).move_to(0.5*DOWN, 3*LEFT)

        title14 = Tex("Now, what part or percentage of his list").scale(0.65).move_to(3*LEFT).set_color(GREEN_A)
        title141 = Tex("were apples?").scale(0.65).next_to(title14, DOWN).set_color(GREEN_A)
        self.play(Write(title14))
        self.play(Write(title141))

        self.wait(2)
        self.play(FadeIn(pie))
        self.wait(1)
        title15 = Tex("So we can now see that there were").scale(0.65).next_to(title141, 1.5*DOWN).set_color(BLUE_A)
        title151 = Tex("25 percent Apples in his list!").scale(0.65).next_to(title15, DOWN).set_color(BLUE_A)
        self.play(Write(title15))
        self.play(Write(title151))
        self.wait(3)

class lop(GraphScene):

   
    def construct(self):

        t1 = Text("X             G                R             J")
        t2 = Text("A             K                L             N")
        t3 = Text("V             Q                T             I")
        t4 = Text("O             Y                B             Y")
        t1.shift(2*UP)
        t2.next_to(t1, 3*DOWN)
        t3.next_to(t2, 3*DOWN)
        t4.next_to(t3, 3*DOWN)
        t = VGroup(t1,t2,t3,t4)

        self.play(FadeIn(t))
        self.wait(1) 

        title16 = Tex("Where is Ravi sitting?").to_edge(UP)
        self.play(Write(title16))
        self.wait(0.5)
        rect1 = Square(side_length=1, fill_opacity=0.1, color=YELLOW)
        rect1.shift(2*RIGHT, 2*UP)
        t5 = Tex("(2,3)").next_to(rect1, RIGHT).scale(0.9).set_color(BLUE_A)
        self.play(Create(rect1))
        self.wait(1)
        
        plane = NumberPlane(
            x_range=[-5, 5, 1], y_range=[-4, 4, 1], x_length=10, y_length=7
        )
        plane.add_coordinates()
        plane.shift(0.5*DOWN)
        plane.set_opacity(0.5)
        
        self.play(DrawBorderThenFill(plane), run_time=2)

        vect1 = Line(
            start=plane.coords_to_point(0, 0),
            end=plane.coords_to_point(2, 3),
            stroke_color=LIGHT_PINK,
        ).add_tip()

        vect2 = Line(
            start=plane.coords_to_point(0, 0),
            end=plane.coords_to_point(2, 0),
            stroke_color=ORANGE,
        )

        vect3 = Line(
            start=plane.coords_to_point(0, 0),
            end=plane.coords_to_point(0, 3),
            stroke_color=ORANGE,
        )

        vect1.set_opacity(0.8)
        
        v2 = Tex("2").next_to(vect2, DOWN)
        v3 = Tex("3").next_to(vect3, LEFT)
        v = VGroup(v2,v3).scale(0.8).set_color(ORANGE)
        self.play(
            GrowFromPoint(vect2, point=vect2.get_start()),FadeIn(v),GrowFromPoint(vect3, point=vect3.get_start()))
        self.wait(0.5)
        self.play(
            GrowFromPoint(vect1, point=vect1.get_start()))
        self.wait(0.5)
        self.play(FadeIn(t5))
        self.wait(2)

        total = VGroup(t,title16,rect1,t5,vect1,vect2,vect3,v)
        self.play(FadeOut(total))
        
        plane1 = NumberPlane(
            x_range=[-15, 15, 1], y_range=[-15, 15, 1], x_length=15, y_length=10
        )
        plane1.shift(0.5*DOWN)
        plane1.set_opacity(0.2)
        
        
        self.play(ReplacementTransform(plane,plane1), runtime=2)
        self.wait(2)

        title17 = Text("Coordinate Plane").to_edge(UP).scale(0.9)
        self.play(FadeIn(title17))
        title21 = Text("Quadrants").to_edge(UP).scale(0.9)
        title18 = Tex("The plane is made of two perpendicular lines called the x-axis and the y-axis.").scale(0.7).next_to(title17,2*DOWN)
        title19 = Tex("These axes are marked according to the required unit and").scale(0.7).next_to(title18,0.5*DOWN)
        title20 = Tex("it helps in locating any desired point by moving along both axes!").scale(0.7).next_to(title19,0.5*DOWN)
        
        self.play(FadeIn(title18))
        self.play(Write(title19))
        self.play(Write(title20))
        self.wait(3)
        self.play(FadeOut(title18,title19,title20))
        plane1.add_coordinates().set_opacity(0.8)
        self.play(plane1.animate.set_opacity(0.7))
        self.play(ReplacementTransform(title17,title21))

        self.wait(2)

        q1 = Text("I").shift(1.5*UP,3*RIGHT).set_color(ORANGE)
        q2 = Text("II").shift(1.5*UP,3*LEFT).set_color(ORANGE)
        q3 = Text("III").shift(2.5*DOWN,3*LEFT).set_color(ORANGE)
        q4 = Text("IV").shift(2.5*DOWN,3*RIGHT).set_color(ORANGE)
        self.play(FadeIn(q1))
        self.wait(0.3)
        self.play(FadeIn(q2))
        self.wait(0.3)
        self.play(FadeIn(q3))
        self.wait(0.3)
        self.play(FadeIn(q4))

        
        self.wait(4)

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










