# -*- coding: utf-8 -*-
"""Chapter6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yy_5B91MkCll1Yw_zUNDFSAPaApYLsWi
"""

!sudo apt update
!sudo apt install libcairo2-dev ffmpeg \
    texlive texlive-latex-extra texlive-fonts-extra \
    texlive-latex-recommended texlive-science \
    tipa libpango1.0-dev
!pip install manim
!pip install IPython --upgrade

from manim import *

# Commented out IPython magic to ensure Python compatibility.
# %%manim -qm -v WARNING Intro
# 
# class Intro(Scene):
#     def construct(self):
#         intro = Tex("Chapter 6: Line and Angles")
#         intro_1 = Tex("Class 8")        
#         intro_1.next_to(intro, 1.5*DOWN)
#         self.play(Write(intro))
#         self.play(FadeIn(intro_1))
#         self.wait(2)
#         self.play(FadeOut(intro), FadeOut(intro_1))
#         self.wait(1)

# Commented out IPython magic to ensure Python compatibility.
# %%manim -qm -v WARNING line
# 
# class line(Scene):
#     def construct(self):
#         title = Tex("Line").scale(1.5)
#         title = title.move_to(3*UP)
#         self.play(Write(title))
#         self.wait(2)
# 
#         line = ImageMobject("Line.png")
#         line.next_to(title, DOWN)
#         text_1 = Tex("This is a never ending line.")
#         line_1 = ImageMobject("Line.png").scale(1.5)
#         line_1.next_to(title, DOWN)
#         text_1.next_to(line_1, DOWN)
# 
#         self.play(FadeIn(line))
#         self.wait(2)
#         self.play(Write(text_1), ReplacementTransform(line, line_1))
#         self.wait(2)

# Commented out IPython magic to ensure Python compatibility.
# %%manim -qm -v WARNING linesegment
# 
# class linesegment(Scene):
#     def construct(self):
#         title = Tex("Line Segment").scale(1.5)
#         title = title.move_to(3*UP)
#         self.play(Write(title))
#         self.wait(2)
# 
#         linesegment = ImageMobject("LineSegment.png").scale(3)
#         linesegment.next_to(title, 5*DOWN)
#         text_1 = Tex("This is a line segment.")
#         text_2 = Tex("We often use a dot(point) to show an endpoint of a line.")
#         text_1.next_to(linesegment, 3*DOWN)
#         text_2.next_to(text_1, DOWN)
# 
#         self.play(FadeIn(linesegment))
#         self.wait(2)
#         self.play(Write(text_1))
#         self.wait(2)
#         self.play(Write(text_2))
#         self.wait(2)

# Commented out IPython magic to ensure Python compatibility.
# %%manim -qm -v WARNING ray
# 
# class ray(Scene):
#     def construct(self):
#         title = Tex("Ray").scale(1.5)
#         title = title.move_to(3*UP)
#         self.play(Write(title))
#         self.wait(2)
# 
#         ray = ImageMobject("Ray.png").scale(1.5)
#         ray.next_to(title, 2*DOWN)
#         text_1 = Tex("This is a ray(a line with only one endpoint).")
#         text_2 = Tex("If three or more points lie on the same line, they are called collinear points, otherwise they are called non-collinear points").scale(0.8)
#         text_1.next_to(ray, DOWN)
#         text_2.next_to(text_1, 2*DOWN)
# 
#         self.play(FadeIn(ray))
#         self.wait(2)
#         self.play(Write(text_1))
#         self.wait(2)
#         self.play(Write(text_2))
#         self.wait(2)

# Commented out IPython magic to ensure Python compatibility.
# %%manim -qm -v WARNING parallel
# 
# class parallel(Scene):
#     def construct(self):
#         title = Tex("Parallel Lines").scale(1.5)
#         title = title.move_to(3*UP)
#         self.play(Write(title))
#         self.wait(2)
# 
#         parallel = ImageMobject("Parallel.png")
#         parallel.next_to(title, 2*DOWN)
#         text_1 = Tex("Non-intersecting Lines are those that never cross each other at any point. These lines are known as Parallel Lines.").scale(0.75)
#         text_2 = Tex("The distance between parallel lines is the common length between two lines. If two lines are parallel to a common line, they will be parallel to each other as well.").scale(0.75)
#         text_1.next_to(parallel, DOWN)
#         text_2.next_to(text_1, DOWN)
# 
#         self.play(FadeIn(parallel))
#         self.wait(2)
#         self.play(Write(text_1))
#         self.wait(2)
#         self.play(Write(text_2))
#         self.wait(2)

# Commented out IPython magic to ensure Python compatibility.
# %%manim -qm -v WARNING angles
# 
# class angles(Scene):
#     def construct(self):
#         title = Tex("Angles").scale(1.5)
#         title = title.move_to(3*UP)
#         text = Tex("Two non-collinear rays intersecting at a common point")
#         text.next_to(title, DOWN)
#         self.play(Write(title))
#         self.wait(2)
#         self.play(Write(text))
#         self.wait(2)
# 
#         acute = ImageMobject("Acute.png").scale(4)
#         acute.next_to(text, 0.5*DOWN)
#         text_1 = Tex("Angle measure between 0 and 90 degrees")
#         text_1.next_to(acute, 0.5*DOWN)
#         
#         self.play(FadeIn(acute))
#         self.wait(2)
#         self.play(Write(text_1))
#         self.wait(2)
# 
#         right = ImageMobject("Right.png").scale(4)
#         right.next_to(text, 0.5*DOWN)
#         text_2 = Tex("Angle measure is exactly 90 degrees")
#         text_2.next_to(right, 0.5*DOWN)
#         
#         self.play(FadeOut(acute), FadeIn(right))
#         self.wait(2)
#         self.play(ReplacementTransform(text_1, text_2))
#         self.wait(2)
# 
#         obtuse = ImageMobject("Obtuse.png").scale(4)
#         obtuse.next_to(text, 0.5*DOWN)
#         text_3 = Tex("Angle measure between 90 and 180 degrees")
#         text_3.next_to(obtuse, 0.5*DOWN)
#         
#         self.play(FadeOut(right), FadeIn(obtuse))
#         self.wait(2)
#         self.play(ReplacementTransform(text_2, text_3))
#         self.wait(2)
# 
#         straight = ImageMobject("Straight.png").scale(4)
#         straight.next_to(text, 2*DOWN)
#         text_4 = Tex("Angle measure is exactly 180 degrees")
#         text_4.next_to(straight, 0.5*DOWN)
#         
#         self.play(FadeOut(obtuse), FadeIn(straight))
#         self.wait(2)
#         self.play(ReplacementTransform(text_3, text_4))
#         self.wait(2)
# 
#         reflex = ImageMobject("Reflex.png").scale(3.5)
#         reflex.next_to(text, 0.5*DOWN)
#         text_5 = Tex("Angle measure between 180 and 360 degrees")
#         text_5.next_to(reflex, 0.5*DOWN)
#         
#         self.play(FadeOut(straight), FadeIn(reflex))
#         self.wait(2)
#         self.play(ReplacementTransform(text_4, text_5))
#         self.wait(2)

# Commented out IPython magic to ensure Python compatibility.
# %%manim -qm -v WARNING twoangles
# 
# class twoangles(Scene):
#     def construct(self):
#         title = Tex("Two Angles").scale(1.5)
#         title = title.move_to(3*UP)
#         text = Tex("Two non-collinear rays intersecting at a common point")
#         text.next_to(title, DOWN)
#         self.play(Write(title))
#         self.wait(2)
#         # self.play(Write(text))
#         # self.wait(2)
# 
#         compliment = ImageMobject("Compliment.png").scale(2.5)
#         compliment.next_to(title, 0.5*DOWN)
#         text_1 = Tex("Two angles whose sum is 90 degrees")
#         text_1.next_to(compliment, 0.5*DOWN)
#         
#         self.play(FadeIn(compliment))
#         self.wait(2)
#         self.play(Write(text_1))
#         self.wait(2)
# 
#         supplement = ImageMobject("Supplement.png").scale(2.5)
#         supplement.next_to(title, 0.5*DOWN)
#         text_2 = Tex("Two angles whose sum is 180 degrees")
#         text_2.next_to(supplement, 0.5*DOWN)
#         
#         self.play(FadeOut(compliment), FadeIn(supplement))
#         self.wait(2)
#         self.play(ReplacementTransform(text_1, text_2))
#         self.wait(2)
# 
#         adjacent = ImageMobject("Adjacent.png").scale(1.10)
#         adjacent.next_to(title, 0.5*DOWN)
#         text_3 = Tex("Angles they have a common side and a common vertex")
#         text_3.next_to(adjacent, 0.5*DOWN)
#         
#         self.play(FadeOut(supplement), FadeIn(adjacent))
#         self.wait(2)
#         self.play(ReplacementTransform(text_2, text_3))
#         self.wait(2)
# 
#         linepair = ImageMobject("LinearPair.png").scale(2.5)
#         linepair.next_to(title, 1.85*DOWN)
#         text_4 = Tex("A linear pair of angles must add up to 180 degrees")
#         text_4.next_to(linepair, 0.5*DOWN)
#         
#         self.play(FadeOut(adjacent), FadeIn(linepair))
#         self.wait(2)
#         self.play(ReplacementTransform(text_3, text_4))
#         self.wait(2)
# 
#         veropp = ImageMobject("VerOpp.png").scale(2.3)
#         veropp.next_to(text, 0.5*DOWN)
#         text_5 = Tex("Equal angles formed when two lines intersect each other at a point").scale(0.90)
#         text_5.next_to(veropp, 1.4*DOWN)
#         
#         self.play(FadeOut(linepair), FadeIn(veropp))
#         self.wait(2)
#         self.play(ReplacementTransform(text_4, text_5))
#         self.wait(2)

# Commented out IPython magic to ensure Python compatibility.
# %%manim -qm -v WARNING theorems
# 
# class theorems(Scene):
#     def construct(self):
#         title = Tex("Theorems").scale(1.5)
#         title = title.move_to(3*UP)
#         title_1 = Tex("Pairs of angle axioms")
#         title_1.next_to(title, 1.10*DOWN)
#         self.play(Write(title))
#         self.wait(2)
#         self.play(Write(title_1))
#         self.wait(2)
# 
#         axiom_1 = ImageMobject("Axiom1.png").scale(1.15)
#         axiom_1.next_to(title_1, DOWN)
#         text_1 = Tex("1. If a ray stands on a line, then the sum of the two adjacent angles formed by that ray is 180 degrees").scale(0.65)
#         text_1.next_to(axiom_1, DOWN)
#         text_2 = Tex("2. If the sum of two adjacent angles is 180°, then the arms which are not common of the angles form a line.").scale(0.65)
#         text_2.next_to(text_1, DOWN)
# 
#         self.play(FadeIn(axiom_1))
#         self.wait(2)
#         self.play(Write(text_1))
#         self.wait(2)
#         self.play(Write(text_2))
#         self.wait(2)
# 
#         axiom_2 = ImageMobject("Axiom2.png").scale(1.15)
#         axiom_2.next_to(title_1, 1.10*DOWN)
#         title_2 = Tex("Vertically opposite Angles Theorem")
#         title_2.next_to(title, 1.10*DOWN)
#         text_3 = Tex("When two lines intersect each other, then the vertically opposite angles so formed will be equal").scale(0.80)
#         text_3.next_to(axiom_2, DOWN)
# 
#         self.play(ReplacementTransform(title_1, title_2))
#         self.play(FadeOut(axiom_1), FadeIn(axiom_2))
#         self.wait(1)
#         self.play(ReplacementTransform(text_1, text_3), ReplacementTransform(text_2, text_3))
#         self.wait(2)
# 
#         axiom_3 = ImageMobject("Traverse.png").scale(2.5)
#         axiom_3.next_to(title_1, 1.10*DOWN)
#         title_3 = Tex("Traversal Theorem")
#         title_3.next_to(title, 1.10*DOWN)
#         text_4 = Tex("When a transversal crosses two parallel lines:").scale(0.80)
#         text_4.next_to(axiom_3, 0.5*DOWN)
#         text_5 = Tex("1. Each pair of corresponding angles is equal.").scale(0.80)
#         text_5.next_to(text_4, DOWN)
#         text_6 = Tex("2. The interior angles of each pair of alternate interior angles will be equal.").scale(0.80)
#         text_6.next_to(text_4, DOWN)
#         text_7 = Tex("3. On the same side of the transversal, each pair of internal angles will be additional.").scale(0.80)
#         text_7.next_to(text_4, DOWN)
# 
#         self.play(ReplacementTransform(title_2, title_3))
#         self.play(FadeOut(axiom_2), FadeIn(axiom_3))
#         self.wait(1)
#         self.play(ReplacementTransform(text_3, text_4)) # ReplacementTransform(text_3, text_5), ReplacementTransform(text_3, text_6), ReplacementTransform(text_3, text_7))
#         self.wait(2)
#         self.play(Write(text_5))
#         self.wait(2)
#         self.play(ReplacementTransform(text_5, text_6))
#         self.wait(2)
#         self.play(ReplacementTransform(text_6, text_7))
#         self.wait(2)
# 
#         axiom_4 = ImageMobject("InteriorAngle.png").scale(1.25)
#         axiom_4.next_to(title_1, 1.10*DOWN)
#         title_4 = Tex("Angle sum property of triangle")
#         title_4.next_to(title, 1.10*DOWN)
#         text_8 = Tex("The sum of the interior angles of a triangle is 180 degrees")
#         text_8.next_to(axiom_4, DOWN)
# 
#         self.play(ReplacementTransform(title_3, title_4))
#         self.play(FadeOut(axiom_3), FadeIn(axiom_4))
#         self.wait(1)
#         self.play(ReplacementTransform(text_4, text_8), ReplacementTransform(text_7, text_8))
#         self.wait(2)
# 
#         axiom_5 = ImageMobject("ExteriorAngle.png").scale(2)
#         axiom_4.next_to(title_1, 1.10*DOWN)
#         text_9 = Tex("If we produce any side of a triangle, then the exterior angle formed is equal to the sum of the two interior opposite angles").scale(0.75)
#         text_9.next_to(axiom_5, DOWN)
# 
#         self.play(FadeOut(axiom_4), FadeIn(axiom_5))
#         self.wait(1)
#         self.play(ReplacementTransform(text_8, text_9))
#         self.wait(2)

# Commented out IPython magic to ensure Python compatibility.
# %%manim -qm -v WARNING thanks
# 
# class thanks(Scene):
#      def construct(self):
#                 thanks=Tex("Thank you!").scale(2)
#                 self.play(Write(thanks))
#                 self.wait(2)
#                 self.play(FadeOut(thanks))
#                 logo=ImageMobject('ihelp.png').scale(1)
#                 self.play(FadeIn(logo), run_time=1)
#                 self.wait(4)