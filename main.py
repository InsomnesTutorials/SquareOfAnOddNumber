from manim import *

class Main(Scene):
    def construct(self):
        odd = Tex("{{Odd}}$^2$ = Odd").move_to(ORIGIN).set_color_by_gradient(RED,BLUE)
        odd_squared = Tex("{{Odd}} $\\times$ Odd = Odd", font_size = 38)
        even = Tex("Even = {{$2x$}}", font_size = 38)
        odd_in_terms_of_even = Tex("{{Odd}} = {{$2x$}}$+1$", font_size = 38)
        odd_squared_in_terms_of_even = Tex("{{Odd}}$^2$ = ({{$2x+1$}})$^2$", font_size=38)
        odd_expanded = Tex("{{Odd}}$^2$ = $4x^2+4x+1$", font_size=38)
        odd_expanded_two_even = Tex("{{Odd$^2$}} = Even + {{Even + 1}}", font_size=38).move_to(ORIGIN + 0.5*DOWN)
        odd_expanded_one_even = Tex("{{Odd$^2$}} = {{Even + 1}}", font_size=38).move_to(ORIGIN + 0.5*DOWN)
        odd_simplified = Tex("{{Odd$^2$}} = Odd", font_size=38).move_to(ORIGIN + 0.5*DOWN)
        
        
        self.add(odd) 
        #self.wait()
        #self.play(TransformMatchingTex(odd, odd_squared))
        self.wait(5.5)
        self.play(Transform(odd, even), run_time=0.7) #6.2s
        self.remove(odd)
        self.play(TransformMatchingTex(even, odd_in_terms_of_even)) #7.2
        self.wait(0.8) #8s
        self.play(TransformMatchingTex(odd_in_terms_of_even, odd_squared_in_terms_of_even)) # 9s
        self.play(TransformMatchingTex(odd_squared_in_terms_of_even, odd_expanded)) #10s
        
        self.wait(1) #11s
        
        self.play(odd_expanded.animate.move_to(ORIGIN + 0.5*UP), Write(odd_expanded_two_even)) #12s
        self.wait(1) #13s
        self.play(TransformMatchingTex(odd_expanded_two_even, odd_expanded_one_even)) #14s
        self.wait(1) #15s
        self.play(TransformMatchingTex(odd_expanded_one_even, odd_simplified)) #16s
        self.wait(1)