from manim import *

class project(Scene):
    def construct(self):
        ihelp=ImageMobject("/home/daksh/Documents/i-Help/logo75.png", fill_opacity=0.5).scale(0.025).to_corner(RIGHT+UP)
        self.add(ihelp)
        intro = Tex("Chapter 1: Mensuration")
        intro_1 = Tex("Class 8")        
        intro_1.next_to(intro, 1.5*DOWN)
        self.play(Write(intro))
        self.play(FadeIn(intro_1))
        self.wait(2)
        self.play(FadeOut(intro), FadeOut(intro_1))
        self.wait(1)

class basic(Scene):
    def construct(self):
        ihelp=ImageMobject("/home/daksh/Documents/i-Help/logo75.png", fill_opacity=0.5).scale(0.025).to_corner(RIGHT+UP)
        self.add(ihelp)

        title = Tex("Basic Math Operations")
        title.set_color(color=["#aec6cf",WHITE])
        self.play(Write(title))
        self.wait(1.5)
        
        title_n = title.copy().move_to(3.1*UP).scale(0.75)
        self.play(Transform(title, title_n))
        self.wait(1)

        add = Tex("Addition").scale(1.4)
        sub = Tex("Subtraction").scale(1.4)
        mul = Tex("Multiplication").scale(1.4)
        div = Tex("Division").scale(1.4)

        add_a = add.copy().scale(0.8)
        add_b = MathTex("+", color = ORANGE).scale(1.25).next_to(add_a, RIGHT)
        
        self.play(Write(add))
        self.play(ReplacementTransform(add, add_a), Create(add_b), runtime=(1.5))
        self.wait(0.5)
        add_g=VGroup(add_a,add_b)
        self.play(add_g.animate.scale(0.8).move_to(2.5*LEFT+1.5*UP))
        self.wait(0.5)

        sub_a = sub.copy().scale(0.8)
        sub_b = MathTex("-", color = ORANGE).scale(1.25).next_to(sub_a, RIGHT)
        
        self.play(Write(sub))
        self.play(ReplacementTransform(sub, sub_a), Create(sub_b), runtime=(1.5))
        self.wait(0.5)
        sub_g=VGroup(sub_a,sub_b)
        self.play(sub_g.animate.scale(0.8).move_to(2.5*RIGHT+1.5*UP))
        self.wait(0.5)

        mul_a = mul.copy().scale(0.8)
        mul_b = Tex("x", color = ORANGE).scale(1.25).next_to(mul_a, RIGHT)
        
        self.play(Write(mul))
        self.play(ReplacementTransform(mul, mul_a), Create(mul_b), runtime=(1.5))
        self.wait(0.5)
        mul_g=VGroup(mul_a,mul_b)
        self.play(mul_g.animate.scale(0.8).move_to(2.5*RIGHT+DOWN))
        self.wait(0.5)

        div_a = div.copy().scale(0.8)
        div_b = Tex("/", color = ORANGE).scale(1.25).next_to(div_a, RIGHT)
        
        self.play(Write(div))
        self.play(ReplacementTransform(div, div_a), Create(div_b), runtime=(1.5))
        self.wait(0.5)
        div_g=VGroup(div_a,div_b)
        self.play(div_g.animate.scale(0.8).move_to(2.5*LEFT+DOWN))
        self.wait(2)

        solve=Tex("How can we apply these to solve real life problems?").scale(0.8).set_color(color=["#aec6cf",WHITE])
        basics=VGroup(add_g,sub_g,mul_g,div_g)
        solve_a=Tex("You can use them to measure things like ", "Area"," and ", "Perimeter", "!").scale(0.8)
        solve_a[1].set_color(color=[ORANGE,RED])
        solve_a[3].set_color(color=[BLUE,GREEN])
        solve_a.next_to(solve, 1.2*DOWN)
        self.play(ReplacementTransform(basics,solve), FadeOut(title))
        self.wait(3)
        
        self.play(solve.animate.move_to(0.5*UP),Write(solve_a))
        self.wait(3)

        self.play(FadeOut(solve),FadeOut(solve_a))
        self.wait(0.5)

class twod(MovingCameraScene):
    def construct(self):
        ihelp=ImageMobject("/home/daksh/Documents/i-Help/logo75.png", fill_opacity=0.5).scale(0.025).to_corner(RIGHT+UP)
        self.add(ihelp)

        twod = Tex("2 Dimensions (2D)").move_to(0.5*UP)

        des = Tex("Shapes that have only length and breadth and exist in one plane").scale(0.7).set_color(BLUE)
        des.next_to(twod, DOWN)
        c = Circle(color=RED, fill_opacity=0.5).move_to(3*LEFT+3*UP)
        s = Square(color=BLUE, fill_opacity=0.5).move_to(3*RIGHT+3*UP)
        t = Polygon(1*UP, 1*DOWN+1*LEFT, 1*DOWN+1*RIGHT, 1*UP, color=YELLOW, fill_opacity=0.5).move_to(3*LEFT+3*DOWN)
        r = Rectangle(height=1.2, breadth=1.4,color=ORANGE, fill_opacity=0.5).move_to(3*RIGHT+3*DOWN)
        pen = Polygon(2*UP, RIGHT+UP, RIGHT+0.5*DOWN, LEFT+0.5*DOWN, LEFT+UP, color=PURPLE, fill_opacity=0.5).move_to(7*RIGHT)
        p = Polygon(LEFT+UP, 2*RIGHT+UP, RIGHT+DOWN, 2*LEFT+DOWN, LEFT+UP, color=GREEN_B, fill_opacity=0.5).move_to(7*LEFT)

        tr = Tex("Triangle").scale(0.5)
        tr.add_updater(lambda m:m.move_to(t.get_center()))
        ci = Tex("Circle").scale(0.5)
        ci.add_updater(lambda m:m.move_to(c.get_center()))
        sq = Tex("Square").scale(0.5)
        sq.add_updater(lambda m:m.move_to(s.get_center()))
        re = Tex("Rectangle").scale(0.5)
        re.add_updater(lambda m:m.move_to(r.get_center()))
        pa = Tex("Parallelogram").scale(0.5)
        pa.add_updater(lambda m:m.move_to(p.get_center()))
        pe = Tex("Pentagon").scale(0.5)
        pe.add_updater(lambda m:m.move_to(pen.get_center()))

    
        self.play(Create(twod))
        self.wait(1)
        self.add(c)
        self.play(self.camera.frame.animate.move_to(c).set(width=c.width*2))
        self.add(s)
        self.wait(0.3)
        self.play(self.camera.frame.animate.move_to(s).set(width=s.width*2))
        self.add(pen)
        self.wait(0.3)
        self.play(self.camera.frame.animate.move_to(pen).set(width=pen.width*2.5))
        self.add(r)
        self.wait(0.3)
        self.play(self.camera.frame.animate.move_to(r).set(width=r.width*1.5))
        self.add(t)
        self.wait(0.3)
        self.play(self.camera.frame.animate.move_to(t).set(width=t.width*2))
        self.add(p)
        self.wait(0.3)
        self.play(self.camera.frame.animate.move_to(p).set(width=p.width*1.5))
        self.wait(0.3)

        self.play(self.camera.frame.animate.move_to(ORIGIN).set(width=18), FadeIn(des), FadeOut(ihelp))
        self.wait(5)
        
        names=VGroup(tr,ci,sq,re,pe,pa)
        self.play(FadeIn(names))

        self.wait(2)

        how = Tex("How do we check if a given shape is 2D?").scale(0.85)
        check = Tex("They can be drawn on a piece of paper!", color=GOLD).scale(1.2)
        check.next_to(how, 1.25*DOWN)

        self.play(FadeOut(des))
        self.play(ReplacementTransform(twod, how))
        self.wait(2)
        self.play(Write(check))
        self.wait(2)
        self.play(FadeOut(names,c,s,pen,r,t,p,how,check))
        self.wait(0.5)
        

class area(Scene):
    def construct(self):
        ihelp=ImageMobject("/home/daksh/Documents/i-Help/logo75.png", fill_opacity=0.5).scale(0.025).to_corner(RIGHT+UP)
        self.play(FadeIn(ihelp))
        title_1=Tex("Area").scale(1.1)
        title_2=Tex("Area").scale(0.9).to_edge(UP).shift(0.2*DOWN)
        desc=Tex("The measure of a surface or a region. It is the amount of space inside a shape.").scale(0.7).set_color_by_gradient(BLUE, WHITE)
        desc.next_to(title_2,1.5*DOWN)
        self.play(Write(title_1))
        self.wait(2)
        self.play(ReplacementTransform(title_1,title_2))
        self.wait(2)
        self.play(Write(desc))
        self.wait(2)

        s = Square(side_length=3, fill_opacity=0.75, color=BLUE, stroke_width=0.7)
        dot = Dot([-1.5, -1.5, 0])
        dot2 = Dot([1.5, -1.5, 0], color=ORANGE)
        line = Line(dot.get_center(), dot2.get_center(), stroke_width=7).set_color(ORANGE)

        dot3=Dot([-1.5,-1.5,0], color=ORANGE)
        dot4=Dot([-1.5,1.5,0], color=ORANGE)
        line2 = Line(dot3.get_center(), dot4.get_center(), stroke_width=7).set_color(ORANGE)

        

        ##line1=Polygon(1.5*UP,1.5*DOWN, stroke_width=10, color="#fdfd96").to_edge(LEFT)
        ##line2=Polygon(1.5*RIGHT,1.5*LEFT, stroke_width=10, color="#fdfd96").next_to(line1,0.001*DOWN).to_edge(LEFT)
        area=Tex("How do we calculate the area?").move_to(2*RIGHT).scale(0.8)
        self.play(GrowFromCenter(s))
        
        ##self.add(dot,dot2,line,dot3,dot4,dot5,dot6,dot7,dot8,line2,line3,line4,line)
        sgroup=VGroup(dot,dot2,line,dot3,dot4,line2,line)
        self.play(s.animate.to_edge(LEFT))

        self.play(s.animate.set_color(color=[BLUE,GREEN]))
        scopy=s.copy()
        self.play(ReplacementTransform(scopy,area), run_time=1.5)
        
        self.wait(3)


        area_formula=Tex("Area =", "Length x Breadth")
        area_formula[0].set_color("#ff6961")
        area_formula[1].set_color("#FAC898").scale(0.8)
        
        #area_formula2=Tex("Length x Breadth ", color=)
        #area_formula2.next_to(area_formula1,0.5*RIGHT)
        #area_group=VGroup(area_formula1, area_formula2)
        #area_group.next_to(area, 2*DOWN)
        area_formula.next_to(area, 2*DOWN)
        sgroup1=sgroup.to_edge(LEFT).shift(0.1*LEFT)
        self.play(Write(area_formula), FadeIn(sgroup1), run_time=2)
        self.wait(2)
        all_group=VGroup(area_formula,sgroup,s,title_2,desc,area)
        self.play(all_group.animate.shift(20*LEFT), run_time=1.5)
        
class perimeter(Scene):
    def construct(self):
        ihelp=ImageMobject("/home/daksh/Documents/i-Help/logo75.png", fill_opacity=0.5).scale(0.025).to_corner(RIGHT+UP)
        self.add(ihelp)

        s = Square(side_length=3, fill_opacity=0.75, stroke_width=0.7).to_edge(LEFT).set_color(color=[BLUE,GREEN])
        now=Tex("Now that we know what Area is, what is the ", "Perimeter", " ?").scale(0.9).set_color(color=["#aec6cf",WHITE])
        self.wait(0.5)
        self.play(GrowFromCenter(now))
        self.wait(3)
        self.play(FadeOut(now[0]),FadeOut(now[2]))
        

        
        title_1=Tex("Perimeter").scale(1.1)
        title_2=Tex("Perimeter").scale(0.9).move_to(3.2*UP)
        desc=Tex("The length of the boundary of any shape or region").scale(0.7).set_color_by_gradient(BLUE, WHITE)
        desc.next_to(title_2,1.5*DOWN)
        sq_peri=Polygon(1.5*UP,1.5*DOWN,3*RIGHT+1.5*DOWN,3*RIGHT+1.5*UP, stroke_width=10).to_edge(RIGHT).set_color(YELLOW_D)

        self.play(ReplacementTransform(now[1],title_1))
        self.wait(1)
        self.play(ReplacementTransform(title_1,title_2), FadeIn(s))
        self.wait(1)
        self.play(Write(desc),s.animate.to_edge(RIGHT).set_color(color=[BLUE_A,BLUE]), run_time=1)

        self.wait(1)
        self.play(FadeOut(title_2,desc))
        self.wait(0.3)

        title_3=Tex("How do we calculate the perimeter?").scale(0.9).set_color(YELLOW_A).move_to(0.6*LEFT)
        title_4=Tex("Perimeter = Sum of all sides").next_to(title_3, 1.5*DOWN).scale(1.2).set_color(color=[ORANGE,YELLOW_B])

        self.play(Write(title_3), Create(sq_peri))
        self.wait(2)
        ##peri_line=Polygon(3*LEFT,3*RIGHT,set_color=YELLOW,stroke_width=6).next_to(title_4, DOWN)
        
        dot=Dot([-3.6,-2.2,0])
        dot1=Dot([2.4,-2.2,0])
        peri_line=Line(dot.get_center(), dot1.get_center()).set_color(YELLOW_D)
        peri=VGroup(peri_line,dot,dot1)
        self.play(title_3.animate.shift(0.5*UP),Write(title_4), ReplacementTransform(sq_peri,peri), run_time=2)
        self.wait(4)
        self.play(FadeOut(title_3), FadeOut(title_4), FadeOut(peri), FadeOut(s))
        self.wait(2)

class example(Scene):
    def construct(self):
        ihelp=ImageMobject("/home/daksh/Documents/i-Help/logo75.png", fill_opacity=0.5).scale(0.025).to_corner(RIGHT+UP)
        self.add(ihelp)

        title_5=Tex("Let's take an example!")
        self.play(Write(title_5))
        self.wait(1)
        self.play(title_5.animate.shift(5*UP).scale(0.9))
        rect=Rectangle(height=3, breadth=5, fill_opacity=0.75, stroke_width=0.7).set_color(color=[BLUE, BLUE_A])
    
        self.play(GrowFromCenter(rect))
        title_6=Tex("Given a rectangle").to_edge(UP).shift(0.2*DOWN)
        self.play(Write(title_6))

        dot3=Dot([-2,-1.5,0])
        dot4=Dot([2,-1.5,0])
        line2 = Line(dot3.get_center(), dot4.get_center()).set_color(ORANGE)
        b3 = Brace(line2)
        b3text = b3.get_text("Length ","= ", "5m").scale(0.9)
        b3text1 = b3.get_text("5m").scale(0.9)
        self.add(line2,dot3,dot4)
        self.play(FadeIn(b3,b3text))

        self.wait(0.5)

        dot = Dot([-2, -1.5, 0])
        dot2 = Dot([-2, 1.5, 0])
        line = Line(dot.get_center(), dot2.get_center()).set_color(ORANGE)
        b2 = Brace(line, direction=line.copy().rotate(PI/2).get_unit_vector())
        b2text = b2.get_text("Breadth ", "= ", "3m").scale(0.9)
        self.add(line,dot,dot2)
        self.play(FadeIn(b2, b2text))

        rectangle=VGroup(rect,line,dot,dot2,b2,b2text,line2,dot3,dot4,b3,b3text)


        self.play(rectangle.animate.shift(1.5*LEFT,2*UP).scale(0.85),FadeOut(title_6))
        self.wait(1.5)

        title_7=Tex("To find the area of the given rectangle").set_color(BLUE_B).scale(0.7).to_corner(UP+RIGHT)
        title_7_1=title_7.shift(1*DOWN)
        title_8=Tex("Area = 3 x 5 = 15 sq metres").next_to(title_7, 1.5*DOWN).set_color(color=[YELLOW_B])

        self.play(Write(title_7_1))
        self.wait(1)
        self.play(Write(title_8))
        self.wait(2)

        rect_area=VGroup(title_7,title_8)
        self.play(FadeOut(rect_area))

        self.wait(1)
        
        self.play(rectangle.animate.to_edge(RIGHT), FadeOut(ihelp))
        self.wait(0.5)
        self.play(FadeOut(b2text[0],b2text[1],b3text[0],b3text[1]))
        self.play(b3text[2].animate.shift(0.9*LEFT))
        self.wait(0.5)
        title_9=Tex("Now to find the perimeter of the rectangle").set_color(BLUE_B).scale(0.7).to_corner(UP+LEFT).shift(1*DOWN,RIGHT)
        title_10=Tex("Perimeter ", "= ", "3 + 5 + 3 + 5").next_to(title_9, 1.5*DOWN).set_color(color=[YELLOW_B])
        title_11=Tex("Perimeter ", "= ", "16 metres").next_to(title_9, 1.5*DOWN).set_color(color=[YELLOW_B])

        self.play(Write(title_9))
        self.wait(1)
        self.play(Write(title_10))
        self.wait(0.5)
        self.play(ReplacementTransform(title_10,title_11))
        self.wait(2)

        out=VGroup(title_9,title_11,rect,line,dot,dot2,b2,b2text[2],line2,dot3,dot4,b3,b3text[2])
        self.play(out.animate.shift(5*UP))
        self.wait(1)
        

class optional(Scene):
    def construct(self):
        ihelp=ImageMobject("/home/daksh/Documents/i-Help/logo75.png", fill_opacity=0.5).scale(0.025).to_corner(RIGHT+UP)
        self.play(FadeIn(ihelp))

        rect=Rectangle(height=3, breadth=5, fill_opacity=0.75, stroke_width=0.7)
        texture="/home/daksh/Documents/i-Help/grass.jpg"

        grass=ImageMobject(texture)

        grassbg=grass.set_opacity(0.3).scale(5)
        title=Tex("Real life applications").shift(15*DOWN)
        self.add(title)
        self.play((title.animate.move_to(0)))
        self.wait(1)
        self.play(FadeOut(title))

        title_1=Tex("You own a field of length 10m and breadth 15m")
        self.play(Write(title_1),FadeIn(grassbg))
        self.wait(1)
        self.play(title_1.animate.shift(2*DOWN).scale(0.8), grassbg.animate.scale(0.15).set_opacity(0.9).shift(1.5*UP), run_time=2)
        
        title_4=Tex("15m").next_to(grassbg, 0.6*DOWN)
        title_5=Tex("10m").next_to(grassbg, 0.6*LEFT)
        grass_g=VGroup(title_4,title_5)
        self.play(FadeIn(title_4,title_5))
        ##self.play(grassbg.animate.scale(0.15).set_opacity(0.9).shift(1.5*UP), run_time=1.5)
        self.wait(1.5)

        title_3=Tex("How will you calculate the size of the grass bed").shift(2*DOWN).scale(0.74).set_color(color=([GREEN_A]))
        title_3_1=Tex("required to cover your garden?").scale(0.74).set_color(color=([GREEN_A])).next_to(title_3,0.5*DOWN)
        title_3g=VGroup(title_3,title_3_1)
        self.play(ReplacementTransform(title_1,title_3g))
        self.wait(2)

        title_6=Tex("We find the area of the garden").set_color(YELLOW).next_to(title_3,0.1*DOWN)
        self.play(grassbg.animate.to_corner(RIGHT+UP).rotate(PI/2).scale(0.8), title_3g.animate.shift(3.6*UP).to_edge(LEFT), Write(title_6), FadeOut(grass_g), FadeOut(ihelp))
        title_8=Tex("10m").next_to(grassbg, 0.6*DOWN).scale(0.8)
        title_9=Tex("15m").next_to(grassbg, 0.5*RIGHT).scale(0.8)
        self.play(FadeIn(title_8,title_9))
        self.wait(1.5)
        title_7=Tex("10 x 15 = 150 sq meters !").next_to(title_6,1.4*DOWN).set_color(RED_B)
        self.play(Write(title_7))
        self.wait(2)

        self.play(title_3g.animate.shift(20*LEFT),title_6.animate.shift(20*LEFT),title_7.animate.shift(20*LEFT))
        self.wait(0.5)
        title_10=Tex("Now you have to calculate the length of fence").shift(2*DOWN).scale(0.74).set_color(color=([GREEN_A]))
        title_11=Tex("required to protect your garden").scale(0.74).set_color(color=([GREEN_A])).next_to(title_10,0.5*DOWN)
        title_11g=VGroup(title_10,title_11)
        self.wait(2)
        title_12=Tex("We find the perimeter of the garden").set_color(YELLOW).next_to(title_10,0.1*DOWN)
        self.play(Write(title_11g))
        self.wait(1)
        self.play(title_11g.animate.shift(3.6*UP).to_edge(LEFT), Write(title_12))
        self.wait(1)
        title_13=Tex("10 + 15 + 10 + 15 = 50 meters !").next_to(title_12,1.4*DOWN).set_color(RED_B)
        self.play(Write(title_13))
        self.wait(2)
        self.play(title_11g.animate.shift(12*UP), title_12.animate.shift(12*UP), title_13.animate.shift(20*UP), grassbg.animate.shift(8*RIGHT), title_8.animate.shift(8*RIGHT), title_9.animate.shift(8*RIGHT))
        self.wait(1)

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
