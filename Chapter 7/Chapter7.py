# -*- coding: utf-8 -*-
"""Chapter7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rtrcj4Fw6aux3_sDW-0DXthKXty2YWYs
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
#         intro = Tex("Chapter 7: Triangles and its Properties")
#         intro_1 = Tex("Class 8")        
#         intro_1.next_to(intro, 1.5*DOWN)
#         self.play(Write(intro))
#         self.play(FadeIn(intro_1))
#         self.wait(2)
#         self.play(FadeOut(intro), FadeOut(intro_1))
#         self.wait(1)

# Commented out IPython magic to ensure Python compatibility.
# %%manim -qm -v WARNING triangle
# 
# class triangle(Scene):
#     def construct(self):
#         title = Tex("Triangles").scale(1.5)
#         title = title.move_to(3*UP)
#         triangle = ImageMobject("triangle.png").scale(1.75)
#         # triangle.move_to(2.5*RIGHT)
#         text_1 = Tex("A triangle is a closed figure having ")
#         text_2 = Tex("3 sides, 3 vertices and 3 angles")
#         text_1.next_to(triangle, DOWN)
#         text_2.next_to(text_1, DOWN)
#         self.play(Write(title))
#         self.wait(2)
#         self.play(FadeIn(triangle))
#         self.wait(2)
#         self.play(Write(text_1), Write(text_2))
#         self.wait(2)

# Commented out IPython magic to ensure Python compatibility.
# %%manim -qm -v WARNING terms
# 
# class terms(Scene):
#     def construct(self):
#         title = Tex("Terms associated with Triangles")
#         title = title.move_to(3*UP)
#         median = ImageMobject("Median.png").scale(1.75)
#         median.next_to(title, DOWN)
#         text_1 = Tex("A median is a line segment that connects a vertex to its opposite sides in a triangle. There are three medians in a triangle.").scale(0.75)
#         text_1.next_to(median, DOWN)
#         self.play(Write(title))
#         self.wait(2)
#         self.play(FadeIn(median))
#         self.wait(2)
#         self.play(Write(text_1))
#         self.wait(2)
#         self.play(FadeOut(median), FadeOut(text_1))
#         self.wait(2)
# 
#         altitude = ImageMobject("Altitude.png").scale(1.75)
#         altitude.next_to(title, DOWN)
#         text_2 = Tex("An altitude of the triangle is a perpendicular line segment that connects a triangle's vertex to its opposite side. There are three altitudes in a triangle.").scale(0.75)
#         text_2.next_to(altitude, DOWN)
#         self.play(FadeIn(altitude))
#         self.wait(2)
#         self.play(Write(text_2))
#         self.wait(2)
#         self.play(FadeOut(altitude), FadeOut(text_2))
#         self.wait(2)
# 
#         title_1 = Tex("Angle Sum Property of Triangles")
#         title_1 = title_1.move_to(3*UP)
#         anglesum = ImageMobject("AngleSum.png").scale(1.50)
#         anglesum.next_to(title, DOWN)
#         text_3 = Tex("The three angles at the vertex measure a total of 180 degrees. This is known as the triangle's angle sum property.").scale(0.75)
#         text_3.next_to(anglesum, DOWN)
#         text_4 = Tex("a+b+c=180°")
#         text_4.next_to(text_3, DOWN)
#         self.play(ReplacementTransform(title, title_1))
#         self.play(FadeIn(anglesum))
#         self.wait(2)
#         self.play(Write(text_3))
#         self.wait(2)
#         self.play(Write(text_4))
#         self.wait(2)
#         self.play(FadeOut(anglesum), FadeOut(text_3), FadeOut(text_4), FadeOut(title_1))
#         self.wait(2)
# 
#

# Commented out IPython magic to ensure Python compatibility.
# %%manim -qm -v WARNING types
# 
# class types(Scene):
#     def construct(self):
#         title = Tex("Types of Triangles")
#         title = title.move_to(3*UP)
#         self.play(Write(title))
#         self.wait(2)
# 
#         title_1 = Tex("Equilateral Triangle")
#         title_1 = title_1.move_to(3*UP)
#         equilateral = ImageMobject("Equilateral.png")
#         equilateral.next_to(title, 1.5*DOWN)
#         text_1 = Tex("When all the sides of the triangle have the same length and all the angles are equal.").scale(0.75)
#         text_1.next_to(equilateral, 2*DOWN)
#         self.play(ReplacementTransform(title, title_1))
#         self.play(FadeIn(equilateral))
#         self.wait(2)
#         self.play(Write(text_1))
#         self.wait(2)
#         self.play(FadeOut(equilateral), FadeOut(text_1))
#         self.wait(2)
# 
#         title_2 = Tex("Isoceles Triangle")
#         title_2 = title_2.move_to(3*UP)
#         isoceles = ImageMobject("Isoceles.png").scale(0.5)
#         isoceles.next_to(title, 1.5*DOWN)
#         text_2 = Tex("When 2 sides of the triangle have the same length. The unequal side is called the base.").scale(0.75)
#         text_2.next_to(isoceles, 2*DOWN)
#         self.play(ReplacementTransform(title_1, title_2))
#         self.play(FadeIn(isoceles))
#         self.wait(2)
#         self.play(Write(text_2))
#         self.wait(2)
#         self.play(FadeOut(isoceles), FadeOut(text_2))
#         self.wait(2)
# 
#         title_3 = Tex("Scalene Triangle")
#         title_3 = title_3.move_to(3*UP)
#         scalene = ImageMobject("Scalene.png").scale(1)
#         scalene.next_to(title, 1.5*DOWN)
#         text_3 = Tex("When all the sides of the triangle have unequal lengths.").scale(0.75)
#         text_3.next_to(scalene, 2*DOWN)
#         self.play(ReplacementTransform(title_2, title_3))
#         self.play(FadeIn(scalene))
#         self.wait(2)
#         self.play(Write(text_3))
#         self.wait(2)
#         self.play(FadeOut(scalene), FadeOut(text_3))
#         self.wait(2)
# 
#         title_4 = Tex("Acute angled Triangle")
#         title_4 = title_4.move_to(3*UP)
#         acute = ImageMobject("Acute.png").scale(0.35)
#         acute.next_to(title, 1.5*DOWN)
#         text_4 = Tex("All angles less than 90°").scale(0.75)
#         text_4.next_to(acute, 2*DOWN)
#         self.play(ReplacementTransform(title_3, title_4))
#         self.play(FadeIn(acute))
#         self.wait(2)
#         self.play(Write(text_4))
#         self.wait(2)
#         self.play(FadeOut(acute), FadeOut(text_4))
#         self.wait(2)
# 
#         title_5 = Tex("Right angled Triangle")
#         title_5 = title_5.move_to(3*UP)
#         right = ImageMobject("Right.png").scale(0.60)
#         right.next_to(title, DOWN)
#         text_5 = Tex("One angle measure is exactly 90°").scale(0.75)
#         text_5.next_to(right, 2*DOWN)
#         self.play(ReplacementTransform(title_4, title_5))
#         self.play(FadeIn(right))
#         self.wait(2)
#         self.play(Write(text_5))
#         self.wait(2)
#         self.play(FadeOut(right), FadeOut(text_5))
#         self.wait(2)
# 
#         title_6 = Tex("Obtuse angled Triangle")
#         title_6 = title_6.move_to(3*UP)
#         obtuse = ImageMobject("Obtuse.png").scale(1.2)
#         obtuse.next_to(title, 1.5*DOWN)
#         text_6 = Tex("One angle is greater than 90° but less than 180°").scale(0.75)
#         text_6.next_to(obtuse, 2*DOWN)
#         self.play(ReplacementTransform(title_5, title_6))
#         self.play(FadeIn(obtuse))
#         self.wait(2)
#         self.play(Write(text_6))
#         self.wait(2)
#         self.play(FadeOut(obtuse), FadeOut(text_6), FadeOut(title_6))
#         self.wait(2)
#         self.clear()

# Commented out IPython magic to ensure Python compatibility.
# %%manim -qm -v WARNING properties
# 
# class properties(Scene):
#     def construct(self):
#         title = Tex("Properties of Triangles")
#         title = title.move_to(3*UP)
#         self.play(Write(title))
#         self.wait(2)
# 
#         property = ImageMobject("Property.png").scale(0.75)
#         property.next_to(title, DOWN)
#         text_1 = Tex("The sum of any two sides of a triangle have a length that is more than the third side's length").scale(0.6)
#         text_1.next_to(property, DOWN)
#         text_2 = Tex("This feature is important in determining whether or not a triangle can be drawn.").scale(0.6)
#         text_2.next_to(text_1, DOWN)
# 
#         self.play(FadeIn(property))
#         self.wait(2)
#         self.play(Write(text_1), Write(text_2))
#         self.wait(2)
# 
#         text_3 = Tex("a+b is greater than c").scale(0.75)
#         text_3.next_to(property, DOWN)
#         text_4 = Tex("b+c is greater than a").scale(0.75)
#         text_4.next_to(text_3, DOWN)
#         text_5 = Tex("a+c is greater than b").scale(0.75)
#         text_5.next_to(text_4, DOWN)
# 
#         self.play(ReplacementTransform(text_1, text_3), ReplacementTransform(text_2, text_4), Write(text_5))
#         self.wait(3)

# Commented out IPython magic to ensure Python compatibility.
# %%manim -qm -v WARNING pythagoras
# 
# class pythagoras(Scene):
#     def construct(self):
#         title = Tex("Pythagoras Theorem")
#         title = title.move_to(3*UP)
#         self.play(Write(title))
#         self.wait(2)
# 
#         pythagoras = ImageMobject("Pythagoras.png")
#         pythagoras.next_to(title, 2*DOWN)
#         text_1 = Tex("The square of a hypotenuse of a right-angled triangle is equal to the sum of the squares of the other two sides.").scale(0.75)
#         text_1.next_to(pythagoras, 2*DOWN)
#         self.play(FadeIn(pythagoras))
#         self.wait(2)
#         self.play(Write(text_1))
#         self.wait(2)
#         self.play(FadeOut(pythagoras), FadeOut(text_1), FadeOut(title))
#         self.wait(2)
#         self.clear()

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