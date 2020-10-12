from manimlib.imports import *

class final(Scene):
    def construct(self):

# class intro(Scene):
#     def construct(self):

        intro_text1 = TextMobject("The following is a sample module made entirely")
        intro_text2 = TextMobject("with")
        intro_text3 = TextMobject("Python and Manim", color=GOLD).scale(2)
        intro_text1.next_to(intro_text2, UP)
        intro_text3.next_to(intro_text2, DOWN)

        self.play(Write(intro_text1))
        self.play(Write(intro_text2))
        self.play(Write(intro_text3))
        self.wait(2)
        self.play(Uncreate(intro_text1), Uncreate(intro_text2), Uncreate(intro_text3))
        self.wait(1)
        
# class mod11(Scene):
#     def construct(self):
        
        mod1_intro = TextMobject("Class 4: Multiplication").scale(1.5)    
    
        mod11_intro = TextMobject("First we'll try to relate Multiplication with Addition")
        mod11 = TextMobject("2 x 3 = 3 + 3 = 6")
        mod11_edge = mod11.to_edge(UP)
        face_holder11 = TextMobject("3 + 3 = 6").scale(2)
        face_holder11.move_to(UP)
        circle11 = Circle(fill_color = YELLOW, fill_opacity = 1, color = YELLOW, radius=0.5)
        circle12 = Circle(fill_color = YELLOW, fill_opacity = 1, color = YELLOW, radius=0.5)
        circle12.next_to(circle11, DOWN)
        circle13 = Circle(fill_color = YELLOW, fill_opacity = 1, color = YELLOW, radius=0.5)
        circle13.next_to(circle12, DOWN)
        circle_group11 = Mobject.add(circle11, circle12, circle13)
        circle_group11.next_to(face_holder11, DOWN)
        circle_group12 = circle_group11.copy().next_to(circle_group11, 4*LEFT)
        circle_group13 = circle_group12.copy().next_to(circle_group11, 4*RIGHT)
        circle_group14 = circle_group12.copy().next_to(circle_group13, RIGHT)
   
        self.play(Write(mod1_intro))
        self.wait(2)
        self.play(ReplacementTransform(mod1_intro, mod11_intro))
        self.wait(2)   
        self.play(ReplacementTransform(mod11_intro, mod11))
        self.wait(1)
        self.play(ReplacementTransform(mod11, mod11_edge))
        self.wait(1)
        self.play(ShowCreation(face_holder11))
        self.wait(1)
        self.play(FadeIn(circle_group11), FadeIn(circle_group12))
        self.wait(2)
        self.play(Transform(circle_group11, circle_group13), Transform(circle_group12, circle_group14), run_time=2)
        self.wait(3)
        self.play(Uncreate(circle_group11), Uncreate(circle_group12), Uncreate(face_holder11), Uncreate(mod11))
        self.wait(2)

# class mod12(Scene):

#     def construct(self):    

        mod12_intro = TextMobject("Another Example").scale(1.5)
        mod12 = TextMobject("3 x 6 = 6 + 6 + 6 = 18")
        mod12_edge = mod12.to_edge(UP)
        face_holder12 = TextMobject("6 + 6 + 6 = 18").scale(2)
        face_holder12.move_to(1.5*UP)
        circle21 = Circle(fill_color = ORANGE, fill_opacity = 1, color = ORANGE, radius=0.25)
        circle22 = Circle(fill_color = ORANGE, fill_opacity = 1, color = ORANGE, radius=0.25).next_to(circle21, DOWN)
        circle23 = Circle(fill_color = ORANGE, fill_opacity = 1, color = ORANGE, radius=0.25).next_to(circle22, DOWN)
        circle24 = Circle(fill_color = ORANGE, fill_opacity = 1, color = ORANGE, radius=0.25).next_to(circle23, DOWN)
        circle25 = Circle(fill_color = ORANGE, fill_opacity = 1, color = ORANGE, radius=0.25).next_to(circle24, DOWN)
        circle26 = Circle(fill_color = ORANGE, fill_opacity = 1, color = ORANGE, radius=0.25).next_to(circle25, DOWN)
        circle_group21 = Mobject.add(circle21, circle22, circle23, circle24, circle25, circle26)
        circle_group21.next_to(face_holder12, DOWN).align_to(face_holder12, LEFT)
        circle_group22 = circle_group21.copy().next_to(circle_group21, 6*RIGHT)
        circle_group23 = circle_group21.copy().next_to(circle_group21, 14*RIGHT)
        circle_group24 = circle_group21.copy().next_to(face_holder12, DOWN).align_to(face_holder12, RIGHT)
        circle_group25 = circle_group21.copy().next_to(circle_group24, RIGHT)
        circle_group26 = circle_group21.copy().next_to(circle_group25, RIGHT)
        
        self.play(Write(mod12_intro))
        self.wait(2)
        self.play(Uncreate(mod12_intro))
        self.play(Write(mod12_edge)) 
        self.wait(2)
        self.play(ShowCreation(face_holder12))
        self.wait(2)
        self.play(ShowCreation(circle_group21), ShowCreation(circle_group22), ShowCreation(circle_group23))
        self.wait(2)
        self.play(Transform(circle_group23, circle_group24), Transform(circle_group22, circle_group25), Transform(circle_group21, circle_group26))
        self.wait(2)
        self.play(Uncreate(circle_group23), Uncreate(circle_group22), Uncreate(circle_group21), FadeOut(face_holder12), FadeOut(mod12_edge))
        self.wait(2)

# class table(Scene):
#     def construct(self):
        table_introtext = TextMobject("Let us take a look at the Multiplication Table now!")
        top_text = TextMobject("Multiplication Table")
        table = ImageMobject("table.jpg").scale(3.2)

        self.play(Write(table_introtext))
        self.wait(1)
        self.play(Uncreate(table_introtext))
        self.wait(1)
        self.play(Write(top_text.to_edge(UP)))
        self.wait(1)
        self.play(FadeIn(table.next_to(top_text, DOWN)))
        self.wait(2)
        self.clear()

# class mod21(Scene):

#     def construct(self):        

        mod21_intro1 = TextMobject("Associative property of Multiplication")
        mod21 = TextMobject("2 x 4 = 4 x 2")
        mod21_main = TextMobject("2 x 4 = 4 x 2")
        circle31 = Circle(fill_color = PURPLE, fill_opacity = 1, color = PURPLE, radius=0.35)
        circle32 = Circle(fill_color = PURPLE, fill_opacity = 1, color = PURPLE, radius=0.35).next_to(circle31, DOWN)
        circle33 = Circle(fill_color = PURPLE, fill_opacity = 1, color = PURPLE, radius=0.35).next_to(circle32, DOWN)
        circle34 = Circle(fill_color = PURPLE, fill_opacity = 1, color = PURPLE, radius=0.35).next_to(circle33, DOWN)
        circle_group31 = Mobject.add(circle31, circle32, circle33, circle34).next_to(mod21_main, LEFT+0.05*DOWN)
        circle_group32 = circle_group31.copy().next_to(circle_group31, RIGHT)
        circle_group_initital = Mobject.add(circle_group31, circle_group32)
        circle_group_final = circle_group_initital.copy().rotate(PI/2).next_to(circle_group_initital, 3*RIGHT)
        end = TextMobject("End of Module")
        more = TextMobject("But wait, there's more!")

        self.play(Write(mod21_intro1), run_time=2)
        self.wait(2)
        self.play(FadeOut(mod21_intro1), run_time=1)
        self.wait(1)
        self.play(FadeInFromDown(mod21.to_edge(UP)))
        self.wait(1)
        self.play(FadeInFromDown(mod21_main.scale(1.5).move_to(UP)))
        self.wait(1)
        self.play(Write(circle_group_initital), run_time=2)
        self.wait(1)
        self.play(Rotate(circle_group_initital, PI/2, axis=OUT))
        self.wait(2)
        self.play(ReplacementTransform(circle_group_initital, circle_group_final), run_time=2)
        self.wait(2)
        self.clear()
        self.play(Write(end))
        self.wait(1)
        self.play(ReplacementTransform(end, more))
        self.wait(1)
        self.clear()

        Graphs = TextMobject("We have Graphs")
        self.play(FadeIn(Graphs))
        self.wait(1)
        self.clear()


class Graph(GraphScene):
    CONFIG = {"x_min": -5,
              "x_max": 5,
              "y_min": -5,
              "y_max": 5,
              "graph_origin": ORIGIN,
              "function_color": WHITE,
              "axes_color": BLUE}

    def construct(self):
        self.setup_axes(animate=True)
        func_graph = self.get_graph(self.func_to_graph, self.function_color)
        graph_lab = self.get_graph_label(func_graph, label = "x^{2}")

        func_graph_2 = self.get_graph(self.func_to_graph_2, self.function_color)
        graph_lab_2 = self.get_graph_label(func_graph_2, label = "x^{3}")

        vert_line = self.get_vertical_line_to_graph(1,func_graph,color=YELLOW)

        x = self.coords_to_point(1, self.func_to_graph(1))
        y = self.coords_to_point(0, self.func_to_graph(0))
        horz_line = Line(x, y, color = YELLOW)

        point = Dot(self.coords_to_point(1, self.func_to_graph(1)))

        self.play(ShowCreation(func_graph), Write(graph_lab), run_time=0.5)
        self.play(ShowCreation(vert_line))
        self.play(ShowCreation(horz_line))
        self.add(point)
        self.wait(1)
        self.play(Transform(func_graph, func_graph_2), Transform(graph_lab, graph_lab_2), run_time=0.5)
        self.wait(2)

        self.clear()
        
        eqn = TextMobject("and Equations as well")
        self.wait(2)
        self.clear()

# class Equations(Scene):
#     def construct(self):
        first_eq = TextMobject("$$J(\\theta) = -\\frac{1}{m} [\\sum_{i=1}^{m} y^{(i)} \\log{h_{\\theta}(x^{(i)})} + (1-y^{(i)}) \\log{(1-h_{\\theta}(x^{(i)}))}] $$")
        second_eq = ["$J(\\theta_{0}, \\theta_{1})$", "=", "$\\frac{1}{2m}$", "$\\sum\\limits_{i=1}^m$", "(", "$h_{\\theta}(x^{(i)})$", "-", "$y^{(i)}$", "$)^2$"]

        second_mob = TextMobject(*second_eq)

        for i, item in enumerate(second_mob):
            if (i != 0):
                item.next_to(second_mob[i-1], RIGHT)

        eq2 = VGroup(*second_mob)

        des1 = TextMobject("Manim can also be used to visualize equations like this")
        des2 = TextMobject("Or like this")

        second_mob.set_color_by_gradient("#33ccff","#ff00ff")

        des1.shift(2*UP)
        des2.shift(2*UP)

        self.play(Write(des1))
        self.play(Write(first_eq))
        self.play(ReplacementTransform(des1, des2), Transform(first_eq, eq2))
        self.wait(2)

        for i, item in enumerate(eq2):
            if (i<2):
                eq2[i].set_color(color=PURPLE)
            else:
                eq2[i].set_color(color="#00FFFF")

        self.add(eq2)
        self.wait(1)
        self.play(FadeOutAndShiftDown(eq2), FadeOutAndShiftDown(first_eq), FadeOutAndShiftDown(des2))
        self.wait(2)
        self.clear()

        thanks = TextMobject("Thank You!")
        self.play(Write(thanks))
        self.wait(2)
        self.clear()
# class Logo(Scene):
#     def construct(self):
        logo = ImageMobject("i-Help.png").scale(3.2)

        self.play(FadeIn(logo))
        self.wait(3)
        self.play(FadeOut(logo))
        self.wait(1)



    def func_to_graph(self, x):
        return (x**2)

    def func_to_graph_2(self, x):
        return(x**3)

        
